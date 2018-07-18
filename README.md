# Amazon Dash as a doorbell using Pushover

Configure an Amazon Dash Button as a doorbell with the help of a Raspberry Pi using Pushover.

## Required pre-requisites:

This app relies on [Pushover](https://pushover.net) which costs around £4.99 on iOS / Android. You'll need to create an app in Pushover as you'll need the API and user tokens later. Further details on how to create an app can be found part-way through [this guide](https://www.raspberrycoulis.co.uk/coding/add-push-notifications-motioneye-os/).

Please run the following before:

```bash
sudo apt-get update && sudo apt-get dist-upgrade -y
sudo apt-get install python-scapy tcpdump python-pip -y
sudo pip install requests
```

## Find your Amazon Dash Button's MAC address

You will need to add your Amazon Dash Button's MAC address to the `dashdoorbell.py` script for this to work. Details on how to find out your MAC address can be found [here](https://www.raspberrypi.org/magpi/hack-amazon-dash-button-raspberry-pi/) and then replace the following in the script:

```python
# Set your Dash Button's MAC address below
DASH_BUTTON_MAC = 'xx:xx:xx:xx:xx:xx'
```

Replace the `xx:xx:xx:xx:xx:xx` with your MAC address, but ensure **it is all lower case!**

## Clone this repository

Unless you want to manually create the Python script yourself, simply clone this by running:

```bash
git clone https://github.com/raspberrycoulis/dashdoorbell.git
```

## Substitute the relevant parts in the dashdoorbell.py script

Specifically, you'll need:

* MAC address of your Amazon Dash Button
* Pushover API and user tokens

You can also customise the message received in Pushover by editing any of the following:

* title
* message
* url
* url_title
* sound (a full list of the sound effects in Pushover can be found [here](https://pushover.net/api#sounds))

If you are feeling creative, you can also enable HTML messaging by changing `html` from `0` to `1`.

## Running on boot

I prefer to use systemd to run Python scripts on boot as you can run them as a service, start, stop, restart them and check the status of them easily. To do so, you need to do the following:

```bash
sudo nano /lib/systemd/system/dashdoorbell.service
```

Then add the following:

```bash
[Unit]
Description=Amazon Dash Doorbell Service
After=multi-user.target

[Service]
Type=idle
ExecStart=/usr/bin/python /home/pi/github/dashdoorbell/dashdoorbell.py > /home/pi/github/dashdoorbell/dashdoorbell.log 2>&1
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
```

The parts to check are the `ExecStart` command as this assumes the `dashdoorbell.py` script is located in `/home/pi/github/dashdoorbell` so please update accordingly if you have installed the script in a different location.

Once you have done this, `Ctrl+X` to exit and `Y` to save then run:

```bash
sudo chmod 644 /lib/systemd/system/dashdoorbell.service
sudo systemctl daemon-reload
sudo systemctl enable dashdoorbell.service
```

You can `sudo reboot` or simply run `sudo systemctl start dashdoorbell.service` to start the script. Check the status by running `sudo systemctl status dashdoorbell.service`.
