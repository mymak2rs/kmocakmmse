window.onpageshow = function(event) {
    if (event.persisted || (window.performance && window.performance.navigation.type == 2)){
        if(details == 'True'){
            alert('잘못된 접근입니다.');
            window.location.replace("/main/details");
        }else{
            alert('잘못된 접근입니다.');
            history.forward();
        }
        
    }
}