from django.shortcuts import render
from .models import Crawring, Crawring_ct
from django.core.paginator import Paginator
import time
def main_page(request):
    # 요약이 없는 모든 Crawring 객체를 가져오고 생성 날짜 순으로 정렬
    craw = Crawring.objects.exclude(summarize='').order_by('-created_at')

    # 요청에서 카테고리 매개변수가 제공되었는지 확인
    if request.GET.get('category', None):
        cate = request.GET.get('category', None)
        print('cate: ', cate)

        # 카테고리별로 필터링된 Crawring_ct 객체를 가져오고 요약이 없는 것은 제외
        craw_ct = Crawring_ct.objects.filter(category=cate).exclude(summarize_ct='').order_by('-created_at_ct')

        # 필터링된 쿼리셋으로 Paginator를 초기화하고 페이지당 항목 수를 설정
        paginator = Paginator(craw_ct, 10)

        # 요청에서 현재 페이지 번호를 가져옴
        page_number = request.GET.get('page')

        # Paginator에서 해당 페이지를 가져옴
        page = paginator.get_page(page_number)

        return render(request, "main.html", {'craw_ct': page})
    else:

        # 메인 Crawring 쿼리셋용 Paginator를 초기화
        paginator = Paginator(craw, 10)  # 필요에 따라 숫자를 변경

        # 요청에서 현재 페이지 번호를 가져옴
        page_number = request.GET.get('page')

        # Paginator에서 해당 페이지를 가져옴
        page = paginator.get_page(page_number)

        return render(request, "main.html", {'craw': page})