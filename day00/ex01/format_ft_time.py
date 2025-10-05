from datetime import datetime

# Get current datetime and calculate seconds since epoch
current_datetime = datetime.now()
epoch = datetime(1970, 1, 1)
current_epoch_seconds = (current_datetime - epoch).total_seconds()

# Format the epoch time for the first line of output
formatted_epoch = f"Seconds since January 1, 1970: {current_epoch_seconds:,.4f} or {current_epoch_seconds:.2e} in scientific notation"

# Format the datetime object for the second line of output
formatted_date = current_datetime.strftime("%b %d %Y")

# Print the expected output
print(formatted_epoch)
print(formatted_date)

