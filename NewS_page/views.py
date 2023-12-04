from django.shortcuts import render, redirect
from .models import Crawring_ct
from django.core.paginator import Paginator
from django.core.mail import EmailMessage
from django.views.decorators.csrf import csrf_exempt

def main_page(request):


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

@csrf_exempt
def email_page(request):
    if request.method == 'POST':
        email = EmailMessage(
            f"새로운 문의 내용",  # 이메일 제목
            f"""내용 : {request.POST.get("message", "예약 내용")} 
        연락처 : {request.POST.get("email", "연락처 미공개")}""",  #이메일 내용
            to=['starhochoitest@gmail.com'],  # 받는 이메일
        )
        email.send()
        return redirect('/')
    else:
        return redirect("/")

    # 여기 redirect가 잘 안돌아가는데 이유는 백그라운드에서 모델이 계속 도는데
    # 서버가 이메일을 보내고 redirect까지 한번 수행하는게 안됨. 모델을 꺼버리면 잘됨.
