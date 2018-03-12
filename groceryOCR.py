

import pytesseract
import cv2 as cv
import numpy as np
import nltk
from autocorrect import spell
import re


source ="" #path to image file
classifierpath1 ="" #path to trained_classifierNM1
classifierpath2 ="" #path to trained_classifierNM2
Outputpathfile ="" #path to output txt file

#read the image
image = cv.imread(source)

#convert to gray scale
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

#perform thresholding OTSU works better but kept normal just in case if anyone wants to try
ret, thresh1= cv.threshold(gray,127,255, cv.THRESH_BINARY)
ret, thresh1= cv.threshold(gray,0,255, cv.THRESH_BINARY + cv.THRESH_OTSU)

#convert the image to text using pytesseract
text = pytesseract.image_to_string(thresh1)

#tokenize text 
words = nltk.word_tokenize(text)
wordlist = []

#make a word list
for e in words:
  if e not in wordlist:
   wordlist.append((e))
   print( spell(e))
 
 # Trying to improve accuracy for low fonts by selecting areas first and performing OCR

# Extract channels to be processed individually
channels = cv.text.computeNMChannels(image)

# Append negative channels to detect ER- (bright regions over dark background)
cn = len(channels)-1
for c in range(0,cn):
  channels.append((255-channels[c]))


for channel in channels:

  erc1 = cv.text.loadClassifierNM1(classifierpath1)
  er1 = cv.text.createERFilterNM1(erc1,25,0.0000025,0.10,0.4,True,0.2)

  erc2 = cv.text.loadClassifierNM2(classifierpath2)
  er2 = cv.text.createERFilterNM2(erc2,0.5)

  regions = cv.text.detectRegions(channel,er1,er2)
  rects = cv.text.erGrouping(image,channel,[r.tolist() for r in regions])
 
  for r in range(0,np.shape(rects)[0]):
    rect = rects[r]
    roi = image[ rect[1] :rect[1]+ rect[3],rect[0]: rect[0]+rect[2]]
    gray = cv.cvtColor(roi, cv.COLOR_BGR2GRAY)
    ret, thresh1= cv.threshold(gray,0,255, cv.THRESH_BINARY + cv.THRESH_OTSU)
    text = pytesseract.image_to_string(thresh1, lang='eng')
    words = nltk.word_tokenize(text)
  for e in words:
   if e not in wordlist:
    wordlist.append((e))
    print(spell(e))

    # save to a file
with open(Outputpathfile, "w") as file:
  for e in wordlist:
   file.write(spell(e))
   file.write(",")


