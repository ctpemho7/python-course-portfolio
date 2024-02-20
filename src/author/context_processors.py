from author.models import Author


def author(request):
    return {"author": Author.objects.last() }
