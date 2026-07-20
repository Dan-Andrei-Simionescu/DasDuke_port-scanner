# DasDuke Port Scanner

A modular TCP port scanner written in Python, built around `socket`, `argparse`, and a custom port registry loaded from a local `services.txt` file. It scans a target IP across a configurable port range, identifies open ports by name, and reports results directly in the terminal.

## Features

- **TCP connect scan** — for each port in the range, opens a socket and attempts a full TCP handshake via `connect_ex()`. A return value of `0` means the port is open; anything else means closed or filtered.
- **Configurable port range** — pass `-p <start>-<end>` (e.g. `-p 1-1024`) to choose what to scan. Defaults to `1-1024` if omitted.
- **Service name resolution** — open ports are matched against a local `services.txt` registry (same format as `/etc/services`) and displayed by name (e.g. `Port SSH is open!`). Falls back to `UNKNOWN` for unregistered ports.
- **"Nothing found" feedback** — if no open ports are discovered in the range, the scanner explicitly says so rather than exiting silently.
- **CLI interface** — no interactive prompts; all input is passed as flags at launch.
- **Modular structure** — scanner logic, argument parsing, and port name resolution are split across separate files.

## Project structure

```
Python_port_scanner/
├── port_scanner.py      # Main scan loop and result output
├── CL_arguments.py      # argparse setup and port range parsing
├── ports.py             # services.txt loader and port name lookup
├── services.txt         # Custom port registry (name / port / protocol)
└── README.md
```

## How it works

**`CL_arguments.py`** sets up the argument parser, reads `-t` (target IP) and `-p` (port range), and splits the range string into `start_port` and `end_port` integers that the main script imports.

**`ports.py`** reads `services.txt` line by line at import time, skipping comments and blank lines, and builds a dictionary mapping port numbers to service names. `find_port_name(port)` looks up a port in that dictionary and returns `UNKNOWN` if it isn't found.

**`port_scanner.py`** imports both modules, iterates over the port range, calls `scan_port()` for each one, and prints results as they come in. After the loop, it checks the `found_anything` flag and prints `Nothing found.` if no open ports were discovered.

## Requirements

- Python 3.x (no third-party packages — standard library only)

First, check if Python 3 is already installed on your system by running:

```console
python3 --version
```

If it is not installed, follow the instructions for your operating system below.

On Debian/Ubuntu:

```console
sudo apt update
sudo apt install python3 -y
```

On macOS:

```console
brew install python
```

## Usage

```console
# Clone the repository
git clone https://github.com/Dan-Andrei-Simionescu/DasDuke_port-scanner.git
cd DasDuke_port-scanner/install; chmod +x install.sh; ./install.sh

# Scan ports 1–1024 on a target (default range)
scan -t 8.8.8.8

# Scan a custom port range (from port 20 to 500)
scan -t 192.168.1.1 -p 20-500

# Scan a single port
scan -t 192.168.1.1 -p 80-80
```
