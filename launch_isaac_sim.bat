@echo off
setlocal
set "ROOT=%~dp0"
set "ROOT=%ROOT:~0,-1%"

if not exist "%ROOT%\isaac_sim\isaac-sim.bat" (
    echo Isaac Sim launcher not found: "%ROOT%\isaac_sim\isaac-sim.bat"
    exit /b 1
)

echo Starting Isaac Sim 6.0 with project extension and default scene...
call "%ROOT%\isaac_sim\isaac-sim.bat" ^
    --ext-folder "%ROOT%\extensions" ^
    --enable mr_liu.project ^
    "%ROOT%\scenes\world.usda" %*
