from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect, JsonResponse
from django.template import RequestContext
from django.views.generic import ListView, View, UpdateView, DeleteView
from menu.models import Menu, MenuFavorito, Relacion
from menu.forms import MenuForm, MenuFavoritoForm, RelacionForm
from mtvmcotizacionv02.views import valor_Personalizacionvisual, get_query
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
# app menu
class MenuListView(ListView):
    model = Menu
    paginate_by = 10
    context_object_name = 'menus'
    template_name = 'menu_lista.html'

    def get_paginate_by(self, queryset):
        if self.request.user.id is not None:
            nropag = valor_Personalizacionvisual(self.request.user.id, "paginacion")
        else:
            nropag = valor_Personalizacionvisual("std", "paginacion")

        page = self.request.GET.get('page')
        if page == '0':
            return None
        else:
            return self.request.GET.get('paginate_by', nropag)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(MenuListView, self).get_context_data(**kwargs)
        # Add in the pais
        if self.request.user.id is not None:
            range_gap = valor_Personalizacionvisual(self.request.user.id, "rangopaginacion")
        else:
            range_gap = valor_Personalizacionvisual("std", "rangopaginacion")

        order_by = self.request.GET.get('order_by')
        search = self.request.GET.get('search')
        if order_by and search is not None and search != u"":
            entry_query = get_query(search, ['menu',
                                             'transaccion',
                                             'namespace',
                                             'name',
                                             'nivel',
                                             'menu_padre__menu', ])
            lista_menu = Menu.objects.filter(entry_query).order_by(order_by)
        elif search is not None and search != u"":
            entry_query = get_query(search, ['menu',
                                             'transaccion',
                                             'namespace',
                                             'name',
                                             'nivel',
                                             'menu_padre__menu', ])
            lista_menu = Menu.objects.filter(entry_query)
        elif order_by:
            lista_menu = Menu.objects.all().order_by(order_by)
        else:
            lista_menu = Menu.objects.all()

        paginator = Paginator(lista_menu, 10)
        page = self.request.GET.get('page')
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

        context['ultimo'] = str(paginator.num_pages)
        context['page_range2'] = range(start, end)
        return context

    def get_queryset(self):

        order_by = self.request.GET.get('order_by')
        search = self.request.GET.get('search')
        if order_by and search is not None and search != u"":
            entry_query = get_query(search, ['menu',
                                             'transaccion',
                                             'namespace',
                                             'name',
                                             'nivel',
                                             'menu_padre__menu', ])
            queryset = Menu.objects.filter(entry_query).order_by(order_by)
        elif search is not None and search != u"":
            entry_query = get_query(search, ['menu',
                                             'transaccion',
                                             'namespace',
                                             'name',
                                             'nivel',
                                             'menu_padre__menu', ])
            queryset = Menu.objects.filter(entry_query)
        elif order_by:
            queryset = Menu.objects.all().order_by(order_by)
        else:
            queryset = Menu.objects.all()

        return queryset


class MenuView(View):
    form_class = MenuForm
    template_name = 'menu_add.html'

    def get(self, request, *args, **kwargs):
        """docstring"""
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            id_reg = form.save()

            if 'regEdit' in request.POST:
                messages.success(self.request, "Menu '" + str(id_reg) + "'  agregado con éxito.",
                                 extra_tags=reverse('umuebles:list_tipodemueble'))
                return HttpResponseRedirect(reverse('umuebles:edit_tipodemueble',
                                                    args=(id_reg.id,)))
            else:
                messages.success(self.request, "Menu '" + str(id_reg) + "'  agregado con éxito.")
                return HttpResponseRedirect(reverse('umenus:list_menu'))

        return render(request, self.template_name, {'form': form})


