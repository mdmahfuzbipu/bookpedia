from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter
def star_rating(value):
    try:
        value = float(value)
        full_stars = int(value)
        half_star = value - full_stars >= 0.5
        empty_stars = 5 - full_stars - int(half_star)

        html = ""

        for _ in range(full_stars):
            html += '<i class="bi bi-star-fill star-yellow text-warning"></i> '

        if half_star:
            html += '<i class="bi bi-star-half star-yellow text-warning"></i> '

        for _ in range(empty_stars):
            html += '<i class="bi bi-star star-yellow text-warning"></i> '

        return mark_safe(html)
    except:
        return ""
