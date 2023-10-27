<h1>Network Scanner:</h1>
<p>This is a simple Python script that utilizes the Scapy library to scann a network and display the IP and MAC addresses of the devices in the network.</p>
<h2>Requirements: </h2>
<ul>
  <li> Python 3.x </li>
  <li>Scapy library</li>
</ul>

<h2> How to Install: </h2>
<ol>
  <li> Install Python from Python's official website. </li>
  <li> Install Scapy library using pip: </li>
  
   ``` bash
      pip instll scapy
   ```
  
</ol>
<!--
<h2>Usage:</h2>
   <ul>
   ``` php
      python <script_name>.py -t <target_ip_range> ```
   ```
  <
<script_name>: Name of this script (e.g., network_scanner.py).
<target_ip_range>: IP range to scan. For example, 192.168.1.1/24 to scan all devices between 192.168.1.1 and 192.168.1.254.
Functionality:
get_arguments():

Uses optparse to parse command line options.
The user must provide a target IP or IP range with the -t or --target flags.
Returns the provided options.
scan(ip):

Initiates an ARP (Address Resolution Protocol) request to the specified IP address or IP range.
Broadcasts the ARP request to the network to get a list of devices that respond.
Processes the list of answered responses to extract IP and MAC addresses.
Returns a list of dictionaries with keys "ip" and "mac" representing the IP and MAC addresses of the responding devices.
print_result(results_list):

Takes the list of dictionaries from scan(ip).
Prints the IP and MAC addresses in a tabulated format.
Execution Flow:
The script starts by fetching the command-line arguments using the get_arguments() function.
The script then scans the network using the provided target IP range with the scan() function.
Finally, the results are displayed using the print_result() function.
-->
