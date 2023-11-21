from apscheduler.schedulers.background import BackgroundScheduler
from .news_craw import newscrawring
from .models import Crawring
from .model_call import summary

def data_num():
    max_records = 50
    current_records = Crawring.objects.count()

    if current_records > max_records:
        # 최신 데이터 기준으로 오래된 레코드를 선택
        records_to_delete = Crawring.objects.order_by('created_at')[:current_records - max_records]

        # 선택된 레코드를 삭제
        for record in records_to_delete:
            record.delete()


def job():

    news = newscrawring()

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



    # 데이터 베이스 50개 초과시 오래된 것 부터 삭제
        data_num()

        for instance in Crawring.objects.filter(summarize=''):
            # 이미 채워진 content를 사용
            content = instance.content

            # summary 모델을 돌리기
            summarize = summary(content)

            # summarize가 비어있는 경우에만 저장
            if not instance.summarize:
                instance.summarize = summarize
                instance.save()


def main():
    sched = BackgroundScheduler()
    sched.add_job(job,'interval', seconds=100000, id='test')
    sched.start()