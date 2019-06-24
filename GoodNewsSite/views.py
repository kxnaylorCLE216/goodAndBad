from django.views.generic.base import TemplateView

class Home(TemplateView):

    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(baseclass, self).get_context_data(**kwargs)
        context['latest_articles'] = Article.objects.all()[:5]
        return context
