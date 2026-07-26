from machine import Pin, PWM
import time

# Pin 15 üzerinde 1000 Hz frekansında PWM başlatıyoruz
# (İstersen Pin("LED") ile Pico W üzerindeki dahili LED'i de deneyebilirsin)
led_pwm = PWM(Pin(15))
led_pwm.freq(1000)

print("--- PWM LED Nefes Efekti Başladı ---")

try:
    while True:
        # Parlaklığı 0'dan 65535'e kadar yavaşça artır
        for duty in range(0, 65536, 1000):
            led_pwm.duty_u16(duty)
            time.sleep_ms(15)
            
        # Parlaklığı 65535'ten 0'a kadar yavaşça azalt
        for duty in range(65535, -1, -1000):
            led_pwm.duty_u16(duty)
            time.sleep_ms(15)

except KeyboardInterrupt:
    # Program durdurulduğunda PWM'i güvenle kapat
    led_pwm.deinit()
    print("PWM Kapatıldı.")