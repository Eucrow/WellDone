from comentary.models import Comentary


class ComentaryQueryset(object):

    @staticmethod
    def get_comentaries(user):
        comentary_queryset = Comentary.objects.all().select_related('author').filter(author=user)
        return comentary_queryset
