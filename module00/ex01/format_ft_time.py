import time
from datetime import datetime, timezone

today = datetime.now()
time = time.time()
epoch = datetime.fromtimestamp(0, timezone.utc)
print(f"Seconds since January 1, 1970: {time:,.4f} "
      f"or {time:.2e} in scientific notation")
print(today.strftime('%b %d %Y'))
