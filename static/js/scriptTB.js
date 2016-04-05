var liFrame = parent.document.getElementById("divFrame");
var wFrame = $(liFrame).css('width');
$('html').css('width', wFrame);
function controlSubmit(event) {
  warn_on_unload = "Si sale de la pagina, no se guardarán los datos, guarde los datos antes de abandonar la pagina.";
  $('.botonGuardar').removeClass('hidden');
  $('.botonCancelar').removeClass('hidden');
  event.preventDefault();
  var parenDoc = parent.document;
  $(parenDoc).click(function(event){
    $('.msj').removeClass('hidden').css('display', 'block').text(warn_on_unload).append('<a onclick="removeHandler();" style="cursor:pointer;"> Deshacer los cambios</a>');
    event.preventDefault();
  });
  $('a').click(function(e){
    $('.msj').removeClass('hidden').css('display', 'block').text(warn_on_unload).append('<a onclick="removeHandler();" style="cursor:pointer;"> Deshacer los cambios</a>');
    e.preventDefault();
  });
}
$(document).ready(function (){
  var  warn_on_unload = "Si sale de la pagina, no se guardarán los datos, guarde los datos antes de abandonar la pagina.";
  $('input:text,input:checkbox,input:radio,textarea,input[type=number]').on('change', function(event){
    controlSubmit(event);
  });
  $(':input').on('keyup', function(event){
    controlSubmit(event);
  });
  $('input[type="checkbox"]').on('switchChange.bootstrapSwitch', function(event, state) {
    controlSubmit(event);
  });
});
$('input,textarea,h3,md-select,.labelSwitch').hover(function(){
    $(this).parent().addClass('md-input-focused');
}, function(){
    $(this).parent().removeClass('md-input-focused');
});
