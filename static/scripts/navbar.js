'use strict';

const navbar = document.querySelector('.navbar__menu');

window.addEventListener('DOMContentLoaded', () => {
    const currentPath = location.pathname.split('/')[1];
    changeMenuColor(currentPath);
})

function changeMenuColor(location){
    const allMenu = Array.from(document.querySelectorAll('.navbar__menu__item'));
    
    if(location === 'centers'){
        location = 'map';
    } else if(location === ''){
        location = 'home';
    }

    const currentMenuId = `#navbar__${location}`;
    const currentMenu = document.querySelector(currentMenuId);
    const otherMenu = allMenu.filter(menu => menu != currentMenu );
    currentMenu.classList.add('current');
    otherMenu.forEach(menu => {
        if(menu.classList.contains('current')){
            menu.classList.remove('current');
        }
    });
}

