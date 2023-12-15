import subprocess
import socket
import platform

def get_network_prefix():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    network_prefix = '.'.join(ip_address.split('.')[:-1]) + '.'

    return network_prefix

def get_ip_range():
    start_ip = int(input("Enter the start of the IP range: "))
    end_ip = int(input("Enter the end of the IP range: "))

    return start_ip, end_ip

def lan_scanner(start_ip=1, end_ip=250):
    network_prefix = get_network_prefix()

    for i in range(start_ip, end_ip + 1):
        ip_address = network_prefix + str(i)
        
        if platform.system() == 'Windows':
            command = ['ping', '-n', '1', '-w', '100', ip_address]  # Windows command
        else:
            command = ['ping', '-c', '1', '-W', '1', ip_address]  # Linux/Mac command
        
        try:
            subprocess.check_output(command, stderr=subprocess.STDOUT)
            print(f"Host {ip_address} is up!")
            
        except subprocess.CalledProcessError:
            print(f"Host {ip_address} is down.")

start_ip, end_ip = get_ip_range()

if start_ip > end_ip:
    print("Invalid IP range.")
    exit()

if start_ip < 1 or end_ip > 255:
    print("Invalid IP range.")
    exit()

if start_ip == end_ip:
    print("Scanning a single host.")

lan_scanner(start_ip, end_ip)