class MenuUpdate(UpdateView):
    template_name = 'menu_edit.html'
    form_class = MenuForm
    model = Menu

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(MenuUpdate, self).get_context_data(**kwargs)
        if self.request.user.id is not None:
            nropag = valor_Personalizacionvisual(self.request.user.id, "paginacion")
        else:
            nropag = valor_Personalizacionvisual("std", "paginacion")

        menu = Menu.objects.get(pk=self.object.pk)
        redirect_to = self.request.REQUEST.get('next', '')
        order_by = self.request.REQUEST.get('order_by', '')
        page = self.request.REQUEST.get('page', '')

        if order_by:
            redirect_to = redirect_to + '&order_by=' + order_by

        if page:
            redirect_to = redirect_to + '&page=' + page

        variable = self.request.REQUEST.get('next', '').split("?")
        if len(variable) > 1:

            if variable[1].split("=")[0] == 'page':
                page = self.request.REQUEST.get('next', '').split("?")[1].split("=")[1]
            elif variable[1].split("=")[0] == 'order_by':
                order_by = self.request.REQUEST.get('next', '').split("?")[1].split("=")[1]

        if order_by:
            lista_menu = Menu.objects.all().order_by(order_by)
        else:
            lista_menu = Menu.objects.all()

        paginator = Paginator(lista_menu, nropag)
        # Show 25 contacts per page

        if page == '0':
            menus = lista_menu
        else:
            try:
                menus = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                menus = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                menus = paginator.page(paginator.num_pages)

        if page != '0':
            countitem = int(nropag)
            for i in range(0, countitem):
                if(menus.object_list[i].id == menu.id):
                    if menus.has_previous:
                        try:
                            previousitem = menus.object_list[i-1].id
                        except:
                            previousitem = None

                    if menus.has_next:
                        try:
                            nextitem = menus.object_list[i+1].id
                        except:
                            nextitem = None
                    break
        else:
            countitem = len(menus)
            for i in range(0, countitem):
                if(menus[i].id == menu.id):
                    try:
                        previousitem = menus[i-1].id
                    except:
                        previousitem = None
                    try:
                        nextitem = menus[i+1].id
                    except:
                        nextitem = None
                    break

        try:
            menu_previous = Menu.objects.get(pk=previousitem)
        except:
            menu_previous = None
        try:
            menu_next = Menu.objects.get(pk=nextitem)
        except:
            menu_next = None

        context['menu_previous'] = menu_previous
        context['menu_next'] = menu_next

        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()

        if 'regEdit' in self.request.POST:

            messages.success(self.request, "Menu '" + str(self.object) + "'  guardado con éxito.")
            return HttpResponseRedirect(self.request.get_full_path())

        else:
            redirect_to = self.request.REQUEST.get('next', '')
            if redirect_to:
                messages.success(self.request, "Menu '" + str(self.object) + "'  guardado con éxito.")
                return HttpResponseRedirect(redirect_to)
            else:
                messages.success(self.request, "Menu '" + str(self.object) + "'  guardado con éxito.")
                return HttpResponseRedirect(reverse('umenus:list_menu'))
                #return render_to_response(self.template_name, self.get_context_data())


class MenuDelete(DeleteView):
    model = Menu
    form_class = MenuForm
    template_name = 'server_confirm_delete.html'

    def delete(self, request, *args, **kwargs):
        self.obj = self.get_object()
        context = self.obj.id

        order_by = self.request.REQUEST.get('order_by', '')
        page = self.request.REQUEST.get('page', '')
        next = self.request.REQUEST.get('next', '')
        variable = self.request.REQUEST.get('next', '').split("?")
        if len(variable) > 1:

            if variable[1].split("=")[0] == 'ficha':
                next = variable[0]
                if order_by and page:
                    next = next + '?order_by=' + order_by + '&page='+ page
                elif order_by:
                    next = next + '?order_by=' + order_by
                elif page:
                    next = next + '?page=' + page
            elif variable[1].split("=")[0] == 'page':
                if order_by:
                    next = next + '&order_by=' + order_by
            elif variable[1].split("=")[0] == 'order_by':
                if page:
                    next = next + '&page=' + page

        self.obj.delete()
        messages.success(self.request, "Menu " + str(self.obj) + " eliminado con éxito.", extra_tags=next)
        return render(request, '../../mensaje/templates/mensaje.html', {'obj': context})


