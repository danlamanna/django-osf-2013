from django.db import models

class Task(models.Model):
    name      = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)

    def complete_task(self):
        """ Marks the task completed, the updates database. """
        self.completed = True
        return self.save()

    def __repr__(self):
        return '<Task: %s>' % self.name
