'use strict';
import PopUp from '../../../static/scripts/popup.js';
import SetScreen from '../../../static/scripts/screen.js';
import * as display from '../../../static/scripts/display.js';

const anonymousBtns = document.querySelectorAll('.anonymous');

const loginBanner = new PopUp();
const mainScreen = new SetScreen();

// main 높이 설정
window.addEventListener('DOMContentLoaded', ()=> {
    mainScreen.setMainHeight(mainScreen.main);
});
window.addEventListener('resize', () =>  {
    mainScreen.setMainHeight(mainScreen.main);
});

mainScreen.setClickListener(() => mainScreen.scrollIntoView('#center__map'));

// 로그인하지 않은 상태로 북마크 클릭시, 로그인 팝업 창 
anonymousBtns.forEach(anonymousBtn => anonymousBtn.addEventListener('click', () => {
    let context = `로그인이 필요한 서비스입니다.
                    로그인 하시겠습니까 ?`
    loginBanner.show(context);
    loginBanner.setClickListener(() => 
        agreeLinkTo(`/accounts/login/?next=${location.pathname}`)
    );
}));

// 게시물 삭제 버튼 클릭시, 확인 팝업 창 
const deleteBtn = document.querySelectorAll('.option__delete');
if(deleteBtn){
    deleteBtn.forEach(btn => btn.addEventListener('click', () => {
        const centerId = btn.querySelector('#centerId').innerHTML;
        const reviewId = btn.querySelector('#reviewId').innerHTML;

        let context = `정말 삭제하시겠습니까 ?`
        loginBanner.show(context);
        loginBanner.setClickListener(() => 
            agreeLinkTo(`/centers/${centerId}/${reviewId}/delete/?next=${location.pathname}`)
        );
    }));
};

function agreeLinkTo(linkTo){
    location.href = linkTo;
}



//게시글 유저 이름 축약
const reviewUsers = document.querySelectorAll('.profile__user');
if(reviewUsers){
    reviewUsers.forEach(user => {
        const emailName = user.innerHTML.split('@')[0];        
        const reduceName = emailName.slice(0,2) + ('*'.repeat(emailName.length - 2));
        user.innerHTML = reduceName;
    })
}

// 게시글 편집 버튼
const editBtn = document.querySelectorAll('.center__review__edit');

if(editBtn){
    editBtn.forEach(btn => btn.addEventListener('click', () => {
        const editOption = btn.querySelector('.edit__option');
        display.toggle(editOption);
    })
)};


// 긴 runhours 펼치기 설정
const runhours = document.querySelector('#runhours .info__description');
const runhoursText = runhours.innerHTML;

if(runhoursText.includes('|')){
    const runhoursList = runhoursText.split('|');
    runhours.innerHTML = '';
    runhoursList.forEach(time => {
        runhours.innerHTML += time + `</br>`
    })
    textOverHandler(runhours, 16);
} else {
    runhours.innerHTML = runhoursText;
    textOverHandler(runhours, 16);
}

// 긴 글 리뷰 펼치기 설정 
const reviews = document.querySelectorAll('.center__review__contents');

window.addEventListener('DOMContentLoaded', ()=> {
    reviews.forEach(review => {
        const reviewText = review.querySelector('.center__review__text');
        textOverHandler(reviewText, 100);
    })
})

function textOverHandler(content, length) {
    const text = content.innerHTML;
    const shortText = text.substring(0, length);
    const foldBtn = content.nextElementSibling;
    if(text.length > length) {
        content.innerHTML = shortText;
        content.classList.add('content__fold');
        foldBtn.classList.add('visible');
    } else {
        content.classList.remove('content__fold');
    }
    
    foldBtn.addEventListener('click', () => {
        toggleContent(content);
    });

    function toggleContent(content){
        if(content.classList.contains('content__fold')){
            // 접기 상태
            foldBtn.innerHTML = '<i class="fas fa-chevron-up"></i>';
            content.innerHTML = text;
            content.classList.remove('content__fold');
        } else {
            // 더보기 상태
            foldBtn.innerHTML = '<i class="fas fa-chevron-down"></i>';
            content.innerHTML = shortText;
            content.classList.add('content__fold');
        }
    }
}


// hashtag에 link 연결 
const hashtags = document.querySelector('.hashtags .info__description');
if(hashtags){
    const hashtag = document.querySelectorAll('.center__hashtag a');
    hashtag.forEach(tag => {
        const query = tag.innerHTML.slice(1);
        tag.setAttribute('href', `/search/center_list?&query=${query}`);
        });
};

// ---------------------------------------------- //
// map 설정 
const centerX = document.querySelector('#centerX').innerHTML;
const centerY = document.querySelector('#centerY').innerHTML;
const centerPosition = new naver.maps.LatLng(centerX, centerY);

const selectedUrl = '../../../static/map/image/big-marker.png';
const selectedSize = new naver.maps.Size(42, 42);
const selectedOffset = new naver.maps.Point(21, 42);


const map = new naver.maps.Map('center__map', {
    center: centerPosition,
    zoom: 15,
    scaleControl: false
});

const marker = new naver.maps.Marker({
    position: centerPosition,
    map,
    icon: {
        url: selectedUrl,
        size: selectedSize,
        origin: new naver.maps.Point(0, 0),
        anchor: selectedOffset
    }
})


