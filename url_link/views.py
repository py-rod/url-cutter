from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import SaveUrlShortened
from django.contrib.sites.shortcuts import get_current_site
from django.contrib import messages
from .forms import CreateUrlShort
from .process_links import TitleIsNotNone, TitleIsNone
from analytics.models import UrlAnalytics
# Create your views here.


@login_required(login_url='signin')
def all_url_links(request):

    urls_obj = SaveUrlShortened.objects.filter(
        user=request.user.email, is_active=True)
    domain = get_current_site(request).domain

    return render(request, 'all_url_links.html', {
        'data_urls': urls_obj,
        'domain': domain
    })


@login_required(login_url='signin')
def create_url_link(request):
    if request.method == 'POST':
        form = CreateUrlShort(request.POST)
        if form.is_valid():
            # Viendo si el usuario introdujo un titulo a la url
            window_title = form.cleaned_data['title']
            if window_title:
                return TitleIsNotNone(request, form).save_when_title_is_not_none()
            else:
                return TitleIsNone(request, form).save_when_title_is_none()
        else:
            messages.error(
                request, 'This custom back-half is already exists. Try another one')
            return redirect('create_url')

    else:
        form = CreateUrlShort()
    return render(request, 'create_url.html', {
        'form': form
    })


def redirect_urls(request, short_url):
    try:

        # SAVE THE NUMBER OF CLICKS WHEN THE USER CLICKS ON THE LINK
        url_obje = SaveUrlShortened.objects.get(short_url=short_url)
        url_obje.clicks += 1
        url_obje.save()

        # URLS ANALYTICS CREATION
        create_analytics = UrlAnalytics()
        create_analytics.id_short_url = short_url
        create_analytics.creator = url_obje.user
        create_analytics.is_mobile = request.user_agent.is_mobile
        create_analytics.is_tablet = request.user_agent.is_tablet
        create_analytics.is_pc = request.user_agent.is_pc
        create_analytics.is_touch_capable = request.user_agent.is_touch_capable
        create_analytics.is_bot = request.user_agent.is_bot
        create_analytics.browser = request.user_agent.browser.family
        create_analytics.system = request.user_agent.os.family
        create_analytics.device = request.user_agent.device.family
        create_analytics.save()

        return redirect(url_obje.original_url)
    except SaveUrlShortened.DoesNotExist:
        return HttpResponse('The short url does not exist')


def delete_url(request, id):
    url_instance = get_object_or_404(SaveUrlShortened, id=id)
    print(url_instance)
    url_instance.delete()
    messages.success(request, 'The short url has been deleted')
    return redirect('all_url_links')
