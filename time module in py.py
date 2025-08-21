"""
    Python Time Module

    |> The `time` module in Python provides functions to work with time values.
    |> Useful for measuring execution time, delays, and formatting time.

    Important Functions:

    1. time.time() 
       - Returns the current time in seconds since Epoch (1 Jan 1970).
    
    2. time.localtime()
       - Converts epoch time into a struct_time object.
    
    3. time.asctime()
       - Converts struct_time into a human-readable string.
    
    4. time.sleep(seconds)
       - Suspends execution for the given number of seconds.
    
    5. time.perf_counter()
       - High-resolution timer (better than time.time() for performance measurement).
"""

import time

# 1️⃣ Measuring execution time
initial = time.time()

for i in range(1000000):
    _ = i * i   # dummy work

print(f"For loop ran in {time.time() - initial} seconds\n")


# 2️⃣ Current time in ticks (epoch time)
print("Current time in ticks:", time.time())

# 3️⃣ Local time (struct_time object)
local_struct = time.localtime(time.time())
print("\nLocal time (struct_time):", local_struct)

# 4️⃣ Human-readable formatted local time
localtime = time.asctime(local_struct)
print("Formatted local time:", localtime)

# 5️⃣ Using sleep()
print("\nWaiting for 3 seconds...")
time.sleep(3)
print("Done waiting!")
