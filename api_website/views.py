from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from random import randint
from .forms import AlcoholForm
from django.core.paginator import Paginator
from .models import Chrab
from django.db.models import Q
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required

# Create your views here.

count = Chrab.objects.count()


def home(request):
    return render(request, "api_website/index.html")


def cocktails(request):
    form = AlcoholForm()
    # alcohol = ""
    message = ""
    page_obj = None
    drinks = None
    page_number = request.GET.get("page")
    alcohol = request.GET.get("alcohol")
    print(f"page number:{page_number}")
    if request.method == 'POST':
        form = AlcoholForm(request.POST)
        if form.is_valid():
            alcohol = form.cleaned_data["alcohol"].title()
            drinks = Chrab.objects.filter(
                Q(first_ingredient=alcohol) | Q(second_ingredient=alcohol) | Q(third_ingredient=alcohol) | Q(
                    fourth_ingredient=alcohol))
            # drinks = Chrab.objects.raw('SELECT * FROM api_website_chrab WHERE first_ingredient OR second_ingredient  = %s', [alcohol])
            print(drinks)
            # print(type(drinks))
            # print(len(drinks))
            if len(drinks) != 0:
                p = Paginator(drinks, 1)
                page_obj = p.get_page(page_number)
            message = f"There isn't a cocktail with {alcohol}, Check your spelling or write a different one"
            return render(request, "api_website/cocktails.html",
                          {'form': form, "message": message, 'alcohol': alcohol, 'drinks': drinks,
                           "page_obj": page_obj})

    else:
        if alcohol:
            drinks = Chrab.objects.filter(
                Q(first_ingredient=alcohol) | Q(second_ingredient=alcohol) | Q(third_ingredient=alcohol) | Q(
                    fourth_ingredient=alcohol))
            p = Paginator(drinks, 1)
            print(p)
            page_obj = p.get_page(page_number)
            print(page_obj)
    return render(request, "api_website/cocktails.html",
                  {'form': form, "message": message, 'alcohol': alcohol, 'drinks': drinks, "page_obj": page_obj})


def random_drinks(request):
    random_object = Chrab.objects.all()[randint(0, count - 1)]
    print(random_object)
    context = {
        "drink": random_object
    }
    return render(request, "api_website/random_drinks.html", context)


class ChrabCreateView(LoginRequiredMixin, CreateView):
    login_url = "/login/"
    model = Chrab
    template_name = 'api_website/add_drinks.html'
    # fields = '__all__'
    fields = ["drink_name",
              "glass",
              "first_ingredient",
              "second_ingredient",
              "third_ingredient",
              "fourth_ingredient",
              "instructions", "drink_image",
              "first_ingredient_measurements",
              "second_ingredient_measurements",
              "third_ingredient_measurements",
              "fourth_ingredient_measurements",
              "date"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
