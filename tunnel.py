import os
from sshtunnel import SSHTunnelForwarder
import threading

class SSHTunnel:
    def __init__(self):
        # SSH and Database Configurations
        self.ec2_host = "13.52.253.115"  # EC2 instance public IP or hostname
        self.ssh_username = "ubuntu"  # The SSH username for your EC2 instance
        self.ssh_private_key_path = os.path.join(os.path.dirname(__file__), "TunnelKey.pem")  # Path to your SSH private key
        self.rds_host = "jeni2.cfeouw8igyj4.us-west-1.rds.amazonaws.com"  # The RDS endpoint
        self.rds_port = 3306  # The RDS port (typically 3306 for MySQL)
        
        # Start the tunnel
        self.tunnel = None
        self.start_tunnel()

    def start_tunnel(self):
        # Create SSH Tunnel through EC2 to access the RDS
        self.tunnel = SSHTunnelForwarder(
            (self.ec2_host, 22),  # EC2 public IP and SSH port
            ssh_username=self.ssh_username,
            ssh_pkey=self.ssh_private_key_path,
            remote_bind_address=(self.rds_host, self.rds_port),  # RDS endpoint and port
            local_bind_address=('127.0.0.1', 3307)  # You can set any available local port
        )
        self.tunnel.start()
        print(f"Tunnel established at 127.0.0.1:3307")

    def stop_tunnel(self):
        if self.tunnel and self.tunnel.is_active:
            self.tunnel.stop()
            print("Tunnel closed")

    def __del__(self):
        # Stop the tunnel when the object is destroyed
        self.stop_tunnel()

# Usage example
if __name__ == "__main__":
    ssh_tunnel = SSHTunnel()
    # Your function or code that interacts with the RDS here
    # The tunnel will automatically close when the object is deleted or the program ends
