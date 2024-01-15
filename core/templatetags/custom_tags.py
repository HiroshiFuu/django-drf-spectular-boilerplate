from django import template
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from django.utils.html import conditional_escape
from django.utils.translation import gettext

register = template.Library()


@register.simple_tag(takes_context=True)
def current_site_name(context):
    request = context.get('request')

    try:
        site_name = get_current_site(request).name
    except AttributeError:
        # This happens if request is None and sites framework is not in INSTALLED_APPS
        site_name = gettext('my site')
    return conditional_escape(site_name)


@register.simple_tag(takes_context=True)
def current_site_domain(context):
    request = context.get('request')
    try:
        site_domain = get_current_site(request).domain
    except AttributeError:
        # This happens if request is None and sites framework is not in INSTALLED_APPS
        site_domain = request.get_host()
    return conditional_escape(site_domain)


@register.simple_tag
def settings_value(name):
    val = getattr(settings, name, None)
    if val is None:
        val = ""
    return val
