https://medium.com/groceristar/ocr-project-part1-simple-introduction-ab7b64bf1864

So, what we have for this moment?
We mostly completed our script. This is what I know so far. Images(grocery lists) converted into JSON or TXT file.

But, data that we have in our output file is raw. It's hard to read the file or work with it as we want. Data should be converted into js objects, and we should be able to push these objects into our database. Database structure can be adjusted in the future, so we need to have the ability to change the logic of output.


Basically, I need ingredients, that related to some department.
like Milk related to Dairy, Carrots related to Vegetables. Looks simple, huh? Not so fast.






List of stages for OCR script


1. :white_check_mark: Setup project with modules, related to OCR conversion
2. :white_check_mark: Fix an issue, related to small fonts, so all images that we have can be converted
3. :white_check_mark: Get an output file with data
4. :white_check_mark: Parsing of measurements from lists
5. Run tests with different cases and understand that all is working as it should.
6. Our output file has data from 30 images. structure of the data should match our database schema
7. This script will be finished when output matching to our current database structure.
8. We have 100 converted and imported grocery lists into our database. All imported data displayed well in our project.





Data that we have are separated between repositories.
It giving us the ability to be more agile. Our code can be shared between different teams.
Like I can pass data between React Frontend developers and Machine learning team.

At the first article, I mentioned a "fetch" plugin that storing data of grocery lists.
Briefly, it's a plugin that reads JSON file and returns data in a format that we need at our NodeJS projects.

If we don't have this plugin - we will struggle with testing. In this case we will be forced to test everything at the server side, before or after importing into a database. This will eat a lot of time and generate a lot of conversations between different teams. With this plugin, our teams are independent but connected by the logic of this plugin.

Example:
ML team can generate data and compare it with data that we have in our plugin.
JS developers can use this plugin without thinking about credentials, connection to our API, etc.


Imagine this situation - we generate a file with data from OCR script - we import it into our server and all start to crash. and it'll be hard to debug where we have an issue. This plugin is trying to prevent that.
----------------------------------




This is our current DB schema at Groceristar.

[we need to put a database schema that we have at groceristar]


This is how our database looks like https://raw.githubusercontent.com/ChickenKyiv/creative/master/database-schemes/Groceristar%20%20%20SqlDBM.png




Our fetch plugin mimics this structure.
Grocery list data separated between a few files.

I don't want to share links to codebase at this article. It'll make it harder to understand. All links to our Github repositories I will share at the next article.






In the ideal world, the result should be something like this
(departments file)[https://github.com/GroceriStar/groceristar-fetch/blob/master/data/Departments/departments.json]

```
[
  {
    "name": "Fresh vegetables",
    "type": "food"
  },
  {
    "name": "Condiments / sauces",
    "type": "food"
  },
  {
    "name": "Dairy",
    "type": "food"
  },
```

(ingredient file)[https://github.com/GroceriStar/groceristar-fetch/blob/master/data/Ingredients/ingredients.json]

```
[{
    "name": "Asparagus",
    "department": "Fresh vegetables"
  },
  {
    "name": "Broccoli",
    "department": "Fresh vegetables"
  },
  {
    "name": "Carrots",
    "department": "Fresh vegetables"
  },
```

Note: Measurement structure is debatable now. We don't have a finished version and tested version at our server. It can be similar to this image.
```
[{
    "singular": "gram",
    "plural": "grams",
    "abbreviation": "g"
  },
  {
    "singular": "slice",
    "plural": "slices"
  },
  {
    "singular": "teaspoon",
    "plural": "teaspoons",
    "abbreviation": "tspn"
  },
```

(measurements file)[https://github.com/GroceriStar/groceristar-fetch/blob/master/data/Measurement/measurements.json]


Just compare json arrays from images above with our current output below. This is what we need to do




----------------------


Summary:

So we have a code stored at our repository on Github.
We have details about how to do it.
We have images can be used in order to test how the script works.
We need to format our output and make it equal to a structure that I show. It also needs to have a good level of accuracy so all necessary data from the Pinterest image will be moved to JSON array.











In the ideal world, the result should be something like this
https://github.com/GroceriStar/groceristar/blob/master/bin/grocery/departments.js
https://github.com/GroceriStar/groceristar/blob/master/bin/grocery/ingredients.js
