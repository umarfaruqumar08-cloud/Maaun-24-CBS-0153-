# 🏥 Health Clinic Queue Manager

A Flask or Simple web application for managing patient queues using FIFO (First-In-First-Out).

## What This App Does

- Register patients with name, age, and symptoms
- View waiting queue in fair FIFO order
- Track currently serving patient
- Monitor statistics (waiting count, total served)
- Automatic timestamps for arrivals 
- Aids in proper management of queue

## Technologies

- Python 3.11
- Flask web framework
- Object-Oriented Programming (Patient, ClinicQueue classes)
- Queue Data Structure (FIFO)
- datetime API

## How to Run

1. Clone this repository
2. Create virtual environment: `python -m venv venv`
3. Activate: `venv\Scripts\activate`
4. Install: `pip install -r requirements.txt`
5. Run: `python app.py`
6. Open browser to ` http://127.0.0.1:5000`

NOTE: No.2 to 5 are to be done on the terminal.

## Project Structure