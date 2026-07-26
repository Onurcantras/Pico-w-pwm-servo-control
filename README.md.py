# ⚙️ Raspberry Pi Pico W - PWM & Servo Motor Control

This repository demonstrates **Pulse Width Modulation (PWM)** implementation on the **Raspberry Pi Pico W** using MicroPython.

## 🚀 Features

- **Breathing LED Effect (`pwm_led.py`):** Uses 16-bit resolution PWM (`0-65535`) at $1000\text{ Hz}$ to smoothly fade an LED in and out.
- **SG90 Servo Motor Control (`servo_control.py`):** Controls a servo motor angle ($0^\circ - 180^\circ$) by driving a $50\text{ Hz}$ PWM signal with precise duty cycle calculations.

## 📐 Servo PWM Calculations ($50\text{ Hz}$)

- **Period:** $T = \frac{1}{50\text{ Hz}} = 20\text{ ms}$
- **$0^\circ$ Angle ($0.5\text{ ms}$ pulse):**
  $$\text{Duty} = \frac{0.5\text{ ms}}{20\text{ ms}} \times 65535 \approx 1638$$
- **$180^\circ$ Angle ($2.5\text{ ms}$ pulse):**
  $$\text{Duty} = \frac{2.5\text{ ms}}{20\text{ ms}} \times 65535 \approx 8192$$

## 📋 Requirements

- **Hardware:** Raspberry Pi Pico W, SG90 Servo Motor (optional), LED & $220\Omega$ resistor (optional).
- **Firmware:** MicroPython (v1.20.0+)
- **IDE:** Thonny IDE