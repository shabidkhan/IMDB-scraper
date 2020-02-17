from web import *

def scrape_movie_details (url):
	movie_dic={}
	movie_url='https://www.imdb.com'+str(url)
	movie_page=requests.get(movie_url)
	movie_page_text=movie_page.text
	movies_soup=BeautifulSoup(movie_page_text,'html.parser')
	movie_name=movies_soup.find('div',class_='title_wrapper')
	movie_name=(movie_name.text).split()
	movie_name=movie_name[0]
	movie_dic['Name']=movie_name
	movie_director=movies_soup.find('div',class_='credit_summary_item')
	movie_director=movie_director.find('a')
	movie_dic['director']=movie_director.text
	movie_country=movies_soup.find_all('div',class_='txt-block')
	for i in movie_country:
		
		if i.find('h4')!=None:
			a=i.find('a')
			if 'Country' in i.find('h4').text:
				movie_dic['country']=a.text
			if 'Language' in i.find('h4').text:
				movie_dic['languae']=a.text
	movies_img=movies_soup.find('div',class_='poster')
	movies_img=movies_img.find('a')
	movies_img=movies_img.find('img')
	movie_dic["poster_image_url"]=movies_img['src']
	movies_bio=movies_soup.find('div',class_='summary_text')
	l=''
	for i in movies_bio.text.split():
			l+=" "+i
	movie_dic['bio']=l
	movies_runtime=movies_soup.find_all('div',class_='txt-block')
	for i in movies_runtime:
		if i.find('h4')!=None:
			if 'Runtime' in i.find('h4').text:
				time=i.find('time').text.split()
				movie_dic['runtime']=int(time[0])
	movie_genres=movies_soup.find('div',class_='subtext')
	movie_genres=movie_genres.find('a')
	movie_dic['genres']= movie_genres.text
	return movie_dic


l=scrape_top_list(soup)
if __name__=='__main__':
	movie_list=[]
	c=0
	for i in l['url']:
		movie_list.append(scrape_movie_details (i))
		break
	pprint.pprint(movie_list)


