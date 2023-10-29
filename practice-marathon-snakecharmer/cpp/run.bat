@echo off
g++ snakecharmer.cpp -o snakecharmer.exe
java -jar "..\snakecharmer.jar" -exec "snakecharmer.exe" -seed "%~1"