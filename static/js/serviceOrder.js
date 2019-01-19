$(document).ready(function () {
    $('#submitBtn').submit(function (event) {
        $('.progress').show();
        event.preventDefault();
    })
});

function recaptchaCallback() {
    $('#submitBtn').removeAttr('disabled');
};

