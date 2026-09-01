@echo off
setlocal
cd /d "%~dp0.."
set "ROOT=%CD%"
if not exist "%ROOT%\isaac_sim\python.bat" (
    echo Isaac Sim Python not found: "%ROOT%\isaac_sim\python.bat"
    exit /b 1
)
call "%ROOT%\isaac_sim\python.bat" "%ROOT%\scripts\run_follow_target.py" %*
