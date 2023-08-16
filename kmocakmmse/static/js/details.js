var radios = document.querySelector("#moca");
var radios11 = radios.querySelectorAll('input[type=radio]');
Array.from(radios11).forEach(function(r){
    r.addEventListener('click', function(){
        findTotal1();

    });
});

function findTotal1(){
    let tot1 = 0;
    let radioList = document.querySelector("#moca > table").querySelectorAll("input[type=radio]:checked");

    radioList.forEach(function(item, index, arr){
        tot1 += parseInt(item.value)
    })

    var score17 = document.getElementById('KMoCA17').value;
    if(score17>=6) tot1+=1;
    document.getElementById('id_mc_score').value = tot1;
}

$(document).ready(function() {
    $('#KMoCA9').attr('min', 0);
    $('#KMoCA9').attr('max', 5);
    $('#KMoCA10').attr('min', 0);
    $('#KMoCA10').attr('max', 5);
    $('#KMoCA17').attr('min', 0);
    $('#KMoCA25').attr('min', 0);
    $('#KMoCA25').attr('max', 5);
    $('#KMoCA26').attr('min', 0);
    $('#KMoCA26').attr('max', 5);
    $('#id_mc_score').attr('min', 0);
    $('#id_mc_score').attr('max', 30);
});

$(document).ready(function() {
    $('#KMoCA9, #KMoCA10, #KMoCA25, #KMoCA26').on('change', function() {
        // 0 미만의 값을 입력 받으면 0으로 설정
        if ($(this).val() < 0) {
            $(this).val(0);
        }
    });
    
    $('#KMoCA9, #KMoCA10, #KMoCA25, #KMoCA26').on('change', function() {
        // 5 이상의 값을 입력 받으면 5로 설정
        if ($(this).val() > 5) {
            $(this).val(5);
        }
    });
});