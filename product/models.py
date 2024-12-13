from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    # parent = models.ForeignKey(
    #     'self',
    #     null=True,
    #     blank=True,
    #     on_delete=models.CASCADE,
    #     related_name='children'
    # )
    # # Corresponds to "type.slug" in NestJS
    # type_slug = models.CharField(max_length=255)

    def __str__(self):
        return self.name
