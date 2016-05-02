(function($) {

  $('.nivel_1').parent().children('.nivel33').slideUp();
  $('.nivel_2').parent().children('.nivel3').slideUp();

$('.nivel_1').click(function(){
    $(this).parent().children('.nivel33').slideToggle();
    var clase1 = $(this).children().attr('class');

    if (clase1 == 'iconoCarpetaAbierta') {
        $(this).children('span').removeClass('iconoCarpetaAbierta');
        $(this).children('span').addClass('iconoCarpetaCerrada');
    } else{
        $(this).children('span').removeClass('iconoCarpetaCerrada');
        $(this).children('span').addClass('iconoCarpetaAbierta');
    }
});


$('.nivel_2').click(function(){

   $(this).parent().children('.nivel3').slideToggle();
    var clase2 = $(this).children().attr('class');

    if (clase2 == 'iconoCarpetaAbierta') {
        $(this).children('span').removeClass('iconoCarpetaAbierta');
        $(this).children('span').addClass('iconoCarpetaCerrada');
    } else{
        $(this).children('span').removeClass('iconoCarpetaCerrada');
        $(this).children('span').addClass('iconoCarpetaAbierta');
    }
});

})(window.jQuery);

$('.titulo-panel').hover(function() {
}, function(){
    $(this).removeClass('c_w_hover');
});
$('.c_w').hover(function() {
    $(this).parent().children('h3').addClass('c_w_hover');
}, function(){
    $(this).parent().children('h3').removeClass('c_w_hover');
});
