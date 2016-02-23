$(function () {
  $('[data-toggletooltip="tooltip"]').tooltip();
});

function transaccion()
    {
        var variable = document.getElementById("transaccion").value;

    $.get('/transaccion',
      {variable: variable},
      function(data) {
        if (data.url != ""){
            location.href = data.url;
        }

      });
    }

function controlarEnter(e) {
    tecla = (document.all) ? e.keyCode : e.which;
    if (tecla == 13){
            var variable = document.getElementById("transaccion").value;

    $.get('/transaccion',
      {variable: variable},
      function(data) {
        if (data.url != ""){
            location.href = data.url;
        }

      });
    }
}
