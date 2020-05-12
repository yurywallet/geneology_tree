# Building Genealogy tree GUI with Python
If you ever tried to collect and organize the data about your family members you will agree that it is not that easy to finish that in one go as it seems from the first glance. I believe that everyone has seen at least once these nicely-organized trees of royal dynasties in history books. 
<img style="float: center;" src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/fe/900-158_Ahnentafel_Herzog_Ludwig.jpg/450px-900-158_Ahnentafel_Herzog_Ludwig.jpg">

Having such image in mind you will probably start with drawing bubbles and filling them with names - starting with you, your parents and siblings as I did. And then you start to collect all the information from your family members and from this point  things start to become more complicated and from a simple “cave painting” the task turns into geo-positioning of the second wives and the third husbands between siblings and cousins of a left branch of your grandfather’s sister’s family. So you create a new version, scale it make it look nicer… you share the photo of this map with you relatives and then receive an info about somebody that you’ve missed to include and you need to insert her or him right into the middle of the tree… 
Actually, when you go deeper and wider it becomes quite messy and position all the nodes and branches. Moreover, you probably will want to have some extended information to be present like a life span, education, profession, country and city where your ancestors came from and so on that you also need to organize somehow.

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
-	'generation' – if for you it is 10, then for your parents it is 9 (required)
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

- Language: Python (+ CSS HTML)
- Database: SQLite
- Visualization: pydotplus
- GUI one: Tkinter
- GUI two: Flask 

## Issues
1)	Pyinstaller doesn’t like pandas to be included into the project (the size of the file becomes over 200MB)
2)	Pyinstaller will generate executables only for your OS version
3)	After creating executable visualization doesn’t work probably due to the same Graphviz problem


## Links

Tkinter

- https://stackoverflow.com/questions/45729624/graphvizs-executables-not-found-anaconda-3
- https://stackoverflow.com/questions/35064304/runtimeerror-make-sure-the-graphviz-executables-are-on-your-systems-path-aft
- https://stackoverflow.com/questions/43886822/pyinstaller-with-pandas-creates-over-500-mb-exe/48846546#48846546
- https://stackoverflow.com/questions/60854871/exe-by-pyinstaller-can-not-produce-an-image-pydotplus-graphviz-windows10

Flask

- https://www.youtube.com/watch?v=Us9DuF4KWUE
and the code for it
- https://github.com/bradtraversy/myflaskapp
