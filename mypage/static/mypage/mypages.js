'use strict';
import SetScreen from '../../../static/scripts/screen.js';
import PopUp from '../../../static/scripts/popup.js';

const mainScreen = new SetScreen();
const confirmBanner = new PopUp();

//뒤로가기 버튼 
const backBtn = document.querySelector('.back__btn');

backBtn.addEventListener('click', ()=> {
    agreeLinkTo('/mypage/');
});

// detail 높이 설정
window.addEventListener('DOMContentLoaded', ()=> {
    mainScreen.setMainHeight(mainScreen.main);
});
window.addEventListener('resize', () =>  {
    mainScreen.setMainHeight(mainScreen.main);
});

mainScreen.setClickListener(() => mainScreen.scrollIntoView('.main'));


// 게시물 삭제 버튼 클릭시, 확인 팝업 창 
const deleteBtn = document.querySelectorAll('.my-reviews__delete');
if(deleteBtn){
    deleteBtn.forEach(btn => btn.addEventListener('click', () => {
        const centerId = btn.querySelector('#centerId').innerHTML;
        const reviewId = btn.querySelector('#reviewId').innerHTML;

        let context = `정말 삭제하시겠습니까 ?`
        confirmBanner.show(context);
        confirmBanner.setClickListener(() => agreeLinkTo(`/centers/${centerId}/${reviewId}/delete/`));
    }));
};

function agreeLinkTo(linkTo){
    location.href = linkTo;
}
