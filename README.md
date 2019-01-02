# OCR Grocery list parcing


Table of Contents
=================

 * [Synopsis](#synopsis)
 * [Screenshot](#screenshot)
 * [Installation](#installation)
 * [License](#license)





#### Synopsis
At this project we're trying to create an algorithm, that will be able to proceed images from Pinterest into js/json arrays, that we can use in our project. We're interested in images, that contains grocery list templates.




#### Ravi
Hi Arthur... I was able to solve the bug and was able to read the initial grocery list you have used to make the Groceristar but it is failing for images with very small font as they are indistinguishable for it..
I am trying to improve  accuracy by different methods (opencv thresholds) etc..
there is a image scrapper python script which helps to scrap images for a given URL..

#### Ravi
Hi Arthur, Can you send me few links which are most important for you .. I will try to use other software to improve the accuracy of text recognition.. my initial idea was to scrape through all websites but it seems the images are quite different from one another...

#### Arthur


#### how to test  
In order to make this script more accurate, i put a different images into docs/Tests.md file.
That images have a different layouts, fonts, etc...
How to check is this algorythm working well - check TESTS.md




We have a sample image and sample output that shows how it actually works....


#### Installation
Install tesseract
install below python packages
* pytesseract
* opencv
* opencv contrib
* nltk
* autocorrect
* re

in pytesseract script at tesseract_cmd add your  tesseract ocr location


Code credits: @vpisarev
