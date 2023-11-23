    // 페이지 스크롤 이벤트가 발생할 때마다 myFunction을 호출
    window.onscroll = function() {myFunction()};    // 스크롤시 myFunction 함수를 호출

    function myFunction() {
        var winScroll = document.body.scrollTop || document.documentElement.scrollTop;   // 스크롤된 길이를 가져옴
        var height = document.documentElement.scrollHeight - document.documentElement.clientHeight; // 페이지의 총 길이를 계산
        var scrolled = (winScroll / height) * 100;      // 스크롤된 백분율을 계산
        document.getElementById("indicator").style.width = scrolled + "%";      // 상태 바의 너비를 스크롤된 백분율로 설정하여 진행 상황을 표시
    }

    // 외부 스크립트를 페이지에 로드
    (function(d, s, id){
        var js, fjs = d.getElementsByTagName(s)[0];
        if (d.getElementById(id)) {return;}
        js = d.createElement(s); js.id = id;
        js.src = 'https://widgets.financewidget.com/loader.js';     // 외부 스크립트의 소스 URL을 설정
        fjs.parentNode.insertBefore(js, fjs);                       // 외부 스크립트를 현재 페이지에 삽입
    }(document, 'script', 'financewidget-jssdk'));

//네이게이션 관련 스크립트
document.addEventListener("DOMContentLoaded", function () {
    // 페이지 로드 시 초기 설정: 현재 카테고리에 언더라인 위치 설정
    setUnderlinePosition(0);
    var activeCategory = getActiveCategoryFromURL();
    var activeIndex = getCategoryIndex(activeCategory);
    setUnderlinePosition(activeIndex); // 해당 카테고리의 인덱스로 언더라인 설정

    // 스크롤 이벤트를 사용하여 네비게이션 바 고정 시 언더라인 위치 조정
    window.addEventListener("scroll", function () {
        var isNavFixed = isNavbarFixed(); // 네비게이션 바가 고정되었는지 확인

        // 현재 활성화된 버튼의 인덱스를 가져와 언더라인 위치 조정
        var activeButtonIndex = getActiveButtonIndex();
        setUnderlinePosition(activeButtonIndex, isNavFixed);
    });

    // 네비게이션 바 버튼을 클릭할 때 언더라인의 위치 설정 및 페이지 이동 함수
    function ul(index) {
        setUnderlinePosition(index); // 해당 인덱스로 언더라인 설정
        navigateToCategory(index); // 해당 카테고리 페이지로 이동
    }

    // 언더라인의 위치 설정 함수
    function setUnderlinePosition(index) {
        var underlines = document.querySelectorAll(".underline");
        var navButtons = document.querySelectorAll("nav a");

        if (index >= 0 && index < navButtons.length) {
            var buttonWidth = navButtons[index].offsetWidth;
            var buttonOffsetLeft = navButtons[index].offsetLeft;

            for (var i = 0; i < underlines.length; i++) {
                underlines[i].style.width = buttonWidth + "px";
                underlines[i].style.transition = 'none';

                var topMargin = isNavbarFixed() ? navButtons[index].offsetTop : 0;
                underlines[i].style.transform = 'translate3d(' + buttonOffsetLeft + 'px,' + topMargin + 'px,0)';
            }

            for (var i = 0; i < navButtons.length; i++) {
                navButtons[i].classList.remove("active");
            }
            navButtons[index].classList.add("active");

            setTimeout(function () {
                for (var i = 0; i < underlines.length; i++) {
                    underlines[i].style.transition = '';
                }
            }, 0);
        }
    }

    // 페이지 URL에서 현재 활성화된 카테고리 가져오기
    function getActiveCategoryFromURL() {
        var urlParams = new URLSearchParams(window.location.search);
        return urlParams.get('category');
    }

    // 카테고리의 인덱스 가져오기
    function getCategoryIndex(category) {
        var categories = ['home', 'society', 'politics', 'economic', 'culture', 'entertain', 'sports', 'IT']; // 카테고리 순서대로 배열에 저장
        return categories.indexOf(category); // 배열에서 해당 카테고리의 인덱스 반환
    }

    // 카테고리 페이지로 이동
    function navigateToCategory(index) {
        var categories = ['/', '/?category=society', '/?category=politics', '/?category=economic', '/?category=culture', '/?category=entertain', '/?category=sports', '/?category=IT'];
        window.location.href = categories[index];
    }

    // 네비게이션 바가 상단에 고정되었는지 확인하는 함수
    function isNavbarFixed() {
        var navbar = document.querySelector("nav");
        var navbarRect = navbar.getBoundingClientRect();
        return navbarRect.top <= 0;
    }

    // 현재 활성화된 버튼의 인덱스를 가져오는 함수
    function getActiveButtonIndex() {
        var navButtons = document.querySelectorAll("nav a");
        for (var i = 0; i < navButtons.length; i++) {
            if (navButtons[i].classList.contains("active")) {
                return i;
            }
        }
        return 0; // 기본적으로 첫 번째 버튼을 반환
    }
});