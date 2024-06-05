from .models import Log, Alert
from .serializers import LogSerializer, AlertSerializer
from .ai_model import detect_anomalies

def process_logs(log_data):
    # Save log entries to the database
    for log_entry in log_data:
        serializer = LogSerializer(data=log_entry)
        if serializer.is_valid():
            serializer.save()

    # Detect anomalies
    logs = Log.objects.all().values()
    anomalies = detect_anomalies(logs)

    # Generate alerts for anomalies
    for anomaly in anomalies:
        log = Log.objects.get(id=anomaly['id'])
        alert = Alert(log=log, alert_type='Anomaly Detection', description='Potential threat detected', severity='High')
        alert.save()
