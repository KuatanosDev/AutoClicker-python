import tkinter as Tk
from tkinter import messagebox
import pyautogui
import threading
import time
import keyboard
root = Tk.Tk()
root.title("Autoclicker")
root.geometry("300x300")
root.resizable(False, False)
root.configure(bg="black")

button = Tk.Button(root, text = 'Destroy', command=root.destroy,bg = 'red', fg = 'black', font = ('Arial' ))
button.place(x=100, y =60)

def b2_clicked():
    left_clicking = False
    right_clicking = False

    def left_autoclicker():
        while left_clicking:
            pyautogui.click(button='left')
            time.sleep(0.01)  

    def right_autoclicker():
        while right_clicking:
            pyautogui.click(button='right')
            time.sleep(0.01) 
    def toggle_left_autoclicker():
        nonlocal left_clicking
        left_clicking = not left_clicking
        if left_clicking:
            threading.Thread(target=left_autoclicker, daemon=True).start()

    def toggle_right_autoclicker():
        nonlocal right_clicking
        right_clicking = not right_clicking
        if right_clicking:
            threading.Thread(target=right_autoclicker, daemon=True).start()

    if button2['bg'] == 'red':
        button2.configure(bg='green')
        
        
        keyboard.add_hotkey('g', toggle_left_autoclicker)
        keyboard.add_hotkey('h', toggle_right_autoclicker)
    else:
        button2.configure(bg='red')
        
        
        left_clicking = False
        right_clicking = False
        keyboard.remove_hotkey('g')
        keyboard.remove_hotkey('h')
   
button2 = Tk.Button(root, text = 'Autoclicker',bg = 'red', fg='black', font = ('Arial'), command = b2_clicked)
button2.place(x=100, y=100)
def help():
    messagebox.showinfo('How to use?', 'Press G to start autoclicking with left mouse button\nPress H to start autoclicking with right mouse button,also the autoclicker button must be enabled to use G and H')
button3 = Tk.Button(root, text = 'How to use?', command=help,bg = 'red', fg = 'black', font = ('Arial' ))
button3.place(x=100, y=150)
root.mainloop()
