from machine import Pin, PWM
import time

# SG90 Servo Sinyal Pini -> GP16
servo = PWM(Pin(16))
servo.freq(50) # Servo motorlar standart 50Hz frekansta çalışır

def set_angle(angle):
    """
    0 ile 180 derece arasındaki açıyı 16-bit PWM duty değerine dönüştürür.
    """
    if angle < 0: angle = 0
    if angle > 180: angle = 180
    
    # 0° (1638) ile 180° (8192) arası lineer haritalama
    duty = int(1638 + (angle / 180) * (8192 - 1638))
    servo.duty_u16(duty)

print("--- Servo Motor Açı Testi Başladı ---")

try:
    while True:
        # 0 dereceden 180 dereceye kadar hareket ettir
        for angle in range(0, 181, 10):
            set_angle(angle)
            print(f"Açı: {angle}°")
            time.sleep(0.1)
            
        time.sleep(1)
        
        # 180 dereceden 0 dereceye geri dön
        for angle in range(180, -1, -10):
            set_angle(angle)
            print(f"Açı: {angle}°")
            time.sleep(0.1)
            
        time.sleep(1)

except KeyboardInterrupt:
    servo.deinit()
    print("Servo durduruldu.")