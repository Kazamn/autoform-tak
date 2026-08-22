@echo off
title Autoform TAK Automation

echo Menjalankan sistem otomatisasi TAK...

:: Otomatis pindah ke direktori tempat file .bat ini berada
cd /d "%~dp0"

:: Menjalankan script Python
python autoform.py
pause