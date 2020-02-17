from webtask4 import *
movies=movies_details()
from webtask12 import *

all_movie_and_actors_details=[]

movies_actor=movie_actors()
for i in range (len(movies)):
	movies[i]['cast']=movies_actor[i]
	all_movie_and_actors_details.append(movies[i])
	# all_movie_and_actors_details.append(movies_actor[i])

if __name__=='__main__':
	pprint.pprint(all_movie_and_actors_details)
