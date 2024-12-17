import graphene
from graphene_django import DjangoObjectType

from product.models import Category, Type


class TypeType(DjangoObjectType):
    class Meta:
        model = Type
        fields = ('id', 'name', 'slug', 'icon', 'settings', 'banners', 'promotional_sliders', 'settings', 'language',
                  'translated_languages')


class CategoryType(DjangoObjectType):
    type = graphene.Field(TypeType)

    class Meta:
        model = Category
        fields = ('id', 'name', 'slug', 'icon', 'image', 'details', 'language', 'translated_languages')
