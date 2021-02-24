call  "C:\Program Files\QGIS 3.16\bin\pyQGIS.bat"

@echo off

echo [START] converting qrc file

rem convert qrc to py

pyrcc5 -o resources.py resources.qrc

echo [END] converting qrc file
pause