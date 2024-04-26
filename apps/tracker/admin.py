from django.contrib import admin

from apps.tracker.models import Client, Contact, Project, TimeEntry


class ContactInline(admin.TabularInline):
    model = Contact
    extra = 1


class ClientAdmin(admin.ModelAdmin):
    inlines = [ContactInline]
    list_display = ["company_name", "country", "phone_number", "email", "billing_email", "created_at"]
    search_fields = ["company_name", "email", "billing_email"]
    list_filter = ["country", "created_at"]
    ordering = ["company_name"]


class ProjectAdmin(admin.ModelAdmin):
    list_display = ["name", "client", "completed", "created_at"]
    search_fields = ["name"]
    list_filter = ["client__company_name", "created_at", "completed"]
    ordering = ["client", "name", "created_at"]
    autocomplete_fields = ["client"]


class TimeEntryAdmin(admin.ModelAdmin):
    list_display = ["project", "start_time", "end_time", "duration", "created_at"]
    search_fields = ["project__name"]
    list_filter = ["project__name", "created_at"]
    ordering = ["project", "start_time", "end_time"]
    autocomplete_fields = ["project"]


class ContactAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "client", "email", "phone_number", "is_primary"]
    search_fields = ["first_name", "last_name", "email", "phone_number"]
    list_filter = ["is_primary", "client__company_name"]
    ordering = ["last_name", "first_name", "email", "phone_number"]
    autocomplete_fields = ["client"]


admin.site.register(Client, ClientAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(TimeEntry, TimeEntryAdmin)
admin.site.register(Contact, ContactAdmin)