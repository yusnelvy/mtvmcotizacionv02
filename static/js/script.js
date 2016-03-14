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
app.controller('buscar',function($scope){
  $('#search').focus();
  $('#search').parent().addClass('md-input-focused');
  });
$('#sidebarWidget').sortable();
$('#sidebarWidget').disableSelection();
$('.iconoExpandirFull').click(function(){
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

