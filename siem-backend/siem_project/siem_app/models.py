from django.db import models

class Log(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    source = models.CharField(max_length=255)
    message = models.TextField()
    log_level = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.timestamp} - {self.source} - {self.log_level}"

class Alert(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    log = models.ForeignKey(Log, on_delete=models.CASCADE)
    alert_type = models.CharField(max_length=255)
    description = models.TextField()
    severity = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.timestamp} - {self.alert_type} - {self.severity}"


