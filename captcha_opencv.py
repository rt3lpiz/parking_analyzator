__author__ = 'rt3lpiz'

from PIL import Image
import cv2

im = Image.open("Captcha.jpg")
im = im.convert("RGB")
im2 = Image.new("RGB",im.size,255)

im = im.convert("P")

temp = {}

for x in range(im.size[1]):
  for y in range(im.size[0]):
    pix = im.getpixel((y,x))
    temp[pix] = pix
    if pix == 46 or pix == 82 or pix==52: # these are the numbers to get
      im2.putpixel((y,x),0)

im2.save("output.jpg")
im3=cv2.imread('output.jpg', cv2.CV_LOAD_IMAGE_UNCHANGED)
cv2.imshow('captcha', im3)
cv2.waitKey(0)
cv2.destroyWindow('captcha')
