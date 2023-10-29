@echo off
csc snakecharmer.cs
java -jar "..\snakecharmer.jar" -exec "snakecharmer.exe" -seed "%~1"