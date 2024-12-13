# from django.core.paginator import Paginator
# from fuzzywuzzy import process
#
# from ..models import Category
#
#
# class CategoryService:
#     @staticmethod
#     def get_categories(text=None, has_type=None, parent=None, page=1, page_size=10):
#         categories = Category.objects.all()
#
#         if text:
#             # Fuzzy search using fuzzywuzzy
#             category_names = [category.name for category in categories]
#             matched_names = process.extract(text, category_names, limit=10)
#             matched_ids = [cat.id for cat in categories if cat.name in [name for name, _ in matched_names]]
#             categories = categories.filter(id__in=matched_ids)
#
#         if has_type:
#             categories = categories.filter(type_slug=has_type)
#
#         if parent is not None:
#             categories = categories.filter(parent=parent)
#
#         paginator = Paginator(categories, page_size)
#         paginated_categories = paginator.get_page(page)
#
#         return {
#             "data": paginated_categories.object_list,
#             "paginator_info": {
#                 "total_items": paginator.count,
#                 "total_pages": paginator.num_pages,
#                 "current_page": paginated_categories.number,
#                 "page_size": page_size,
#             },
#         }
#
#     @staticmethod
#     def get_category(id=None, slug=None):
#         if id:
#             return Category.objects.filter(id=id).first()
#         if slug:
#             return Category.objects.filter(slug=slug).first()
#         return None
