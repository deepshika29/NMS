import time

# Calculate the duration of 5 minutes in seconds
duration = 10

# Get the current time
start_time = time.time()

# Loop until the specified duration has elapsed
while time.time() - start_time < duration:
    # Perform any necessary operations here
    # Replace this with your actual code
    
    # Sleep for a short interval (e.g., 1 second) to avoid excessive CPU usage
    time.sleep(1)

print("Script execution completed.")
