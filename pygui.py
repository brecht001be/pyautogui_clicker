import random
from time import sleep
import pyautogui


refresh = (2008,57)
back = (1944,59)
advertisement = (2056,873)

def randomSleep():
  delay = random.randint(5,10)
  print("Sleeping for:", delay, "s ...") # test comment
  sleep(delay)

# moves to (1717,352) in 1 sec
def goToAndClick(coords, duration):
    pyautogui.moveTo(coords[0] + random.randint(0,4), coords[1] + random.randint(0,4), duration)
    pyautogui.click() # another comment added here
 
while True:
  print("Clicked Advertisement...")
  goToAndClick(advertisement, 1)
  randomSleep()
  print("Clicked Back...")
  goToAndClick(back, 1)
  randomSleep()
  print("Clicked Refresh...")
  goToAndClick(refresh, 1)
  randomSleep()
