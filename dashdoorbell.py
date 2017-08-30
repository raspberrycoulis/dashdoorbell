#!/usr/bin/python

import datetime
import logging
import urllib
import httplib
  
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *
  
def button_pressed_dash1():
    #current_time = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d_%H:%M:%S')
    #print 'Button Pressed at ' + current_time
    conn = httplib.HTTPSConnection("api.pushover.net:443")
    conn.request("POST", "/1/messages.json",
        urllib.urlencode({
            "token":"PUSHOVER_API_TOKEN",
            "user":"PUSHOVER_USER_TOKEN",
            "html":"0",	# 1 to enable
            "title":"Doorbell!",
            "message":"There's somebody at the door!",
            "url":"https://ADDYOUROWN.URL",
            "url_title":"View Link",
            "sound":"pushover",
        }), { "Content-type": "application/x-www-form-urlencoded" })
    conn.getresponse()
 
 
def udp_filter(pkt):
    options = pkt[DHCP].options
    for option in options:
        if isinstance(option, tuple):
            if 'requested_addr' in option:
                mac_to_action[pkt.src]()
                break
  
mac_to_action = {'xx:xx:xx:xx:xx:xx' : button_pressed_dash1} # Add MAC address in lowercase
mac_id_list = list(mac_to_action.keys())
  
#print "Waiting for a button press..."
sniff(prn=udp_filter, store=0, filter="udp", lfilter=lambda d: d.src in mac_id_list)
  
if __name__ == "__main__":
 main()

