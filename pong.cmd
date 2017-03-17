@echo off
SET scriptpath=%~dp0

rem simple way to check for python presense:
rem  https://stackoverflow.com/questions/4920483/batch-file-to-check-if-python-is-installed/26241114#26241114
python --version 2>NUL
if errorlevel 1 (
echo Python not installed. Continue with standard ping:
goto errorNoPython
)
rem Detection method from
rem   https://stackoverflow.com/questions/4051883/batch-script-how-to-check-for-admin-rights/11995662#11995662
echo Administrative permissions required. Detecting permissions...
net session >nul 2>&1
if %errorLevel% == 0 (
echo Success: Administrative permissions confirmed.
rem here goes python
python %scriptpath%pong.py

goto errorNoPython
) else (
echo Failure: Python found but current permissions inadequate. Running with standard ping tool. 
goto errorNoPython
)


goto:eof
:errorNoPython
echo.
echo ==========================
echo World-wide PING starting
echo ==========================

for /F "delims=; tokens=1,*" %%A   in (%scriptpath%pinglist.txt) do @echo ========================== & @echo . & @echo     %%B & ping -w 500 -l 100 -n 3 %%A

echo ==========================
echo World-wide PING complete
echo ==========================
echo next stage - long ping 8.8.8.8
pause
ping -w 50 -l 32 -t 8.8.8.8
