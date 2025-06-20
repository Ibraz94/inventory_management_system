#!/bin/bash

# Start backend server
cd /home/ubuntu/inventory-management-system/backend
source venv/bin/activate
cd app
uvicorn main:app --host 0.0.0.0 --port 8000 &
BACKEND_PID=$!

echo "Backend server started with PID: $BACKEND_PID"
echo "Backend API available at: http://localhost:8000"

# Start frontend development server
cd /home/ubuntu/inventory-management-system/frontend
npm run dev &
FRONTEND_PID=$!

echo "Frontend development server started with PID: $FRONTEND_PID"
echo "Frontend available at: http://localhost:3000"

# Function to handle script termination
function cleanup {
  echo "Stopping servers..."
  kill $BACKEND_PID
  kill $FRONTEND_PID
  echo "Servers stopped"
}

# Register the cleanup function to be called on script termination
trap cleanup EXIT

# Keep the script running
echo "Press Ctrl+C to stop both servers"
wait
