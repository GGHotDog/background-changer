import struct, ctypes, time, os, config

i = 1

start = os.path.abspath(os.curdir)

def changeBG(PATH): #change
    SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoW(20, 0, PATH, 3)
    return;

print(start)

while True:
    PATH = start + "\\img\\" + str(i) +".jpg"
    time.sleep(config.times)

    if os.path.exists(PATH):
        print("Background changed to " + str(i) + ".jpg")
        changeBG(PATH)
        i += 1
    else:
        print("The background cannot be changed to " + str(i) +".jpg")
        print("Background changed to 1.jpg")
        PATH = start + "\\img\\" + "1.jpg"
        changeBG(PATH)
        i = 2

