# ocr-grocery-parsing

#### Ravi
Hi Arthur... I was able to solve the bug and was able to read the initial grocery list you have used to make the Groceristar but it is failing for images with very small font as they are indistinguishable for it.. 
I am trying to improve  accuracy by different methods (opencv thresholds) etc.. 
will let you know if there is any improvement .. 
fyi ignore if you already know it.. 
there is a image scrapper python script which helps to scrap images for a given URL..

#### Ravi
Hi Arthur, Can you send me few links which are most important for you .. I will try to use other software to improve the accuracy of text recognition.. my initial idea was to scrape through all websites but it seems the images are quite different from one another...

#### Arthur
Check this issue for images/samples for your algo: https://github.com/GroceriStar/groceristar/issues/447
i tried a different layouts, fonts - in order to make tests better

#### Ravi
it would do for clear image but can't for small font ones.. so I have asked your help to find which images are important for you such that I can fine tune the algo to our needs..

I thought of improving model by highlighting the text and then converting it but it couldn't complete ..
I have added  a sample image and sample output of the code for reference..


#### How to use it
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
