"""
IV-01 · "What happens inside your ear when a plane takes off" – Blender-Szene (stilisiertes Schnittmodell).

Ausführen (Blender 4.2+ / 5.x), ohne Oberfläche:
    blender -b -P iv01_ear.py -- --out C:/InsideView/render/IV-01 --fps 30 --seconds 42
oder in Blender: Scripting-Tab → Datei öffnen → Run Script (rendert dann nicht automatisch, nur Szene bauen).

Baut: Kopf-Hälfte mit Schnittfläche, Gehörgang, Trommelfell (Shape Keys bulge_out / bulge_in),
Mittelohr-Kammer (türkis leuchtend), Eustachische Röhre (Kurve, Radius animiert = öffnen),
Luftpartikel entlang der Röhre, Druckpfeile, Kamera 1080×1920 mit Push-ins je Shot.
Timing folgt den Shots in ../skripte/IV-01-ear-plane-takeoff.md (Richtwerte für 42 s; nach der
Artlist-Aufnahme die SHOTS-Tabelle unten anpassen).

Look (Konzept): Hintergrund #1B2430 · Haut Beige · Highlight Orange #FF8A3D · Luft Türkis #3DD6C8.
"""
import bpy, math, sys
from mathutils import Vector

# ----------------------------------------------------------------- Argumente
argv = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
def arg(name, default):
    return argv[argv.index(name) + 1] if name in argv else default
OUT = arg("--out", "//render/IV-01")
FPS = int(arg("--fps", 30))
SECONDS = float(arg("--seconds", 42))
RENDER = "--no-render" not in argv and bpy.app.background

# Shot-Zeiten in Sekunden (Start) – an die echte Sprachaufnahme anpassen
SHOTS = {"hook": 0.0, "pocket": 5.0, "cabin": 13.0, "bulge": 20.0, "pop": 27.0, "swallow": 32.0, "landing": 38.0}
F = lambda s: int(round(s * FPS)) + 1

# ----------------------------------------------------------------- Szene leeren
bpy.ops.wm.read_factory_settings(use_empty=True)
scene = bpy.context.scene
scene.render.resolution_x, scene.render.resolution_y = 1080, 1920
scene.render.fps = FPS
scene.frame_start, scene.frame_end = 1, F(SECONDS)
for eng in ("BLENDER_EEVEE_NEXT", "BLENDER_EEVEE"):
    try:
        scene.render.engine = eng; break
    except TypeError:
        continue
scene.render.image_settings.file_format = "PNG"
scene.render.filepath = OUT + "_"
if hasattr(scene, "eevee"):
    scene.eevee.taa_render_samples = 32
world = bpy.data.worlds.new("World"); scene.world = world
world.use_nodes = True
bg = world.node_tree.nodes["Background"]; bg.inputs[0].default_value = (0.105, 0.141, 0.188, 1); bg.inputs[1].default_value = 1.0

# ----------------------------------------------------------------- Materialien
def hexrgb(h):
    h = h.lstrip("#"); return tuple(int(h[i:i+2], 16) / 255 for i in (0, 2, 4))
def mat(name, color, emission=0.0, alpha=1.0, rough=0.6):
    m = bpy.data.materials.new(name); m.use_nodes = True
    p = m.node_tree.nodes["Principled BSDF"]
    p.inputs["Base Color"].default_value = (*color, 1)
    p.inputs["Roughness"].default_value = rough
    if "Emission Color" in p.inputs:
        p.inputs["Emission Color"].default_value = (*color, 1); p.inputs["Emission Strength"].default_value = emission
    if alpha < 1:
        p.inputs["Alpha"].default_value = alpha; m.blend_method = "BLEND"
    return m
