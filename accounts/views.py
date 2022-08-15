from django.shortcuts import render


def account(request):
    """ Displays the user's account. """

    template = 'accounts/account.html'
    context = {}

    return render(request, template, context)