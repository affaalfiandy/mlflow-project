#!/bin/bash

# Start MLflow UI in the background
mlflow ui --host 0.0.0.0 &

# Run the training script
python main.py &

# Run the api script
python app.py