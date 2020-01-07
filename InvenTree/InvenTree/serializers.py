"""
Serializers used in various InvenTree apps
"""


# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth import get_user_model

from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    """ Serializer for User - provides all fields """

    class Meta:
        model = User
        fields = 'all'


class UserSerializerBrief(serializers.ModelSerializer):
    """ Serializer for User - provides limited information """

    class Meta:
        model = User
        fields = [
            'pk',
            'username',
        ]


class InvenTreeModelSerializer(serializers.ModelSerializer):
    """
    Inherits the standard Django ModelSerializer class,
    but also ensures that the underlying model class data are checked on validation.
    """

    def validate(self, data):
        """ Perform serializer validation.
        In addition to running validators on the serializer fields,
        this class ensures that the underlying model is also validated.
        """
        
        # Run any native validation checks first (may throw an ValidationError)
        data = super(serializers.ModelSerializer, self).validate(data)

        # Now ensure the underlying model is correct
        instance = self.Meta.model(**data)
        instance.clean()

        return data
