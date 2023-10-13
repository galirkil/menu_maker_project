from django.shortcuts import render


def main_view(request):

    title = request.path
    template = 'some_main_app/base.html'
    context = {
        'title': title,
    }
    return render(request, template, context)
