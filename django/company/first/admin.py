from django.contrib import admin
import first.models

# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    fields=['pub_date','content','headline','reporter']


class ReporterAdmin(admin.ModelAdmin):
    fields=['full_name']


admin.site.register(first.models.Article, ArticleAdmin)
admin.site.register(first.models.Reporter, ReporterAdmin)


