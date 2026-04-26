import qrcode

data = input("Enter the data to encode in the QR code: ").strip()
filename = input("Enter the filename for the generated QR code: ").strip()

qr = qrcode.QRCode(box_size=10, border=4)
qr.add_data(data)
image = qr.make_image(fill_color="black", back_color="white")
# This ensures the file is saved as a PNG image
image.save(f"{filename}.png")
print(f"QR code generated and saved as {filename}.")
