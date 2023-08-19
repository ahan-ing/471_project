from django import template
import re

register = template.Library()

@register.filter(name="words")
def truncate_words(value, num_words=20):
    words = value.split()
    truncated_words = ' '.join(words[:num_words])
    return truncated_words
