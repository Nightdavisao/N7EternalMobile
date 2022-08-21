@echo off

:: thanks stackoverflow https://stackoverflow.com/a/10052222
:: BatchGotAdmin
:-------------------------------------
REM  --> Check for permissions
    IF "%PROCESSOR_ARCHITECTURE%" EQU "amd64" (
>nul 2>&1 "%SYSTEMROOT%\SysWOW64\cacls.exe" "%SYSTEMROOT%\SysWOW64\config\system"
) ELSE (
>nul 2>&1 "%SYSTEMROOT%\system32\cacls.exe" "%SYSTEMROOT%\system32\config\system"
)

REM --> If error flag set, we do not have admin.
if '%errorlevel%' NEQ '0' (
    echo Requesting administrative privileges...
    goto UACPrompt
) else ( goto gotAdmin )

:UACPrompt
    echo Set UAC = CreateObject^("Shell.Application"^) > "%temp%\getadmin.vbs"
    set params= %*
    echo UAC.ShellExecute "cmd.exe", "/c ""%~s0"" %params:"=""%", "", "runas", 1 >> "%temp%\getadmin.vbs"

    "%temp%\getadmin.vbs"
    del "%temp%\getadmin.vbs"
    exit /B

:gotAdmin
    pushd "%CD%"
    CD /D "%~dp0"
:--------------------------------------

color 09
echo Never7 -the end of infinity- Eternal Edition v0.4 for Mobile Devices patcher
for /F %%x in ('dir .\patch /b /a-d') do (
	.\patch.exe %%~nx .\patch\%%x
)
echo PLEASE NOTE: the patching was supposedly done (check if the output was different from 'patching file X', if it was, then the patching was not successful), pressing any key will close this window
echo PLEASE NOTE: if the patching was not successful, then the files were modified (is it a different version of the game? if not, either you have corrupted files or you modified the files yourself in some way)
pause