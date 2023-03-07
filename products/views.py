from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import Products
from .forms import ProductForm, RawProductForm

# Create your views here.


#to list out all the models
def product_list_view(request):
    queryset = Products.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, 'product/product_list.html', context)
def dynamic_lookup_view(request, my_id):
     # obj = Products.objects.get(id=my_id)
    # obj = get_object_or_404(Products, id=my_id)
    try:
        obj = Products.objects.get(id=my_id)
    except Products.DoesNotExist:
        raise Http404
        
    context = {
        'object': obj
    }
    return render(request, 'product/product_create.html', context)
# # def product_create_view(request):
# #     my_form = RawProductForm()
# #     if request.method == 'POST':
# #         my_form = RawProductForm(request.POST)
# #         if my_form. is_valid():
# #             #now the data is good
# #             print(my_form.cleaned_data)
# #             Products.objects.create(**my_form.cleaned_data)
# #         else:
# #             print(my_form.errors)
# #     context = {
# #         "form": my_form
# #     }
# #     return render(request, 'product/product_create.html', context)
# # def product_detail_view(request):
# #     obj = Products.objects.get(id=1)
# #     # context = {
# #     #     'title': obj.title,
# #     #     'description': obj.description,
# #     # }
# #     context = {
# #         'object': obj
# #     }
# #     return render(request, "product/detail.html", context)




# def product_create_view(request):
#     form = ProductForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         form = ProductForm()
#     context = {
#         'form': form
#     }
#     return render(request, "product/product_create.html", context)

# def render_initial_data(request):
#     intial_data = {
#         'title': 'my awesomwe title'
#     }
#     form = RawProductForm(request.POST or None, initial=intial_data)
#     context = {
#         'form': form
#     }
#     return render(request, "product/product_create.html", context)