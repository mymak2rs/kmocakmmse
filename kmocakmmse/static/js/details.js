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

