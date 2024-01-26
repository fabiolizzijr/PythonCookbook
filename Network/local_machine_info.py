# Simple script to get ip adress, machine info
# Import
import socket

# Create a function to display host_name and ip_adress
def print_machine_info():
    """ () -> str
    Return two str, one with host_name and second with it's ip adress

    >>> print_machine_info()
    Host name: michelle
    Ip adress: 192.168.181.1
    """
    host_name = socket.gethostname() # Get the host_name
    ip_adress = socket.gethostbyname(host_name) # Use host_name to get ip_adress

    # Print a nice report
    print(f"Host name: {host_name}")
    print(f"Ip adress: {ip_adress}")

# Call the function to test if
print_machine_info()