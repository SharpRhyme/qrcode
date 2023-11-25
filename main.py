import qrcode
import os

qr = qrcode.QRCode(
    version = 1,
    box_size = 10,
    border = 4
)

data = input("Enter data to encode: ")
qr.add_data(str(data))
qr.make(fit=True)

fill = input("Enter fill colour: ")
fill = fill.lower()
back = input("Enter back colour: ")
back = back.lower()

img = qr.make_image(fill_color = fill, back_color=back)

img.save("qr.png")

print(f"Saved to '{os.path.abspath(os.getcwd())}\\qr.png'")