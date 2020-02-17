from web import *

# l=scrape_top_list(soup)
# l['Year'].sort()
# for i in l['Year']:
# 	'Year'(i)
l['year'].sort()
x=[]
k=[]
for i in l['year']:
	if i not in x:
		x.append(i)
move_list=[]
dic_list=[]
c=10
for i in x:
	
	for j in l['data']:
		if int(j['Year'])==int(i) and j not in dic_list :
			if (1955+c)>=j['Year'] and j['Year'] not in dic_list:
				dic_list+=k
				k=[]
				dic_list.append(j)
			else:
				k.append(dic_list)
			# pprint.pprint(dic_list)
			# print(1955+c)
			if (1955+c)<j['Year']:
				move_list.append(dic_list)
				dic_list=[]
				c=c+10
pprint.pprint(move_list)
