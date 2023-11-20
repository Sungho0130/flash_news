    window.onscroll = function() {myFunction()};

    function myFunction() {
        var winScroll = document.body.scrollTop || document.documentElement.scrollTop;
        var height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
        var scrolled = (winScroll / height) * 100;
        document.getElementById("indicator").style.width = scrolled + "%";
    }

    (function(d, s, id){
        var js, fjs = d.getElementsByTagName(s)[0];
        if (d.getElementById(id)) {return;}
        js = d.createElement(s); js.id = id;
        js.src = 'https://widgets.financewidget.com/loader.js';
        fjs.parentNode.insertBefore(js, fjs);
    }(document, 'script', 'financewidget-jssdk'));

//	async function fetchData() {
//		try {
//			// 비동기적으로 서버에서 데이터 가져오기
//			const response = await fetch('/your-model-endpoint/', {
//				method: 'GET',
//				credentials: 'include',  // CSRF 토큰을 함께 전송
//			});
//			const data = await response.json();
//
//			// 여러 기사에 대한 결과를 표시
//			data.result.forEach((summarize, index) => {
//				document.getElementById(`loading-screen-${index + 1}`).style.display = "none";
//				document.getElementById(`result-section-${index + 1}`).style.display = "block";
//				document.getElementById(`result-section-${index + 1}`).innerHTML = `<p>${summarize}</p>`;
//			});
//
//			// 확인용으로 모델 결과를 콘솔에 출력
//			console.log('Model result:', data.result);
//		} catch (error) {
//			console.error('Error fetching data:', error);
//		}
//		}
//
//		// fetchData 함수를 바로 호출하여 페이지 로딩시 실행
//	fetchData();
	// fetchData 함수를 바로 호출하여 페이지 로딩시 실행
//	fetchData();

	#navBar {
	position: fixed;
	top: -header.height;
	width: 100%;
	transition: top 0.5s;
	transition: top 0.5s;
	}

    var navbar = document.querySelector('.main-menu-con');

    // 네비게이션 바의 초기 위치를 가져옵니다.
    var navbarOffset = navbar.offsetTop;

