from django.shortcuts import redirect


def custom_login_required(func):
    def wrapper(request):
        if not request.user.is_authenticated:
            return redirect('login')
        return func(request)
    return wrapper
