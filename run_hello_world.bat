@echo off
setlocal
set "ROOT=%~dp0"
set "ROOT=%ROOT:~0,-1%"

if not exist "%ROOT%\isaac_sim\python.bat" (
    echo Isaac Sim Python not found: "%ROOT%\isaac_sim\python.bat"
    exit /b 1
)

call "%ROOT%\isaac_sim\python.bat" "%ROOT%\scripts\hello_world.py" %*
