from django.shortcuts import render, redirect
from .models import Crawring
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def main_page(request):

    craw = Crawring.objects.exclude(summarize='').order_by('-created_at')[:20]




    # Paginator를 사용하여 뉴스 기사를 페이지로 나눔
    paginator = Paginator(craw, 10)  # 한 페이지에 15개의 뉴스 기사를 표시

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