# app menu favorito
class MenuFavoritoListView(ListView):
    model = MenuFavorito
    paginate_by = 10
    context_object_name = 'menufavoritos'
    template_name = 'menufavorito_lista.html'

    def get_paginate_by(self, queryset):
        if self.request.user.id is not None:
            nropag = valor_Personalizacionvisual(self.request.user.id, "paginacion")
        else:
            nropag = valor_Personalizacionvisual("std", "paginacion")

        page = self.request.GET.get('page')
        if page == '0':
            return None
        else:
            return self.request.GET.get('paginate_by', nropag)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(MenuFavoritoListView, self).get_context_data(**kwargs)
        # Add in the pais
        if self.request.user.id is not None:
            range_gap = valor_Personalizacionvisual(self.request.user.id, "rangopaginacion")
        else:
            range_gap = valor_Personalizacionvisual("std", "rangopaginacion")

        order_by = self.request.GET.get('order_by')
        search = self.request.GET.get('search')
        if order_by and search is not None and search != u"":
            entry_query = get_query(search, ['usuario__username',
                                             'menu__menu',
                                             'grupo', ])
            lista_menufavorito = MenuFavorito.objects.filter(entry_query).order_by(order_by)
        elif search is not None and search != u"":
            entry_query = get_query(search, ['usuario__username',
                                             'menu__menu',
                                             'grupo', ])
            lista_menufavorito = MenuFavorito.objects.filter(entry_query)
        elif order_by:
            lista_menufavorito = MenuFavorito.objects.all().order_by(order_by)
        else:
            lista_menufavorito = MenuFavorito.objects.all()

        paginator = Paginator(lista_menufavorito, 10)
        page = self.request.GET.get('page')
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

        context['ultimo'] = str(paginator.num_pages)
        context['page_range2'] = range(start, end)
        return context

    def get_queryset(self):

        order_by = self.request.GET.get('order_by')
        search = self.request.GET.get('search')
        if order_by and search is not None and search != u"":
            entry_query = get_query(search, ['usuario__username',
                                             'menu__menu',
                                             'grupo', ])
            queryset = MenuFavorito.objects.filter(entry_query).order_by(order_by)
        elif search is not None and search != u"":
            entry_query = get_query(search, ['usuario__username',
                                             'menu__menu',
                                             'grupo', ])
            queryset = MenuFavorito.objects.filter(entry_query)
        elif order_by:
            queryset = MenuFavorito.objects.all().order_by(order_by)
        else:
            queryset = MenuFavorito.objects.all()

        return queryset


class MenuFavoritoView(View):
    form_class = MenuFavoritoForm
    template_name = 'menufavorito_add.html'

    def get(self, request, *args, **kwargs):
        """docstring"""
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            id_reg = form.save()

            if 'regEdit' in request.POST:
                messages.success(self.request, "Menu favorito '" + str(id_reg) + "' agregado con éxito.",
                                 extra_tags=reverse('umenus:list_menufavorito'))
                return HttpResponseRedirect(reverse('umenus:edit_menufavorito',
                                                    args=(id_reg.id,)))
            else:
                messages.success(self.request, "Menu favorito '" + str(id_reg) + "' agregado con éxito.")
                return HttpResponseRedirect(reverse('umenus:list_menufavorito'))

        return render(request, self.template_name, {'form': form})


