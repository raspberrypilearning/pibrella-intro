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

![](add-pibrella.jpg)

Then connect your micro usb power supply to the Pibrella board and your Raspberry Pi shall boot. 

To program your Pibrella you can use [Scratch GPIO](http://scratchgpio.github.io) or Python. In this tutorial we will be using Python. 

To program your Pibrella using Python then you can download and install the Pibrella Python Library by opening an LXTerminal window and first making sure that your software *Raspbian* is up to date. 

###Activity Checklist:

Type `sudo apt-get update` and press enter. Then type `sudo apt-get upgrade` and press enter. Once this process is finished type `sudo apt-get install python-pip` followed by `sudo pip install pibrella`.

##Step 2: Test that your Pibrella works

With the Pirella python library downloaded you can easily test to make sure that your Pibrella is working by writing a few lines of code.

###Activity Checklist:
1. If you have loaded the desktop environment by styping `startx` after logging in then you will need to open an LXTerminal window by double clicking on the desktop icon. If you are still on the command line then you can skip this step.
2. Open the text editor nano and name your python pibrella file by typing `nano test.py`.
3. To use the Pibrella library, start your test program by typing `import pibrella` and then leave a line by pressing enter.
4. Underneath type the line `pibrella.lights.on()`.
5. Beneath this type `pibrella.buzzer.success()`. 
6. Then Press **CTRL** and **X** on the keyboard, followed by **Y** to save and exit the text editor nano.
7. Run your test code by typing `sudo python test.py`. You should see the lights on the Pibrella board turn on and hear a tune coming from the buzzer. 
8. To stop the program press **CTRL** and **C**.

##Step 3: Create a Pibrella Program

Now you know that your Pibrella is operating correctly, with the led lights turning on and off, and the buzzer sounding a tune, you can start to write a python program to control it.

###Activity Checklist:
1. Create a new python file by typing `nano pibrella.py` in an LXTerminal window or on the command line. This will open a text editor wndow, just like before.
2. 
