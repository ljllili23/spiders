# -*- coding: utf-8 -*-
"""
@author:LeeJiangLee
@contact:ljllili23@gmail.com

@time: 7/31/2018 5:18 PM

"""

import urllib.request
import json
import time
from bs4 import BeautifulSoup

genres = ["剧情","喜剧","动作","爱情","科幻","悬疑","惊悚","恐怖","犯罪","同性","音乐","歌舞","传记","历史","战争","西部","奇幻","冒险","灾难","武侠","情色"]

for genre in genres:
    start = 0
    movies = []
    genre = urllib.parse.quote(genre)
    while start<=100:
        url = "https://movie.douban.com/j/new_search_subjects?sort=T&range=0,10&tags=&start={0}&genres={1}".format(str(start),genre)
        print(url)

        request = urllib.request.Request(url)
        response = urllib.request.urlopen(request, timeout=20)
        result = response.read()
        result =json.loads(result)
        result = result['data']

        if len(result)==0:
            break

        for item in result:
            movies.append(item)

        start += 20
    genre = urllib.parse.unquote(genre)
    formattedMovies = {genre:movies}
    moviesJson = json.dumps(formattedMovies)

    with open('./{0}.json'.format(genre),'w',encoding='utf-8') as file:
        file.write(moviesJson)
