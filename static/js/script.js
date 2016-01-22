var cont = 0;
$(".menu-toggle").click(function(e) {
    e.preventDefault();
    $("#wrapper").toggleClass("toggled");
    if(cont == 1){

        cont = 0;
        $('#menuSidebar').css('display', 'block');
    } else {
        cont = 1;

        $('#menuSidebar').css('display', 'none');
    }
});