class MenuFavoritoUpdate(UpdateView):
    template_name = 'menufavorito_edit.html'
    form_class = MenuFavoritoForm
    model = MenuFavorito

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(MenuFavoritoUpdate, self).get_context_data(**kwargs)
        if self.request.user.id is not None:
            nropag = valor_Personalizacionvisual(self.request.user.id, "paginacion")
        else:
            nropag = valor_Personalizacionvisual("std", "paginacion")

        menufavorito = MenuFavorito.objects.get(pk=self.object.pk)
        redirect_to = self.request.REQUEST.get('next', '')
        order_by = self.request.REQUEST.get('order_by', '')
        page = self.request.REQUEST.get('page', '')

        if order_by:
            redirect_to = redirect_to + '&order_by=' + order_by

        if page:
            redirect_to = redirect_to + '&page=' + page

        variable = self.request.REQUEST.get('next', '').split("?")
        if len(variable) > 1:

            if variable[1].split("=")[0] == 'page':
                page = self.request.REQUEST.get('next', '').split("?")[1].split("=")[1]
            elif variable[1].split("=")[0] == 'order_by':
                order_by = self.request.REQUEST.get('next', '').split("?")[1].split("=")[1]

        if order_by:
            lista_menufavorito = MenuFavorito.objects.all().order_by(order_by)
        else:
            lista_menufavorito = MenuFavorito.objects.all()

        paginator = Paginator(lista_menufavorito, nropag)
        # Show 25 contacts per page

        if page == '0':
            menufavoritos = lista_menufavorito
        else:
            try:
                menufavoritos = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                menufavoritos = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                menufavoritos = paginator.page(paginator.num_pages)

        if page != '0':
            countitem = int(nropag)
            for i in range(0, countitem):
                if(menufavoritos.object_list[i].id == menufavorito.id):
                    if menufavoritos.has_previous:
                        try:
                            previousitem = menufavoritos.object_list[i-1].id
                        except:
                            previousitem = None

                    if menufavoritos.has_next:
                        try:
                            nextitem = menufavoritos.object_list[i+1].id
                        except:
                            nextitem = None
                    break
        else:
            countitem = len(menufavoritos)
            for i in range(0, countitem):
                if(menufavoritos[i].id == menufavorito.id):
                    try:
                        previousitem = menufavoritos[i-1].id
                    except:
                        previousitem = None
                    try:
                        nextitem = menufavoritos[i+1].id
                    except:
                        nextitem = None
                    break

        try:
            menufavorito_previous = MenuFavorito.objects.get(pk=previousitem)
        except:
            menufavorito_previous = None
        try:
            menufavorito_next = MenuFavorito.objects.get(pk=nextitem)
        except:
            menufavorito_next = None

        context['menufavorito_previous'] = menufavorito_previous
        context['menufavorito_next'] = menufavorito_next

        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()

        if 'regEdit' in self.request.POST:

            messages.success(self.request, "Menu favorito '" + str(self.object) + "'  guardado con éxito.")
            return HttpResponseRedirect(self.request.get_full_path())

        else:
            redirect_to = self.request.REQUEST.get('next', '')
            if redirect_to:
                messages.success(self.request, "Menu favorito '" + str(self.object) + "'  guardado con éxito.")
                return HttpResponseRedirect(redirect_to)
            else:
                messages.success(self.request, "Menu favorito '" + str(self.object) + "'  guardado con éxito.")
                return HttpResponseRedirect(reverse('umenus:list_menufavorito'))
                #return render_to_response(self.template_name, self.get_context_data())


class MenuFavoritoDelete(DeleteView):
    model = MenuFavorito
    form_class = MenuFavoritoForm
    template_name = 'server_confirm_delete.html'

    def delete(self, request, *args, **kwargs):
        self.obj = self.get_object()
        context = self.obj.id

        order_by = self.request.REQUEST.get('order_by', '')
        page = self.request.REQUEST.get('page', '')
        next = self.request.REQUEST.get('next', '')
        variable = self.request.REQUEST.get('next', '').split("?")
        if len(variable) > 1:

            if variable[1].split("=")[0] == 'ficha':
                next = variable[0]
                if order_by and page:
                    next = next + '?order_by=' + order_by + '&page='+ page
                elif order_by:
                    next = next + '?order_by=' + order_by
                elif page:
                    next = next + '?page=' + page
            elif variable[1].split("=")[0] == 'page':
                if order_by:
                    next = next + '&order_by=' + order_by
            elif variable[1].split("=")[0] == 'order_by':
                if page:
                    next = next + '&page=' + page

        self.obj.delete()
        messages.success(self.request, "Menu favorito " + str(self.obj) + " eliminado con éxito.", extra_tags=next)
        return render(request, '../../mensaje/templates/mensaje.html', {'obj': context})


