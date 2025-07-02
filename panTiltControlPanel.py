import tkinter as tk
from tkinter import messagebox
import cv2
from PIL import Image, ImageTk
import serial

class CameraSerialUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Kamera Kontrol")
        self.root.geometry("900x600")
        self.root.configure(bg='white')
        
        #serial port paramaters
        self.serial_port = None
        self.port_name = "COM6"
        self.baudrate = 115200
        
        
        self.cap = None
        self.is_camera_running = False
        
        #create interface
        self.setup_ui()
        
        #initialization serial port
        self.init_serial()
        
        #initialization webcam
        self.init_camera()
        
        
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
    
    def setup_ui(self):

        #main frame

        main_frame = tk.Frame(self.root, bg='white')
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        
        self.camera_label = tk.Label(main_frame, bg='black', text="Kamera Yükleniyor...", 
                                   fg='white', font=('Arial', 12))
        self.camera_label.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 20))
        
        
        control_frame = tk.Frame(main_frame, bg='white')
        control_frame.pack(side=tk.RIGHT)
        
        #button style
        
        button_style = {
            'font': ('Arial', 20, 'bold'),
            'bg': '#4CAF50',
            'fg': 'white',
            'width': 4,
            'height': 2,
            'border': 0
        }
        
        #add button
        self.up_btn = tk.Button(control_frame, text="↑", 
                               command=lambda: self.send_command('w'),
                               **button_style)
        self.up_btn.grid(row=0, column=1, padx=5, pady=5)
        
        
        self.left_btn = tk.Button(control_frame, text="←", 
                                 command=lambda: self.send_command('a'),
                                 **button_style)
        self.left_btn.grid(row=1, column=0, padx=5, pady=5)
        
        
        self.right_btn = tk.Button(control_frame, text="→", 
                                  command=lambda: self.send_command('d'),
                                  **button_style)
        self.right_btn.grid(row=1, column=2, padx=5, pady=5)
        
        
        self.down_btn = tk.Button(control_frame, text="↓", 
                                 command=lambda: self.send_command('s'),
                                 **button_style)
        self.down_btn.grid(row=2, column=1, padx=5, pady=5)
        
        
        self.status_label = tk.Label(control_frame, text="Hazır", 
                                   font=('Arial', 10), 
                                   bg='white', fg='gray')
        self.status_label.grid(row=3, column=0, columnspan=3, pady=20)
        
        # connection keyboard
        self.root.bind('<KeyPress>', self.on_key_press)
        self.root.focus_set()
    
    def init_serial(self):
        
        try:
            self.serial_port = serial.Serial(self.port_name, self.baudrate, timeout=1)
            self.status_label.config(text="Seri port bağlı", fg='green')
        except Exception as e:
            self.status_label.config(text="Seri port hatası", fg='red')
            messagebox.showerror("Hata", f"Seri port açılamadı: {str(e)}")
    
    def init_camera(self):
        
        try:
            self.cap = cv2.VideoCapture(0)
            if self.cap.isOpened():
                
                self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
                self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
                
                self.is_camera_running = True
                self.update_camera()
                self.status_label.config(text="Kamera aktif", fg='green')
            else:
                self.status_label.config(text="Kamera hatası", fg='red')
                messagebox.showerror("Hata", "Kamera açılamadı")
        except Exception as e:
            self.status_label.config(text="Kamera hatası", fg='red')
            messagebox.showerror("Hata", f"Kamera hatası: {str(e)}")
    
    def update_camera(self):
        
        if self.cap and self.is_camera_running:
            ret, frame = self.cap.read()
            if ret:
                
                frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                
                
                height, width = frame_rgb.shape[:2]
                max_width, max_height = 640, 480
                
                scale = min(max_width/width, max_height/height)
                new_width = int(width * scale)
                new_height = int(height * scale)
                frame_rgb = cv2.resize(frame_rgb, (new_width, new_height))
                
                
                image = Image.fromarray(frame_rgb)
                photo = ImageTk.PhotoImage(image)
                
                
                self.camera_label.configure(image=photo, text="")
                self.camera_label.image = photo
        
        if self.is_camera_running:
            self.root.after(30, self.update_camera)
    
    def send_command(self, command):
        
        if self.serial_port and self.serial_port.is_open:
            try:
                self.serial_port.write(command.encode())
                
                
                button_map = {
                    'w': self.up_btn,
                    'a': self.left_btn,
                    's': self.down_btn,
                    'd': self.right_btn
                }
                
                if command in button_map:
                    btn = button_map[command]
                    btn.configure(bg='#FF5722')
                    self.root.after(100, lambda b=btn: b.configure(bg='#4CAF50'))
                    
            except Exception as e:
                self.status_label.config(text="Gönderme hatası", fg='red')
        else:
            self.status_label.config(text="Port bağlı değil", fg='red')
    
    def on_key_press(self, event):
        
        key = event.keysym.lower()
        
        if key in ['up', 'left', 'down', 'right']:
            key_map = {'up': 'w', 'left': 'a', 'down': 's', 'right': 'd'}
            self.send_command(key_map[key])
    
    def on_closing(self):
        
        self.is_camera_running = False
        
        if self.cap:
            self.cap.release()
        
        if self.serial_port and self.serial_port.is_open:
            self.serial_port.close()
        
        self.root.destroy()

def main():
    
    
    root = tk.Tk()
    app = CameraSerialUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
