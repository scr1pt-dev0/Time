import time

while True:
    timereal = time.strftime("%H:%M:%S")
    print("Aktuelle Uhrzeit:", timereal, end="\r")
    time.sleep(1)
