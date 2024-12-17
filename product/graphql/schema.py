import graphene

from .mutations import CreateCategory, UpdateCategory, DeleteCategory
from .types import CategoryType, TypeType
from ..models import Category, Type


class Query(graphene.ObjectType):
    all_categories = graphene.List(CategoryType)
    category = graphene.Field(CategoryType, id=graphene.Int(required=True))
    all_types = graphene.List(TypeType)

    def resolve_all_categories(root, info):
        return Category.objects.all()

    def resolve_category(root, info, id):
        try:
            return Category.objects.get(pk=id)
        except Category.DoesNotExist:
            return None

    def resolve_all_types(root, info, **kwargs):
        return Type.objects.all()


class Mutation(graphene.ObjectType):
    create_category = CreateCategory.Field()
    update_category = UpdateCategory.Field()
    delete_category = DeleteCategory.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