# app relación
class RelacionListView(ListView):
    model = Relacion
    paginate_by = 10
    context_object_name = 'relaciones'
    template_name = 'relacion_lista.html'

    def get_paginate_by(self, queryset):
        if self.request.user.id is not None:
            nropag = valor_Personalizacionvisual(self.request.user.id, "paginacion")
        else:
            nropag = valor_Personalizacionvisual("std", "paginacion")

        page = self.request.GET.get('page')
        if page == '0':
            return None
        else:
            return self.request.GET.get('paginate_by', nropag)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(RelacionListView, self).get_context_data(**kwargs)
        # Add in the pais
        if self.request.user.id is not None:
            range_gap = valor_Personalizacionvisual(self.request.user.id, "rangopaginacion")
        else:
            range_gap = valor_Personalizacionvisual("std", "rangopaginacion")

        order_by = self.request.GET.get('order_by')
        search = self.request.GET.get('search')
        if order_by and search is not None and search != u"":
            entry_query = get_query(search, ['nombre',
                                             'item_origen__menu',
                                             'item_relacion__menu', ])
            lista_relacion = Relacion.objects.filter(entry_query).order_by(order_by)
        elif search is not None and search != u"":
            entry_query = get_query(search, ['nombre',
                                             'item_origen__menu',
                                             'item_relacion__menu', ])
            lista_relacion = Relacion.objects.filter(entry_query)
        elif order_by:
            lista_relacion = Relacion.objects.all().order_by(order_by)
        else:
            lista_relacion = Relacion.objects.all()

        paginator = Paginator(lista_relacion, 10)
        page = self.request.GET.get('page')
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

        context['ultimo'] = str(paginator.num_pages)
        context['page_range2'] = range(start, end)
        return context

    def get_queryset(self):

        order_by = self.request.GET.get('order_by')
        search = self.request.GET.get('search')
        if order_by and search is not None and search != u"":
            entry_query = get_query(search, ['nombre',
                                             'item_origen__menu',
                                             'item_relacion__menu', ])
            queryset = Relacion.objects.filter(entry_query).order_by(order_by)
        elif search is not None and search != u"":
            entry_query = get_query(search, ['nombre',
                                             'item_origen__menu',
                                             'item_relacion__menu', ])
            queryset = Relacion.objects.filter(entry_query)
        elif order_by:
            queryset = Relacion.objects.all().order_by(order_by)
        else:
            queryset = Relacion.objects.all()

        return queryset


class RelacionView(View):
    form_class = RelacionForm
    template_name = 'relacion_add.html'

    def get(self, request, *args, **kwargs):
        """docstring"""
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            id_reg = form.save()

            if 'regEdit' in request.POST:
                messages.success(self.request, "Menu relación '" + str(id_reg) + "' agregado con éxito.",
                                 extra_tags=reverse('umenus:list_relacion'))
                return HttpResponseRedirect(reverse('umenus:edit_relacion',
                                                    args=(id_reg.id,)))
            else:
                messages.success(self.request, "Menu relación '" + str(id_reg) + "' agregado con éxito.")
                return HttpResponseRedirect(reverse('umenus:list_relacion'))

        return render(request, self.template_name, {'form': form})


class RelacionUpdate(UpdateView):
    template_name = 'relacion_edit.html'
    form_class = RelacionForm
    model = Relacion

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(RelacionUpdate, self).get_context_data(**kwargs)
        if self.request.user.id is not None:
            nropag = valor_Personalizacionvisual(self.request.user.id, "paginacion")
        else:
            nropag = valor_Personalizacionvisual("std", "paginacion")

        relacion = Relacion.objects.get(pk=self.object.pk)
        redirect_to = self.request.REQUEST.get('next', '')
        order_by = self.request.REQUEST.get('order_by', '')
        page = self.request.REQUEST.get('page', '')

        if order_by:
            redirect_to = redirect_to + '&order_by=' + order_by

        if page:
            redirect_to = redirect_to + '&page=' + page

        variable = self.request.REQUEST.get('next', '').split("?")
        if len(variable) > 1:

            if variable[1].split("=")[0] == 'page':
                page = self.request.REQUEST.get('next', '').split("?")[1].split("=")[1]
            elif variable[1].split("=")[0] == 'order_by':
                order_by = self.request.REQUEST.get('next', '').split("?")[1].split("=")[1]

        if order_by:
            lista_relacion = Relacion.objects.all().order_by(order_by)
        else:
            lista_relacion = Relacion.objects.all()

        paginator = Paginator(lista_relacion, nropag)
        # Show 25 contacts per page

        if page == '0':
            relaciones = lista_relacion
        else:
            try:
                relaciones = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                relaciones = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                relaciones = paginator.page(paginator.num_pages)

        if page != '0':
            countitem = int(nropag)
            for i in range(0, countitem):
                if(relaciones.object_list[i].id == relacion.id):
                    if relaciones.has_previous:
                        try:
                            previousitem = relaciones.object_list[i-1].id
                        except:
                            previousitem = None

                    if relaciones.has_next:
                        try:
                            nextitem = relaciones.object_list[i+1].id
                        except:
                            nextitem = None
                    break
        else:
            countitem = len(relaciones)
            for i in range(0, countitem):
                if(relaciones[i].id == relacion.id):
                    try:
                        previousitem = relaciones[i-1].id
                    except:
                        previousitem = None
                    try:
                        nextitem = relaciones[i+1].id
                    except:
                        nextitem = None
                    break

        try:
            relacion_previous = Relacion.objects.get(pk=previousitem)
        except:
            relacion_previous = None
        try:
            relacion_next = Relacion.objects.get(pk=nextitem)
        except:
            relacion_next = None

        context['relacion_previous'] = relacion_previous
        context['relacion_next'] = relacion_next

        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()

        if 'regEdit' in self.request.POST:

            messages.success(self.request, "Menu relación '" + str(self.object) + "'  guardado con éxito.")
            return HttpResponseRedirect(self.request.get_full_path())

        else:
            redirect_to = self.request.REQUEST.get('next', '')
            if redirect_to:
                messages.success(self.request, "Menu relación '" + str(self.object) + "'  guardado con éxito.")
                return HttpResponseRedirect(redirect_to)
            else:
                messages.success(self.request, "Menu relación '" + str(self.object) + "'  guardado con éxito.")
                return HttpResponseRedirect(reverse('umenus:list_relacion'))
                #return render_to_response(self.template_name, self.get_context_data())


