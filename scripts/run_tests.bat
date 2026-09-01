@echo off
setlocal
cd /d "%~dp0.."
set "ROOT=%CD%"
if exist "%ROOT%\isaac_sim\python.bat" (
    call "%ROOT%\isaac_sim\python.bat" -m unittest discover -s "%ROOT%\tests" -v
) else (
    python -m unittest discover -s "%ROOT%\tests" -v
)
