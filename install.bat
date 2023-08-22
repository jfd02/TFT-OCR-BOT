@echo off


rem Check if requirements.txt file exists
if exist requirements.txt (
    call :colortheword "Found requirements.txt file. Installing dependencies..." 2
    pip install -r requirements.txt
) else (
    call :colortheword "requirements.txt file not found." 4
)

rem Check if tesserocr install file exists
if exist tesserocr-2.6.0-cp311-cp311-win_amd64.whl (
    call :colortheword "Found requirements.txt file. Installing dependencies..." 2
    pip install tesserocr-2.6.0-cp311-cp311-win_amd64.whl
) else (
    call :colortheword "tesserocr installation file not found." 4
)

pause
goto :eof

:colortheword <str1=output> [str2=colour] 
set "objFile=%~1"
set "objColor=07"&if not "%~2."=="." set "objColor=%~2"
for /F %%a in ('"prompt $h & for %%b in (1) do rem"')do set /p="%%a"<nul>"%objFile%"
findstr /a:%objColor% .* "%objFile%" nul
echo.
del /q "%objFile%" >nul 2>nul
goto :eof
