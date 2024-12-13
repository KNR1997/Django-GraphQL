from graphene_django import DjangoObjectType

from product.models import Category


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ('id', 'name', 'slug')