This script uses a linux log file (syslog.log) and it parses ERROR and INFO lines using Regex.
It generates two csv files as an output.

File 1 : error_message.csv
This file shows the count of the each error messages sorted from the most comman error message to less.

File 2: user_statistics.csv
This shows the count of INFO and ERROR messages for each user. It is sorted by the username. 

Belows are done in the order.
- Use regex to parse a log file
- Append and modify values in a dictionary
- Write to a file in CSV format
