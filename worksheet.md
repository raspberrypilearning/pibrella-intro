# Getting started with Pibrella 

## Step 1: Set up your Raspberry Pi to use Pibrella

### Activity checklist:

1. The Pibrella fits onto the GPIO pins on your Raspberry Pi. Make sure that your Pi is turned off before pushing it onto the GPIO pins.
1. Then connect your micro USB power supply to the Pibrella board, and your Raspberry Pi will boot. 

  *Note:To program your Pibrella you can use [Scratch GPIO](http://scratchgpio.github.io) or Python. In this tutorial we will be using Python.* 

1. To program your Pibrella using Python, download and install the Pibrella Python Library by opening an LXTerminal window and first making sure that your software *Raspbian* is up to date. 

### Activity checklist:

1. Type `sudo apt-get update` and press Enter. 
1. Then type `sudo apt-get upgrade` and press Enter. 
1. Once this process is finished, type `sudo apt-get install python-pip` followed by `sudo pip install pibrella`.

## Step 2: Test that your Pibrella works

With the Pibrella Python library downloaded, you can easily test to make sure that your Pibrella is working by writing a few lines of code.

### Activity checklist:

1. If you have loaded the desktop environment by typing `startx` after logging in, then you will need to open an LXTerminal window by double-clicking on the desktop icon. If you are still on the command line then you can skip this step.
2. Open the text editor nano and name your Python Pibrella file by typing `nano test.py`.
3. To use the Pibrella library, start your test program by typing `import pibrella` and then leave a line by pressing Enter.
4. Underneath type the line `pibrella.lights.on()`.
5. Beneath this type `pibrella.buzzer.success()`. 
6. Then press **CTRL** and **X** on the keyboard, followed by **Y** to save and exit the text editor nano.
7. Run your test code by typing `sudo python test.py`. You should see the lights on the Pibrella board turn on and hear a tune coming from the buzzer. 
8. To stop the program press **CTRL** and **C**.


## Step 3: Create a random looping light program

As well as using the Pibrella library in a simple program, you can also use the functionality of other libraries like `random` and `time`. 

### Activity checklist:

1. Create a new Python file by typing `nano disco.py` in an LXTerminal window or on the command line. A new and empty text editor file will open. 
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
  
  Each label is called a variable. Variables have been used here to store the long command as a shorthand for the next step.

4. Underneath, add the colour names to a list like this:
  
  ```python
  colour = [red, amber, green]
  ```
  
  Items, like colours, can be stored in a list and given a name in Python. You can also write the list like this `colour = [pibrella.light.red, pibrella.light.amber, pibrella.light.green] instead of using variable names to store the command. 
  
5. Now you have set up the program, create a loop using `while True:` that selects a random colour from the list of colours, and then turns the corresponding light on and off for 0.2 second:

  ```python
  while True:
      result = random.choice(colour)
      time.sleep(1)
      result.pulse(0.2)
  ```
  
  Inside this loop, which will repeat forever, you have used the random.choice function to select a colour from the list you created at random and then store it in the variable called `result`. After 1 second the colour LED that was selected at random and stored in the result variable will pulse for 0.2 second.
  
6. Now save and exit by pressing **CTRL** and **X** on the keyboard and then **Y** for yes. 
7. To run your program type `sudo python disco.py`. 
8. As you have used a continual loop, this program will not end until you press and hold **CTRL** and **C** on the keyboard to interrupt it.

## Step 4: Loop 5 times

Now that you have a looping disco light, let's add some code so that it only repeats for a number of times, rather than forever.

### Activity checklist:

1. Open your disco program by typing `nano disco.py` in an LXTerminal window or from the command line. 
1. Using the arrows on your keyboard, navigate down to just underneath the colour list and before the `while` loop. Type `n = 0` to store the numeric value 0 as a variable.
1. Then amend the `while` loop to read:

  ```python
  n = 0
  
  while n < 5:
      result = random.choice(colour)
      time.sleep(1)
      result.pulse(0.2)
      n = n + 1
  ```
  
  Instead of giving the command `while True:` to loop forever, you have used `while n < 5:` or while `n` is less than or equal to the value of 5. That means that this loop will only repeat whilst `n` contains a value that is less than 5 or 5. You have already set the value of `n` as 0 before the loop starts. Then at the bottom of the loop you have added the line `n = n + 1` which will add 1 to the value each time round the loop. For example, 0 + 1, then 1 + 1, then 2 + 1, and so on, each time storing the new value in the variable `n`. 
  
1. Now save and exit by pressing **CTRL** and **X** on the keyboard and then **Y** for yes. 
1. To run your program type `sudo python disco.py`. 

## Step 5: Using a function to store your disco light loop

Functions allow you to store parts of code so that you can use them again later on. Let's put your new loop into a function.

### Activity checklist:

1. With your disco.py program open, navigate to the line `n = 0` and wrap your code in a function like this:
  
  ```python
  def disco():
      n = 0
      while n < 5:
          result = random.choice(colour)
          time.sleep(1)
          result.pulse(0.2)
          n = n + 1
  ```        
  
  If you run your program now nothing will happen, because like variables you have given this piece of a code a name. You have not yet called it to run!

1. Beneath the loop type `disco()`.
1. Now save and run the code to see what happens!

## Step 6: Using a button to start your Disco program 

Now that you have a disco Pibrella program working you can start to use some of the other items on the Pibrella board, for example an input button to trigger the program. Putting the looping code in a function makes this super easy to do.

### Activity checklist:

1. Beneath the disco function create a forever repeating loop like this:

  ```python
  while True:
      if pibrella.button.read():
          disco()
  ```  
  
  Inside the loop is a condition, which means the disco function will only be triggered if the condition is met. In this case the condition is met when the button is pressed. 
  
1. Save your code and run it to see what happens.
1. You may have noticed that the lights keep flashing now. You can break out of the continuous loop after 5 seconds by typing `break`inside the `while True:` loop like this:

  ```python
  while True:
      if pibrella.button.read():
          disco()
          time.sleep(5)
          break
  ```        
