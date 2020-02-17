from webtask4 import *
movie_list=movies_details()
def  analyse_movies_language (list1):
	list2=[]
	for i in list1:
		if i['director'] not in list2:
			list2.append(i['director'])
	final_list=[]
	director_dic={}
	for j in list2:
		movie_director_list=[]
		count_director=0
		for i in list1:
			if j==i['director']:
				movie_director_list.append(i)
				count_director+=1
		final_list.append(movie_director_list)
		director_dic[j]=count_director

	return {'all':final_list,'count_director':director_dic}
detaile=analyse_movies_language (movie_list)
if __name__=='__main__':
	pprint.pprint(detaile['all'])
	pprint.pprint(detaile['count_director'])