How to install openvpn on Ubuntu 16 Desktop.

First, in a the terminal install the following packages:

sudo apt-get install network-manager network-manager-openvpn

Then restart the network-manager daemon

sudo service network-manager restart

Unzip the openvpn zip with the configuration inside it.

In the UI, do the following steps:

•	Go to Settings -> Network
•	Add the “+” icon in the lower-left corner and select VPN
•	Select “Import a saved VPN configuration”
•	Click on “Create” and point to the just unzipped vpn configuration files.
•	Fill-out the username and password. Also use your password in the Private Key Password field

Click “Save”, Now you can toggle the vpn and access https://jenkins01.vadain.nl for example.
