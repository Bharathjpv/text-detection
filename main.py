import cv2
import easyocr
import matplotlib.pyplot as plt

#### read images

img = cv2.imread('test3.png')

## instance text detector

reader = easyocr.Reader(['en'], gpu=False)

# detect text on image

text = reader.readtext(img)
# print(text)

##### draw binding box
for i in text:
    bbox, text, score = i

    cv2.rectangle(img, bbox[0], bbox[2], (0,255,0), 5)

    cv2.putText(img,text, bbox[0], cv2.FONT_HERSHEY_COMPLEX, 0.95, (0, 0, 255), 2)

plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show()