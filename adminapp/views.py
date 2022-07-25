from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.contrib.auth.decorators import user_passes_test
from django.urls import reverse, reverse_lazy
from django.views.generic import UpdateView, CreateView, DeleteView, ListView, DetailView
from django.utils.decorators import method_decorator
from adminapp.forms import ShopUserEditForm



from authapp.models import ShopUser
from mainapp.models import Products_categories, Products
from authapp.forms import ShopUserRegisterForm
from adminapp.forms import ShopUserAdminEditForm, CategoryAdminEditForm, ProductAdminEditForm


class AccessMixin:

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class UsersCreateView(AccessMixin, CreateView):
    model = ShopUser
    template_name = 'adminapp/user_update.html'
    success_url = reverse_lazy('adminapp:user_list')
    form_class = ShopUserRegisterForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'добавление пользователя'
        return context


# @user_passes_test(lambda u: u.is_superuser)
# def user_create(request):
#     title = 'добавление пользователя'
#
#     if request.method == 'POST':
#         user_form = ShopUserRegisterForm(request.POST, request.FILES)
#         if user_form.is_valid():
#             user_form.save()
#             return HttpResponseRedirect(reverse('adminapp:user_list'))
#
#     user_form = ShopUserRegisterForm()
#
#     content = {
#         'title': title,
#         'user_form': user_form
#     }
#
#     return render(request, 'adminapp/user_update.html', context=content)

class UsersListView(AccessMixin, ListView):
    model = ShopUser
    template_name = 'adminapp/user_list.html'

    def get_queryset(self):
        return ShopUser.objects.all().order_by('-is_active')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'пользователи'
        return context

# @user_passes_test(lambda u: u.is_superuser)
# def user_list(request):
#     title = 'пользователи'
#
#     objects = ShopUser.objects.all().order_by('-is_active')
#
#     content = {
#         'title': title,
#         'objects': objects
#     }
#
#     return render(request, 'adminapp/user_list.html', context=content)

class UserUpdateView(AccessMixin, UpdateView):
    model = ShopUser
    template_name = 'adminapp/user_update.html'
    success_url = reverse_lazy('adminapp:user_list')
    form_class = ShopUserAdminEditForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'изменение пользователя'
        return context


# @user_passes_test(lambda u: u.is_superuser)
# def user_update(request, pk):
#     title = 'изменение пользователя'
#
#     edit_user = get_object_or_404(ShopUser, pk=pk)
#     if request.method =='POST':
#         edit_form = ShopUserAdminEditForm(request.POST, request.FILES, instance=edit_user)
#         if edit_form.is_valid:
#             edit_form.save()
#             return HttpResponseRedirect(reverse('adminapp:user_list'))
#
#     edit_form = ShopUserAdminEditForm(instance=edit_user)
#     content = {
#         'title': title,
#         'user_form': edit_form
#     }
#     return render(request, 'adminapp/user_update.html', context=content)

class UserDeleteView(AccessMixin, DeleteView):
    model = ShopUser
    template_name = 'adminapp/user_delete.html'
    success_url = reverse_lazy('adminapp:user_list')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.is_active:
            self.object.is_active = False
        else:
            self.object.is_active = True
        self.object.save()

        return HttpResponseRedirect(self.get_success_url())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['delete_user'] = get_object_or_404(ShopUser, pk=self.kwargs.get('pk'))
        context['title'] = 'удаление пользователя'
        return context


# @user_passes_test(lambda u: u.is_superuser)
# def user_delete(request, pk):
#     title = 'удаление пользователя'
#
#     delete_user = get_object_or_404(ShopUser, pk=pk)
#     if request.method == 'POST':
#         if delete_user.is_active:
#             delete_user.is_active = False
#         else:
#             delete_user.is_active = True
#         delete_user.save()
#         return HttpResponseRedirect(reverse('adminapp:user_list'))
#
#     content = {
#         'title': title,
#         'delete_user': delete_user
#     }
#
#     return render(request, 'adminapp/user_delete.html', context=content)

class ProductCategoryCreateView(AccessMixin, CreateView):
    model = Products_categories
    template_name = 'adminapp/category_update.html'
    success_url = reverse_lazy('adminapp:category_list')
    form_class = CategoryAdminEditForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'добавление категории'
        return context

# @user_passes_test(lambda u: u.is_superuser)
# def category_create(request):
#
#     title = 'добавление категории'
#     if request.method == 'POST':
#         category_form = CategoryAdminEditForm(request.POST, request.FILES)
#         if category_form.is_valid:
#             category_form.save()
#
#         return HttpResponseRedirect(reverse('adminapp:category_list'))
#
#     category_form = CategoryAdminEditForm()
#
#     content = {
#         'title': title,
#         'category_form': category_form
#     }
#
#     return render(request, 'adminapp/category_update.html', context=content)

class ProductCategoryListView(AccessMixin, ListView):
    model = Products_categories
    template_name = 'adminapp/category_list.html'

    def get_queryset(self):
        return Products_categories.objects.all().order_by('-is_active')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'категории'
        return context
# @user_passes_test(lambda u: u.is_superuser)
# def category_list(request):
#     title = 'категории'
#
#     objects = Products_categories.objects.all()
#     content = {
#         'title': title,
#         'objects': objects
#
#     }
#
#     return render(request, 'adminapp/category_list.html', context=content)

