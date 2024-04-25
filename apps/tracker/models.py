import uuid
from django.db import models
from django_countries.fields import CountryField


class Contact(models.Model):
    """A model to represent a contact person for a client.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    client = models.ForeignKey("Client", on_delete=models.CASCADE, related_name="contacts")

    class Meta:
        ordering = ["last_name", "first_name"]
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"


class Client(models.Model):
    """
    A model to represent a client company.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    company_name = models.CharField(max_length=255)
    address_line_1 = models.CharField(max_length=255, blank=True, null=True)
    address_line_2 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    postal_code = models.CharField(max_length=255, blank=True, null=True)
    country = CountryField(blank=True, null=True)
    phone_number = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True)
    billing_email = models.EmailField(max_length=255, blank=True, null=True)
    primary_contact = models.ForeignKey(Contact, on_delete=models.SET_NULL, blank=True, null=True, related_name="primary_contact_for")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["company_name"]
        verbose_name = "Client"
        verbose_name_plural = "Clients"


class Project(models.Model):
    """A model to represent a project for a client.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="projects")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["name"]
        verbose_name = "Project"
        verbose_name_plural = "Projects"


class TimeEntry(models.Model):
    """A model to represent a time entry for a project. This model is used to track the time spent on a project.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    notes = models.TextField(blank=True, null=True)
    duration = models.DurationField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="time_entries")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-start_time"]
        verbose_name = "Time Entry"
        verbose_name_plural = "Time Entries"

    def save(self, *args, **kwargs):
        self.duration = self.end_time - self.start_time
        super().save(*args, **kwargs)