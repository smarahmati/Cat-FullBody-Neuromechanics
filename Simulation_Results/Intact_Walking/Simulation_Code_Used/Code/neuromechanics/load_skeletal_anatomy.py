"""Load exact mechanical arrays; mesh removal only affects rendering."""

import xml.etree.ElementTree as ET

import numpy as np

import mujoco as mj

from model_configuration.paths import ROOT


def load_skeletal_anatomy(graphics=False, variant="base"):
    """Select an explicitly saved anatomy variant; base files are preserved."""
    directory = ROOT / "Data/Skeletal_Geometry/Model" if variant == "base" else ROOT / "Data/Skeletal_Geometry/Model" / variant
    root = ET.parse(directory / "cat.xml").getroot()
    meshdir = ROOT / "Data/Skeletal_Geometry/Model/meshes"
    root.find("compiler").set("meshdir", str(meshdir))
    use_meshes = graphics and all((meshdir / mesh.get("file", "")).is_file() for mesh in root.find("asset").findall("mesh"))
    if graphics and not use_meshes:
        print("Optional anatomical meshes absent: using schematic bones; mechanics are unchanged.")
    if not use_meshes:
        for geom in root.iter("geom"):
            if geom.get("type") == "mesh":
                geom.set("type", "sphere")
                geom.set("size", "1e-6")
                if graphics:
                    geom.set("size", "0.008")
                    geom.set("rgba", "0.9 0.86 0.72 1")
                geom.attrib.pop("mesh", None)
        for mesh in list(root.find("asset").findall("mesh")):
            root.find("asset").remove(mesh)
    if graphics and not use_meshes:
        for body in root.iter("body"):
            child = body.find("body")
            end = np.fromstring(child.get("pos", "0.03 0 0"), sep=" ") if child is not None else np.array([0.025, 0, 0])
            if np.linalg.norm(end) < 0.01:
                end = np.array([0.03, 0, 0])
            for geom in body.findall("geom"):
                if geom.get("mesh") is None and ("_bone" in geom.get("name", "") or "axial_surface" in geom.get("name", "")):
                    geom.set("type", "capsule")
                    geom.set("fromto", "0 0 0 " + " ".join(map(str,end)))
                    geom.attrib.pop("pos", None)
                    geom.attrib.pop("quat", None)
                    geom.set("size", "0.008")
    m = mj.MjModel.from_xml_string(ET.tostring(root, encoding="unicode"))
    for key, value in np.load(directory / "mechanics_exact.npz").items():
        if key.endswith("_names"):
            # Skip the remaining work for this item.
            continue
        if not use_meshes and key == "geom_size":
            ids = [
                i
                for i in range(m.ngeom)
                if m.geom(i).name.find("_bone") < 0
                and m.geom(i).name.find("axial_surface") < 0
            ]
            getattr(m, key)[ids] = value[ids]
        else:
            getattr(m, key)[:] = value
    # Mesh geoms never enter collisions and all mass/inertia is explicit.
    mj.mj_setConst(m, mj.MjData(m))
    return m
