<h1>Requirements</h1>
<ul>
  <li>Python3.x</li>
  <li>This script is designed for UNIX-like systems (e.g.,Linux, macOS)</li>
</ul>
<h2>Functions:</h2>
<ol>
  <li><b>get_arguments():</b></li>
    <ul>
      <li>Uses the <b>optparse</b> module to parse command-line arguments.</li>
      <li>Takes two arguments from the user:</li>
      <ul>
        <li> <b>-i</b> or <b>--interface</b>: Specifies the network interface whose MAC address needs to be changed.</li>
        <li> <b>-m</b> or <b>--mac</b>: Specifies the new MAC address..</li>
      </ul>
      <li>If the user does not provide either of these arguments, the script will produce an error message and exit.</li>
      <li>Returns the parsed options.</li>
    </ul>
  <li><b>change_mac(interface, new_mac):</b></li>
  <ul>
    <li>This function is responsible for changing the MAC address.</li>
    <li>It first prints a message indicating the change.</li>
    <li>Then, it uses the <b>subprocess</b> module to execute system commands to bring the interface down, change its MAC address, and then bring the interface back up.</li>
  </ul>
  <li><b>get_current_mac(interface): </b></li>
  <ul>
    <li>Retrieves the current MAC address of the specified network interface.</li>
    <li>It uses the <b>ifconfig</b> command and the <b>re</b> (regular expression) module to extract the MAC address from the command's output.</li>
    <li>If a MAC address is found, it's returned; otherwise, an error message is printed.</li>
  </ul>
  <h2>Execution</h2>
  <ol>
    <li>The script starts by fetching the command-line arguments using the <b>get_arguments()</b> function.</li>
    <li>It retrieves and prints the current MAC address of the specified interface.</li>
    <li>It attempts to change the MAC address to the one provided by the user.</li>
    <li>Finally, it checks and verifies if the MAC address was successfully changed, and prints the result.</li>
  </ol>
  <h2>Usage</h2>
  <p>Execute the script with the necessary arguments</p>
  
   ``` bash
      python <script_name>.py -i <interface_name> -m <new_mac_address>
   ```

  <p>Replace <b><'script_name'></b> with the name you've saved this script as (e.g.,<b> change_mac.py), <'interface_name'></b> with the name of your network interface (e.g., <b>eth0</b> or <b>wlan0</b>), and <b><'new_mac_address'></b> with the desired MAC address (e.g., <b>00:11:22:33:44:55</b>).</p>

</ol>
<p><b>Note:</b> Changing your MAC address can affect network connectivity and is often used for spoofing or privacy purposes. Always ensure you understand the implications and have the appropriate permissions before changing it. This script requires administrative (root) privileges to modify network interface settings.</p>
