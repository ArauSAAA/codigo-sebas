from django.http import HttpResponse

# Create your views here.
def index(request):
    html = """"
        <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
    </head>
    <body>
        <h1>Welcome to the Django World</h1>
        <p>This is the first try we give to Django</p>
    </body>
    </html>
    """
    return HttpResponse(html)