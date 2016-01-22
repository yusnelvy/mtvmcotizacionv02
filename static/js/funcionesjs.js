function ocultarASCDesc(id){
    if ('{{request.GET.order_by}}' == id){
        $('#'+id).css('display', 'none');
    }else{
        $('#-'+id).css('display', 'none');
    }
}
