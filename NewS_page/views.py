from django.shortcuts import render, redirect
from .models import Crawring_ct
from django.core.paginator import Paginator
from django.core.mail import EmailMessage
import time
from .send_email import send_email_task

def main_page(request):

    if request.method == 'POST':
        message = request.POST.get("message", "예약 내용")
        email = request.POST.get("email", "연락처 미공개")

        # 비동기 작업으로 이메일 보내기
        send_email_task.delay(message, email)

        return redirect('/')

    cate = request.GET.get('category', "main")

    print('cate: ', cate)

    # 카테고리별로 필터링된 Crawring_ct 객체를 가져오고 요약이 없는 것은 제외
    craw_ct = Crawring_ct.objects.filter(category=cate).exclude(summarize_ct='').order_by('-created_at_ct')

    # 필터링된 쿼리셋으로 Paginator를 초기화하고 페이지당 항목 수를 설정
    paginator = Paginator(craw_ct, 10)

    # 요청에서 현재 페이지 번호를 가져옴
    page_number = request.GET.get('page')

    # Paginator에서 해당 페이지를 가져옴
    page = paginator.get_page(page_number)

    return render(request, "main.html", {'craw_ct': page, 'category': cate})



