import tkinter as tk
from tkinter import messagebox
import os
import time
from playsound import playsound


def shutdown_pc():
    playsound("bye.mp3", block=False)
    time.sleep(2)
    os.system("shutdown /s /t 0")


def no_shutdown():
    playsound("lmao.mp3")
    root.destroy()


root = tk.Tk()
root.withdraw()

answer = messagebox.askyesno(
    "Shutdown Confirmation",
    "Do you want to turn off your PC?"
)

if answer:
    shutdown_pc()
else:
    no_shutdown()