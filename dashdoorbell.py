#!/usr/bin/python

# This was based on http://bit.ly/keschy-dash by Keschy but updated for                   #
# indentation formatting and to remove unnecessary console outputs for running headless.  #
# I have also added additional API parameters, such as URL, HTML and sound.               #

import datetime
import logging
import urllib
import httplib

logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *

# Set your Dash Button's MAC address below
DASH_BUTTON_MAC = 'xx:xx:xx:xx:xx:xx'

# Add your Pushover tokens below
APP_TOKEN = 'ADD_YOURS_HERE'    # The app token - required for Pushover
USER_TOKEN = 'ADD_YOURS_HERE'   # Ths user token - required for Pushover

# Function to trigger the Pushover notification
def pushover():
    conn = httplib.HTTPSConnection("api.pushover.net:443")
    conn.request("POST", "/1/messages.json",
        urllib.urlencode({
            "token": APP_TOKEN,       # Get this from your Pushover app
            "user": USER_TOKEN,       # Get this from your Pushover account
            "html":"0",	                        # 1 to enable
            "title":"Doorbell!",
            "message":"There's somebody at the door!",
            "url":"https://ADDYOUROWN.URL",
            "url_title":"View Link",
            "sound":"pushover",
        }), { "Content-type": "application/x-www-form-urlencoded" })
    conn.getresponse()

# Function to sniff and capture the Dash button's request online
def udp_filter(pkt):
    if pkt.haslayer(DHCP):
        options = pkt[DHCP].options
        for option in options:
            if isinstance(option, tuple):
                if 'requested_addr' in option:
                    mac_to_action[pkt.src]()
                    break

# Below is required to ensure the Dash Button is detected when pushed.
mac_to_action = {DASH_BUTTON_MAC : pushover}
mac_id_list = list(mac_to_action.keys())
sniff(prn=udp_filter, store=0, filter="udp", lfilter=lambda d: d.src in mac_id_list)
