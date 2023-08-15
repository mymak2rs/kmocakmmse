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
