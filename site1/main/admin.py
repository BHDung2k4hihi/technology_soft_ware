from django.contrib import admin
from .models import Name

# Customize admin site header
admin.site.site_header = 'Trang Quản Trị Site1'
admin.site.site_title = 'Site1 Admin'
admin.site.index_title = 'Quản lý dữ liệu'


@admin.register(Name)
class NameAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)
    ordering = ('-created_at',)
    readonly_fields = ('created_at',)

