
# This is the template code for the CNE335 Final Project
# Rasmane Sawadogo
# CNE 335Fall


import os
import subprocess

from Server import Server

os.system("ping -n 1 3.3.11.1")
def print_program_info():
    # TODO - Change your name
    print("Server Automator v0.1 by Your Name")

# This is the entry point to our program
if __name__ == '__main__':
    print_program_info()
    server_ip = "3.3.11.1"
    server = Server(server_ip)



    # TODO - Create a Server object
    # TODO - Call Ping method and print the results

class Server:
    def __init__(self, server_ip):
        self.server_ip = server_ip

    def ping(self):
        try:
            # Use subprocess to run the ping command and capture the output
            result = subprocess.check_output(["ping", "-n", "1", self.server_ip], text=True)
            return result
        except subprocess.CalledProcessError as e:
            return f"Error: {e}"




        # TODO - Call the Ping method and print the results

    ping_result = server.ping()
    print(f"Ping result for {server_ip}:")
    print(ping_result)
