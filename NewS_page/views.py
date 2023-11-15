from django.shortcuts import render, redirect
from .models import Crawring
from .news_craw import newscrawring
from .model_call import summary
from django.http import JsonResponse

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

    craw = Crawring.objects.all()

    for instance in craw:
        instance.save()

    return render(request, "main.html", {'craw': craw})



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








