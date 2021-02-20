'use strict';

export default class SetScreen {
    constructor() {
        this.main = document.querySelector('.main');
        this.navBar = document.querySelector('.navbar');
        
        this.arrowUp = document.querySelector('.arrow-up');

        this.main && this.main.addEventListener('scroll', ()=> {
            if(this.main.scrollTop > window.innerHeight / 2){
                this.arrowUp.classList.add('visible');
            } else {
                this.arrowUp.classList.remove('visible');
            }
        });

        this.arrowUp && this.arrowUp.addEventListener('click',()=>{
            this.onClick && this.onClick(); 
        });
    }
    
    setClickListener(onClick){
        this.onClick = onClick;
    }

    // main 높이 설정
    setMainHeight(section){
        const sectionTop = section.getBoundingClientRect().top;
        const navBarTop = this.navBar.getBoundingClientRect().top;
        const sectionHeight = navBarTop - sectionTop;
        section.style.height = sectionHeight + 'px';   
    }
    
    // 상단으로 가기
    scrollIntoView(selector){
        const scrollTo = document.querySelector(selector);
        scrollTo && scrollTo.scrollIntoView({ behavior: 'smooth'});
    };
}

