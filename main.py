from modelling import create_model
import json
import time
from database import get_data_length

def read_last_length(file_path):
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
            return data.get('last_length', 0)
    except FileNotFoundError:
        return 0

def write_last_length(file_path, length):
    with open(file_path, 'w') as f:
        json.dump({'last_length': length}, f)


def check_data_length_and_process(last_length):
    current_length = get_data_length()
    if current_length is None:
        print("Unable to get data length. Exiting.")
        return last_length
    
    print(f"Current length: {current_length}")
    print(f"Last length: {last_length}")
    
    if current_length != last_length:
        print("Data length has changed. Processing new data...")
        create_model()
    else:
        print("Data length has not changed. No action needed.")
    
    return current_length


# File path to store the last length
length_file_path = 'last_length.json'

# Initialize last_length from file
last_length = read_last_length(length_file_path)
print(f"Initial length: {last_length}")

# Continuous monitoring loop
while True:
    last_length = check_data_length_and_process(last_length)
    write_last_length(length_file_path, last_length)
    # Wait before the next check (e.g., 60 seconds)
    time.sleep(10800)
