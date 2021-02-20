'use strict';
import PopUp from '../../../static/scripts/popup.js';
import SetScreen from '../../../static/scripts/screen.js'

const reviewBanner = new PopUp();
const mainScreen = new SetScreen();

const submitBtn = document.querySelector('.submit__btn');
const backBtn = document.querySelector('.back__btn');

const score = document.querySelector('.review__score');
const scoreOne = document.querySelector('#score1');
const errorMessage = document.querySelector('.error__message');

// main 높이 설정
window.addEventListener('DOMContentLoaded', ()=> {
    mainScreen.setMainHeight(mainScreen.main);
});
window.addEventListener('resize', () =>  {
    mainScreen.setMainHeight(mainScreen.main);
});

// back 버튼 팝업
backBtn.addEventListener('click', () => {
    let context = '리뷰 작성을 취소하시겠습니까?';
    reviewBanner.show(context);
    reviewBanner.agreeBtn.setAttribute('type','button');
    reviewBanner.agreeBtn.setAttribute('form','');
    reviewBanner.setClickListener(() => history.go(-1));
});


// 등록 팝업 창 
submitBtn.addEventListener('click', () => {
    isValueFilled();
});


// 별점 체크 안했을 경우 에러 메세지
function isValueFilled(){
        if(!scoreOne.checked){
            showErrorMessage();
        }else{
            hideErrorMessage();
            let context = '리뷰를 등록하시겠습니까?';
            reviewBanner.show(context);
            reviewBanner.agreeBtn.setAttribute('type','submit');
            reviewBanner.agreeBtn.setAttribute('form','review__form');
        }
}

// 에러메세지
function showErrorMessage() {
    errorMessage.textContent = '별점을 남겨주세요';
}

function hideErrorMessage() {
    errorMessage.textContent = ''; 
}



//별점 마킹 모듈 프로토타입으로 생성
function Rating(){};
Rating.prototype.rate = 0;
Rating.prototype.setRate = function(newrate){
    //별점 마킹 - 클릭한 별 이하 모든 별 체크 처리
    this.rate = newrate;
    let items = document.querySelectorAll('.rate__radio');
    items.forEach(function(item, idx){
        if(idx < newrate){
            item.checked = true;
        }else{
            item.checked = false;
        }
    });
}
let rating = new Rating();//별점 인스턴스 생성

document.addEventListener('DOMContentLoaded', function(){
    score.addEventListener('click',function(e){
        let elem = e.target;
        if(elem.classList.contains('rate__radio')){
            rating.setRate(parseInt(elem.value));
        }
    })
});

// 편집 화면에서 별점확인
const prevScore = document.querySelector('#score');
if(prevScore){
    rating.setRate(parseInt(prevScore.innerHTML));
}


// -- 이미지 업로드 미리보기 (1개만 등록되도록 설정) --
const reviewImage = document.querySelector('.review__image');
const imagePreview = document.querySelector('#image__preview');
const deleteImage = document.querySelector('.image__delete');

// 업로드된 이미지가 있다면, x 클릭시 삭제 
if(deleteImage){
    deleteImage.addEventListener('click', () => {
        initThumbnail(imagePreview);
    });  
}

reviewImage.addEventListener('change', setThumbnail);
reviewImage.addEventListener('click', () => {
    reviewImage.value = null;
});

function setThumbnail(event) { 
    initThumbnail(imagePreview);
    
    const reader = new FileReader();
    reader.onload = (event) => { 
        // 새로운 이미지 업로드
        const img = document.createElement('img'); 
        img.setAttribute('src', event.target.result); 
        img.classList.add('image__uploaded');
        
        // 이미지 삭제 버튼 추가
        const checkbox = document.createElement('input');
        checkbox.classList.add('image__delete');
        checkbox.setAttribute('type','checkbox');
        checkbox.setAttribute('name','image__delete');
        checkbox.setAttribute('value','delete');

        imagePreview.append(img);
        imagePreview.append(checkbox);

        const deleteImage = imagePreview.lastElementChild;
        deleteImage.addEventListener('click', () => {
            console.log(imagePreview);
            initThumbnail(imagePreview);
            reviewImage.value = null;
        });
    }; 
    reader.readAsDataURL(event.target.files[0]); 
}

// 이전 이미지 삭제
function initThumbnail(parent){
    const thumbnailImg = parent.querySelector('img');
    if(!thumbnailImg) return;
    parent.removeChild(thumbnailImg);
    parent.lastElementChild.style.display ='none';
}

