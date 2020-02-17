from webtask13 import *
def movies_(i,c):
	c+=1
	dic={}
	id_dic={}
	dic['name']=i[0]['name']
	dic1={}
	list1=[]
	dic1['imdb_id']=str(i[1]['imdb_id'])
	dic1['name']=str(i[1]['name'])
	count=0
	for j in movies_actor:
		if c<len(j):
			if str(i[1]['name'])==str(j[c]['name']):
				count+=1
	dic1['num_mov']=count
	list1.append(dic1)
	dic["frequent_co_actors"]=str(list1)
	new_dict=(dic)
	id_dic[(i[0]['imdb_id'])]=new_dict
	if len(i)==2:
		final_list.append(str(id_dic))
		return final_list
	final_list.append(str(id_dic))
	final_list.append(movies_(i[1:],c))
	return final_list


def function():

	c=0
	co_actors=[]
	for n in movies_actor:
		
		l=movies_(n,c)
		co_actors.append((l[:len(n)-1]))
	return(co_actors)

final_list=[]
if __name__ == '__main__':
	pprint.pprint(function())