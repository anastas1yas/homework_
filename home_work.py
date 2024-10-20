import cv2
from PIL import Image

image_path = 'face.jpg'
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
image = cv2.imread(image_path)
faces = face_cascade.detectMultiScale(image)

face_image = Image.open(image_path)
glasses = Image.open('glasses.png')
mustache = Image.open('mustache.png')

face_image = face_image.convert("RGBA")
glasses = glasses.convert("RGBA")
mustache = mustache.convert("RGBA")

for (x, y, w, h) in faces:
    glasses_resized = glasses.resize((w, int(h / 2)))
    face_image.paste(glasses_resized, (x, int(y + h / 6)), glasses_resized)

    mustache_resized = mustache.resize((w, int(w / 3)))
    face_image.paste(mustache_resized, (x, int(y + h / 2)), mustache_resized)

face_image.save("face_with_glasses_and_mustache.png")
face_with_glasses_and_mustache = cv2.imread("face_with_glasses_and_mustache.png")

cv2.imshow("face_with_glasses_and_mustache", face_with_glasses_and_mustache)
cv2.waitKey()
