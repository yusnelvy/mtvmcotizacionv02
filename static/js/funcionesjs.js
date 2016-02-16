$(function () {
  $('[data-toggletooltip="tooltip"]').tooltip();
});
//Abrir y cerrar sidebar
function sidebarBtn() {
    $(".wrapper").toggleClass("toggled");
}
function actualizarSidebar() {
    $.get('/sidebarUpdate/',
      {},
      function(data) {
        //alert(data.sidebarStatus);
      });
}
