from web import *

def scrape_movie_details (url):
	actors_name_list=[]
	movie_url='https://www.imdb.com'+str(url)
	movie_page=requests.get(movie_url)
	movie_page_text=movie_page.text
	movies_soup=BeautifulSoup(movie_page_text,'html.parser')
	table=movies_soup.find('table',class_='cast_list')
	name_actor=table.find_all('td',class_='')
	count=count1=0
	for i in name_actor:
		name_actor_dic={}
		count+=1
		name_actor=i.text
		name=''
		for j in name_actor.split():
			name+=j+' '
		name_actor_dic['name']=name
		name_actor_dic['imdb_id']=i.find('a')['href'][6:-1]
		actors_name_list.append(name_actor_dic)

	return actors_name_list

def movie_actors():
	movie_actors_list=[]
	if os.path.exists("webtask12.json")==False :
		x=0
		for i in l['url']:
			movie_actors_list.append(scrape_movie_details (i))
		c=open('webtask12.json','w')
		json.dump(movie_actors_list,c)
		c.close()
	c=open('webtask12.json','r')
	movie_actors_list=json.load(c)
	return movie_actors_list

if __name__=='__main__':
	pprint.pprint(movie_actors())
	




