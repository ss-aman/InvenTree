import pdb
from rest_framework import generics, permissions
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.http import JsonResponse

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from django.contrib.auth.models import Permission, Group, _user_has_module_perms, _user_has_perm


from company import models 

from .serializers import UserSerializer, PasswordChangeSerializer

from .mail_verification import get_token_generator
from .utils import *

User = get_user_model()


class GetAuthToken(ObtainAuthToken):
    """ Return authentication token for an authenticated user. """

    def post(self, request, *args, **kwargs):
        return self.login(request)

    def delete(self, request):
        return self.logout(request)

    def login(self, request):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)

        return Response({
            'token': token.key,
            'pk': user.pk,
            'username': user.username,
            'email': user.email
        })

    def logout(self, request):
        try:
            request.user.auth_token.delete()
            return Response({"success": "Successfully logged out."},
                            status=status.HTTP_202_ACCEPTED)
        except (AttributeError, ObjectDoesNotExist):
            return Response({"error": "Bad request"},
                            status=status.HTTP_400_BAD_REQUEST)


# todo set frontend site domain, ser permission_CLASSES
class UserModelViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serailizer):
        user = serailizer.save(password='')
        uid, token = get_token_generator().generate_uid_token(user)
        current_site = get_current_site(self.request)
        message = render_to_string('verification_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': uid,
                'token': token,
            })
        user.email_user('account activation mail', message, 'inven@inventree.com')


class AccountActivationView(generics.CreateAPIView):
    serializer_class = PasswordChangeSerializer
    permission_classes = ()
     
    def perform_create(self, serializer):
        uid = self.kwargs.get('uid')
        token = self.kwargs.get('token')
        user = get_token_generator().validate_uid_token(uid, token)
        result = False

        _password = serializer.validated_data.get('password')
        if user:
            user.set_password(_password)
            user.save()
            result = True
        return result

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        result = self.perform_create(serializer)
        return Response({'result': result})


class CheckPermissions(generics.GenericAPIView):

    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        user = User.objects.get(email=email)

        perm = user.has_perm('company.add_company')

        return Response({'user': user.username, 'perm': perm,})


# class GroupAdd/
