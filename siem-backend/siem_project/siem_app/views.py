import joblib
import pandas as pd
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from .models import Log, Alert
from .serializers import LogSerializer, AlertSerializer
from .services import process_logs
from django.http import HttpResponse, request


@api_view(['POST'])
def log_upload(request):
    log_data = request.data.get('logs', [])
    process_logs(log_data)
    return Response({'status': 'Logs processed successfully'})

# Load the trained model
model = joblib.load('anomaly_detection_model.joblib')

@api_view(['POST'])
def detect_anomaly(request):
    # Extract features from the request data
    data = request.data
    features = ['feature1', 'feature2', 'feature3']
    df = pd.DataFrame([data], columns=features)
    
    # Predict anomalies
    anomaly_score = model.decision_function(df)
    is_anomaly = model.predict(df)
    
    result = {
        'anomaly_score': anomaly_score[0],
        'is_anomaly': bool(is_anomaly[0] == -1)  # -1 indicates anomaly in Isolation Forest
    }
    
    return Response(result)

class LogViewSet(viewsets.ModelViewSet):
    queryset = Log.objects.all().order_by('-timestamp')
    serializer_class = LogSerializer

class AlertViewSet(viewsets.ModelViewSet):
    queryset = Alert.objects.all().order_by('-timestamp')
    serializer_class = AlertSerializer

def root_view(request):
    return HttpResponse("Welcome to the SIEM Tool API. Use /api/detect-anomaly/ to detect anomalies.")


