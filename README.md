# Pibrella

###Introduction
Do you have an add on board for your Raspberry Pi called a [Pibrella?](http://pibrella.com/) Then what are you waiting for, let's get programming it!

![](pibrella.jpg)

This project will teach you how to use Scratch GPIO and the Python Pibrella library in order to make use of your Pibrella.

You will require the following components alongside your Raspberry Pi:

- A Pibrella
- An internet connection either by Wifi or Ethernet to get the files you need only.

##Step 0: Set up your Raspberry Pi
You will need to set up your Raspberry Pi to take part in this activity. See the [Raspberry Pi Quick Start Guide here](http://www.raspberrypi.org/help/quick-start-guide/) to get you up and running.

##Step 1: Set up your Raspberry Pi to use Pibrella

The Pibrella fits onto the GPIO pins on your Raspberry Pi. Make sure that your Pi is turned off before pushing it onto the GPIO pins like this:

![]()

Then connect your micro usb power supply to the Pibrella board and your Raspberry Pi shall boot. 

To program your Pibrella you can use Scratch GPIO or Python. If you have not done so already, you will need to download and install Scratch GPIO by ..

To program your Pibrella using Python then you can download and install the Pibrella Python Library by opening an LXTerminal window and first making sure that your software *Raspbian* is up to date. 

Type `sudo apt-get update` and press enter. Then type `sudo apt-get upgrade` and press enter. Once this process is finished type `sudo apt-get install python-pip` followed by `sudo pip install pibrella`.

##Step 2: Test that your Pibrella works

With the Pirella python library downloaded you can easily test to make sure that your Pibrella is working by writing a few lines of code.

###Activity Checklist
1. If you have loaded the desktop environment by styping 'startx' after logging in then you will need to open an LXTerminal window by double clicking on the desktop icon. If you are still on the command line then you can skip this step.
2. Open the text editor nano and name your python pibrella file by typing `nano pibrella.py`.
3. To use the Pibrella library, start your test program by typing `import pibrella`.
4. 

##Step 3: Create a Pibrella Program

