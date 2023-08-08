document.querySelector("#edu_0").checked = true;

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

if (machine == true){
    $("#machin").click(function(e) {
        var allFilled = true;
        // my-form 안의 input들을 모두 체크
        $("#my-form input").each(function() {
            var id = $(this).attr('id');
            if(id === 'id_edu_input' && $('#edu_0').is(':checked') && $(this).val() == "") {
                allFilled = false;
                return false;
            }
            else if(id !== 'id_edu_input' && id !== 'hand_0' && id !== 'hand_1' && id !== 'hand_2' && id !== 'depress_0' && id !== 'depress_1' && id !== 'depress_2' && id !== 'kmoca_total' && id !== 'sgds' && id !== 'neu_prob_0' && id !== 'neu_prob_1' && id !== 'neu_prob_2' && $(this).val() == "") {
                allFilled = false;
                return false;
            }
        });
    
        if(allFilled) {
            // 모든 항목이 채워져 있으면 form을 제출
            $("#my-form").submit();
        } else {
            // 모든 항목이 채워져 있지 않으면 alert 표시
            alert("기계학습을 위한 항목을 채워주세요!");
            e.preventDefault(); // form 제출 막기
        }
    });
}

