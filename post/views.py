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
