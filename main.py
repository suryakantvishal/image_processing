from PIL import Image, ImageFilter

img = Image.open('pika.jpeg')
filtered_img = img.convert('L')
box = (300, 0, 700, 500)
region = filtered_img.crop(box)
region.save("grey.png", 'png')