class RelacionDelete(DeleteView):
    model = Relacion
    form_class = RelacionForm
    template_name = 'server_confirm_delete.html'

    def delete(self, request, *args, **kwargs):
        self.obj = self.get_object()
        context = self.obj.id

        order_by = self.request.REQUEST.get('order_by', '')
        page = self.request.REQUEST.get('page', '')
        next = self.request.REQUEST.get('next', '')
        variable = self.request.REQUEST.get('next', '').split("?")
        if len(variable) > 1:

            if variable[1].split("=")[0] == 'ficha':
                next = variable[0]
                if order_by and page:
                    next = next + '?order_by=' + order_by + '&page='+ page
                elif order_by:
                    next = next + '?order_by=' + order_by
                elif page:
                    next = next + '?page=' + page
            elif variable[1].split("=")[0] == 'page':
                if order_by:
                    next = next + '&order_by=' + order_by
            elif variable[1].split("=")[0] == 'order_by':
                if page:
                    next = next + '&page=' + page

        self.obj.delete()
        messages.success(self.request, "Menu relación " + str(self.obj) + " eliminado con éxito.", extra_tags=next)
        return render(request, '../../mensaje/templates/mensaje.html', {'obj': context})


def lista_Relacion(request):
    """docstring"""
    menu = Menu.objects.filter(nivel=3)
    url1 = request.path
    relacion = ''
    for i in menu:

        url2 = reverse('%s:%s' % (i.namespace, i.name))
        if (url1 == (url2)):
            relacion = Relacion.objects.filter(item_origen_id=i.id)

            break

    context = {'relacion': relacion, 'url1': url1}
    return context


def lista_Menu(request):
    """docstring"""
    urlactual = request.path

    idActual = 0

    idActualFav = 0

    urln3 = ''

    nivel1 = Menu.objects.filter(nivel=1)

    nivel2 = Menu.objects.filter(nivel=2)

    nivel3 = Menu.objects.filter(nivel=3)

    favoritos = MenuFavorito.objects.all().order_by('orden')

    grupos = MenuFavorito.objects.values('grupo').distinct().order_by()

    for i in nivel3:
        urln3 = reverse('%s:%s' % (i.namespace, i.name))
        if (urlactual == urln3):
            idActual = i.id
            favoritos2 = MenuFavorito.objects.all().filter(menu_id=i.id)
            for j in favoritos2:
                    idActualFav = j.id

    context = {'nivel1': nivel1, 'nivel2': nivel2,
               'nivel3': nivel3, 'favoritos': favoritos,
               'urlactual': urlactual, 'idActual': idActual,
               'idActualFav': idActualFav, 'grupos': grupos}
    return context


def lista_Transaccion(request):
    """docstring"""
    transaccion2 = request.GET.get('variable')
    relacion = Menu.objects.filter(nivel=3)

    for i in relacion:

        if (i.transaccion == transaccion2):
            url = '%s:%s' % (i.namespace, i.name)
            return JsonResponse({'url': reverse(url)}, safe=False)

    return JsonResponse({'url': ''}, safe=False)


def mostrar_Menu(request):
    """Docstring"""
    return render(request, 'Menu_general.html')
