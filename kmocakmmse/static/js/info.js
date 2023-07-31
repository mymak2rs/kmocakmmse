document.getElementById("parkins_0").disabled = true;
document.getElementById("parkins_1").disabled = true;
document.getElementById("parkins_2").disabled = true;

if(first == 'True' && error == ''){
    document.querySelector("#edu_0").checked = true;
}else{
    document.querySelector("#id_edu_input").value = parseInt(edu);
}

diag_du = $("#dia_duration");
hy = $("#hy");
motor = $("#updrs");

diag_du_q = $("#dia_duration_q");
hy_q = $("#hy_q");
motor_q = $("#updrs_q");

// diag_du.attr("disabled", true);
// hy.attr("disabled", true);
// motor.attr("disabled", true);

// diag_du_q.hide();
// hy_q.hide();
// motor_q.hide();


if(document.querySelector("#edu_0").checked){
    $('#input-edu_1').show();
}else{
    $('#input-edu_1').hide();
}

var radios = document.querySelectorAll('[name=education]');
var park_radios = document.querySelectorAll('[name=parkinson_disease]');

Array.from(radios).forEach(function(r){
r.addEventListener('click', function(){
    var eduEl = document.getElementById('edu');
    if((this.id == 'edu_0') ){
        $('#input-edu_1').show();
    }
    else{
        $('#input-edu_1').hide();
        
    }
});
});

Array.from(park_radios).forEach(function(r){
    r.addEventListener('click', function(){
        if((this.id == 'parkins_0') ){
            diag_du.attr("disabled", false);
            hy.attr("disabled", false);
            motor.attr("disabled", false);
            $('#dia_duration_q').show();
            $('#hy_q').show();
            $('#updrs_q').show();
        }
        else{
            diag_du.attr("disabled", true);
            hy.attr("disabled", true);
            motor.attr("disabled", true);
            $('#dia_duration_q').hide();
            $('#hy_q').hide();
            $('#updrs_q').hide();
        }
    });
    });

window.onpageshow = function(event) {
    if (event.persisted || (window.performance && window.performance.navigation.type == 2)){
        alert('확인 또는 수정을 눌러주세요.'); 
        window.location.replace("/main/confirm");
    }
}