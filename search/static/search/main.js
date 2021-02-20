import * as display from '../../../static/scripts/display.js';
import SetScreen from '../../../static/scripts/screen.js';

const mainScreen = new SetScreen();

//뒤로가기 버튼 
const backBtn = document.querySelector('.back__btn');

backBtn.addEventListener('click', ()=> {
    history.go(-1);
});

// main - height 설정
window.addEventListener('DOMContentLoaded', ()=>{
    mainScreen.setMainHeight(mainScreen.main);
});
window.addEventListener('resize', ()=>{
    mainScreen.setMainHeight(mainScreen.main);
});

// search-bar icon 변경 
const input = document.querySelector('.search-bar__input');
const searchIcon = document.querySelector('.search__icon');
const cancelIcon = document.querySelector('.cancel__icon');

input.addEventListener('input', () => {
    if(input.value == ""){
        display.show(searchIcon);
        display.hide(cancelIcon);
    } else {
        display.show(cancelIcon);
        display.hide(searchIcon);
    }
});

// search - cancel icon 클릭시 검색어 초기화
cancelIcon.addEventListener('click', initInput);

function initInput(){
    input.value = '';
    display.show(searchIcon);
    display.hide(cancelIcon);
}


// -- ajax로 사용자 위치 보내고, 데이터 받아오기 --
let userX = 37.5666103; // 위치허용 하지 않을때, 사용자 중심값 : 서울시청
let userY = 126.9783882; 

// 현재 위치 허용하면, 서버에 현재 사용자 위치 전달
window.addEventListener('DOMContentLoaded', ()=> {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(onSuccessLocation, onErrorGeolocation);
    } else {
        alert('GPS를 지원하지 않습니다.');
    };   
});

// 다른 페이지로 이동할 때, 위치허용 한번 더 물어봄
window.addEventListener('beforeunload', ()=> {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(onSuccessLocation, onErrorGeolocation);
    } else {
        alert('GPS를 지원하지 않습니다.');
    };  
});
//필요없는 경우 여기까지 삭제

function onSuccessLocation(position) {
    userX = position.coords.latitude;
    userY = position.coords.longitude;
    //sendPosition(userX, userY);
    setLocation(userX, userY);
}

function onErrorGeolocation() {
    alert('설정에서 위치 접근 권한을 허용해 주세요.');
}

function setLocation(userX, userY){
    const userLocation1 = document.querySelector('input[name="userX"]');
    userLocation1.value = userX;

    const userLocation2 = document.querySelector('input[name="userY"]');
    userLocation2.value = userY;
}