M_SKIN  = mat("skin", hexrgb("#D9B894"), rough=0.7)
M_CUT   = mat("cut", hexrgb("#F2E3CF"), rough=0.9)
M_DRUM  = mat("eardrum", hexrgb("#FF8A3D"), emission=0.4)
M_AIR   = mat("air", hexrgb("#3DD6C8"), emission=1.2, alpha=0.55)
M_TUBE  = mat("tube", hexrgb("#E0A080"), rough=0.5)
M_ARROW = mat("arrow", hexrgb("#FF8A3D"), emission=2.0)
M_PART  = mat("particle", hexrgb("#3DD6C8"), emission=3.0)

def add(obj_fn, name, loc=(0, 0, 0), scale=(1, 1, 1), rot=(0, 0, 0), material=None, **kw):
    obj_fn(location=loc, rotation=rot, **kw)
    o = bpy.context.active_object; o.name = name; o.scale = scale
    if material: o.data.materials.append(material)
    bpy.ops.object.shade_smooth()
    return o

# ----------------------------------------------------------------- Kopf (Schnitt entlang y=0, wir sehen die hintere Hälfte)
head = add(bpy.ops.mesh.primitive_uv_sphere_add, "Head", loc=(0, 0, 0), scale=(1.0, 1.15, 1.3), material=M_SKIN, segments=64, ring_count=48)
cutter = add(bpy.ops.mesh.primitive_cube_add, "Cutter", loc=(0, -1.5, 0), scale=(3, 1.5, 3))
cutter.hide_render = True; cutter.hide_viewport = True
b = head.modifiers.new("Cut", "BOOLEAN"); b.operation = "DIFFERENCE"; b.object = cutter
head.data.materials.append(M_CUT)
# Schnittfläche bekommt Material-Index 1 via Modifier? Einfacher: Schnittebene als eigene Platte
cutface = add(bpy.ops.mesh.primitive_circle_add, "CutFace", loc=(0, 0.0, 0), rot=(math.radians(90), 0, 0), scale=(0.98, 1.28, 1), material=M_CUT, fill_type="NGON", vertices=96)
cutface.scale = (1.0, 1.3, 1.0)

# ----------------------------------------------------------------- Ohr-Anatomie (stilisiert, auf der Schnittfläche, rechts im Bild)
EAR = Vector((0.55, 0.02, 0.05))
canal = add(bpy.ops.mesh.primitive_cylinder_add, "EarCanal", loc=EAR + Vector((0.3, 0, 0)), rot=(0, math.radians(90), 0), scale=(0.07, 0.07, 0.32), material=M_TUBE, vertices=48)
drum = add(bpy.ops.mesh.primitive_circle_add, "Eardrum", loc=EAR, rot=(0, math.radians(90), 0), scale=(0.085, 0.085, 1), material=M_DRUM, fill_type="TRIFAN", vertices=48)
bpy.ops.object.modifier_add(type="SUBSURF"); drum.modifiers[-1].levels = 2
# Shape Keys für Wölbung: Mittelpunkt nach außen (+x) bzw. innen (−x)
drum.shape_key_add(name="Basis")
for key, dx in (("bulge_out", 0.06), ("bulge_in", -0.06)):
    sk = drum.shape_key_add(name=key)
    for i, v in enumerate(drum.data.vertices):
        r = (v.co.x ** 2 + v.co.y ** 2) ** 0.5  # lokaler Radius 0..1; lokal z zeigt nach der Rotation in Welt-x (nach außen)
        sk.data[i].co = v.co + Vector((0, 0, dx * max(0.0, 1.0 - r) ** 1.5))
chamber = add(bpy.ops.mesh.primitive_uv_sphere_add, "MiddleEarAir", loc=EAR + Vector((-0.12, 0, 0)), scale=(0.12, 0.1, 0.1), material=M_AIR, segments=32, ring_count=24)
# Eustachische Röhre: Kurve vom Mittelohr schräg nach unten-innen zum Rachen
curve = bpy.data.curves.new("EustachianTube", "CURVE"); curve.dimensions = "3D"; curve.bevel_depth = 0.012; curve.bevel_resolution = 6
sp = curve.splines.new("BEZIER"); sp.bezier_points.add(2)
pts = [EAR + Vector((-0.2, 0, -0.05)), EAR + Vector((-0.45, 0, -0.45)), EAR + Vector((-0.65, 0, -0.95))]
for bp, p in zip(sp.bezier_points, pts):
    bp.co = p; bp.handle_left_type = bp.handle_right_type = "AUTO"
