import graphene

from .mutations import CreateCategory, UpdateCategory, DeleteCategory
from .types import CategoryType
from ..models import Category


class Query(graphene.ObjectType):
    all_categories = graphene.List(CategoryType)
    category = graphene.Field(CategoryType, id=graphene.Int(required=True))

    def resolve_all_categories(root, info):
        return Category.objects.all()

    def resolve_category(root, info, id):
        try:
            return Category.objects.get(pk=id)
        except Category.DoesNotExist:
            return None


class Mutation(graphene.ObjectType):
    create_category = CreateCategory.Field()
    update_category = UpdateCategory.Field()
    delete_category = DeleteCategory.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
