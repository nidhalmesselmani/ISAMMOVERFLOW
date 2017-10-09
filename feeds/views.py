from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from .models import Feed
# Create your views here.


class IndexView(LoginRequiredMixin, TemplateView):
    pass


class FeedsList(LoginRequiredMixin,ListView):
    model = Feed
    queryset = Feed.objects.all()
    context_object_name = 'all_feeds'
    template_name = "feeds/feeds.html"
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'

#@login_required
# def feeds(request):
    #all_feeds = Feed.get_feeds()
    #context = {'feeds':feeds}
    # return render(request, 'feeds/feeds.html', context)
