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
