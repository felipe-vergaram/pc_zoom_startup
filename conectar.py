import pyautogui
import time
import subprocess

print("Este programa preparara el computador para su uso, por favor esperar 1\
      minuto")
print("Creado por FVM")
time.sleep(50)
# Click Connect button
pyautogui.moveTo(760,325)
pyautogui.click()
time.sleep(10)

# Close open windows
pyautogui.moveTo(821,125)
pyautogui.click()

pyautogui.moveTo(851,101)
pyautogui.click()

# Move mouse away from screen
pyautogui.moveTo(1024,325)

# Start Zoom
p ='C:\\Documents and Settings\\Usuario\\Datos de programa\\Zoom\\bin\\Zoom.exe'
subprocess.Popen(p)
