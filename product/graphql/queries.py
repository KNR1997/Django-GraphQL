# import graphene
#
# from product.graphql.schema import CategoryType
#
#
# class Query(graphene.ObjectType):
#     categories = graphene.Field(
#         graphene.List(CategoryType),
#         text=graphene.String(),
#         has_type=graphene.String(),
#         parent=graphene.Int(),
#         page=graphene.Int(default_value=1),
#         page_size=graphene.Int(default_value=10)
#     )
#     category = graphene.Field(CategoryType, id=graphene.Int(), slug=graphene.String())
#
#     def resolve_categories(self, info, text=None, has_type=None, parent=None, page=1, page_size=10):
#         service = CategoryService()
#         result = service.get_categories(text, has_type, parent, page, page_size)
#         return result["data"]
#
#     def resolve_category(self, info, id=None, slug=None):
#         service = CategoryService()
#         return service.get_category(id, slug)
