import argparse

parser = argparse.ArgumentParser(description="DasDuke Port Scanner")
parser.add_argument("-t", dest="target", required=True, help="Target IP address")
parser.add_argument("-p", dest="ports", default="1-1024", help="Port range to scan")
args = parser.parse_args()

parts = args.ports.split("-")
start_port = int(parts[0])
end_port = int(parts[1])

