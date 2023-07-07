# stem logger for localhost in python
# source https://github.com/VolkanSah/Stem-local-log.py/
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
  # ad more if you need ;)
  # Use code with caution, please!
