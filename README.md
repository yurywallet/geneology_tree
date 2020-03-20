# geneology_tree
GUI for the Genealogy Tree project

Interface that allows to draw a geneology tree.
You can add/modify/delete data.

How the tree is build:
There are 2 types of relations between people:
- between generations - parents - child (mother / father) 
- same generation - spouse 

The connection is created by adding the persons ID as a father, mother or spouse

Fields:
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

The resulting tree can be stored as PNG image
The data can be exported as CSV or Excel files.

The project is created in Python and tested on Windows 10.

