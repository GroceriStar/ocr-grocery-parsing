import pytesseract
import cv2 as cv
import json
import codecs
import nltk 
import re 
from nltk.corpus import stopwords
from nltk.corpus import words
import os


from nltk.corpus import words
stop_words  = set(stopwords.words('english'))
correct_spelling = words.words()

def spellchecker(misspelled_word='caaar',n_gram = 1):
    correct_words = [i for i in correct_spelling if i.startswith(misspelled_word[0]) and len(i) > 1]
    min_distance = 1
    min_word = ''
    for word in correct_words:
        distance = nltk.jaccard_distance(set(nltk.ngrams(misspelled_word,n=n_gram)) , set(nltk.ngrams(word,n=n_gram)))
        
        if distance < min_distance:
            min_distance = distance
            min_word = word
    
    return min_word





imageList = os.listdir('../creative/OCR/')
imageList = [i for i in imageList if re.search('.*\.png$',i) or re.search('.*\.jpg',i)]
counter = 0
json_data = []
for img in imageList:
	print(counter,'th image')
	counter += 1
	print(img)
	 	# read the image file and store it in image variable
	image = cv.imread('../creative/OCR/'+img)


	# resize the image to achive more resolution 
	im = cv.resize(image,(5000,5000))


		#convert to gray scale
	gray = cv.cvtColor(im, cv.COLOR_BGR2GRAY)


		# Binarize the gray scale (set threshold 200)
	ret3,th3 = cv.threshold(gray,200,255,cv.THRESH_BINARY)

		# Blur the binarize image to get more accuracy
	blur = cv.GaussianBlur(th3,(5,5),0)

		# use OSTU thresolding to binarize the image again
	ret4 , th4 = cv.threshold(blur,200,255,cv.THRESH_BINARY + cv.THRESH_OTSU)

	print('converting to text')

		# Convert the image to text
	text = pytesseract.image_to_string(th4)

	

	 
	print('converting done')


	tokens = nltk.word_tokenize(text)

	words = [i.lower() for i in tokens if len(i) > 1 and not re.search('.*[0-9\\\-]+',i)]

	checked_words = [spellchecker(i) for i in words]

	print('hi')
	checked_words = [i for i in checked_words if (i not in stop_words)]
	lines = text.split('\n')



    
    

	q_measure = []


	for line in lines:
		s = re.search('([\d]+%* [\w]+)',line)
		if s != None :
			s = s.group(1)
			q_measure.append(s)

		# for line in lines:
		#     s = re.search('([\d]+%* [\w]+)',line)
		#     if s != None :
		#         s = s.group(1)
		#         q_measure.append(s)

	print('write to json')
	json_data.append({'words':checked_words,'quntity&measurements':q_measure})



with codecs.open('test.json','w','utf-8') as f:
	json_file = json.dumps(json_data,indent=2)
	f.write(json_file)




# file = codecs.open('text.txt','w','utf-8')
# file.write(text)
# file.close()
# # Print the output text
# print(text)
	