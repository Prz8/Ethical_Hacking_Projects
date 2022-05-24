#!/usr/bin/env python

import subprocess
import optparse
import re


def get_args():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface whose mac has to be changed")
    parser.add_option("-m", "--mac-addr", dest="macAddr", help="New MAC Address")
    (options, arguments) =  parser.parse_args()
    if not options.interface:
        parser.error("[-] Please Specify an interface, use --help for more info")
    elif not options.macAddr:
        parser.error("[-] Please Specify a new mac address, use --help for more info")
    return options


def is_valid_interface(interface):
    interfaces = subprocess.check_output("ifconfig -a | sed 's/[ \t].*//;/^$/d'", shell=True)
    interfaces = str(interfaces).split(':\n')
    return interface in interfaces


def change_mac(interface, mac_addr):
    if not is_valid_interface(interface):
        print("[-] Not a valid interface " + interface)
        exit(0)
    current_mac_addr = get_current_mac_address(interface)
    if current_mac_addr == mac_addr:
        print("[-] Current MAC address is same as provided "+current_mac_addr)
        exit(0)
    print("[+] Changing MAC address for " + interface + " from " + current_mac_addr + " to " + mac_addr)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", mac_addr])
    subprocess.call(["ifconfig", interface, "up"])
    new_mac_addr = get_current_mac_address(interface)
    if mac_addr == new_mac_addr:
        print("[+] New MAC address " + new_mac_addr)
    else:
        print("[-] MAC address didn't get change")


def get_current_mac_address(interface):
    mac_address = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", subprocess.check_output(["ifconfig", interface]))
    if not mac_address:
        print("[-] could not found MAC address")
    else:
        return mac_address.group(0)


options = get_args()
change_mac(options.interface, options.macAddr)