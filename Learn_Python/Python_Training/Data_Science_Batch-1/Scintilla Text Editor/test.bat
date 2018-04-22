
down vote
	

@echo off
for /F "tokens=1 delims=# " %%a in ('"prompt #$H# & echo on & for %%b in (1) do rem"') do set "BSPACE=%%a"
<nul set /p =Step 1
ping 127.0.0.1 >nul
<nul set /p =%BSPACE%
<nul set /p =2
ping 127.0.0.1 >nul
<nul set /p =%BSPACE%
<nul set /p =3
ping 127.0.0.1 >nul
<nul set /p =%BSPACE%%BSPACE%%BSPACE%%BSPACE%%BSPACE%%BSPACE%
<nul set /p =End.  
pause