class ProductCategoryUpdateView(AccessMixin, UpdateView):
    model = Products_categories
    template_name = 'adminapp/category_update.html'
    success_url = reverse_lazy('adminapp:category_list')
    form_class = CategoryAdminEditForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'изменение категории'
        return context
# @user_passes_test(lambda u: u.is_superuser)
# def category_update(request, pk):
#     title = 'изменение категории'
#
#     category_edit = get_object_or_404(Products_categories, pk=pk)
#     if request.method == 'POST':
#         category_form = CategoryAdminEditForm(request.POST, request.FILES, instance=category_edit)
#         if category_form.is_valid:
#             category_form.save()
#
#     category_form = CategoryAdminEditForm(instance=category_edit)
#
#     content = {
#         'title': title,
#         'category_form': category_form
#     }
#
#     return render(request, 'adminapp/category_update.html', context=content)

class ProductCategoryDeleteView(AccessMixin, DeleteView):
    model = Products_categories
    template_name = 'adminapp/category_delete.html'
    success_url = reverse_lazy('adminapp:category_list')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.is_active:
            self.object.is_active = False
        else:
            self.object.is_active = True
        self.object.save()

        return HttpResponseRedirect(self.get_success_url())


# @user_passes_test(lambda u: u.is_superuser)
# def category_delete(request, pk):
#
#     title = 'удаление категории'
#
#     delete_category = get_object_or_404(Products_categories, pk=pk)
#     if request.method == 'POST':
#         if delete_category.is_active:
#             delete_category.is_active = False
#         else:
#             delete_category.is_active = True
#         delete_category.save()
#         return HttpResponseRedirect(reverse('adminapp:category_list'))
#
#     content = {
#         'title': title,
#         'delete_category': delete_category
#     }
#
#     return render(request, 'adminapp/category_delete.html', context=content)


class ProductCreateView(AccessMixin, CreateView):
    model = Products
    template_name = 'adminapp/product_update.html'
    success_url = reverse_lazy('adminapp:product_list')
    form_class = ProductAdminEditForm

    def get_success_url(self):
        return reverse('adminapp:product_list', args=(self.kwargs.get('pk'),))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = "добавление продукта"
        context['category_product'] = get_object_or_404(Products_categories, pk=self.kwargs.get('pk'))
        return context

# @user_passes_test(lambda u: u.is_superuser)
# def product_create(request, pk):
#     title = 'добавление продукта'
#     category_product = get_object_or_404(Products_categories, pk=pk)
#
#     if request.method == 'POST':
#         product_form = ProductAdminEditForm(request.POST, request.FILES, instance=category_product)
#         if product_form.is_valid:
#             product_form.save()
#             HttpResponseRedirect(reverse('adminapp:product_list'))
#
#     product_form = ProductAdminEditForm(instance=category_product)
#     content = {
#         'title': title,
#         'product_form': product_form,
#         'category_product':category_product
#     }
#
#     return render(request, 'adminapp/product_update.html', context=content)

class ProductListView(AccessMixin, ListView):
    model = Products
    template_name = 'adminapp/product_list.html'

    def get_queryset(self):
        return Products.objects.filter(category__pk=self.kwargs.get('pk')).order_by('-is_active')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['category'] = get_object_or_404(Products_categories, pk=self.kwargs.get('pk'))
        context['title'] = 'товары категории'
        return context

# @user_passes_test(lambda u: u.is_superuser)
# def product_list(request, pk):
#     title = f'продукты категории {Products_categories.objects.get(pk=pk).name}'
#
#     category = get_object_or_404(Products_categories, pk=pk)
#     objects = Products.objects.filter(category__pk=pk)
#
#     content = {
#         'title': title,
#         'objects': objects,
#         'category': category
#     }
#
#     return render(request, 'adminapp/product_list.html', context=content)


class ProductDetailView(AccessMixin, DetailView):
    model = Products
    template_name = 'adminapp/product_read.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = 'изменение продукта'
        return context

# @user_passes_test(lambda u: u.is_superuser)
# def product_detail(request, pk):
#     # title = Products.objects.get(pk=pk).name
#     #
#     # objects = Products.objects.get(pk=pk)
#     #
#     # content = {
#     #     'title': title,
#     #     'objects': objects
#     # }
#     #
#     # return render(request, '', context=content)

class ProductUpdateView(AccessMixin, UpdateView):
    model = Products
    template_name = 'adminapp/product_update.html'
    form_class = ProductAdminEditForm

    def get_success_url(self):
        return reverse('adminapp:product_list', args = (self.kwargs.get('pk'),))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['category_product'] = get_object_or_404(Products_categories, pk=self.object.category.pk)
        context['title'] = 'title'
        return context

# @user_passes_test(lambda u: u.is_superuser)
# def product_update(request, pk):
#     # title = f'изменение {Products.objects.get(pk=pk).name}'
#     # content = {
#     #     'title': title
#     # }
#     #
#     # return render(request, '', context=content)

class ProductDeleteView(AccessMixin, DeleteView):
    model = Products
    template_name = 'adminapp/product_delete.html'

    def get_success_url(self):
        return reverse('adminapp:product_list', args=(self.object.category.pk,))

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.is_active:
            self.object.is_active = False
        else:
            self.object.is_active = True
        self.object.save()

        return HttpResponseRedirect(self.get_success_url())
# @user_passes_test(lambda u: u.is_superuser)
# def product_delete(request):
#     # title = f'удаление {Products.objects.get(pk=pk).name}'
#     # content = {
#     #     'title': title
#     # }
#     #
#     # return render(request, '', context=content)
#     pass
