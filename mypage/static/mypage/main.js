'use strict';
import PopUp from '../../../static/scripts/popup.js';

const anonymousBtns = document.querySelectorAll('.anonymous');
const logoutBtn = document.querySelector('.btn__logout');

// 로그인하지 않은 상태로 북마크 클릭시, 로그인 팝업 창 
if(anonymousBtns){
    const loginBanner = new PopUp();
    anonymousBtns.forEach(anonymousBtn => anonymousBtn.addEventListener('click', () => {
        let context = `로그인이 필요한 서비스입니다.
                        로그인 하시겠습니까 ?`
        loginBanner.show(context);
    }));
}

// 로그아웃 버튼 클릭시 팝업창 
if(logoutBtn){
    const logoutBanner = new PopUp();
    logoutBtn.addEventListener('click', ()=> {
        let context = `정말 로그아웃 하시겠습니까 ?`;
        logoutBanner.show(context);
    });
}
