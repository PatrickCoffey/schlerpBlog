import markdown

from django import template
from django.template.defaultfilters import stringfilter
#from django.utils.encoding import force_unicode
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter(is_safe=True)
@stringfilter
def custom_markdown(value):
    extensions = ["nl2br", "codehilite", "fenced_code", "sane_lists"]
    return mark_safe(markdown.markdown(value, #force_unicode(value),
                                       extensions,
                                       pygments_style="manni",
                                       safe_mode=True,
                                       enable_attributes=False))
