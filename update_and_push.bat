@echo off
echo ============================================================
echo   Updating System Name to "Traffic Detection and Recognition"
echo ============================================================
echo.

git add app.py
git add templates/index.html
git add START_HERE.bat
git add README_GITHUB.md
git add START_WEB_APP.md
git add HOW_TO_USE.md
git add FINAL_SUMMARY.md
git add SYSTEM_SUMMARY.md
git add demo.py

git commit -m "Update system name to Traffic Detection and Recognition"
git push

echo.
echo ============================================================
echo   Done! System name updated on GitHub
echo ============================================================
pause
