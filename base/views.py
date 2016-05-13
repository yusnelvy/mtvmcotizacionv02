from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def paginate_acordeon(nropag, page, ch_var, lista_var1, lista_var2, range_gap):
    if ch_var:
        paginator = Paginator(lista_var1, nropag)
        variables2 = lista_var2
        if page == '0':
            variables1 = lista_var1
        else:
            try:
                variables1 = paginator.page(page)
            except PageNotAnInteger:
                variables1 = paginator.page(1)
            except EmptyPage:
                variables1 = paginator.page(paginator.num_pages)
    else:
        paginator = Paginator(lista_var2, nropag)
        variables1 = lista_var1
        if page == '0':
            variables2 = lista_var2
        else:

            try:
                variables2 = paginator.page(page)
            except PageNotAnInteger:
                variables2 = paginator.page(1)
            except EmptyPage:
                variables2 = paginator.page(paginator.num_pages)

    if page:

        if int(page) > int(range_gap):
            start = int(page)-int(range_gap)
        else:
            start = 1

        if int(page) < paginator.num_pages-int(range_gap):
            end = int(page)+int(range_gap)+1
        else:
            end = paginator.num_pages+1
    else:
        if 1 > int(range_gap):
            start = 1-int(range_gap)
        else:
            start = 1

        if 1 < paginator.num_pages-int(range_gap):
            end = 1+int(range_gap)+1
        else:
            end = paginator.num_pages+1

    data = {
        'ultimo': str(paginator.num_pages),
        'page_range2': range(start, end),
        'variables1': variables1,
        'variables2': variables2
        }

    return data
