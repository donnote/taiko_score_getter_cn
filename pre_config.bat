@echo off
REM ________________________________________________________________
REM Setting working directory to the script directory
cd /d "%~dp0"

>nul 2>&1 "%SYSTEMROOT%\system32\cacls.exe" "%SYSTEMROOT%\system32\config\system"
if '%errorlevel%' NEQ '0' (
    goto UACPrompt
) else (
    goto gotAdmin
)

:UACPrompt
echo Set UAC = CreateObject("Shell.Application") > "%temp%\getAdmin.vbs"
echo UAC.ShellExecute "%~s0", "", "", "runas", 1 >> "%temp%\getAdmin.vbs"
"%temp%\getAdmin.vbs"
exit /B

:gotAdmin
del "%temp%\getAdmin.vbs" 2>nul
REM Setting local proxy
set proxy_host=127.0.0.1
set proxy_port=8080
REG ADD "HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings" /v ProxyEnable /t REG_DWORD /d 1 /f
REG ADD "HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings" /v ProxyServer /t REG_SZ /d %proxy_host%:%proxy_port% /f
curl -x %proxy_host%:%proxy_port% -o mitmproxy-ca-cert.cer http://mitm.it/cert/cer

certutil.exe -addstore root mitmproxy-ca-cert.cer
if %errorlevel% EQU 0 (
    echo Cert file is installed successfully
) else (
    echo Failed to install cert file
)

exit /B