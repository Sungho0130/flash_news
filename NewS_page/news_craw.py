from urllib.request import urlopen
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
from .models import Crawring


def iframe_src(detail_url):
    extracted_url = ''
    chrome_options = Options()
    chrome_options.add_argument('--headless')  # headless 모드 활성화
    chrome_options.add_argument('--disable-gpu')  # GPU 가속 비활성화
    chrome_options.add_argument("--user-agent=Mozilla/5.0")

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)

    # 웹페이지 열기
    driver.get(detail_url)

    WebDriverWait(driver, 20)

    # iframe 찾기
    iframes = driver.find_elements(By.CLASS_NAME, 'player_iframe')

    # 첫 번째 iframe 선택
    if len(iframes) > 0:

        iframe = iframes[0]

        # iframe으로 전환
        driver.switch_to.frame(iframe)

        # iframe 내에서 HTML 가져오기
        iframe_html = driver.page_source

        # BeautifulSoup으로 HTML 파싱
        iframe_soup = BeautifulSoup(iframe_html, 'html.parser')

        # 원하는 div 태그 찾기
        div_tag = iframe_soup.find('div', {'id': 'coverImage'})

        # div 태그에서 정보 추출
        if div_tag:
            div_style = div_tag.get('style')

            match = re.search(r'url\("(.+)"\);', div_style)

            if match:
                extracted_url = match.group(1)
            else:
                print('URL을 찾을 수 없습니다.')
        else:
            print('Div 태그를 찾을 수 없습니다.')
    else:
        print('player_iframe 클래스를 가진 iframe을 찾을 수 없습니다.')

    # 웹드라이버 종료
    driver.quit()

    return extracted_url


def newscrawring():
    url = 'https://news.daum.net/'
    page = urlopen(url)
    soup = BeautifulSoup(page, "lxml")
    news_list = soup.select('div.box_news_issue li')
    home = []
    for news in news_list:
        home.append(news.select_one('a').get('href', None))


    # 모델에서 가져온 값
    model_values = Crawring.objects.values_list('src', flat=True)

    # 리스트 a에서 모델에 있는 값을 제외
    home = [item for item in home if item not in model_values]

    home_news = {'title': [], 'content': [], 'img': [], 'src': []}

    if len(home) == 0:
        return print('pass')

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
                a.append(i.img.get('src',''))
                if a != '':
                    break
            elif i.name == 'iframe':
                a.append(iframe_src(url_de))
                if a != '':
                    break
            else:
                pass

        # 이미지 주소 추가
        if a:
            home_news['img'].append(a[0])
        else:
            home_news['img'].append('')

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


