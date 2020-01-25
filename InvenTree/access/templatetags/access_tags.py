from django import template

register = template.Library()

@register.filter
def user_permission(user, perem):
    return user.has_perm(perm)

@register.filter
def user_module_permission(user, module):
    return user.has_modules_perm(module)

