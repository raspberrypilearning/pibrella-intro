# Getting started with Pibrella 

##Step 1: Set up your Raspberry Pi to use Pibrella

The Pibrella fits onto the GPIO pins on your Raspberry Pi. Make sure that your Pi is turned off before pushing it onto the GPIO pins like this:

![](add-pibrella.jpg)

Then connect your micro usb power supply to the Pibrella board and your Raspberry Pi shall boot. 

To program your Pibrella you can use [Scratch GPIO](http://scratchgpio.github.io) or Python. In this tutorial we will be using Python. 

To program your Pibrella using Python then you can download and install the Pibrella Python Library by opening an LXTerminal window and first making sure that your software *Raspbian* is up to date. 

###Activity Checklist:

1. Type `sudo apt-get update` and press enter. 
1. Then type `sudo apt-get upgrade` and press enter. 
1. Once this process is finished type `sudo apt-get install python-pip` followed by `sudo pip install pibrella`.

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


##Step 3: Create a Random Looping Light Program
As well as using the Pibrella library in a simple program, you can also use the functionality of other libraries like random and time. 

###Activity Checklist:
1. Create a new python file by typing `nano disco.py` in an LXTerminal window or on the command line. A new and empty text editor file will open. 
2. On the first line, import the libraries which you will need to use:

  ```python
  import pibrella, random, time
  ```
3. Then label each of the lights like this:
  
  ```python
  red = pibrella.light.red
  amber = pibrella.light.amber
  green = pibrella.light.green
  ```
  Each label is called a variable. Variables have been used here to store the long command as a short hand for the next step.

4. Underneath, add the colour names to a list like this:
  
  ```python
  colour = [red, amber, green]
  ```
  Items, like colours, can be stored in a list and given a name in Python. You can also write this list like this `colour = [pibrella.light.red, pibrella.light.amber, pibrella.light.green] instead of using variable names to store the command. 
  
5. Now you have set up the program, create a loop using `while True:` that selects a random colour light from the list of colours and then turn on and off that light for 0.2 of a second:

  ```python
  while True:
      result = random.choice(colour)
      time.sleep(1)
      result.pulse(0.2)
  ```
  
  Inside this loop that will repeat forever, you have used the random.choice function to select a colour from the colour list you created at random and then store it in the variable called result. After 1 second the colour led that was selected at random and stored in the result variable will pulse for 0.2 of a second.
  
6. Now save and exit by pressing **CTRL** and **X** on the keyboard and then **Y** for yes. 
7. To run your program type `sudo python disco.py` 
8. As you have used a continual loop this program will not end untill you press and hold **CTRL** and **C** on the keyboard to interput it. We can fix this in the next step.

##Step 4: Loop 5 times
Now that you have a looping disco light, let's add some code so that it only repeats for a number of times, rather than forever.

###Activity Checklist:
1. Open your disco program by typing `nano disco.py` in an LXTerminal window or from the command line. 
1. Using the arrows on your keyboard, naviagte down to just underneath the colour list and before the while loop. Type `n = 0` to store the numeric value 0 as a variable.
1. Then amend the while loop to read:

  ```python
  while n < 5:
      esult = random.choice(colour)
      time.sleep(1)
      result.pulse(0.2)
      n = n + 1
  ```
  

## Step 5: Using a function to store your disco light loop.  


## Step 6: Using a button to start your Disco program 
Now that you have a disco pibrella program working you can start to use some of the other items on the pibrella board, for example something to trigger the program, an input button.
