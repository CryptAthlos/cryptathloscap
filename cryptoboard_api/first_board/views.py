from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from first_board.models import Main


# Create your views here.
def index(request):
    context_dict = {'text': 'hello world', 'number': 100}
    return render(request, 'first_board/index.html', context_dict)


def help_page(request):
    help_dict = {'help': 'This is the help page'}
    return render(request, 'first_board/help.html', context=help_dict)


@login_required()
def cryptos(request):
    crypto_list = Main.objects.all().order_by('rank')
    crypto_dict = {'cryptos': crypto_list}
    return render(request, 'first_board/cryptos.html', context=crypto_dict)
