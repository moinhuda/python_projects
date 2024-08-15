#import QR code module

import qrcode as qr
img= qr.make("https://github.com/moinhuda/python_projects")
img.save("my_account.png")

# to make multiple color QR code
#from PIL import Image

'''qr=qrcode.QRcode(version = 1,
                 error_correction=qrcode.constants.ERROR_CORRECT_H,
                 box_size=10, border=4)
qr.add_data("https://github.com/moinhuda/python_projects")
qr.make(fit=True)
img=qr.make_image(fill_color="red",back_color="white")
img.save("my_account.png")'''
