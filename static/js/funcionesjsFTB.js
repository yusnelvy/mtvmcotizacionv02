function removeHandler() {
 // $('a').removeEventListener("click", preventDef, false);
 var parenDoc = parent.document;
 var btnFicha = $(parent.document.getElementsByClassName('btnFicha'));
 var tag = $(parent.document.getElementsByTagName('a'));
 $(tag).unbind('click');
 $(btnFicha).unbind('click');
 $(parenDoc).unbind('click');
 $('a').unbind('click');
 $('.botonGuardar').addClass('hidden');
 $('.botonCancelar').addClass('hidden');
 $('.msj').addClass('hidden');
}
