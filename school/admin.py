from django.contrib import admin
from django.contrib.admin import AdminSite
from .models import Teacher, Student, Principal

class TenantAdminSite(AdminSite):
    site_header = "School Admin"
    site_title = "School Admin Portal"
    index_title = "Welcome to School Admin Portal"

tenant_admin = TenantAdminSite(name='tenant_admin')

@admin.register(Teacher, site=tenant_admin)
class TenantSpecificModelAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'email')


@admin.register(Student, site=tenant_admin)
class TenantSpecificModelAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'email')


@admin.register(Principal, site=tenant_admin)
class TenantSpecificModelAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'email')
