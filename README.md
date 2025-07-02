# Camera Control System with Servo Motors (STM32 + Python)

This project controls a pan-tilt mechanism using **two servo motors** driven by an STM32 microcontroller. A custom `Tkinter` GUI built with Python communicates over a serial port to control the servo motors in real time.

## Hardware Components

- 1x **STM32F103C8T6** (Bluepill)
- 2x **Servo motors** (MG996R)
- 1x **Pan-tilt mechanism**
- 1x **Webcam** (Logitech Brio 500)
- 1x **FTDI** (YP-05)
- 1x **6V 4Ah Battery**
- 1x **Personal Computer**
- **Connecting cables**
## System Architecture
- The servo motors are powered by a 6V 4Ah battery. Serial communication with the PC is established via an FTDI USB-to-Serial adapter.
- The camera feed is streamed using a Logitech Brio 500 webcam.
- Servo motor control is handled by the STM32 microcontroller.

Note: Be sure to connect the GND of the STM32 and the servo motors together to have a common ground reference.
![schema](https://github.com/user-attachments/assets/86e5ada0-e938-468c-acbc-101e327746f3)
## Software Details

### STM32CubeIDE (Firmware)
- PWM signals are generated using TIM2 and TIM3 timers.
- Servo motors are connected to pins `A3` and `A6`.
- UART is used to receive control characters (`w`, `a`, `s`, `d`) for movement.
### Configurations
- PA9 is configured as USART1_TX, and PA10 as USART1_RX for serial communication with the PC.
- PA3 is used as TIM2_CH4 to control the pan servo motor via PWM.
- PA6 is used as TIM3_CH1 to control the tilt servo motor via PWM.

![image](https://github.com/user-attachments/assets/a3faf8cb-6189-4fe1-805a-e0b86ae9e60f)


- The HSE oscillator is set to use an external crystal/ceramic resonator. The PLL multiplies the 8 MHz HSE input by 9 to achieve a system clock of 72 MHz.

![image](https://github.com/user-attachments/assets/d0643ebf-f0db-40d8-843f-f8f16934f38a)


- Under the SYS configuration in STM32CubeIDE, Serial Wire (SWD) is selected as the debug interface to enable programming and debugging using ST-Link.

![image](https://github.com/user-attachments/assets/48e6746e-8d1b-4fdf-8d5e-c5efa6d8d4be)


- TIM2 is configured to generate a PWM signal on Channel 4 (PA3) for controlling the pan servo.

- **Prescaler is set to 144 - 1**
- **Auto-reload register (ARR) is set to 10000 - 1**
- This results in a PWM frequency of approximately 50 Hz, which is suitable for standard servo motors.

![image](https://github.com/user-attachments/assets/7078c58f-fe01-40fe-abe4-4e21668f0ce1)

- TIM3 is configured to generate a PWM signal on Channel 1 (PA6) for controlling the tilt servo.

**Prescaler is set to 144 - 1**
**Auto-reload register (ARR) is set to 10000 - 1**
![image](https://github.com/user-attachments/assets/b5d7e06d-e51f-469d-bc75-8d8bdc56f9df)


- USART1 is configured for asynchronous serial communication at a baud rate of 115200.
- Communication with the STM32 is established via an **FTDI USB-to-Serial** adapter connected to pins **PA9 (TX)** and **PA10 (RX)**.

- The microcontroller receives simple character commands (w, a, s, d) from a Python GUI running on the PC.

![image](https://github.com/user-attachments/assets/a26474ff-ef6d-4986-83af-d90b1ddc7ef9)


### Clock Configurations

- The system clock is configured to run at **72 MHz**, providing stable operation for PWM generation and serial communication.
![image](https://github.com/user-attachments/assets/d9d73a2c-e362-42d3-b541-dd2760e1f8bb)


### Python (GUI)
- Developed using `tkinter` with 4-direction control buttons.
- Keyboard arrow keys and GUI buttons send characters over serial to STM32.
- Live webcam feed is displayed within the same GUI window.
- Libraries used: `pyserial`, `opencv-python`, `Pillow`, `tkinter`
