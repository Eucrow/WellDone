from django.contrib.auth.models import User
from profiles.models import Profile

from django.views import View

from django.shortcuts import redirect, render
from django.views.generic import TemplateView

from profiles.forms import SignUpForm

from django.utils.translation import ugettext as _


# Create your views here.
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
        Method to save the new user
        :param request:
        :return:
        """
        user_form = SignUpForm(request.POST, request.FILES)


        if user_form.is_valid():

            user = Profile()
            user.username = user_form.cleaned_data.get('username')
            user.first_name = user_form.cleaned_data.get('first_name')
            user.last_name = user_form.cleaned_data.get('last_name')
            user.email = user_form.cleaned_data.get('email')
            user.set_password(user_form.cleaned_data.get('password1'))
            user.profile.avatar = user_form.cleaned_data.get('avatar')

            user.save()

            return redirect('signup_success')

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
        except User.MultipleObjects:
            message = _("Error: there are multiple users!! :O")

        context = {'message': message}
        return render(request, 'users/delete_user.html', context)





class DeleteUserSuccessView(TemplateView):
    """
    Show template delete_user_success
    """
    template_name = 'users/delete_user.html'


