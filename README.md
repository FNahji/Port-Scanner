# Port-Scanner
A Python based TCP port scanner that identifies open ports on a target host.

##FEATURES
-Scan ports 1-1025.
-Logs scan start and end timestamp.
-Saves results to results.txt
-Optimized timeout for fast results

##USAGE
Run the script and enter a target IP address or domain name when prompted.
Results will be saved automatically to results.txt.

##EXAMPLE OUTPUT
Scanning 127.0.0.1
Scan started at: 2026-05-07 16:32:01
Port 135 Open
Port 445 Open
Scan ended at: 2026-05-07 16:35:12
Results saved to results.txt

##TECHNOLOGIES 
-Python
-Socket Library
-Datetime Library
