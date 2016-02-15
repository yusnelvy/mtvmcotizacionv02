$(function () {
  $('[data-toggletooltip="tooltip"]').tooltip();
});
//Abrir y cerrar sidebar
function sidebarBtn() {
    $(".wrapper").toggleClass("toggled");
    if(cont == 1){

        cont = 0;
        $('.menuSidebar').css('display', 'block');
    } else {
        cont = 1;

        $('.menuSidebar').css('display', 'none');
    }
}
