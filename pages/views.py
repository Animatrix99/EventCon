from django.views.generic import TemplateView

# Create your views here.

class HomePageView(TemplateView):
    template_name = 'index.html'


class PerformerPageView(TemplateView):
    template_name = 'performer.html'


class AboutPageView(TemplateView):
    template_name = 'about.html'


class ContactPageView(TemplateView):
    template_name = 'contact.html'


# class BlogPageView(TemplateView):
#     template_name = 'blog.html'