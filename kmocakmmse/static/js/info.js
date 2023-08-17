document.querySelector("#edu_2").checked = true;

if(document.querySelector("#edu_2").checked){
    $('#input-edu_1').show();
}else{
    $('#input-edu_1').hide();
}

var radios = document.querySelectorAll('[name=education]');

Array.from(radios).forEach(function(r){
r.addEventListener('click', function(){
    if((this.id == 'edu_2') ){
        $('#input-edu_1').show();
    }
    else{
        $('#input-edu_1').hide();
        
    }
});
});
$(document).ready(function() {
    $('#kmoca_total').attr('min', 0);
    $('#kmoca_total').attr('max', 30);
    $('#age').attr('min', 0);
    $('#id_edu_input').attr('min', 0);
    $('#sgds').attr('min', 0);
    $('#sgds').attr('max', 15);
    $('#dia_duration').attr('min', 1);
    $('#hy').attr('min', 0);
    $('#hy').attr('max', 5);
    $('#updrs').attr('min', 0);
    $('#updrs').attr('max', 200);
});
$(document).ready(function() {
    $('#kmoca_total, #age, #id_edu_input, #sgds, #dia_duration, #hy, #updrs').on('change', function() {
        // 0 미만의 값을 입력 받으면 0으로 설정
        if ($(this).val() < 0) {
            $(this).val(0);
        }
    });
    
    $('#sgds').on('change', function() {
        // 15 이상의 값을 입력 받으면 15로 설정
        if ($(this).val() > 15) {
            $(this).val(15);
        }
    });
});

// if (machine == 'True'){
//     $("#machine").click(function(e) {
//         var allFilled = true;
//         // my-form 안의 input들을 모두 체크
//         $("#my-form input").each(function() {
//             var id = $(this).attr('id');
//             if(id === 'id_edu_input' && $('#edu_0').is(':checked') && $(this).val() == "") {
//                 allFilled = false;
//                 return false;
//             }
//             else if(id !== 'id_edu_input' && id !== 'sgds' &&  $(this).val() == "") {
//                 allFilled = false;
//                 return false;
//             }
//         });
    
//         if(allFilled) {
//             // 모든 항목이 채워져 있으면 form을 제출
//             $("#my-form").submit();
//         } else {
//             // 모든 항목이 채워져 있지 않으면 alert 표시
//             alert("환자정보를 모두 입력해주세요.");
//             e.preventDefault(); // form 제출 막기
//         }
//     });
// }

