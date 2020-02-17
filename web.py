from bs4 import BeautifulSoup
import requests,pprint,os,json

def scrape_top_list(soup):
	main=soup.find('div',class_='lister')
	tbody=main.find('tbody',class_='lister-list')
	tr=tbody.find_all('tr')
	data=[]
	name_list=[]
	year_list=[]
	possition_list=[]
	rating_list=[]
	url_list=[]
	for i in tr:
		detale={}
		td=i.find('td',class_='titleColumn')
		name=td.find('a')
		name_text=str(name.text)
		name_list.append(name_text)
		detale['Name']=name_text
		year=td.find('span',class_='secondaryInfo')
		year_text=year.text
		l=''
		for j in year_text:
			if(j!='(' and j!=')'):
				l+=j
		l=l.split()
		l=int(l[0])

		year_list.append(l)
		detale['Year']=l
		possition1=(td.text)
		l=''
		for j in possition1:
			if '.'==j:
				break
			l+=j
		l=l.split()
		l=int(l[0])
		possition_list.append(l)
		detale['possition']=l
		rating=i.find('td',class_='ratingColumn imdbRating')
		l=(rating.text).split()
		l=float(l[0])
		# print(l)
		rating_list.append(l)
		detale['rating']=l
		url=str(name['href'])
		url_list.append(url)
		detale['url']=url
		data.append(detale)
		break
	return {'data':data,'Name':name_list,'year':year_list,'possition':possition_list,'rating':rating_list,'url':url_list}
def data():
	if os.path.exists("web.json")==False:
		URL=' https://www.imdb.com/india/top-rated-indian-movies/'
		page=requests.get(URL)
		page_text=page.text
		soup=BeautifulSoup(page_text,'html.parser')
		Title=soup.title
		# print(soup)

		l=scrape_top_list(soup)
		c=open('web.json','w')
		json.dump(l,c)
		c.close()
	c=open('web.json','r')
	jsl1=json.load(c)
	return jsl1
	return jsl1

l=data()
if __name__=='__main__':
	pprint.pprint(l['data'])








