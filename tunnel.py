import sys
import os
from sshtunnel import SSHTunnelForwarder
import threading

def tunnel(function):
    # SSH and Database Configurations
    ec2_host = "13.52.253.115"  # EC2 instance public IP or hostname
    ssh_username = "ubuntu"        # The SSH username for your EC2 instance (usually 'ec2-user' or 'ubuntu')
    ssh_private_key_path = os.path.join(os.path.dirname(__file__), "TunnelKey.pem")  # Path to your SSH private key
    rds_host = "jeni2.cfeouw8igyj4.us-west-1.rds.amazonaws.com"  # The RDS endpoint
    rds_port = 3306  # Typically, this is the default MySQL port, adjust if you're using a different DBMS
    
    # Create SSH Tunnel through EC2 to access the RDS
    with SSHTunnelForwarder(
        (ec2_host, 22),  # EC2 public IP and SSH port
        ssh_username=ssh_username,
        ssh_pkey=ssh_private_key_path,
        remote_bind_address=(rds_host, rds_port),  # RDS endpoint and port
        local_bind_address=('127.0.0.1', 3307)  # You can set any available local port
    ) as tunnel:
        print(f"Tunnel established at 127.0.0.1:3307")
        
        try:
            while True:
                #input("Press Enter to close the tunnel...")
                function()  # Run your application logic here
        except KeyboardInterrupt:
            print("\nTerminating the tunnel...")
        finally:
           tunnel.stop()  # Manually stop the tunnel
           print("Tunnel closed")   

def start_tunnel():
    ssh_thread = threading.Thread(target=tunnel, daemon=True)
    ssh_thread.start()
