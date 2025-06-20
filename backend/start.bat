@echo off
echo Starting Inventory Management System Backend...

REM Activate virtual environment
call venv\Scripts\activate.bat

REM Install dependencies if needed
pip install -r requirements.txt

REM Start the FastAPI server
cd app
uvicorn main:app --host 0.0.0.0 --port 8000 --reload

pause 