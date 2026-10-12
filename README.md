# Simulated Device Monitoring and Alert System
 
**Student Name:** (your full name)
**Student Number:** (your student number)
**Section:** (your section)
 
## Project Description
This program monitors simulated device temperature readings using Python. It classifies each reading as NORMAL, WARNING, or CRITICAL based on its temperature value. The program allows users to view stored readings, add new valid readings, and generate a numerical summary with an overall system status. It also validates user input to prevent invalid temperature readings and menu choices.
 
## Features
- View all stored temperature readings
- Add a new reading (whole numbers from 0 to 100 only)
- Classify every reading
- Generate a numerical summary and overall status
- Reject invalid menu choices and invalid readings
 
## Requirements
- Python 3 (no external packages)
 
## How to Run
1. Open a terminal inside the Week17 folder.
2. Type: python device_monitor.py
   (On macOS or Linux, type: python3 device_monitor.py)
 
## Sample Output
SIMULATED DEVICE MONITORING SYSTEM
----------------------------------
[1] View Readings
[2] Add Reading
[3] Classify Readings
[4] Generate Summary
[5] Exit
Enter choice: 4

MONITORING SUMMARY
------------------
Number of readings : 5
Total of readings : 160
Average temperature : 32.00 °C
Minimum temperature : 28 °C
Maximum temperature : 37 °C

NORMAL : 2 (40.00%)
WARNING : 2 (40.00%)
CRITICAL : 1 (20.00%)

Overall Status: ATTENTION REQUIRED

SIMULATED DEVICE MONITORING SYSTEM
----------------------------------
[1] View Readings
[2] Add Reading
[3] Classify Readings
[4] Generate Summary
[5] Exit
Enter choice: 5
Thank you for using the Device Monitoring System.
 
## Test Cases
I performed 10 tests. __ passed and __ failed.
Full details are in test_cases.md.
 
## Known Limitations
- Example: Readings are lost when the program closes.
- Temperature readings are lost when the program closes because the data is not saved to a file.
- The program uses simulated temperature readings rather than data from a real device.
- The alert classifications depend on predefined temperature thresholds.
- The program does not provide real-time monitoring or automatic notifications.
 
## Reflection
The hardest part of this project was implementing the input validation and temperature classification correctly. I learned how to handle invalid inputs and prevent the program from accepting values outside the allowed range. One improvement I would make is to provide clearer error messages whenever the user enters an invalid value. In the future, I would also add file storage so that readings can be saved and loaded when the program is restarted.