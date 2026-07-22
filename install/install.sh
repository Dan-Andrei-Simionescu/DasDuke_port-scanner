#!/bin/bash

INSTALL_DIR="$(pwd)"

echo '#!/bin/bash' > scan_temp
echo "python3 \"${INSTALL_DIR}/src/port-scanner.py\" \"\$@\"" >> scan_temp

sudo mv scan_temp /usr/local/bin/scan
sudo chmod +x /usr/local/bin/scan

echo "Installing DasDuke Port Scanner..."
sleep 3s

echo "Installation complete!"
echo "You can now run 'scan -t <IP_TARGET> -p <PORT_RANGE>' from anywhere in your terminal."