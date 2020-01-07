from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()



class UserSerializer(serializers.HyperlinkedModelSerializer):
    """ Serializer for a User
    """

    class Meta:
        model = User
        fields = ('pk',
                  'username',
                  'first_name',
                  'last_name',
                  'email',)
