import requests
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.utils.encoding import smart_text

from django.views import View

from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from requests import Response
from rest_framework.renderers import StaticHTMLRenderer

from users.forms import SignUpForm

from django.utils.translation import ugettext as _


# Create your views here.
from users.serializers import UserSerializer


class SignUpView(View):

    def get(self, request):
        """
        Method to show the form to create a new user
        :param request: HttpRequest object
        :return: HttpResponse object with the response
        """
        message = None

        user_form = SignUpForm()
        context = {'form': user_form, 'message': message}
        return render(request, 'users/signup.html', context)

    def post(self, request):
        """
        Method to save the new user by calling to the rest-auth registration endpoint
        :param request:
        :return:
        """
        user_form = SignUpForm(request.POST)

        if user_form.is_valid():
            r = requests.post('http://127.0.0.1:8000/api/rest-auth/registration/', data=user_form.data)
            json = r.json()

            request_get = 'http://127.0.0.1:9000/api/detail/detail/' + str(json.get('user').get('pk'))

            r = requests.get(request_get)
            r2 = smart_text(r.text)
            r3 = smart_text(r.content)

            return HttpResponse(r)
            # return HttpResponse(smart_text(r.text))
            # return redirect('api/detail/detail/' + str(json.get('user').get('pk')))

        # if user_form.is_valid():
        #
        #     user = User()
        #     user.username = user_form.cleaned_data.get('username')
        #     user.email = user_form.cleaned_data.get('email')
        #     user.set_password(user_form.cleaned_data.get('password1'))
        #
        #     user.save()
        #
        #     return redirect('signup_success')

        else:

            context = {'form': user_form}

            return render(request, 'users/signup.html', context)


class SignUpSuccessView(TemplateView):
    """
    Show template signup_success
    """
    template_name = 'users/signup_success.html'


class DeleteUserView(View):
    def get(self, request, pk):
        """
        Function to delete user
        :param request:
        :param pk: user id
        :return:
        """

        try:
            user = User.objects.get(pk=pk)
            user.delete()
            message = _("User deleted")
        except User.DoesNotExist:
            message = _("Error: user does not exists")
        except User.MultipleObjectsReturned:
            message = _("Error: there are multiple users!! :O")

        context = {'message': message}
        return render(request, 'users/delete_user.html', context)


class DeleteUserSuccessView(TemplateView):
    """
    Show template delete_user_success
    """
    template_name = 'users/delete_user.html'