tube = bpy.data.objects.new("EustachianTube", curve); scene.collection.objects.link(tube); curve.materials.append(M_TUBE)
throat = add(bpy.ops.mesh.primitive_cylinder_add, "Throat", loc=EAR + Vector((-0.7, 0, -1.25)), scale=(0.09, 0.09, 0.35), material=M_TUBE, vertices=32)

# Partikel: 24 kleine Kugeln, die bei "pop" und "swallow" die Röhre entlang laufen (Follow Path)
particles = []
for i in range(24):
    p = add(bpy.ops.mesh.primitive_uv_sphere_add, f"Air{i:02}", scale=(0.012,) * 3, material=M_PART, segments=12, ring_count=8)
    c = p.constraints.new("FOLLOW_PATH"); c.target = tube; c.use_fixed_location = True; c.offset_factor = 0.0
    p.hide_render = True; p.keyframe_insert("hide_render", frame=1)
    particles.append((p, c))
def run_particles(start_s, dur_s):
    for i, (p, c) in enumerate(particles):
        t0 = F(start_s + i * dur_s * 0.35 / len(particles))
        p.hide_render = False; p.keyframe_insert("hide_render", frame=t0)
        c.offset_factor = 0.0; c.keyframe_insert("offset_factor", frame=t0)
        c.offset_factor = 1.0; c.keyframe_insert("offset_factor", frame=t0 + int(dur_s * FPS * 0.65))
        p.hide_render = True; p.keyframe_insert("hide_render", frame=t0 + int(dur_s * FPS * 0.65) + 1)

# Druckpfeile im Mittelohr (zeigen auf das Trommelfell)
arrows = []
for k in range(3):
    a = add(bpy.ops.mesh.primitive_cone_add, f"Arrow{k}", loc=EAR + Vector((-0.08, 0, -0.04 + 0.04 * k)), rot=(0, math.radians(90), 0), scale=(0.02, 0.02, 0.05), material=M_ARROW, vertices=16)
    a.scale = (0, 0, 0); a.keyframe_insert("scale", frame=1); arrows.append(a)
def arrows_show(start_s, show):
    for a in arrows:
        a.scale = (0.02, 0.02, 0.05) if show else (0, 0, 0); a.keyframe_insert("scale", frame=F(start_s))

# Flugzeug-Silhouette + Druckbalken für Shot "cabin" (außerhalb des Kopfes, wird eingeblendet)
plane = add(bpy.ops.mesh.primitive_cone_add, "Plane", loc=(-1.6, 0, 1.2), rot=(0, math.radians(90), 0), scale=(0.08, 0.08, 0.35), material=M_ARROW, vertices=24)
plane.scale = (0, 0, 0); plane.keyframe_insert("scale", frame=1)
bar = add(bpy.ops.mesh.primitive_cube_add, "CabinBar", loc=(-1.6, 0, 0.2), scale=(0.08, 0.08, 0.5), material=M_AIR)
bar.scale = (0, 0, 0); bar.keyframe_insert("scale", frame=1)

# Gaumenmuskel (kleiner Zylinder am Röhrenende), zieht bei "swallow"
muscle = add(bpy.ops.mesh.primitive_cylinder_add, "PalateMuscle", loc=pts[2] + Vector((0.12, 0, 0.05)), rot=(0, math.radians(70), 0), scale=(0.025, 0.025, 0.12), material=M_TUBE, vertices=24)

