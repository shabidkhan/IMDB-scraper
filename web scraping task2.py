from web import *

l['year'].sort()
x=[]
for i in l['year']:
	if i not in x:
		x.append(i)
move_list=[]
for i in x:
	dic_list=[]
	for j in l['data']:
		if int(j['Year'])==int(i) and j not in dic_list :
			dic_list.append(j)
			# pprint.pprint(dic_list)
	move_list.append(dic_list)
pprint.pprint(move_list)








