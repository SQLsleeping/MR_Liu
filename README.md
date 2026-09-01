# MR Liu Isaac Sim 工程

基于 NVIDIA Isaac Sim 6.0。`isaac_sim/` 是引擎安装，不纳入 Git。

当前进度：**一期** — SO-101 可规划描述 + cuMotion follow-target。相机 / CV 尚未接入。

## 目录

```
MR_Liu/
├── configs/                      # YAML：场景、机器人、规划、相机（二期）
├── assets/robots/so101/          # URDF / XRDF / rmp_flow.yaml
├── source/mr_liu/                # 业务包（sim / robot / motion / vision / control / app）
├── scenes/world.usda             # 静态 USD
├── scripts/                      # 启动脚本，不含逻辑
├── tests/                        # 关节映射等无 GUI 测试
├── extensions/mr_liu.project/    # 薄 Kit UI
└── isaac_sim/                    # 引擎
```

## 一期：follow-target

```bat
scripts\run_follow_target.bat
```

Play 后拖动 `/World/TargetCube`，SO-101 用 cuMotion RMPflow 跟随。Stop/Play 会重置控制器。

关节名自检：

```bat
scripts\run_tests.bat
```

## 其它入口

```bat
launch_isaac_sim.bat          :: GUI + 工程扩展
scripts\hello_world.bat       :: 仅加载桌 + 臂（若仍指向旧脚本，用 python.bat scripts\hello_world.py）
isaac_sim\python.bat scripts\hello_world.py
```

## 资产

- 桌子：`Isaac/Props/Mounts/SeattleLabTable/table_instanceable.usd`
- 机械臂 USD：`Isaac/Robots/RobotStudio/so101_new_calib/so101_new_calib.usd`
- 规划：`assets/robots/so101/robot.urdf` + `robot.xrdf`（cuMotion 不读取 STL）

基座通过 `/World/SO101Mount` Fixed Joint 焊在桌面位姿上。
