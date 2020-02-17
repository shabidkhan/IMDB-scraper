from webtask4 import *
movie_list=movies_details()
def  analyse_movies_language (list1):
	list2=[]
	for i in list1:
		if i['language'] not in list2:
			list2.append(i['language'])
	final_list=[]
	language_dic={}
	for j in list2:
		movie_language_list=[]
		count_languae=0
		for i in list1:
			if j==i['language']:
				movie_language_list.append(i)
				count_languae+=1
		final_list.append(movie_language_list)
		language_dic[j]=count_languae

	return {'all':final_list,'count_language':language_dic}
detaile=analyse_movies_language (movie_list)
if __name__=='__main__':
	pprint.pprint(detaile['all'])
	pprint.pprint(detaile['count_language'])