'use strict';
import SetScreen from '../../../static/scripts/screen.js';
import Sorting from '../../../static/scripts/sorting.js';

const mainScreen = new SetScreen();
const orderedBy = new Sorting();

const searchResult = document.querySelector('.search__result');

// 뒤로가기 버튼 
const backBtn = document.querySelector('.back__btn');

backBtn.addEventListener('click', () => {
    history.go(-1);
});

// result list 높이 설정 
if(mainScreen.main){
    window.addEventListener('DOMContentLoaded', () => {
        mainScreen.setMainHeight(searchResult);
        mainScreen.setMainHeight(mainScreen.main);
    });
    window.addEventListener('resize', () => {
        mainScreen.setMainHeight(searchResult);
        mainScreen.setMainHeight(mainScreen.main);
    });
    
    mainScreen.setClickListener(() => mainScreen.scrollIntoView('.center__list .center__item'));    
};


// -- center 정보 내 거리 및 주소 요약 --

const centerItems = document.querySelectorAll('.center__item');

    centerItems && centerItems.forEach(item => {
        const distanceData = getText(item, '.center__distance');
        const addressData = getText(item, '.center__address');
    
        const distance = setDistance(distanceData);
        const address = setAddress(addressData);
    
        setText(item, '.center__distance', distance);
        setText(item, '.center__address', address);
});


// html 태그의 내용 가져오기 
function getText(parent, selector){
    const text = parent.querySelector(selector).innerHTML;
    return text;
}

// html 태그 안에 내용 넣기
function setText(parent, selector, text){
    const tag = parent.querySelector(selector);
    tag.textContent = text;
}

// 주소 요약 하기
function setAddress(address){
    const longAddress = address.split(' ');
    const shortAddress = `${longAddress[0]} ${longAddress[1]||''} ${longAddress[2]|| ''} `;
    return shortAddress;
}

// 거리 단위 설정 
function setDistance(distance){
    if(distance < 1){
        distance = `${distance * 1000}m`;
    }else{
        distance= `${Math.round(distance *10)/10}km`;
    }
    return distance;
}


// 결과 url에서 user 좌표 파라미터 제거
const url = location.search;
const urlParts = url.split('?');
const params = new URLSearchParams(urlParts[1]);
params.delete('userX');
params.delete('userY');
const newUrl = urlParts[0] + '?' + params.toString();
history.replaceState({}, null, newUrl);




