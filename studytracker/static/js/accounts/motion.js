const marker = document.querySelectorAll(".marker");

document.addEventListener("scroll", ()=>{
    for (let i = 0; i < marker.length; i++) {
        const element = marker[i];
        const distance = element.getBoundingClientRect().top;
        if(distance < window.innerHeight * .8){
            element.classList.add("active");
        }
    }
})

$(function(){
    $(window).scroll(function (){
        $('.fadein').each(function(){
            var elemPos = $(this).offset().top;
            var scroll = $(window).scrollTop();
            var windowHeight = $(window).height();
            if (scroll > elemPos - windowHeight + 200){
                $(this).addClass('scrollin');
            }
        });
    });
});

$(function (){
    var webStorage = function() {
        if(sessionStoragee.getItem('access')) {
            
        }
    }
})