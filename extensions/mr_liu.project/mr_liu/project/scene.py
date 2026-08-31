"""Spawn the lab table and SO-101 arm from Isaac Sim 6.0 assets."""

from __future__ import annotations

TABLE_REL = "/Isaac/Props/Mounts/SeattleLabTable/table_instanceable.usd"
SO101_REL = "/Isaac/Robots/RobotStudio/so101_new_calib/so101_new_calib.usd"
HDRI_REL = "/NVIDIA/Assets/Skies/Studio/photo_studio_01_4k.hdr"

# Table origin is the top surface (~1.05 m). Robot sits on that surface at the near edge.
TABLE_POS = [0.5, 0.0, 1.05]
TABLE_ORIENT_WXYZ = [0.70710678, 0.0, 0.0, 0.70710678]  # 90 deg about Z
SO101_POS = [0.0, 0.0, 1.05]


def resolve_asset(rel_path: str) -> str:
    from isaacsim.storage.native import get_assets_root_path

    root = get_assets_root_path()
    if not root:
        raise RuntimeError("Isaac Sim asset root is not available. Check network or ISAACSIM_ASSET_ROOT.")
    return root.rstrip("/") + rel_path


def apply_environment_map() -> None:
    """Attach a studio HDRI to the dome light so the far field is not black."""
    from isaacsim.core.experimental.objects import DomeLight
    from pxr import Sdf

    hdri = resolve_asset(HDRI_REL)
    dome = DomeLight(
        "/World/DomeLight",
        texture_files=hdri,
        texture_formats="latlong",
    )
    dome.set_intensities(1000)
    dome.prims[0].CreateAttribute("visibleInPrimaryRay", Sdf.ValueTypeNames.Bool).Set(True)
    print(f"[mr_liu.project] Environment HDRI: {hdri}")


def spawn_table_and_so101() -> None:
    import isaacsim.core.experimental.utils.stage as stage_utils
    from isaacsim.core.experimental.prims import XformPrim

    apply_environment_map()

    table_usd = resolve_asset(TABLE_REL)
    so101_usd = resolve_asset(SO101_REL)

    stage_utils.add_reference_to_stage(usd_path=table_usd, path="/World/Table")
    stage_utils.add_reference_to_stage(usd_path=so101_usd, path="/World/SO101")

    XformPrim(
        "/World/Table",
        positions=[TABLE_POS],
        orientations=[TABLE_ORIENT_WXYZ],
        reset_xform_op_properties=True,
    )
    XformPrim(
        "/World/SO101",
        positions=[SO101_POS],
        reset_xform_op_properties=True,
    )
    print(f"[mr_liu.project] Table: {table_usd}")
    print(f"[mr_liu.project] SO-101: {so101_usd}")
