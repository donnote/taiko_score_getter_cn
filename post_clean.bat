@echo off
@REM REM ________________________________________________________________
@REM REM Setting working directory to the script directory
@REM cd /d "%~dp0"
@REM
@REM >nul 2>&1 "%SYSTEMROOT%\system32\cacls.exe" "%SYSTEMROOT%\system32\config\system"
@REM if '%errorlevel%' NEQ '0' (
@REM     goto UACPrompt
@REM ) else (
@REM     goto gotAdmin
@REM )
@REM
@REM :UACPrompt
@REM echo Set UAC = CreateObject("Shell.Application") > "%temp%\getAdmin.vbs"
@REM echo UAC.ShellExecute "%~s0", "", "", "runas", 1 >> "%temp%\getAdmin.vbs"
@REM "%temp%\getAdmin.vbs"
@REM exit /B
@REM
@REM :gotAdmin
@REM del "%temp%\getAdmin.vbs" 2>nul
REG ADD "HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings" /v ProxyEnable /t REG_DWORD /d 0 /f

pause
exit /B