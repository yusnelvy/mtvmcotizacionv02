function actualizarVisible(name) {
   $.get('/widget/actualizarVisible/?name='+name,
     {},
     function(data) {
       //alert(data.sidebarStatus);
     });
}

function controlWidgetCerrar(e, name) {
  document.getElementById(e).style.display='none';
  actualizarVisible(name);
}

function controlWidgetMostrar(e){
  document.getElementById(e).style.display='block';
}

function viewWidgetVisible(e, name) {
   $.get('/widget/configurar_WidgetVisible/?name='+name,
     {},
     function(data) {
      var control = data[0].isVisible;
      if (control == false){
        document.getElementById(e).style.display='none';
      }
      else{
        document.getElementById(e).style.display='block';
      }
     });
}

function nivelpruebaBtn() {
    $(".wrapper").toggleClass("nivel2");
}

//funcion que llama el botn expandir de los widgets y cambia su
//tamaño al mas grande que permite el sidebar que corresponde a la clase tamaño2x3 de css
function actualizarColumna1(id1, id2, e, name) {
      $(".wrapper").addClass("nivel2");
      $('#'+id1).addClass('hidden');
      $('#'+id2).removeClass('hidden');
      $('#'+e).addClass('tamano2x3');
      actutamanoFicha();
      actutamanoFrame();
      $.get('/widget/actualizarColumna/?name='+name,
        {},
      function(data) {

      });
}

//funcion que controla el boton expandir en segundo nivel y cambia el
//tamaño del widget a el tamaño medio.
function actualizarColumna2(id1, id2, e, name) {
      $('#'+id2).addClass('hidden');
      $('#'+id1).removeClass('hidden');
      $('#'+e).removeClass('tamano2x3');
      $('#'+e).addClass('tamano1x2');
      actutamanoFicha();
      actutamnoFrame();
      $.get('/widget/actualizarColumnaMin/?name='+name,
        {},
      function(data) {

      });
}
//funcion que llama el botn expandir en 2do nivel de los widgets y cambia su
//tamaño al mas pequeño que se maneja que corresponde a la clase minima de css
function minimizarColumna(e, name) {
  $('#'+e).removeClass('tamano1x1');
  $('#'+e).removeClass('tamano1x2');
  $('#'+e).removeClass('tamano1x3');
  $('#'+e).removeClass('tamano2x1');
  $('#'+e).removeClass('tamano2x2');
  $('#'+e).removeClass('tamano2x3');
  $('#'+e).addClass('minima');
   $.get('/widget/actualizarColumna2/?name='+name,
     {},
     function(data) {

     });
}

/*function gestionarCotizacion(e) {
  var idEstado = 0;

  if (e == 'regSeguimiento'){
    idEstado = 19;
    $.get('/widget/actualizarFasesProceso/?idEstado='+idEstado,
        {},
      function(data) {

      });
  }
  else if (e == 'canCotizacion'){
    $('#'+e).addClass('hidden');
    $('#reaCotizacion').removeClass('hidden');

    $.get('/widget/cantidadDeSeguimientos/?idCotizacion='+idCotizacion,
        {},
      function(data) {
        cantidad = data[0].seguimientos;
        if (cantidad>0){
          idEstado = 22;
        }
        else{
          idEstado = 23;
        }

      });

    $.get('/widget/actualizarFasesProceso/?idEstado='+idEstado,
        {},
      function(data) {

      });
  }
  else if (e == 'reaCotizacion'){
    $('#'+e).addClass('hidden');
    $('#canCotizacion').removeClass('hidden');
    $.get('/widget/actualizarFasesProceso/?idEstado='+idEstado,
        {},
      function(data) {
        idEstado = data[0].idEstadoAlCancelar;

      });
    alert(idEstado);
    $.get('/widget/actualizarFasesProceso/?idEstado='+idEstado,
        {},
      function(data) {

      });

  }
  else if (e == 'confCotizacion'){
    $('#'+e).addClass('hidden');
    $('#terCotizacion').removeClass('hidden');

    idEstado = 20;
    $.get('/widget/actualizarFasesProceso/?idEstado='+idEstado,
        {},
      function(data) {

      });
  }
  else if (e == 'terCotizacion'){
    idEstado = 21;
    $.get('/widget/actualizarFasesProceso/?idEstado='+idEstado,
        {},
      function(data) {

      });
  }
  else{

  }
}
*/
