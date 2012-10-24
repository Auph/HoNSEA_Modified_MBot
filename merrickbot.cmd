@echo off
MODE CON: COLS=150 LINES=500

:START
echo honbot starting
c:\python27\python.exe merrickbot -c c:\Users\{username}\{folder}\.honbot
echo honbot exited, restarting
GOTO START
@echo on
