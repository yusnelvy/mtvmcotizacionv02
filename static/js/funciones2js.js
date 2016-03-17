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

function controlWidgetExpandir(name) {
  if(name = 'Autofiltros'){

  }
  else if(name = 'Ficha'){

  }
  else if(name = 'Filtros Rápidos'){

  }
  else if(name = 'Menú'){

  }
  else if(name = 'Tablas Relacionadas'){

  }
  else{

  }
}
