"""Standalone Isaac Sim 6.0 entry point for the MR Liu project."""

from isaacsim import SimulationApp

simulation_app = SimulationApp({"headless": False})

import isaacsim.core.experimental.utils.app as app_utils
import isaacsim.core.experimental.utils.stage as stage_utils
from isaacsim.core.experimental.materials import PreviewSurfaceMaterial
from isaacsim.core.experimental.objects import Cube, DistantLight, GroundPlane
from isaacsim.core.experimental.prims import GeomPrim, RigidPrim
from isaacsim.core.simulation_manager import SimulationManager

stage_utils.create_new_stage()

GroundPlane("/World/GroundPlane", positions=[0, 0, 0])

distant_light = DistantLight("/World/DistantLight")
distant_light.set_intensities(3000)

cyan_material = PreviewSurfaceMaterial("/World/Materials/cyan")
cyan_material.set_input_values("diffuseColor", [0.15, 0.65, 0.95])

dynamic_cube = Cube(
    paths="/World/DynamicCube",
    positions=[0, 0, 1.2],
    sizes=0.4,
)
dynamic_cube.apply_visual_materials(cyan_material)
RigidPrim(paths="/World/DynamicCube")
GeomPrim(paths="/World/DynamicCube", apply_collision_apis=True)

SimulationManager.set_physics_dt(1.0 / 60.0)
app_utils.play()

print("[mr_liu] Hello World scene is running. Close the window to exit.")

while simulation_app.is_running():
    simulation_app.update()

simulation_app.close()
