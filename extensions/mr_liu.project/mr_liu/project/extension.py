import os

import omni.ext
import omni.ui as ui
import omni.usd


def _project_root() -> str:
    # extensions/mr_liu.project/mr_liu/project/extension.py -> repo root
    return os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))


def _default_scene_path() -> str:
    return os.path.join(_project_root(), "scenes", "world.usda")


class MrLiuProjectExtension(omni.ext.IExt):
    def on_startup(self, ext_id: str) -> None:
        self._ext_id = ext_id
        self._window = ui.Window("MR Liu Project", width=360, height=180)
        scene_path = _default_scene_path()

        with self._window.frame:
            with ui.VStack(spacing=8):
                ui.Label("MR Liu Isaac Sim Project", height=24)
                ui.Label(f"Scene: {scene_path}", word_wrap=True, height=40)

                def load_scene() -> None:
                    if not os.path.isfile(scene_path):
                        print(f"[mr_liu.project] Scene not found: {scene_path}")
                        return
                    omni.usd.get_context().open_stage(scene_path)
                    print(f"[mr_liu.project] Opened {scene_path}")

                ui.Button("Load Default Scene", height=32, clicked_fn=load_scene)

        print(f"[mr_liu.project] Extension started ({ext_id})")

    def on_shutdown(self) -> None:
        if self._window:
            self._window.destroy()
            self._window = None
        print("[mr_liu.project] Extension shutdown")
