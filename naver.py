import requests
from bs4 import BeautifulSoup

# # 청소년 불가 영화 code
# base_url = 'https://movie.naver.com/movie/sdb/browsing/bmovie.nhn?grade=1001004'
# option = '&page='
# tail = 1

# remove_list = []
# for tail in range(tail, 768, 1):
#     URL = base_url + option + str(tail)

#     response = requests.get(URL)
#     soup = BeautifulSoup(response.text, 'html.parser')

#     remove = soup.select('#content > .article > div:nth-of-type(1) > #cbody > #old_content > ul > li')
    
#     for re in remove:
#         remove = re.select_one('a')['href'].split('code=')[1]
#         remove_list.append(remove)

# print(remove_list)
# print(len(remove_list))



# 크롤링 메인부분
base_url = 'https://movie.naver.com/movie/bi/mi/basic.nhn'
option = '?code='
code = 160000

for n in range(code, 171540, 1):

    URL = base_url + option + str(n)
    response = requests.get(URL)

    soup = BeautifulSoup(response.text, 'html.parser')
    movie = soup.select_one(
        '#content > .article')

     # 청소년 불가 영화 예외처리
    if movie is None:
        continue

    if movie.select_one('.mv_info_area > .mv_info > .info_spec > dd:nth-of-type(4)'):
        remove = movie.select_one('.mv_info_area > .mv_info > .info_spec > dd:nth-of-type(4) > p > a')
        remove = remove.text

    a_tag = movie.select_one('.mv_info_area > .mv_info > .h_movie > a')
    movie_title = a_tag.text

    a_tag2 = movie.select('.mv_info_area > .mv_info > .info_spec > dd > p > span:nth-of-type(1) > a')

    movie_genre = []
    for genre in a_tag2:
        movie_genre.append(genre.text)

    summary = movie.select('div:nth-of-type(4) > .obj_section > .video > .story_area > p')

    print('id:', int(n)-code+1, 'title:', movie_title, ' genre:',movie_genre)
    print('summary:', summary ,'\n')
