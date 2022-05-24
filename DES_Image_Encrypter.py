#install "pip install psutil"
import des as D
import base64
import os
import PIL
import sys
import time
import psutil

#switch case to encrypt and decrypt
print("1. Encrypt or 2. Decrpyt")
a = int(input())
if a == 1:
    print("Virtual memory = {}".format(psutil.virtual_memory().percent))
    print("CPU usage = {}".format(psutil.cpu_percent()))
    start = time.time()
    key = D.DesKey(b"10293847") #100111010001001001010111
    key.is_single()
    #Change the file location
    imgp = open(r"D:\picture.bmp", 'rb')
    img = imgp.read()
    #base64 is used to conver binary to ASCII values
    img64 = base64.encodebytes(img)
    imgdes = key.encrypt(img64, padding=True)

    imr = open('encodedimg.bmp', 'wb')
    imr.write(imgdes)
    print("Encrypted file has been saved in your folder!")
    end = time.time()
    print("Time = {}".format(end - start))
    print("CPU usage = {}".format(psutil.cpu_percent()))
    print("Virtual memory = {}".format(psutil.virtual_memory().percent))
    process = psutil.Process(os.getpid())
    print("Memory required = {}".format(process.memory_info().rss))

elif a == 2:
    print("Virtual memory = {}".format(psutil.virtual_memory().percent))
    print("CPU usage = {}".format(psutil.cpu_percent()))
    start = time.time()
    key = D.DesKey(b"10293847")
    key.is_single()
    imgp = open(r"C:\Users\91937\Desktop\py4e\img.jpg", 'rb')
    img = imgp.read()
    img64 = base64.encodebytes(img)
    imgdes = key.encrypt(img64, padding=True)
    imgdesdec = key.decrypt(imgdes)
    finaldecode = base64.decodebytes(imgdesdec)

    imr = open('decodedimg.bmp', 'wb')
    imr.write(finaldecode)
    print("Decrpyted file has been saved in your folder!")
    end = time.time()
    print("Time = {}".format(end - start))
    print("CPU usage = {}".format(psutil.cpu_percent()))
    print("Virtual memory = {}".format(psutil.virtual_memory().percent))
    process = psutil.Process(os.getpid())
    print("Memory required = {}".format(process.memory_info().rss))
