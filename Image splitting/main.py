import cv2
img = cv2.imread('lena.tiff')
height = img.shape[0]
width = img.shape[1]
width_cutoff = width // 2
left1 = img[:,:width_cutoff]
right1 = img[:,width_cutoff:]
img = cv2.rotate(left1,cv2.ROTATE_90_CLOCKWISE)
height = img.shape[0]
width = img.shape[1]
width_cutoff = width // 2
l2 = img[:,:width_cutoff]
l1 = img[:,width_cutoff:]
l2 = cv2.rotate(l2,cv2.ROTATE_90_COUNTERCLOCKWISE)
cv2.imwrite('lena_2.tiff',l2)
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
img = Image.open('lena_2.tiff')
I1 = ImageDraw.Draw(img)
myFont = ImageFont.truetype('Arial.ttf',25);
I1.text((10,10),"2nd Quadrant",font=myFont,fill=(255,0,0))
img.show()
img.save('lena_2.tiff')
l1 = cv2.rotate(l1,cv2.ROTATE_90_COUNTERCLOCKWISE)
cv2.imwrite('lena_1.tiff',l1)
img = Image.open('lena_1.tiff')
I1 = ImageDraw.Draw(img)
myFont = ImageFont.truetype('Arial.ttf',25);
I1.text((10,10),"1st Quadrant",font=myFont,fill=(255,0,0))
img.show()
img.save('lena_1.tiff')
img = cv2.rotate(right1,cv2.ROTATE_90_CLOCKWISE)
height = img.shape[0]
width = img.shape[1]
width_cutoff = width // 2
r4 = img[:,:width_cutoff]
r3 = img[:,width_cutoff:]
r4 = cv2.rotate(r4,cv2.ROTATE_90_COUNTERCLOCKWISE)
cv2.imwrite('lena_4.tiff',r4)
img = Image.open('lena_4.tiff')
I1 = ImageDraw.Draw(img)
myFont = ImageFont.truetype('Arial.ttf',25);
I1.text((10,10),"4th Quadrant",font=myFont,fill=(255,0,0))
img.show()
img.save('lena_4.tiff')
r3 = cv2.rotate(r3,cv2.ROTATE_90_COUNTERCLOCKWISE)
cv2.imwrite('lena_3.tiff',r3)
img = Image.open('lena_3.tiff')
I1 = ImageDraw.Draw(img)
myFont = ImageFont.truetype('Arial.ttf',25);
I1.text((10,10),"3rd Quadrant",font=myFont,fill=(255,0,0))
img.show()
img.save('lena_3.tiff')
img = cv2.imread('lena.tiff')
height = img.shape[0]
width = img.shape[1]
width_cutoff = width // 2
left1 = img[:,:width_cutoff]
rigth1 = img[:,width_cutoff:]
cv2.imwrite('lena_left.tiff',left1)
cv2.imshow('lena_left.tiff',left1)
cv2.imwrite('lena_right.tiff',right1)
cv2.imshow('lena_right.tiff',right1)
image = cv2.imread('lena.tiff')
height,width,channels = image.shape
half_height = height//2
top_section = image[:half_height,:]
bottom_section = image[half_height:,:]
cv2.imshow('lena_top',top_section)
cv2.imshow('lena_bottom',bottom_section)
cv2.imwrite('lena_top.tiff',top_section)
cv2.imwrite('lena_bottom.tiff',bottom_section)
cv2.waitKey(0)

