@echo off
cd /d "C:\Users\vapor\OneDrive\Desktop\my foodie app"
call .venv\Scripts\activate.bat
python manage.py runserver
pause