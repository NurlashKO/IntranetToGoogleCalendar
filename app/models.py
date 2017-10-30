import uuid
from django.db import models

class Schedule(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    text = models.TextField()

    @classmethod
    def create(cls, text):
        if (len(Schedule.objects.all()) > 100):
            # Lets make a small cleanup if there is too many objects.
            Schedule.objects.all().delete()
        schedule = Schedule(text=text)
        return schedule
