import qrcode

data='''Hi, I am saifullah khan jadoon
        ph no= 03360009866
        email = skjadoon405@gmail.com'''

qr=qrcode.QRCode(version=1,box_size=10,border=5)

qr.add_data(data)

qr.make(fit=True)
img=qr.make_image(fill_color='grey',back_color='white')

img.save("C:/Users/Saifullah Khan Jadoon/Desktop/khan/new/myinfo3.pnp")

        