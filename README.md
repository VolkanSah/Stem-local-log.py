# Stem local log (Python)
#### useful small hacks for, pssst!
Python script that can be used to log connections from localhost.
### Use code with caution!
This script will create three connections to localhost (127.0.0.1). 
- The first connection will be to port 8080,
- Tthe second connection will be to port 8081,
- and the third connection will be to port 8082. 
- The script will then log the information about each connection to a CSV file called "connections.csv".

### will log
 - time
 - duration
 - files
 - destination_ip 

### Misk
[torproject/stem](https://github.com/torproject/stem)
### Credits
[VolkanSah](https://github.com/volkansah)
