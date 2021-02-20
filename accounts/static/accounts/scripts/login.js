//오류 메세지
const validityMessage = {
    username: {
        typeMismatch:"이메일 형식에 맞게 다시 작성해주세요.",
        badInput: "이메일 형식에 맞게 다시 작성해주세요.",
        valueMissing: "필수 입력 정보입니다."
    },
    password: {
        patternMismatch: "영문과 숫자를 포함하여 6자리 이상 입력해주세요.",
        tooShort: "영문과 숫자를 포함하여 6자리 이상 입력해주세요.",
        valueMissing: "필수 입력 정보입니다."
    }
};

// 에러메세지
function getMessage(target, validity){
    for(let key in validityMessage[target]) {
        if (validity[key]) {
            return validityMessage[target][key];
        };
    };
}

function showErrorMessage(input) {
    const errorTag = $(`#${input.id}`).parent();
    const errorMessage = $('<span class="form__error"></span>');
    errorMessage.html(getMessage(input.id, input.validity));
    errorTag.after(errorMessage);
}

const inputs = document.querySelectorAll('input');
inputs.forEach(input => {
    input.addEventListener('invalid', e => {
        e.preventDefault();
        showErrorMessage(input);
    });
});

function initError(){
    const formError = $('.form__error');
    if(!formError) return;
    $('span').remove('.form__error');
}

$('.submit__btn').on('click', () => {
    initError();
});


function goBack(){
    window.history.go(-2);
}