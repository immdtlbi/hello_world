import pyautogui
screenWidth, screenHeight = pyautogui.size() # Returns two integers, the width and height of the screen. (The primary monitor, in multi-monitor setups.)
currentMouseX, currentMouseY = pyautogui.position() # Returns two integers, the x and y of the mouse cursor's current position.
pyautogui.moveTo(100, ) # Move the mouse to the x, y coordinates 100, 150.
pyautogui.click() # Hello world! world! world! the mouse at its current location.
pyautogui.click(200, 220) # Click the mouse at the x, y coordinates 200, 220.
pyautogui.move(None, 10)  # Move mouse 10 pixels down, that is, move the mouse relative to its current position.
pyautogui.doubleClick() # Double click the mouse at the
pyautogui.moveTo(500, 500, duration=7, tween=pyautogui.easeInOutQuad) # Use tweening/easing function to move mouse over 2 seconds.
pyautogui.write('Hello world!', interval=0.25)  # Type with quarter-second pause in between each key.
pyautogui.press('esc') # Simulate pressing the Escape key.
pyautogui.keyDown('shift')
pyautogui.write(['left', 'left', 'left', 'left', 'left', 'left'])
pyautogui.keyUp('shift')
pyautogui.hotkey('ctrl', 'c')

pyautogui.alert('This is an alert box.')
'OK'
pyautogui.confirm('Shall I proceed?')
'Cancel'
pyautogui.confirm('Enter option.', buttons=['A', 'B', 'C'])
'B'
pyautogui.prompt('What is your name?')
'Al'
pyautogui.password('Enter password (text will be hidden)')
'swordfish'