import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname='34.219.16.35', username='ec2-user', key_filename= r"C:\Users\Master_Ras\Downloads\AWS_RasyKey.pem")

cmd = [
    'sudo yum update -y',
    'sudo ym upgrade -y'
]

for cmd in cmd:
    print(f"Running command: {cmd}")
    stdin, stdout, stderr = ssh.exec_command(cmd)
    print(stdout.read().decode('utf-8'))
    print(stderr.read().decode('utf-8'))

ssh.close()




