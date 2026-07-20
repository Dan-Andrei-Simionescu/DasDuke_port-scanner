import socket
import ports
import CL_arguments

from concurrent.futures import ThreadPoolExecutor, as_completed

def scan_port(target, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)
    result = sock.connect_ex((target, port))
    sock.close()
    return port, result == 0

if __name__ == "__main__":
    target = CL_arguments.args.target
    start_port = CL_arguments.start_port
    end_port = CL_arguments.end_port

    print(f"    ＞ Scanning {target} ports {start_port}-{end_port}...")

    open_ports = []

    with ThreadPoolExecutor(max_workers=100) as executor:
        futures = {
            executor.submit(scan_port, target, port): port
            for port in range(start_port, end_port + 1)
        }
        
        for future in as_completed(futures):
            port, is_open = future.result()
            if is_open:
                open_ports.append(port)

    open_ports.sort()

    if open_ports:
        for port in open_ports:
            port_name = ports.find_port_name(port)
            print(f"      ⦕ Port {port_name} is open!")
    else:
        print("      !!! Nothing found.")

    print("    Scan complete.")