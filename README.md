# 🎯 Camera Control System with Servo Motors (STM32 + Python)

This project controls a pan-tilt mechanism using **two servo motors** driven by an STM32 microcontroller. A custom `Tkinter` GUI built with Python communicates over a serial port to control the servo motors in real time.

## 🛠️ Hardware Components

- 1x **STM32F103C8T6** (Bluepill)
- 2x **Servo motors** (MG996R)
- 1x **Pan-tilt mechanism**
- 1x **Webcam** (Logitech Brio 500)
- 1x **FTDI** (YP-05)
- 1x **6V 4Ah Battery**
- 1x **Personal Computer**
- **Connecting cables**
## ⚙️ System Architecture
![schema](https://github.com/user-attachments/assets/86e5ada0-e938-468c-acbc-101e327746f3)
## 🧪 Software Details

### STM32CubeIDE (Firmware)
- PWM signals are generated using TIM2 and TIM3 timers.
- Servo motors are connected to pins `A3` and `A6`.
- UART is used to receive control characters (`w`, `a`, `s`, `d`) for movement.
### Configurations
![image](https://github.com/user-attachments/assets/a3faf8cb-6189-4fe1-805a-e0b86ae9e60f)
![image](https://github.com/user-attachments/assets/d0643ebf-f0db-40d8-843f-f8f16934f38a)
![image](https://github.com/user-attachments/assets/48e6746e-8d1b-4fdf-8d5e-c5efa6d8d4be)
![image](https://github.com/user-attachments/assets/7078c58f-fe01-40fe-abe4-4e21668f0ce1)
![image](https://github.com/user-attachments/assets/b5d7e06d-e51f-469d-bc75-8d8bdc56f9df)
![image](https://github.com/user-attachments/assets/a26474ff-ef6d-4986-83af-d90b1ddc7ef9)
### Clock Configurations
![image](https://github.com/user-attachments/assets/d9d73a2c-e362-42d3-b541-dd2760e1f8bb)


### Python (GUI)
- Developed using `tkinter` with 4-direction control buttons.
- Keyboard arrow keys and GUI buttons send characters over serial to STM32.
- Live webcam feed is displayed within the same GUI window.
- Libraries used: `pyserial`, `opencv-python`, `Pillow`, `tkinter`
