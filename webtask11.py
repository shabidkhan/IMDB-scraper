from webtask4 import *

def analyse_movies_genre(list1) :
	movies_genre_list=[]
	genre_count_dict={}
	for i in list1:
		movies_genre_list2=[]
		count=0
		for j in list1:
			if i['genres']==j['genres'] and i not in movies_genre_list2: 
				movies_genre_list2.append(j)
				count+=1
		if movies_genre_list2 not in movies_genre_list:
			movies_genre_list.append(movies_genre_list2)
			genre_count_dict[i['genres']]=count
	return movies_genre_list,genre_count_dict



movie_list=movies_details()
genre_detaile=analyse_movies_genre(movie_list)
if __name__=='__main__':
	pprint.pprint(genre_detaile)
