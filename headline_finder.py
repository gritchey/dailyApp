import requests


class GetNews(object):
    '''  Uses Api to gather Top News titles from The Wall Street Journal '''

    def __init__(self):

        wsj_url = ('https://newsapi.org/v2/top-headlines?'
                   'sources=the-wall-street-journal&'
                   'apiKey=API KEY GOES HERE')

        title_number = 1
        json_data = requests.get(wsj_url).json()

        while title_number <= 5:
            news_title = json_data['articles'][title_number]['title']
            print(news_title)
            title_number += 1


get_news = GetNews()
print(get_news)
