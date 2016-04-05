var app = angular.module('AppMudarte',['ngMaterial', 'ngMessages']);

app.config(function($interpolateProvider) {
  $interpolateProvider.startSymbol('{$');
  $interpolateProvider.endSymbol('$}');
});

/*sidebar open and close | modificacion= 02-02-2016*/

/*$(".menu-toggle").click(function(e) {
e.preventDefault();

});*/
var cont = 0;
app.controller('ControlNavbar', function ($scope) {
  $scope.toggleSide = function (nivel) {
    sidebarBtn();
    $('.menuSidebar').addClass('hidden');
    actualizarSidebar(nivel);
  };
});
app.controller('ControlSidebar', function ($scope) {
  $scope.toggleSide = function (nivel) {
    sidebarBtn();
    $('.menuSidebar').removeClass('hidden');
    $('.wrapper').removeClass('nivel2');
    actualizarSidebar(nivel);
  };
  $scope.nivel2 = function (nivel) {
    nivel2Btn();
    $('.expandirNivel1').removeClass('hidden');
    $('.expandirNivel2').addClass('hidden');
    actualizarSidebar(nivel);
  };
  $scope.nivel1 = function (nivel) {
    nivel2Btn();
    $('.expandirNivel2').removeClass('hidden');
    $('.expandirNivel1').addClass('hidden');
    actualizarSidebar(nivel);
  };
});
$('#sidebarWidget').sortable({
   placeholder: "ui-state-highlight",
   update: function(){
      var nuevo = $(this).sortable("toArray").toString();
      var aaaaa = $( "#sidebarWidget" ).sortable( "toArray" );

      var tamano = nuevo.length;
      for (i=0; i<=tamano; i++)
      {
        var nuevoOrdenDos = nuevo.replace(",,,",",");
        nuevoOrden = nuevoOrdenDos;
      }

      for (j=0; j<=tamano; j++)
      {
        var nuevoOrden = nuevoOrdenDos.replace(",,",",");
        nuevoOrdenDos = nuevoOrden;
      }

      var arreglo = nuevoOrden.split(",");

      $.get('/widget/actualizarOrden/?nuevoOrden='+nuevoOrden,
        {},
      function(data) {
        var contador = 1;
        for (k=0; k<=tamano; k++)
      {
      console.log(data[2]);
        var nombre = data[k];
        var name = nombre.replace("-"," ");
        var order = contador++;
        //alert(nombre);
       $.get('/widget/actualizarOrden2/?name='+name+'&order='+order,
        {},
        function(data) {

          });
      }

      });
   }
});




$('#sidebarWidget').disableSelection();
$('.iconoExpandirFull2').click(function(){
  var w = $(this).parent();
  var ul = w.parent().css('width');
  if (w.css('width') == '225px' ) {
    w.css('width', '450px');
    w.css('height', '350px');
    tamañoFrame();
    $("#divFrame").contents().find("html").css('width', '450px');
    if (ul == '475px') {

    }else{
      $('.expandirNivel1').removeClass('hidden');
      $('.expandirNivel2').addClass('hidden');
      nivel2Btn();
      actualizarSidebar(2);
      tamañoFrame();
    }
  }else{
    w.css('width', '225px');
    w.css('height', '350px');
    tamañoFrame();
    $("#divFrame").contents().find("html").css('width', '225px');
  }
});
$('.mega').click(function(){
  var w = $(this).parent();
  var ul = w.parent().css('width');
  if (w.css('width') == '225px') {
    w.css('width', '450px');
    w.css('height', '600px');
    $("#divFrame").contents().find("html").css('width', '450px');
    if (ul == '475px') {

    }else{
      nivel2Btn();
      $('.expandirNivel1').removeClass('hidden');
      $('.expandirNivel2').addClass('hidden');
      actualizarSidebar(2);
    }
  }
  if (w.css('width') == '450px') {
    w.css('width', '450px');
    w.css('height', '600px');
    $("#divFrame").contents().find("html").css('width', '450px');
    if (ul == '475px') {

    }else{
//nivel2Btn();
$('.expandirNivel1').removeClass('hidden');
$('.expandirNivel2').addClass('hidden');
}
}
tamañoFrame();
});
tamañoFrame();
$('.c_td').hover(function() {
    $(this).parent().children('td').addClass('c_td_hover');
}, function(){
    $(this).parent().children('td').removeClass('c_td_hover');
});
$(function(){
    function searchSuccess(url){
        $('#divFrame').attr('src', url);
}
$('.btnFicha').dblclick(function(event){
var  warn_on_unload = "Si sale de la pagina, no se guardarán los datos, guarde los datos antes de abandonar la pagina.";
$('#divFrame').parent().css('overflow-y', 'hidden');
var url = $(this).data('url');
var trId = $(this).attr('id');
var vis = $("#divFrame").contents().find("button[name=regEdit]");
if( $(vis).is(":visible") ){
    $('.msj').text(warn_on_unload).append('<a onclick="removeHandler();" style="cursor:pointer;"> Deshacer los cambios</a>');
    if(warn_on_unload = ""){

    }else{
        event.preventDefault();
    }
}else{
    $('.btnFicha').removeClass('seleccion');
    $(this).addClass('seleccion');
    searchSuccess(url);
    $('#divFrame').css('visibility', 'visible');
    $('#divFrame').css('position', 'relative');
    $('.mega').click();
    $('.wrapper').addClass('toggled nivel2');
    $('.menuSidebar').addClass('hidden');
}
});
});
$('md-input-container').hover(function(){
  $(this).addClass('md-input-focused focusMD');
//alert('hi');
}, function(){
  $(this).removeClass('md-input-focused focusMD');
});

