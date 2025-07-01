import tkinter as tk
from tkinter import Label
import serial
import cv2
from PIL import Image, ImageTk

ser = serial.Serial('COM6', 115200, timeout=1)  # Kendi COM portuna göre ayarla

cap = cv2.VideoCapture(0)

def send_command(cmd):
    try:
        ser.write(cmd.encode())
        print(f"Gönderildi: {cmd}")
    except Exception as e:
        print("Hata:", e)


def on_key_press(event):
    key_map = {
        'Up': 'w',
        'Down': 's',
        'Left': 'a',
        'Right': 'd'
    }
    if event.keysym in key_map:
        send_command(key_map[event.keysym])


root = tk.Tk()
root.title("Servo ve Kamera Kontrol")
root.geometry("640x500")
root.bind("<KeyPress>", on_key_press)


camera_label = Label(root)
camera_label.grid(row=0, column=0, columnspan=3)


def update_camera():
    ret, frame = cap.read()
    if ret:
        
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(frame)
        imgtk = ImageTk.PhotoImage(image=img)
        camera_label.imgtk = imgtk
        camera_label.configure(image=imgtk)
    root.after(10, update_camera)  


btn_up = tk.Button(root, text="↑", width=10, height=2, command=lambda: send_command('w'))
btn_down = tk.Button(root, text="↓", width=10, height=2, command=lambda: send_command('s'))
btn_left = tk.Button(root, text="←", width=10, height=2, command=lambda: send_command('a'))
btn_right = tk.Button(root, text="→", width=10, height=2, command=lambda: send_command('d'))

btn_up.grid(row=1, column=1, pady=10)
btn_left.grid(row=2, column=0, padx=10)
btn_right.grid(row=2, column=2, padx=10)
btn_down.grid(row=3, column=1, pady=10)


update_camera()

root.mainloop()

cap.release()
