
import requests 
from PIL import Image 
from StringIO import StringIO

'''
PYTHON SCRIPT FOR DOWNLOADING NARUTO GAIDEN FROM goodmanga.net

'''


'''
You can change base_url ^ for shippudden also. see website
no color for shippudden
This is the url when i downloaded the shippudden

http://w6.goodmanga.net/images/manga/naruto/
'''

base_url = 'http://w5.goodmanga.net/images/manga/naruto-gaiden-the-seventh-hokage/'




########################################

# for colored pages.See website until which episode they are available
color = True  # set to false if black and white pages are present

# starting episode
episode_start = 1

# ending episode
episode_end = 10

#######################################


##### Don't make changes after this line #####


for page in xrange(episode_start , episode_end + 1): 

	if color:
		page = str(page) + '.1'
	else : 
		page = str(page)

	for episode in xrange(1,30): 
		episode = str(episode) + '.jpg'
		url = base_url + page + '/' + episode
		print 'downloading..' + url

		r = requests.get(url)
		print 'Done with status ' + str(r.status_code)
		if r.status_code == 200 : 
			i = Image.open(StringIO(r.content))
			i.save(page+ '_' + episode)


