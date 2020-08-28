import json,pprint
with open("webtask12.json",'r') as file:
	movie_actors_list = json.load(file)


def function():
	MoviesCastList = []
	for CastList in movie_actors_list:
		CastDict={}
		for CastIndex in range(len(CastList)-1):
			CoActorsList=[]
			CoActorsDict={}
			CoActorsDict['imdb_id'] = CastList[CastIndex+1]["imdb_id"]
			CoActorsDict["name"] = CastList[CastIndex+1]['name']
			Count = 0
			for Movies in movie_actors_list :
				if CastList[CastIndex] in Movies and CastList[CastIndex+1] in Movies:
					Count+=1
			CoActorsDict['num_movies'] = Count
			CoActorsList.append(CoActorsDict)
			CastDict[CastList[CastIndex]['imdb_id']]={
				"Name":CastList[CastIndex]['name'],
				'frequent_co_actors':CoActorsList
			}

		MoviesCastList.append(CastDict)
	return MoviesCastList	

final_list=[]
if __name__ == '__main__':
	pprint.pprint(function())


	