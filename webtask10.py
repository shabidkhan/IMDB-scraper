from webtask4 import *
movie_list=movies_details()
director_dic_name={}
for i in movie_list:
	language_dic_name={}
	for j in movie_list:
		count=0
		for k in movie_list:
			if j['language']==k['language'] and i['director']==j['director']==k['director'] and j['language'] not in language_dic_name :
				count+=1
		if count!=0:
			language_dic_name[j['language']]=count
	director_dic_name[i['director']]=language_dic_name
pprint.pprint(director_dic_name)
