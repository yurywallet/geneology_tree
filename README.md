GUI for the Genealogy Tree project

## Description
This tool helps to create and visialize a geneology tree of your family.

You can add/modify/delete data, search and visualize.

## How the tree is built?
There are 2 types of relations between people:
- between generations - parents - child (mother / father) 
- same generation - spouse 

The connection is created by adding the persons ID as a father, mother or spouse

## Fields:
-	'id' unique ID of a person (required)
-	'name' name of a person (required)
-	'surname' surname of a person                                  
-	'date_birth' 
-	'date_death',
-	'mother_id' unique ID of a mother, needed to draw connections
-	'father_id' unique ID of a father, needed to draw connections
-	'spouse_id' unique ID of a spouse, needed to draw connections                                   
-	'generation' – if fro you it is 10, then for your parents it is 9 (required)
-	'cluster' – by default 1, for larger trees helps to organize it better (required)
-	'gender' – gender 
-	'place_birth' –place of birth (city, town, etc.)
-	'country_birth' – country of birth
-	'country' – current country
-	'comments'- any extra info

## Result
The resulting tree can be stored as PNG image
The data can be exported as CSV or Excel files.

## Inteface (GUI)
- Tkinter interface
- Flask web interface


## Project details
The project is created in Python and tested on Windows 10.

- Language: Python
- Database: SQLite
- Visualization: pydotplus
- GUI one: Tkinter
- GUI two: Flask

## Links

- Tkinter
https://stackoverflow.com/questions/45729624/graphvizs-executables-not-found-anaconda-3
https://stackoverflow.com/questions/35064304/runtimeerror-make-sure-the-graphviz-executables-are-on-your-systems-path-aft
https://stackoverflow.com/questions/43886822/pyinstaller-with-pandas-creates-over-500-mb-exe/48846546#48846546
https://stackoverflow.com/questions/60854871/exe-by-pyinstaller-can-not-produce-an-image-pydotplus-graphviz-windows10

- Flask
https://www.youtube.com/watch?v=Us9DuF4KWUE
and the code for it
https://github.com/bradtraversy/myflaskapp
