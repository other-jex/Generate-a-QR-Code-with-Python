import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.colormasks import RadialGradiantColorMask

website_link = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley'

qr = qrcode.QRCode(version = 10, box_size = 5, border = 5)
qr.add_data(website_link)
qr.make()

img = qr.make_image(image_factory=StyledPilImage, color_mask=RadialGradiantColorMask())

img.save('youtube_qr.png')