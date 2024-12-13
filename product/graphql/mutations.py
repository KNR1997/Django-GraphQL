import graphene

from product.models import Category


class CreateCategory(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        slug = graphene.String()

    category = graphene.Field("product.graphql.types.CategoryType")

    def mutate(root, info, name, slug=None):
        category = Category.objects.create(name=name, slug=slug)
        return CreateCategory(category=category)


class UpdateCategory(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        name = graphene.String()
        slug = graphene.String()

    category = graphene.Field("product.graphql.types.CategoryType")

    def mutate(root, info, id, name=None, slug=None):
        try:
            category = Category.objects.get(pk=id)
            if name:
                category.name = name
            if slug:
                category.slug = slug
            category.save()
            return UpdateCategory(category=category)
        except Category.DoesNotExist:
            raise Exception("Category not found")


class DeleteCategory(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)

    success = graphene.Boolean()

    def mutate(root, info, id):
        try:
            category = Category.objects.get(pk=id)
            category.delete()
            return DeleteCategory(success=True)
        except Category.DoesNotExist:
            return DeleteCategory(success=False)

# class CreateCategory(graphene.Mutation):
#     class Arguments:
#         name = graphene.String(required=True)
#         slug = graphene.String(required=True)
#         parent_id = graphene.Int()
#         type_slug = graphene.String()
#
#     category = graphene.Field(CategoryType)
#
#     def mutate(self, info, name, slug, type_slug, parent_id=None):
#         parent = Category.objects.filter(id=parent_id).first() if parent_id else None
#         category = Category.objects.create(name=name, slug=slug, type_slug=type_slug, parent=parent)
#         return CreateCategory(category=category)
#
#
# class UpdateCategory(graphene.Mutation):
#     class Arguments:
#         id = graphene.Int(required=True)
#         name = graphene.String()
#         slug = graphene.String()
#         type_slug = graphene.String()
#         parent_id = graphene.Int()
#
#     category = graphene.Field(CategoryType)
#
#     def mutate(self, info, id, name=None, slug=None, type_slug=None, parent_id=None):
#         category = Category.objects.filter(id=id).first()
#         if not category:
#             raise Exception("Category not found")
#
#         if name:
#             category.name = name
#         if slug:
#             category.slug = slug
#         if type_slug:
#             category.type_slug = type_slug
#         if parent_id:
#             category.parent = Category.objects.filter(id=parent_id).first()
#
#         category.save()
#         return UpdateCategory(category=category)
#
#
# class DeleteCategory(graphene.Mutation):
#     class Arguments:
#         id = graphene.Int(required=True)
#
#     success = graphene.Boolean()
#
#     def mutate(self, info, id):
#         category = Category.objects.filter(id=id).first()
#         if not category:
#             raise Exception("Category not found")
#
#         category.delete()
#         return DeleteCategory(success=True)
