import qrcode
from PIL import Image
data = input("Enter the message you want to convert: ")

img = qrcode.make(data)

img.save('C:/Users/harsh/Desktop/python/QRCodeGenerator/codes/qrcode.png')
