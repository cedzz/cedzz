This is a simple python script for getting mangas from goodmanga.net

Dependency : 

Requires Requests LIBRARY
command to install :  pip install Requests 


Download the manga you mentioned in the base_url parameter

You also have to mention the starting and ending of episodes.
Note: Try limit it to 100 episodes at a time.

For example:


------------------------------------------
PYTHON SCRIPT FOR DOWNLOADING NARUTO GAIDEN FROM goodmanga.net

You have to set base_url as: 
base_url = 'http://w5.goodmanga.net/images/manga/naruto-gaiden-the-seventh-hokage/'
-------------------------------------------

----------------------------------------
You can change base_url ^ for shippudden also. see website
No color pages for shippudden, depends on availability
This is the url when i downloaded the shippudden

base_url = http://w6.goodmanga.net/images/manga/naruto/
---------------------------------------

STATUS Codes

200 -> File downloaded and saved

404 -> File not found


NOTE: 

-> All the files will be downloaded in the same folder where you run the script.
