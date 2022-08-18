from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from django.views import View

from .models import Product, Category
from .forms import ProductForm, ReviewForm


def product_display(request):
    """ A view to show all products with filtering """

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'search' in request.GET:
            query = request.GET['search']
            if not query:
                messages.error(request, "No search criteria was entered!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    user_sort = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_result': query,
        'categories': categories,
        'user_sort': user_sort,
    }

    return render(request, 'products/products.html', context)


def product_view(request, product_id):
    """ A view that provides all relevant information for the products """

    product = get_object_or_404(Product, pk=product_id)
    review_form = ReviewForm()

    if request.method == 'POST':
        review_form = ReviewForm(request.POST)
        if request.method == "POST":
            review_form = ReviewForm(request.POST)
            if review_form.is_valid():
                review = review_form.save(commit=False)
                review.name = request.user.username
                review.product = product
                review_form.save()
            
            messages.success(request, "An admin may approve your review shortly.")
            return render(
                request,
                "products/product_view.html",
                {
                    "product": product,
                    "left_review": True,
                    "review_form": review_form,
                },
            )
        else:
            messages.error(request,
                           "There was an issue with the form. Please try again.")
    else:
        review_form = ReviewForm()
    context = {
        'product': product,
        "review_form": review_form,
    }

    return render(request, 'products/product_view.html', context)

    def get(self, request, slug, *args, **kwargs):
        queryset = Product.objects.get()
        product = get_object_or_404(queryset, slug=slug)
        reviews = product.reviews.filter(approved_reviews=True).order_by(" \
            -date_created")

        return render(
            request,
            "products/product_view.html",
            {
                "product": product,
                "reviews": reviews,
                "left_review": False,
                "review_form": ReviewForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):

        queryset = Product.objects
        product = get_object_or_404(queryset, slug=slug)
        reviews = product.reviews.filter(approved_reviews=True).order_by(" \
            -date_created")

        review_form = ReviewForm(data=request.POST)
        if review_form.is_valid():
            review_form.instance.email = request.user.email_address
            review_form.instance.name = request.user.username
            review = review_form.save(commit=False)
            review.product = product
            review.save()
        else:
            review_form = ReviewForm()

        return render(
            request,
            "products/product_view.html",
            {
                "product": product,
                "reviews": reviews,
                "left_review": True,
                "review_form": review_form,
            },
        )


@login_required
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_view', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. \
            Please ensure the form is valid.')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_view', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. \
                Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))
