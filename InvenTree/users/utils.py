from django.core.exceptions import PermissionDenied


def check_permission(func, perm):
    def permitted_func(request, *args, **kwargs):
        if request.user.has_perm(perm):
            return func(request, *args, **kwargs)
        raise PermissionDenied
    return permitted_func
    
def check_module_permission(func, perm):
    def permitted_func(request, *args, **kwargs):
        if request.user.has_module_perms(perm):
            return func(request, *args, **kwargs)
        raise PermissionDenied


# todo template tags
