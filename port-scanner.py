import socket
import ports
import CL_arguments

def scan_port(target, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)
    result = sock.connect_ex((target, port))
    sock.close()
    return result == 0

if __name__ == "__main__":
    print(f"Scanning ports...")

    found_anything = False

    for port in range(CL_arguments.start_port, CL_arguments.end_port + 1):
        is_open = scan_port(CL_arguments.args.target, port)
        
        if is_open:
            port_name = ports.find_port_name(port)
            print(f"Port {port_name} is open!")
            found_anything = True
    
    if not found_anything:
        print("Nothing found.")

    print("Scan complete.")