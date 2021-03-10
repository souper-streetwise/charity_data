from django import template

register = template.Library()

@register.inclusion_tag("record/bulk_entry.html", takes_context=True)
def bulk_entry(context):
    return context

@register.inclusion_tag("record/clicker_entry.html", takes_context=True)
def clicker_entry(context):
    return context
