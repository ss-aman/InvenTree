import pdb
from rest_framework import generics, permissions
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status

# from company.models import Employee

from .serializers import UserSerializer

from .forms import UserCreationForm, UserUpdateForm

User = get_user_model()


class UserDetail(generics.RetrieveAPIView):
    """ Detail endpoint for a single user """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)


class UserList(generics.ListAPIView):
    """ List endpoint for detail on all users """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)


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


class UserListView(ListView):
    template_name = 'user_list.html'
    model = User
    paginated_by = 10
    context_object_name = 'user_list'


class CreateUserView(CreateView):
    model = User
    template_name = 'user_form.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('user-list')


    # def form_valid(self, form):
    #     user = form.save()
    #     user.is_active = False
    #     user.save()
    #     return HttpResponseRedirect(self.get_success_url())


class UpdateUserView(UpdateView):
    model = User
    template_name = 'user_form.html'
    form_class = UserUpdateForm
    success_url = reverse_lazy('user-list')
    # pk_url_kwarg = 'pk'
