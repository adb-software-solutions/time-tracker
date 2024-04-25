from django.contrib import admin

from apps.tracker.models import Client, Contact, Project, TimeEntry

admin.site.register(Client)
admin.site.register(Contact)
admin.site.register(Project)
admin.site.register(TimeEntry)