import qrcode
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=5,
    border=4,
)
data = 'Flopcoders softsolutions. \n We provide best software solutions and products as per your requirements. \n Instagram Handle : @flopcoders'
qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save('flopcoders.png')
