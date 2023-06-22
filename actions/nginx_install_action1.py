import paramiko

from st2common.runners.base_action import Action

class Nginx(Action):
    def run(self):

        ubuntu_ip = '15a8810bac11'
        username = 'root'
        password='root'

        # Create an SSH client
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        try:
            # Connect to the Ubuntu container
            ssh.connect(ubuntu_ip, username=username, password=password)

            # Install Nginx
            install_command = 'apt-get update && apt-get install -y nginx'
            stdin, stdout, stderr = ssh.exec_command(install_command)

            # Check the installation result
            if stderr.channel.recv_exit_status() == 0:
                print('Nginx installed successfully.')
            else:
                print('Failed to install Nginx. Error:', stderr.read().decode())
        finally:
            # Close the SSH connection
            ssh.close()


