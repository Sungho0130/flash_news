# 📄 프로젝트 소개

현대사회는 "대 정보 시대"라고 불리는 만큼 하루에도 수백, 수천 개의 뉴스가 발간되어 기업, 국가, 지역, 또는 개개인의 활동에 대한 정보를 제공합니다. 하지만 양이 지나치게 방대하여 개인이 전부 읽은 뒤 정확하고 필요한 정보만 찾거나 얻기에는 시간의 압박이라는 어려움이 있습니다. 따라서 저희는 빠른 전달력과 정확한 정보를 중점으로 기사 요약을 하여 요약된 기사에 대한 접근성과 가독성이 높은 형태로 제공하려고 합니다.

# 🗓️ 개발 기간

23.11.13 - 23.11.27(총 15일)

# 👨‍👨‍👧‍👧 멤버 구성 및 역할

| [최성호](https://github.com/Sungho0130)                                                                                                                                                                                                                                                                               | [홍승재](https://github.com/ghdtmd4117)   | [김건희](https://github.com/Geonzzang)              | [김성진](https://github.com/dolrea77)                  |



- **최성호**
    - Frontend

- **홍승재**
    - Frontend

- **김건희**
    - Backend
    - 사용 가능 모델 탐색 
    - 자료 수집 및 정리
    - 서기

- **김성진**
    - Backend
    - 웹 서버 관리
    - 모델 성능 실험 및 연동
    - DB 관리



# ⚒️ 기능


## 기사 요약

- IT / 경제분야 뉴스를 이용하여 학습한 모델(`T5`, `polyglot-ko`)을 이용하여 뉴스를 요약 제공합니다.
- `T5` 모델을 이용하여 한줄 요약을 만들어내고, 이후 자세한 내용은 `polyglot-ko` 모델을 이용하여 상대적으로 긴 요약 내용을 추가해 줍니다.
- 모델을 이용하여 생성된 결과는 유의미한 문장만을 가져와 후처리하여 반환합니다.

# 🏗️ 프로젝트 구조

# 서버 구조

<img src="images/flash_news 서버구조2.jpg">

# DB 구조

<img src="images/flash_news 구조2.jpg">

# 👨‍🔬 사용 모델

사용한 이유~~~
이러한 이유로 따로 미세조정을 하지않고 'bertshared-kor-base' 모델을 사용하였습니다.

## 기사 요약

- 논문 요약 데이터셋과 IT / 경제분야 뉴스 요약 데이터셋을 실험한 결과 선정된 IT / 경제분야 뉴스 요약 데이터셋을 선정하여 요약 모델을 학습시켰습니다.
- 선정된 데이터셋을 이용하여 본 서비스에서 사용될 `T5-base`, `polyglot-ko 1.3b` 모델을 학습시켰습니다.

# 데모 영상

![](/assets/img/demo.gif)

# 🔗 링크

- [랩업 리포트](https://github.com/Sungho0130/flash_news/blob/fc8fbed8fea65c3c66ad61c1b245edc0a8a3d8fa/images/Flash%20News.pdf)
- [프로젝트 소개 노션 페이지](https://www.notion.so/Flsah-News-7f856b82e54c4ef6a42cfeca0868ada3)
- [서비스 바로가기](https://www.flash-newss.kro.kr/)
