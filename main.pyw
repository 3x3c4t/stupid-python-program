import tkinter as tk
from tkinter import messagebox
import os
import time
import sys
from playsound import playsound


def path(filename):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, filename)


def shutdown_pc():
    playsound(path("bye.mp3"), block=False)
    time.sleep(2)
    os.system("shutdown /s /t 0")


def no_shutdown():
    playsound(path("lmao.mp3"))
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