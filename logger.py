# Python script that you can use to log connections to your localhost:

# Python
import stem
import csv

def log_connection(connection):
  time = connection.timestamp
  duration = connection.duration
  files = connection.get_files()
  destination_ip = connection.get_destination_ip()

  with open("connections.csv", "a") as csvfile:
    writer = csv.writer(csvfile, delimiter=",")
    writer.writerow([time, duration, files, destination_ip])

if __name__ == "__main__":
  circuit = stem.Circuit()
  connection = circuit.create_connection("127.0.0.1", 8080)
  log_connection(connection)

  connection = circuit.create_connection("127.0.0.1", 8081)
  log_connection(connection)

  connection = circuit.create_connection("127.0.0.1", 8082)
  log_connection(connection)
# Use code with caution. Learn more
# This script will create three connections to your localhost. 
The first connection will be to port 8080, the second connection will be to port 8081, and the third connection will be to port 8082. 
The script will then log the information about each connection to a CSV file called "connections.csv".

