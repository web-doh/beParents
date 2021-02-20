export function show(target){
    target.classList.remove('inactive');
}

export function hide(target){
    target.classList.add('inactive');
}

export function toggle(target){
    target.classList.toggle('inactive');
}

