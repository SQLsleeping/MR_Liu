# MR Liu Isaac Sim 工程

基于 NVIDIA Isaac Sim 6.0 的本地仿真工程。`isaac_sim/` 是引擎安装目录，不纳入 Git。

## 目录结构

```
MR_Liu/
├── isaac_sim/                 # Isaac Sim 6.0 安装（已 gitignore）
├── extensions/mr_liu.project/ # Kit 扩展：启动后出现 “MR Liu Project” 窗口
├── scripts/hello_world.py     # 独立 Python 仿真入口
├── scenes/world.usda          # 默认场景（地面、灯光、物理立方体）
├── assets/                    # 自定义机器人 / 网格资源
├── launch_isaac_sim.bat       # 启动 GUI，并加载本工程扩展与默认场景
└── run_hello_world.bat        # 用 Isaac Sim Python 运行独立脚本
```

## 启动 GUI

双击 `launch_isaac_sim.bat`，或在当前目录执行：

```bat
launch_isaac_sim.bat
```

首次启动可能需要 5–10 分钟（着色器编译与扩展缓存）。窗口标题为 **Isaac Sim Full**。扩展加载后会出现 **MR Liu Project** 面板。

也可以直接启动引擎（不自动加载本工程扩展）：

```bat
isaac_sim\isaac-sim.bat
```

## 运行独立 Python 脚本

```bat
run_hello_world.bat
```

等价于：

```bat
isaac_sim\python.bat scripts\hello_world.py
```

## Git

仓库已在当前目录初始化。请把本地提交身份改成你自己的：

```bat
git config user.name "Your Name"
git config user.email "you@example.com"
```
