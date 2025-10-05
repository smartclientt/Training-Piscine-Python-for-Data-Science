from datetime import datetime

current_datetime = datetime.now()
epoch = datetime(1970, 1, 1)
current_epoch_seconds = (current_datetime - epoch).total_seconds()

formatted_epoch = f"Seconds since January 1, 1970: {current_epoch_seconds:,.4f} or {current_epoch_seconds:.2e} in scientific notation"

formatted_date = current_datetime.strftime("%b %d %Y")

print(formatted_epoch)
print(formatted_date)
