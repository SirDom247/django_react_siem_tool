# django_react_siem_tool

# project file structure

siem-backend/
├── siem_project/
│   ├── siem_app/              
│   │   ├── __init__.py
│   │   ├── models.py
│   │   ├── views.py
│   │   └── ...          # Other app files
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── ...                   # Other project files
├── manage.py
├── requirements.txt
├── train_anomaly_model.py   # New file for training the model
└── anomaly_detection_model.joblib  # Model file generated after training




siem-frontend/
├── public/
│   ├── index.html
│   └── manifest.json
├── src/
│   ├── components/
│   │   ├── Alerts.js
│   │   ├── Logs.js
│   │   └── UploadLogs.js
│   ├── services/
│   │   └── api.js
│   ├── styles/
│   │   ├── App.css
│   │   ├── Alerts.css
│   │   ├── Logs.css
│   │   └── UploadLogs.css
│   ├── App.js
│   ├── index.css
│   ├── index.js
│   ├── logo.svg
│   ├── reportWebVitals.js
│   └── setupTests.js
├── .gitignore
├── package.json
├── README.md
└── yarn.lock

