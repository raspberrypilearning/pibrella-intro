import pibrella, random, time

red = pibrella.light.red
amber = pibrella.light.amber
green = pibrella.light.green

colour = [red, amber, green]

def disco():
    n = 0
    while n < 5:
        result = random.choice(colour)
        time.sleep(1)
        result.pulse(0.2)
        n = n + 1
    
while True:
    if pibrella.button.read():
        disco()
        time.sleep(5)
        break
