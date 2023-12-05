# 📄 프로젝트 소개

현대사회는 "대 정보 시대"라고 불리는 만큼 하루에도 수백, 수천 개의 뉴스가 발간되어 기업, 국가, 지역, 또는 개개인의 활동에 대한 정보를 제공합니다. 하지만 양이 지나치게 방대하여 개인이 전부 읽은 뒤 정확하고 필요한 정보만 찾거나 얻기에는 시간의 압박이라는 어려움이 있습니다. 따라서 저희는 빠른 전달력과 정확한 정보를 중점으로 기사 요약을 하여 요약된 기사에 대한 접근성과 가독성이 높은 형태로 제공하려고 합니다.

# 🗓️ 개발 기간

23.11.10 - 23.11.27(총 18일)

# 👨‍👨‍👧‍👧 멤버 구성 및 역할

- [**최성호**](https://github.com/Sungho0130)
    - Frontend
        - HTML, CSS, JS
    - 소스트리 및 github 관리
    - Model 탐색

- [**홍승재**](https://github.com/ghdtmd4117)
    - Frontend
        - HTML, CSS, JS
    - Model 탐색 및 비교
    - 데이터 수집

- [**신건희**](https://github.com/Geonzzang)
    - Backend
    - 사용 가능 모델 탐색 
    - 자료 수집 및 정리
    - 회의록 작성 및 관리
    - 노션 관리
    - Model 탐색
    - DB 연동

- [**김성진**](https://github.com/dolrea77)
    - Backend
    - 웹 서버 관리
    - Model 성능 실험 및 연동
    - DB 관리


# 🏗️ 프로젝트 구조

# 서버 구조

<img src="images/flash_news 서버구조2.jpg">



# 벡엔드 구조

<img src="images/flash_news 구조2.jpg">



# 👨‍🔬 사용 모델


## 모델 소개

저희가 사용한 'Bertshared-kor-base' 모델은 ~~~모델설명

## 사용한 이유

밑에 나오는 표는 kobart와 저희가 사용한 모델과 비교한 루지 지표입니다.

<p align="center" width="100%">
    <img src="images/BERTShared vs KoBART.png" width="50%">
    <img src="images/512_over_BERTShared vs KoBART.png" width="50%">
</p>

kobart와 bertshared 두 모델 중에 bertshared를 사용한 이유는 저희의 기획 의도 자체가 정확한 정보를 가독성이 좋게 전달함에 있기 때문에 요약되어 나오는 출력값에 대해 초점을 뒀습니다.
아무래도 kobart는 한국어에 대한 미세조정만 된 것이지 한국어 뉴스 기사에 대한 미세조정이 잘 되어있는 모델은 아니기 때문에 bertshared를 선택했습니다.
그리고 bert는 기본적으로 문맥 파악에 제일 큰 강점을 가지고 있는 모델이다보니 뉴스에서 정확한 정보를 파악 후 요약해서 전달 함에 있어서 최적이라고 생각이 들었습니다. 이러한 이유로 따로 미세조정을 하지않고 'bertshared-kor-base' 모델을 사용하였습니다.


# ⚒️ 기능

## 기사 크롤링

- 다음뉴스에서 크롤링 작업을 시행합니다. 홈 과 각 카테고리 별로 크롤링을 해옵니다.
- 크롤링을 하는 작업에서 DB안에 뉴스 기사 제목을 통한 중복값과 url을 확인한 후 필터링 합니다.
- 실시간으로 크롤링을 계속 돌리는게 한정적인 서버를 이용해야하는 저희의 입장에서 많이 부담이 되었으며, 현실적인 서비스 이용에 있어서 불가능하다고 판단하여 실시간 => 매시간 으로 크롤링해오는 시간을 설정하여 자동화를 시켰습니다.


## 기사 요약

- 다음 뉴스에서 크롤링해온 뉴스 기사들을 병렬 작업하여 요약합니다.
- bert기반 모델을 사용하기때문에 크롤링 해온 데이터의 text가 512자가 넘는건 자르고, 너무 짧으면 요약 할 이유가 없으니 30자 이내로는 그대로 사용했습니다.
- text 데이터의 길이에 따라 출력되는 요약 text의 최소, 최대 길이를 정해주었습니다.

```
min_length = max(10, int(0.1 * sentence_length))
max_length = min(128, int(0.3 * sentence_length))
```


# 발표 영상(or 시현 영상인데 시현 영상이 들어가는게 좋아보임)

![](images/웹서비스시현영상.gif)

# 발전 가능성

- 모바일 어플리케이션 개발
    - 현재 모바일로 서비스 이용은 가능하나 모바일 전용으로 만든것은 아니어서 서비스에 이용에 있어서 불편함이 있다. 이동시간에도 서비스 사용할 수 있도록 어플리케이션 개발을 하는 것이 좋다고 판단하였음.
- 해외 뉴스에 대한 기사 요약 모델 추가
    - 요즘은 국내 뉴스보다도 해외뉴스에 관심이 많이 가지는 추세라고 함. 그러므로 해외 뉴스에 대한 요약 할 수 있는 모델도 추가하여 서비스를 광범위하게 넓힐수 있다고 판단.
- 서버 및 컴퓨터 성능 업그레이드
    - 현재 컴퓨터와 서버 성능으로는 요약 모델이 무거워 실시간 => 매시간으로 서비스를 구현중인데 이 부분이 개선된다면 DB의 용량 뿐아니라 "매시간"이 아니라 "실시간"으로 크롤링하여 바로 요약할 수 있도록 개선 할 수 있음.

# 🔗 링크

- [PPT](https://github.com/Sungho0130/flash_news/blob/fc8fbed8fea65c3c66ad61c1b245edc0a8a3d8fa/images/Flash%20News.pdf)
- <a href="https://smooth-cinnamon-b2d.notion.site/Flsah-News-7f856b82e54c4ef6a42cfeca0868ada3?pvs=4" target="_blank">[프로젝트 소개 노션 페이지]</a>
- <a href="https://www.flash-news.kro.kr/" target="_blank">[서비스 바로가기]</a>


# Reference
- <a href="https://github.com/hyunwoongko/kobart-transformers" target="_blank">[Kobart]</a>
- <a href="https://github.com/kiyoungkim1/LMkor" target="_blank">[Bertshared]</a>
- <a href="https://github.com/huggingface/transformers" target="_blank">[Huggingface Transformers]</a>
- <a href="https://github.com/google-research/bert" target="_blank">[Bert]</a>
