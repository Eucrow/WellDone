from django.db.models import Q
from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.utils.datetime_safe import datetime
from django.views import View
from django.views.generic import ListView
from django.contrib.auth.models import User

from post.models import Post


class PostQueryset(object):
    @staticmethod
    def get_num_comentary_post(post):
        post_num_queryset = Post.objects.all()

        """persona_queryset = Persona.objects.all().select_related('Usuario')
        if not user.is_authenticated():
            persona_queryset = None
        else:
            persona_queryset = persona_queryset.filter(Usuario=user)"""
        return post_num_queryset

class HomeView(View):
    def get(self, request):
        """
        Renderiza el home con un listado de los ultimos post publicados por los usuarios
        :param request: objeto HttpRequest con los datos de la peticion
        :return:
        """
        posts = Post.objects.all().filter(publicate_at__lte=datetime.now()).order_by(
            '-publicate_at').select_related("author")
        context = {'posts_list': posts[:5]}
        return render(request, "post/home.html", context)

class UserPostsView(ListView):
    """
    Muestra la lista de posts del blog de un usuario
    :param request: objeto HttpRequest con los datos de la peticion
    :param blogger: nombre de usuario de la persona cuyo blog queremos ver
    :return:
    """
    model = Post
    template_name = 'post/user_posts.html'

    def get(self, request, *args, **kwargs):
        if not User.objects.filter(username=self.kwargs["blogger"]).exists():
            return HttpResponseNotFound("No existe ningún blog con este nombre")
        else:
            posts = self.get_queryset()
            context = {'posts_list': posts, 'blogger': self.kwargs["blogger"]}
            return render(request, 'post/user_posts.html', context)


    # Si el usuario que pide la lista es el propio usuario se le devuelven todos los posts. Si es otro cualquiera,
    # se devuelven unicamente los posts publicados.
    def get_queryset(self):
        if User.objects.filter(username=self.kwargs["blogger"]).exists():
            if self.request.user.is_authenticated() and self.request.user.username == self.kwargs["blogger"]:
                result = super().get_queryset().filter(author__username=self.kwargs["blogger"]).order_by(
                    '-publicate_at')
                return result
            else:
                result = super().get_queryset().filter(
                    Q(author__username=self.kwargs["blogger"]) & Q(publicate_at__lte=datetime.now())).order_by(
                    '-publicate_at')
                return result

