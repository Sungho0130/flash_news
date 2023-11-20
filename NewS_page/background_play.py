import sched

from apscheduler.schedulers.background import BackgroundScheduler
from .news_craw import newscrawring, category_crawring
from .models import Crawring, Crawring_ct
from .model_call import summary
from datetime import datetime, timedelta
from tqdm import tqdm

def data_num():
    max_records = 40
    current_records = Crawring.objects.count()

    if current_records > max_records:
        # 최신 데이터 기준으로 오래된 레코드를 선택
        records_to_delete = Crawring.objects.order_by('created_at')[:current_records - max_records]

        # 선택된 레코드를 삭제
        for record in records_to_delete:
            record.delete()

def data_num_ct(category):
    max_records = 60
    current_records = Crawring_ct.objects.filter(category=category).count()

    if current_records > max_records:
        # 최신 데이터 기준으로 오래된 레코드를 선택
        records_to_delete = Crawring_ct.objects.filter(category=category).order_by('created_at_ct')[:current_records - max_records]

        # 선택된 레코드를 삭제
        for record in records_to_delete:
            record.delete()


def job():

    news = newscrawring()

    print('home 크롤링 완료!')

    if len(news['title']) != 0:

        for i in range(len(news['title'])):
            # 중복 확인
            if not Crawring.objects.filter(title=news["title"][i]).exists():
                title = news['title'][i]
                content = news['content'][i]
                img = news['img'][i]
                src = news['src'][i]

                # Crawring 모델 인스턴스 생성 및 저장
                Crawring.objects.create(title=title, content=content, img=img, src=src)

        print('home 데이터베이스 저장 완료')

    else:
        print('크롤링 필요없음')

    # 데이터 베이스 50개 초과시 오래된 것 부터 삭제
    data_num()

    if not Crawring.objects.filter(summarize=''):
        print('비어있는 summarize 없음')

    else:
        for instance in tqdm(Crawring.objects.filter(summarize='')):
            # 이미 채워진 content를 사용
            content = instance.content

            if len(content)>10:
                # summary 모델을 돌리기
                summarize = summary(content)
            else:
                summarize = content

            # summarize가 비어있는 경우에만 저장
            if not instance.summarize:
                instance.summarize = summarize
                instance.save()

        print('요약 모델 작동 완료')



    cate_list = ['society', 'politics', 'economic', 'culture', 'entertain', 'sports', 'digital']

    for cate in cate_list:

        news_ct = category_crawring(cate)

        print(f'{cate} 크롤링 완료!')

        if len(news_ct['title']) != None:

            for i in range(len(news_ct['title'])):
                # 중복 확인
                if not Crawring_ct.objects.filter(title_ct=news_ct["title"][i]).exists():
                    title_ct = news_ct['title'][i]
                    content_ct = news_ct['content'][i]
                    img_ct = news_ct['img'][i]
                    src_ct = news_ct['src'][i]
                    category = news_ct['category'][i]

                    # Crawring 모델 인스턴스 생성 및 저장
                    Crawring_ct.objects.create(title_ct=title_ct, content_ct=content_ct, img_ct=img_ct, src_ct=src_ct, category=category)

            print(f'{cate} 데이터베이스 저장 완료')

        else:
            print('크롤링 필요없음')


        # 해당카테고리의 오래된 순서로 90개초과시 삭제
        data_num_ct(cate)

        if not Crawring_ct.objects.filter(summarize_ct=''):
            print('비어있는 summarize_ct가 없습니다')

        else:
            for instance in tqdm(Crawring_ct.objects.filter(summarize_ct='')):

                # 이미 채워진 content를 사용
                content_ct = instance.content_ct
                print('src: ', instance.src_ct)
                if len(content_ct)>10:
                    # summary 모델을 돌리기
                    summarize_ct = summary(content_ct)
                else:
                    summarize_ct = content_ct

                # summarize가 비어있는 경우에만 저장
                if not instance.summarize_ct:
                    instance.summarize_ct = summarize_ct
                    instance.save()

            print('요약 모델 작동 완료')


def main():
    sched = BackgroundScheduler()


    sched.add_job(job,'interval', minutes=60, id='test') #, next_run_time=datetime.now()
    sched.start()

if __name__ == '__main__':
    main()