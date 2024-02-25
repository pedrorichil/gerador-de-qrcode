import qrcode
from PIL import Image, ImageDraw, ImageFont

def generate_advanced_qr_code(data, filename, logo=None, scale=4, border=4):
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=scale,
        border=border,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img = img.convert("RGBA")

    if logo:
        logo_img = Image.open(logo)
        logo_img = logo_img.convert("RGBA")

        # Calculate the size and position for the logo
        qr_size = img.size[0]
        logo_size = int(qr_size / 4)

        x = (qr_size - logo_size) // 2
        y = (qr_size - logo_size) // 2

        # Resize the logo
        logo_img = logo_img.resize((logo_size, logo_size), Image.ANTIALIAS)

        # Paste the logo on the QR code
        img.paste(logo_img, (x, y), logo_img)

    # Draw a custom border around the QR code
    draw = ImageDraw.Draw(img)
    border_size = border * scale
    draw.rectangle([0, 0, qr_size - 1, qr_size - 1], outline="black", width=border_size)

    # Save the final image
    img.save(filename)

# Example usage
data = "https://www.example.com"
filename = "advanced_qr_code.png"
logo = "logo.png"  # Path to your logo image file
scale = 8  # Change the scale for finer details
border = 8  # Change the border width

generate_advanced_qr_code(data, filename, logo, scale, border)
