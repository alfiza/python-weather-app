#!/bin/bash

echo "Pulling latest code..."
git pull origin main

echo "Activating virtual environment..."
source venv/bin/activate

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Restarting Gunicorn service..."
sudo systemctl restart weather.service

echo "Deployment complete!"
