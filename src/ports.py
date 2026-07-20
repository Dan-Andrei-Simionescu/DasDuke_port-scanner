import os

# empty dictionary
port_dict = {}

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SERVICES_FILE = os.path.join(BASE_DIR, "services.txt")

def load_services_file(filename="services.txt"):
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            
            # Skip empty lines or comments
            if not line or line.startswith('#'):
                continue
            # Split the line into its parts
            parts = line.split()
            if len(parts) >= 2:
                service_name = parts[0]
                port_and_proto = parts[1]
                
                # Extract just the number from '80/tcp'
                if '/' in port_and_proto:
                    port_str = port_and_proto.split('/')[0]
                    
                    if port_str.isdigit():
                        # Store it in the dictionary (uppercase)
                        port_dict[int(port_str)] = service_name.upper()

load_services_file()

def find_port_name(port_index):
    if port_index in port_dict:
        return port_dict[port_index]
    else:
        return f"{port_index} (UNKNOWN)"
    