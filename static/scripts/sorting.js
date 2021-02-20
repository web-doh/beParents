'use strict';
import * as display from './display.js';
import SetScreen from './screen.js';

const mainScreen = new SetScreen();

export default class Sorting {
    constructor(){
        this.sortByBtn = document.querySelector('.sort-by__btn i');
        this.optionNow = document.querySelector('.sort-by__method');
        this.sortOption = document.querySelector('.sort-by__option');
        this.byDistance = document.querySelector('#by-distance');
        this.byScore = document.querySelector('#by-score');

        this.centerList = document.querySelector('.center__list');
        this.centers = [];
        

        this.sortByBtn && this.sortByBtn.addEventListener('click', () => {
            display.toggle(this.sortOption);  
        });

        this.sortOption && this.sortOption.addEventListener('click', e => {
            const target = e.target.parentElement;
            if(target.nodeName != 'LI') return;
            this._changeOption(target);
            display.hide(this.sortOption); 
        });
    }

    _changeOption(target){
        this._setCenters();
        if(target.id == 'by-distance'){
            this.optionNow.innerHTML = '거리순';
            display.show(this.byDistance.lastElementChild);
            display.hide(this.byScore.lastElementChild);
            this._ascending(this.centers, 'distance');
            mainScreen.scrollIntoView('.center__list .center__item');
        }else{
            this.optionNow.innerHTML = '평점순';
            display.show(this.byScore.lastElementChild);
            display.hide(this.byDistance.lastElementChild);
            this._descending(this.centers, 'score');
            mainScreen.scrollIntoView('.center__list .center__item');
        }
    }

    _initList(){
        while(this.centerList.hasChildNodes()) {
            this.centerList.removeChild(this.centerList.firstChild);
        };
    }

    _setList(){
        this._initList();
        for(let i = 0; i < this.centers.length; i++){
            this.centerList.append(this.centers[i]);
        };
    }

    _setCenters(){
        this.center = this.centerList.querySelectorAll('.center__item');
        for(let i = 0; i < this.center.length; i++){
            this.centers[i] = this.center[i];
        };
        return this.centers;
    }

    _ascending(list, option){
        list.sort((a,b) => {
            return a.dataset[option] - b.dataset[option];
        });

        this._setList();
    }

    _descending(list, option){
        list.sort((a,b) => {
            return b.dataset[option] - a.dataset[option];
        });

        this._setList();
    }
}





