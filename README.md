# Amazon Dash as a doorbell using Pushover

Configure an Amazon Dash Button as a doorbell with the help of a Raspberry Pi using Pushover.

## Required pre-requisites:

This app relies on [Pushover](https://pushover.net) which costs around £4.99 on iOS / Android. You'll need to create an app in Pushover as you'll need the API and user tokens later. Further details on how to create an app can be found part-way through [this guide](https://www.raspberrycoulis.co.uk/coding/add-push-notifications-motioneye-os/).

Please run the following before:

````
sudo apt-get update && sudo apt-get upgrade -y
sudo apt-get install python-scapy tcpdump -y
````

## Capturing the Amazon Dash Button's MAC address

Setup the Amazon Dash Button using the iOS or Android app, but stop before you add a product. Force close the app on your device to be safe.

There are various methods to obtaining the MAC address of the Dash Button, but I simply used [Fing](https://www.fing.io/) to scan my network and then copied the MAC address from the button.

## Clone this repository

Unless you want to manually create the Python script yourself, simply clone this by running:

````git clone https://github.com/raspberrycoulis/dashdoorbell.git````

## Substitute the relevant parts in the dashdoorbell.py script

Specifically, you'll need:

* MAC address of your Amazon Dash Button
* Pushover API and user tokens

You can also customise the message received in Pushover by editing any of the following:

* title
* message
* url
* url_title
* sound (a full list of the sound effects in Pushover can be found [here](https://pushover.net/api#sounds)

If you are feeling creative, you can also enable HTML messaging by changing `html` from `0` to `1`.
