import time
from datetime import datetime

my_dict = {}

while True:
    # Get the current time as a string: "YYYY-MM-DD HH:MM:SS"
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Add it to the dictionary with an empty value
    my_dict[current_time] = ""

    print(f"Added: {current_time} → (empty)")

    # Wait for 60 seconds
    time.sleep(60)

