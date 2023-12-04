
# This is the template code for the CNE335 Final Project
#
# CNE 335Fall


# import os
# import subprocess
#
# from Server import Server


#def print_program_info():
    # TODO - Change your nameM
    #print("Server Automator v0.1 by Your Name")

# This is the entry point to our program
#if __name__ == '__main__':
    #print_program_info()


    #server_ip = "54.201.204.242"
    #my_server = Server(server_ip)
    #ping_result = my_server.ping()
    #print(ping_result)

################################################################################################################
# SSH PARAMIKO 12/02

import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname='192.168.10.10', username='ubuntu', key_filename='/home/ubuntu/.ssh/mykey.pem')

stdin, stdout, stderr = ssh.exec_command('lsb_release -a')

for line in stdout.read().splitlines():
    print(line)

ssh.close()

