from apscheduler.schedulers.background import BackgroundScheduler
from .news_craw import crawring
from .models import Crawring_ct
from .model_call import summary
from datetime import datetime, timedelta

import concurrent.futures
def summarize_parallel(content_list):
    # content_list는 각각의 content를 포함하는 리스트입니다.
    # 요약된 결과를 저장할 리스트
    summarized_results = []
    # 요약 모델을 병렬로 실행하는 함수
    def run_summary(content):
        return summary(content)
    max_workers = min(len(content_list), 2)  # 예: 최대 ?개의 스레드 사용(본인 컴퓨터에 맞는 스레드 사용)
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        # 각 content에 대해 run_summary 함수를 실행하고 결과를 리스트에 저장
        results = list(executor.map(run_summary, content_list))
        summarized_results.extend(results)
    return summarized_results

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
    cate_list = ['main', 'society', 'politics', 'economic', 'culture', 'entertain', 'sports', 'digital']
    for cate in cate_list:
        print(f'{cate}크롤링 시작')
        news_ct = crawring(cate)
        print(f'{cate} 크롤링 완료!')
        try:
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
        except:
            print('크롤링 필요없음')
        # 해당카테고리의 오래된 순서로 60개초과시 삭제
        data_num_ct(cate)
        if not Crawring_ct.objects.filter(summarize_ct=''):
            print('비어있는 summarize_ct가 없습니다')
        else:
            content_ct_queryset = Crawring_ct.objects.filter(summarize_ct='', category=cate).exclude(title_ct='').values_list('content_ct', flat=True)
            content_ct_list = list(content_ct_queryset)
            summarized_ct_results = summarize_parallel(content_ct_list)
            queryset_ct = Crawring_ct.objects.filter(summarize_ct='', title_ct__isnull=False, category=cate)
            for obj, summary_text in zip(queryset_ct, summarized_ct_results):
                obj.summarize_ct = summary_text
                obj.save()
            print('요약 모델 작동 완료')
def main():
    sched = BackgroundScheduler()
    sched.remove_all_jobs()
    sched.add_job(job,'interval', minutes=60, id='test',  next_run_time=datetime.now()) # job 모델 얼마나 한번씩 돌릴건지
    sched.start() # job 모델 시작하는 코드
if __name__ == '__main__':
    main()