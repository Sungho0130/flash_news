from bs4 import BeautifulSoup
from urllib.request import urlopen


def newscrawring():
    url = 'https://news.daum.net/'
    page = urlopen(url)
    soup = BeautifulSoup(page, "lxml")
    news_list = soup.select('div.box_news_issue li')
    home = []
    for news in news_list:
        home.append(news.select_one('a').get('href', ''))

    home_news = {'title': [], 'content': [], 'img': [], 'src':[]}

    for de in home:
        url_de = de
        page = urlopen(url_de)
        soup2 = BeautifulSoup(page, "lxml")


        # 기사 링크
        home_news['src'].append(de)

        # 제목 크롤링
        home_news['title'].append(soup2.select('div.head_view h3')[0].string)

        # 본문 내용 크롤링
        sep = soup2.div.article.section.find_all()


        a = []
        #이미지 1개 크롤링
        for i in sep:
            if i.name == 'figure':
                a = i.img.get('src','')
            # elif i.name == 'iframe':
            #     a = iframe_src(soup2)
            else:
                pass

        if a and len(a) == 0:
            a = '#'


        # 이미지 주소 추가
        home_news['img'].append(a)

        # 처음 사진 설명 나오는 figure요소 제거
        nofig = [nofig for nofig in sep if nofig.name != 'figure']
        # 중간 사진 설명 나오는 figcaption요소 제거
        nofigg = [nofigg for nofigg in nofig if nofigg.name != 'figcaption']

        contens = []
        for i in nofigg:
            contens.append(i.text)

        # 리스트 안에 문자열 합치기
        contens = ''.join(contens)

        # 전처리
        contens = contens.strip()
        contens = contens.replace('\n', '')
        # 앞부분 기사설명 스킵해준뒤 두칸이상 띄어쓰기 제거
        contens = contens.replace("  ", "")


        # 기사 본문 저장
        home_news['content'].append(contens)


    return home_news



# # 이미지 주소가 있다면
# if a and len(a) > 0:
#     # a의 0번째가 빈값이 아니라면
#     if a[0] != '':
#         a = a[0]
#     # 0번째가 빈값이면 1번째 주소
#     else:
#         a = a[1]
# # 이미지 주소가 없다면
# else:
#     for i in sep:
#         if i.name == 'iframe':
#             a = iframe_src(soup2)

