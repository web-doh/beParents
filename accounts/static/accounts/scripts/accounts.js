'use strict';
const submitBtn = document.querySelector('.submit__btn');
const inputForm = document.querySelector('.form');
const termsAgree = document.querySelector('.terms__checklist'); 
const inputs = document.querySelectorAll('input');

//오류 메세지
const errorMessage = {
    username_error: "이메일 형식에 맞게 다시 작성해주세요.",
    duplicate_error: "아이디 중복 확인을 해주세요.",
    duplicate_fail: "이미 가입된 아이디입니다.",
    duplicate_pass: "사용 가능한 아이디입니다.",
    password_error: "영문과 숫자를 포함하여 6자리 이상 입력해주세요.",
    password_check_error: "비밀번호가 일치하지 않습니다. 다시 입력해주세요.",
    user_phone_error: "'-'를 제외한 휴대폰 번호 10-11자리를 입력해주세요.",
    user_realname_error: "숫자와 특수기호를 제외한 2자 이상의 문자를 입력해주세요.",
    essential: "필수 입력 항목입니다.",
    essential_agree: "필수 선택 항목입니다."
};

// --아이디 중복 체크--
const checkBtn = document.querySelector('#duplicate-check');
const username = document.querySelector('#username');


// 아이디 중복확인 - 서버 통신
function checkIdDuplicate(){
    if(isValid(username) === false) {
        return;
    };
    
    ajaxCommunication()
    .then(data => {
        const message = document.querySelector("#duplicate_message"); 
        if(data['duplicate'] === 'fail') {
            isFailed(username, 'duplicate_message', 'duplicate_fail');
            message.style.color = 'var(--color-point)';
            return;
        } else {
            isPassed(username, 'duplicate_message');
            showErrorMessage('duplicate_message', 'duplicate_pass');
            message.style.color = "var(--color-main)";
            isDisabled();
            return;
        }
    })
    .catch(e =>
        console.log('error:'+e.status)
    );
}

function ajaxCommunication(){
    return new Promise(function (resolve, reject){
        $.ajax({
            url: '/accounts/check_id_duplicate/',
            data: {
                'username': username.value
            },
            datatype: 'json',
            success: resolve,
            error: reject
            })
    });
}

checkBtn.addEventListener("click", checkIdDuplicate);

// 아이디 입력 변경 시 중복 확인 결과 초기화
username.addEventListener("change", () => {
    username.dataset.result = "fail";
    hideErrorMessage("duplicate_message");

    if (isValid(username) === false) {
        isDisabled();
    } else {
        isAbled();
    }
});

// 아이디 중복 확인 하지 않은 경우 에러 메세지 
submitBtn.addEventListener('click', () => {
    if(username.dataset.result === "fail"){
        const message = document.querySelector("#duplicate_message"); 
        isFailed(username, 'duplicate_message', 'duplicate_error');
        message.style.color = "var(--color-point)";
    }
});


// 양식에 맞게 작성하면 버튼 활성화 / 안맞는 경우 비활성화
function isAbled(){
    checkBtn.className = "btn__abled";
    checkBtn.disabled = false;
}

function isDisabled(){
    checkBtn.className = "btn__disabled";
    checkBtn.disabled = true;
}



//--오류 체크--
inputForm.addEventListener("change", (e) => {
    const target = e.target;
    if (target.id !== "password_check") {
        isValid(target);
    } else {
        isPwdMatch(target);
    }
});

inputs.forEach((input) => {
    input.addEventListener("invalid", (e) => {
        const target = e.target;
        e.preventDefault();
        if (target.type !== "checkbox" && target.id !== "password_check") {
            isValid(target);
        };
        
        isValueFilled(target);
    });
});

// 필수 동의 체크 안하고 제출했다가 에러 메세지 받은 후, 나중에 동의하면 에러메세지 삭제
termsAgree.addEventListener("click", (e) => {
    const target = e.target.id;
    if (!target.includes("must")) return;
    const errorName = `${target}_error`;
    const errorTag = document.querySelector(`#${errorName}`);
    if (errorTag.textContent) hideErrorMessage(errorName);
});


// 유효성 검사 
const validityPattern = {
    username: /^[^@\s]+@[^@\s]+\.[^@\s]+$/,
    password : /^(?=.*[A-Za-z])(?=.*\d).{6,}$/,
    user_phone:/[0-9]{3}[0-9]{3,4}[0-9]{4}/,
    user_realname: /^[가-힣a-z]{2,}$/i
};

function isValid(input){
    const pattern = validityPattern[input.id];
    const errorName = `${input.id}_error`;
    if(!pattern.test(input.value)){
        showErrorMessage(errorName, errorName);
        return false;
    } else {
        hideErrorMessage(errorName);
    }
}

// 필수 입력 항목 검사
function isValueFilled(input){
    const errorName = `${input.id}_error`;
    if(input.type !== 'checkbox'){
        if(input.value === ''){
            showErrorMessage(errorName,'essential');
        }
    } else {
        if(!input.checked){
            showErrorMessage(errorName, 'essential_agree');
        }else{
            hideErrorMessage(errorName);
        }
    };
}


// 비밀번호 확인 검사 
function isPwdMatch(target){
    let password = document.querySelector('#password').value;
    let password2 = document.querySelector('#password_check').value;
    const errorName = 'password_check_error';
    
    if (password !== "" || password2 !== "") {
        if(password !== password2) {
            isFailed(target, errorName, errorName);
        } else {
            isPassed(target, errorName);
        }
    };
}

function isFailed(target, input, errorName) {
    showErrorMessage(input,errorName);
    preventSubmit(target);
}

function isPassed(target, input){
    hideErrorMessage(input);
    activateSubmit(target);
}

// 에러메세지
function showErrorMessage(input, errorName) {
    const messageTag = document.querySelector(`#${input}`);
    messageTag.textContent = errorMessage[errorName];
}

function hideErrorMessage(input) {
    const messageTag = document.querySelector(`#${input}`);
    messageTag.textContent = ''; 
}


// 제출방지
function preventSubmit( target){
    target.dataset.result = 'fail';
    submitBtn.disabled = true;
}

function activateSubmit(target){
    target.dataset.result = 'pass';
    submitBtn.disabled = false;
}


// -- 체크박스 선택 -- 
// 전체 선택
const checkAll = document.querySelector("#agree_all");

function selectAll() {
    const checkboxes = document.querySelectorAll(".checklist__input");

    checkboxes.forEach((checkbox) => {
    checkbox.checked = checkAll.checked;
    });
}

checkAll.addEventListener("click", selectAll);

// 개별 선택
function selectOne(e){
    if (e.target === checkAll || e.target.nodeName !== "INPUT" && e.target.nodeName !== "LABEL") return;
    let is_checked = true;

    const checkboxes = document.querySelectorAll(".normal");
    const checked = document.querySelectorAll(".normal:checked");
    checkAll.checked = (checkboxes.length === checked.length) ? true :false;
}

termsAgree.addEventListener("click", selectOne);