# ----------------------------------------------------------------- Licht + Kamera
key = add(bpy.ops.object.light_add, "Key", loc=(2, -3, 3), type="AREA"); key.data.energy = 600; key.data.size = 4
fill = add(bpy.ops.object.light_add, "Fill", loc=(-2.5, -2.5, 1), type="AREA"); fill.data.energy = 200; fill.data.size = 5
rim = add(bpy.ops.object.light_add, "Rim", loc=(0, 3, 2), type="AREA"); rim.data.energy = 300; rim.data.size = 3
cam = add(bpy.ops.object.camera_add, "Camera", loc=(0.3, -4.2, 0.1), rot=(math.radians(88), 0, 0)); scene.camera = cam
cam.data.lens = 50; cam.data.dof.use_dof = True; cam.data.dof.focus_object = drum; cam.data.dof.aperture_fstop = 2.8
def cam_to(sec, loc, lens):
    cam.location = loc; cam.data.lens = lens
    cam.keyframe_insert("location", frame=F(sec)); cam.data.keyframe_insert("lens", frame=F(sec))

# ----------------------------------------------------------------- Animation je Shot
# Shot 1 – Hook: Schnittlinie = Cutter fährt in 0,5 s von oben durch (Boolean wird sichtbar), Kamera weit
cutter.location.z = 3.2; cutter.keyframe_insert("location", frame=1)
cutter.location.z = 0.0; cutter.keyframe_insert("location", frame=F(0.5))
cam_to(0.0, (0.3, -4.2, 0.1), 50); cam_to(SHOTS["pocket"] - 0.1, (0.35, -3.9, 0.1), 55)
# Shot 2 – Pocket: Push-in aufs Mittelohr, Kammer pulsiert
cam_to(SHOTS["pocket"], (0.35, -3.9, 0.1), 55); cam_to(SHOTS["cabin"] - 0.1, (0.5, -2.2, 0.0), 85)
for t, s in ((0, 1.0), (0.6, 1.25), (1.2, 1.0)):
    chamber.scale = (0.12 * s, 0.1 * s, 0.1 * s); chamber.keyframe_insert("scale", frame=F(SHOTS["pocket"] + 1.0 + t))
