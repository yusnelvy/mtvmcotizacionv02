$(document).ready(function() {
$('.c_td,div,a').hover(function() {
    $(this).parent().children('td').addClass('c_td_hover');
}, function(){
    $(this).parent().children('td').removeClass('c_td_hover');
});
$(function(){

$('.agregar').click(function() {
  var url = $(this).data('url');
  urlSuccess(url);
  sidebarBtn(2);
  actutamanoFrame();
});
$('.btnFicha').dblclick(function(event){
document.body.onselectstart = function() { return false; };
$('#divFrame').parent().css('overflow-y', 'hidden');
var url = $(this).data('url');
var trId = $(this).attr('id');
//var dget = $(this).data('get');
var vis = $("#divFrame").contents().find("button[name=regEdit]");
//location.href = "?ficha="+trId+"";
    $('.btnFicha').removeClass('seleccion');
    $(this).addClass('seleccion');
    urlSuccess(url);
    $('#divFrame').css('visibility', 'visible');
    $('#divFrame').css('position', 'relative');
    sidebarBtn(2);

    actutamanoFrame();
});
});
$(function() {
    $( "#id_fecha_nacimiento" ).datepicker({
      changeMonth: true,
      changeYear: true
    });
  });
$('md-input-container').hover(function(){
  $(this).addClass('md-input-focused focusMD');
//alert('hi');
}, function(){
  $(this).removeClass('md-input-focused focusMD');
});
$(function() {
  $('input[type=radio]').focus(function() {
   $(this).parent().parent().parent().addClass('inputFocus');
   radioColor();
}).focusout(function() {
    $(this).parent().parent().parent().removeClass('inputFocus');
    radioColor();
  });
 $('input[type=text],input[type=number],input[type=radio],input[type=email],select,textarea').focus(function() {
   var pos = $(this).position();
   var scroll = $(document.getElementsByClassName("page-content-wrapper"));
   $(scroll).animate({ scrollTop: pos.top - 100 }, 250);
    console.log(pos.top);
 });

// $('input[type=checkbox]').focus(function() {
//   var pos = $(this).parent().parent().position();
//   var scroll = $(document.getElementsByClassName("page-content-wrapper"));
//   $(scroll).animate({ scrollTop: pos.top - 100 }, 500);
//   console.log(pos);
// });



$('#sidebarWidget').sortable({
   placeholder: "ui-state-highlight",
   update: function(){
      var nuevo = $(this).sortable("toArray").toString();
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
        var name2 = nombre.replace("-"," ");
        var name = name2.replace("-"," ");
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
$('input[type=radio]').on('click', function () {
         radioColor();
    });
radioColor();
});

$('input:text,input:checkbox,input:radio,textarea,input[type=number],select').on('change', function(event){
    cambiosporGuardar();
});
$(':input').on('keyup', function(event){
    cambiosporGuardar();
  });

$("input[type='checkbox']").on('switchChange.bootstrapSwitch', function(event, state) {
  cambiosporGuardar();
});


  $("select").select2();
  $("input[type='checkbox']").bootstrapSwitch();

});
$('[data-toggletooltip="tooltip"]').tooltip();
