from django.shortcuts import render, redirect
from .models import Crawring
from .news_craw import newscrawring
from .model_call import summary
from django.http import JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def main_page(request):
    Crawring.objects.all().delete()

    news = newscrawring()

    for i in range(len(news['title'])):
        title = news['title'][i]
        content = news['content'][i]
        img = news['img'][i]
        src = news['src'][i]

        # Crawring 모델 인스턴스 생성 및 저장
        Crawring.objects.create(title=title, content=content, img=img, src=src)

    # 모든 뉴스 기사 가져오기
    craw = Crawring.objects.all()

    # Paginator를 사용하여 뉴스 기사를 페이지로 나눔
    paginator = Paginator(craw, 15)  # 한 페이지에 15개의 뉴스 기사를 표시

    page = request.GET.get('page')  # GET 파라미터에서 현재 페이지 번호 가져오기
    try:
        paginated_craw = paginator.page(page)
    except PageNotAnInteger:
        # 페이지 번호가 정수가 아닌 경우, 첫 번째 페이지로 이동
        paginated_craw = paginator.page(1)
    except EmptyPage:
        # 페이지 번호가 너무 큰 경우, 마지막 페이지로 이동
        paginated_craw = paginator.page(paginator.num_pages)

    return render(request, "main.html", {'craw': paginated_craw})



def your_model_endpoint(request):
    try:
        news = newscrawring()
        summarizations = []

        for j in range(len(news['content'])):
            summarize = summary(news['content'][j])
            summarizations.append(summarize)

        result_data = {'result': summarizations}

        # 서버 측 로그 추가
        print("Model Result:", summarizations)

        return JsonResponse(result_data)
    except Exception as e:
        print("Error in your_model_endpoint:", str(e))
        return JsonResponse({'result': []})








