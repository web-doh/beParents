'use strict';

export default class PopUp {
    constructor() {
        this.popUp = document.querySelector('#pop-up');
        this.popUpContext = document.querySelector('.pop-up__context');

        this.agreeBtn = document.querySelector('.btn-agree');
        this.disagreeBtn = document.querySelector('.btn-disagree');
        this.agreeBtn && this.agreeBtn.addEventListener('click',()=>{
            this.onClick && this.onClick();   
            this.hide();
        });
        this.disagreeBtn && this.disagreeBtn.addEventListener('click',()=>{
            this.hide();
        });

    }
    setClickListener(onClick){
        this.onClick = onClick;
    }
    
    show(message){
        this.popUp.classList.remove('pop-up__hide');
        this.popUpContext.innerText = message;
        new PopUpAlign().align();
    }

    hide(){
        this.popUp.classList.add('pop-up__hide');
    }
}

class PopUpAlign {
    constructor(){
        this.popUp = document.querySelector('#pop-up');
        this.popUpWidth = this.popUp.getBoundingClientRect().width;
        this.popUpHeight = this.popUp.getBoundingClientRect().height;
        this.popUpWindow = document.querySelector('.pop-up__window');
        this.popUpWindowWidth = this.popUpWindow.getBoundingClientRect().width;
        this.popUpWindowHeight = this.popUpWindow.getBoundingClientRect().height;
        this.popUpX = (this.popUpWidth - this.popUpWindowWidth) /2;
        this.popUpY = (this.popUpHeight - this.popUpWindowHeight - 60) /2;
    }

    align(){
        this.popUpWindow.style.left = this.popUpX + 'px';
        this.popUpWindow.style.top = this.popUpY + 'px';
    }
}