# Shot 3 – Cabin: Flugzeug + Balken einblenden, Balken sinkt
cam_to(SHOTS["cabin"], (0.0, -4.5, 0.3), 45); cam_to(SHOTS["bulge"] - 0.1, (0.0, -4.5, 0.3), 45)
plane.scale = (0.08, 0.08, 0.35); plane.keyframe_insert("scale", frame=F(SHOTS["cabin"] + 0.4))
plane.location = (-1.6, 0, 1.2); plane.keyframe_insert("location", frame=F(SHOTS["cabin"]))
plane.location = (-0.9, 0, 1.9); plane.keyframe_insert("location", frame=F(SHOTS["bulge"]))
bar.scale = (0.08, 0.08, 0.5); bar.keyframe_insert("scale", frame=F(SHOTS["cabin"] + 0.4))
bar.scale = (0.08, 0.08, 0.3); bar.keyframe_insert("scale", frame=F(SHOTS["bulge"] - 0.3))
plane.scale = (0, 0, 0); plane.keyframe_insert("scale", frame=F(SHOTS["bulge"]))
bar.scale = (0, 0, 0); bar.keyframe_insert("scale", frame=F(SHOTS["bulge"]))
# Shot 4 – Bulge: Pfeile erscheinen, Trommelfell wölbt nach außen
cam_to(SHOTS["bulge"], (0.5, -2.0, 0.05), 90); cam_to(SHOTS["pop"] - 0.1, (0.55, -1.7, 0.05), 100)
arrows_show(SHOTS["bulge"] + 0.3, True)
ko = drum.data.shape_keys.key_blocks["bulge_out"]; ki = drum.data.shape_keys.key_blocks["bulge_in"]
ko.value = 0.0; ko.keyframe_insert("value", frame=F(SHOTS["bulge"] + 0.5))
ko.value = 1.0; ko.keyframe_insert("value", frame=F(SHOTS["bulge"] + 2.0))
# Shot 5 – Pop: Röhre öffnet (Bevel-Radius), Partikel fließen, Trommelfell schnappt zurück, Pfeile weg
cam_to(SHOTS["pop"], (0.4, -2.3, -0.3), 80); cam_to(SHOTS["swallow"] - 0.1, (0.4, -2.3, -0.3), 80)
curve.bevel_depth = 0.012; curve.keyframe_insert("bevel_depth", frame=F(SHOTS["pop"]))
curve.bevel_depth = 0.03; curve.keyframe_insert("bevel_depth", frame=F(SHOTS["pop"] + 0.3))
curve.bevel_depth = 0.012; curve.keyframe_insert("bevel_depth", frame=F(SHOTS["pop"] + 1.6))
run_particles(SHOTS["pop"] + 0.3, 2.0)
ko.value = 1.0; ko.keyframe_insert("value", frame=F(SHOTS["pop"] + 0.3))
ko.value = 0.0; ko.keyframe_insert("value", frame=F(SHOTS["pop"] + 0.7))
arrows_show(SHOTS["pop"] + 0.5, False)
# Shot 6 – Swallow: Muskel zieht, Röhre öffnet erneut, Partikel
cam_to(SHOTS["swallow"], (0.2, -2.6, -0.6), 75); cam_to(SHOTS["landing"] - 0.1, (0.2, -2.6, -0.6), 75)
muscle.scale = (0.025, 0.025, 0.12); muscle.keyframe_insert("scale", frame=F(SHOTS["swallow"]))
muscle.scale = (0.035, 0.035, 0.08); muscle.keyframe_insert("scale", frame=F(SHOTS["swallow"] + 0.6))
muscle.scale = (0.025, 0.025, 0.12); muscle.keyframe_insert("scale", frame=F(SHOTS["swallow"] + 1.8))
curve.bevel_depth = 0.03; curve.keyframe_insert("bevel_depth", frame=F(SHOTS["swallow"] + 0.6))
curve.bevel_depth = 0.012; curve.keyframe_insert("bevel_depth", frame=F(SHOTS["swallow"] + 2.2))
run_particles(SHOTS["swallow"] + 0.7, 2.0)
# Shot 7 – Landing/Loop: Trommelfell nach innen, Kamera zurück auf Hook-Position, Cutter fährt hoch
cam_to(SHOTS["landing"], (0.5, -2.0, 0.05), 90); cam_to(SECONDS - 0.6, (0.3, -4.2, 0.1), 50)
ki.value = 0.0; ki.keyframe_insert("value", frame=F(SHOTS["landing"]))
ki.value = 1.0; ki.keyframe_insert("value", frame=F(SHOTS["landing"] + 1.5))
cutter.location.z = 0.0; cutter.keyframe_insert("location", frame=F(SECONDS - 0.5))
cutter.location.z = 3.2; cutter.keyframe_insert("location", frame=F(SECONDS))

# Sanfte Interpolation für Kamera
for fc in cam.animation_data.action.fcurves:
    for kp in fc.keyframe_points: kp.interpolation = "BEZIER"; kp.easing = "EASE_IN_OUT"

bpy.ops.wm.save_as_mainfile(filepath=bpy.path.abspath(OUT.rsplit("/", 1)[0] + "/IV-01.blend") if "/" in OUT else "IV-01.blend")
print(f"Szene gebaut: {scene.frame_end} Frames @ {FPS} fps, Ausgabe {OUT}_####.png")
if RENDER:
    bpy.ops.render.render(animation=True)
    print("Render fertig. Zusammenfügen: ffmpeg -framerate %d -i %s_%%04d.png -c:v libx264 -pix_fmt yuv420p IV-01-raw.mp4" % (FPS, OUT))
