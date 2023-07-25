#!/usr/bin/env python

import subprocess
# optparse allows us to get arguments from the user and add them to our code
import optparse
import re

def get_arguments():
    # Object that can handle user inputs using arguments
    parser = optparse.OptionParser()

    # Adding options to this object
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")

    # Method with this object called parse_args which allows the object to understand what the user has entered and handle it. also returns the arguments and the values the user entered to a variable.
    (options,arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify an interface, use --help for more info.")

    elif not options.new_mac:
        parser.error("[-] Please specify a new_mac, use --help for more info.")
    return options

def change_mac(interface, new_mac):
    print("[+] Changing MAC address for " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])


def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig_result))

    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print("[-] Could not read MAC address.")

options = get_arguments()
current_mac = get_current_mac(options.interface)
print("Current MAC = " + str(current_mac))

change_mac(options.interface, options.new_mac)

current_mac = get_current_mac(options.interface)
if current_mac == options.new_mac:
    print("[+] MAC address was successfully changed to " + current_mac)
else:
    print("[+] MAC address did not get changed.")

# Allows the user to type multiple answers that aare not requested
#subprocess.call("ifconfig " + interface + " down", shell=True)
# # subprocess.call("ifconfig", shell=True)
# subprocess.call("ifconfig " + interface + " hw ether " + new_mac , shell=True)
# subprocess.call("ifconfig " + interface + " up", shell=True)
# subprocess.call("ifconfig "+ interface, shell=True)
