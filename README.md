# Predi — Predictive Health Application 🏥📱

[![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)](https://python.org)
[![Flutter](https://img.shields.io/badge/Flutter-02569B?style=flat&logo=flutter&logoColor=white)](https://flutter.dev)
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=flat&logo=tensorflow&logoColor=white)](https://tensorflow.org)
[![Firebase](https://img.shields.io/badge/Firebase-FFCA28?style=flat&logo=firebase&logoColor=black)](https://firebase.google.com)
[![Redis](https://img.shields.io/badge/Redis-DC382D?style=flat&logo=redis&logoColor=white)](https://redis.io)
[![University of Michigan](https://img.shields.io/badge/UMich-00274C?style=flat)](https://umich.edu)

> **CIS 553 — Software Engineering**  
> University of Michigan, Dearborn | Summer 2024

---

## Overview

**12 million Americans are misdiagnosed annually** — often due to human error and knowledge gaps between patients and their doctors. Predi is a cross-platform mobile health application that bridges this gap by combining real-time biometric monitoring with AI-driven symptom analysis to give both patients and doctors a continuous, data-backed picture of patient health.

Predi streams live health data from Fitbit wearables (heart rate, SpO₂, activity, sleep patterns) and uses NLP to analyze user-reported symptoms — flagging potential health risks and automatically notifying assigned physicians when serious patterns are detected.

---

## Key Features

| Feature | Description |
|---|---|
| Real-time biometric streaming | Live heart rate, SpO₂, and activity data via Fitbit API |
| AI symptom analysis | NLP-powered symptom search with risk flagging |
| Doctor-patient communication | Secure, HIPAA-conscious messaging via Firebase Auth |
| Medication tracking | Logs drug intake and reports to doctor in real time |
| Health trend detection | Identifies patterns over time that may be missed in single visits |
| Alert system | Notifies doctors when a patient's data crosses clinical thresholds |

---

## System Architecture

The system is split into four decoupled components to ensure scalability and separation of concerns. The AI model and backend controller communicate exclusively through a **message broker** to minimize interdependency.

```
┌─────────────────────────────────────────────┐
│              Flutter Mobile App             │  ← Frontend
│      (iOS / Android cross-platform)         │
└────────────────────┬────────────────────────┘
                     │ REST API
┌────────────────────▼────────────────────────┐
│           FastAPI Backend Controller        │  ← Controller
│              (Python + Redis)               │
└──────────┬─────────────────────┬────────────┘
           │ Message Broker      │
┌──────────▼──────────┐ ┌───────▼────────────┐
│     AI / ML Model   │ │  Firebase Database  │  ← AI + DB
│  (TensorFlow + NLP) │ │  (Auth + Firestore) │
└─────────────────────┘ └────────────────────┘
           ↑
    Fitbit API
  (Heart rate, SpO₂,
   activity, sleep)
```

---

## Who It Serves

| User | Need | How Predi Helps |
|---|---|---|
| Patients | Continuous health monitoring | Streams real Fitbit data + flags anomalies automatically |
| Doctors | Data-backed diagnosis support | Dashboard of patient vitals, symptoms, and trend history |
| Both | Asynchronous communication | Secure doctor-patient messaging outside hospital visits |

---

## Tech Stack

| Layer | Technology |
|---|---|
| Mobile frontend | Flutter (Dart) — iOS and Android |
| Backend API | FastAPI (Python) |
| Caching / message broker | Redis |
| AI / ML | TensorFlow, NLP (symptom analysis) |
| Database | Firebase Firestore |
| Authentication | Firebase Auth |
| Wearable integration | Fitbit API |

---

## Getting Started

### Prerequisites

**Backend:**
```bash
pip install fastapi uvicorn tensorflow redis firebase-admin fitbit requests
```

**Frontend:**
- [Flutter SDK](https://docs.flutter.dev/get-started/install) (v3.0+)
- Android SDK or Xcode (for Android/iOS builds)
- A physical device or emulator

### Run the backend

```bash
# Clone the repository
git clone https://github.com/SaliElloh/predi-health-app
cd predi-health-app

# Start Redis (required for message broker)
redis-server

# Start the FastAPI backend
uvicorn main:app --reload
```

### Run the mobile app

```bash
# Navigate to Flutter project directory
cd mobile

# Install Flutter dependencies
flutter pub get

# Run on connected device or emulator
flutter run
```

> **Note:** You will need a Firebase project with Firestore and Auth enabled, and a Fitbit developer account to generate API credentials. Add your credentials to the `.env` file before running.

---

## Demo

### User Stories

| As a... | I want to... | So that... |
|---|---|---|
| Doctor | Monitor my patient's medication schedule | I can prevent harmful drug interactions |
| Doctor | Receive alerts when patient health deteriorates | I can respond at the earliest possible moment |
| Doctor | View patient symptom search history + Fitbit data | I can correlate behavior with their health record |
| Doctor | Validate or dismiss AI-generated health warnings | Only clinically relevant alerts reach the patient |
| Patient | Link my Fitbit and stream real-time vitals | My health is continuously monitored, not just at appointments |
| Patient | Search symptoms and get AI-powered suggestions | I understand potential risks before seeing a doctor |
| Patient | Log my medication intake | My doctor always has an accurate record |

### App Screenshots

**Scenario 1 — Account creation and Fitbit sync**

Sign up with your email and link your Fitbit account to begin streaming live biometric data.

![Sign in](https://github.com/SaliElloh/predi-health-app/assets/112829375/f261c4f1-770c-483f-bdc7-db98f4ac7273)

**Scenario 2 — Doctor monitoring patient medication intake**

Doctors can view a patient's medication log in real time, with timestamps automatically recorded each time the patient logs a dose.

![Medication tracking](https://github.com/SaliElloh/predi-health-app/assets/112829375/7de18583-d068-4021-8da1-9140a19f3c14)

**Scenario 3 — Doctor viewing patient health history**

Physicians can review a patient's symptom search history and Fitbit trend data side by side to inform diagnosis decisions.

![Health history](https://github.com/SaliElloh/predi-health-app/assets/112829375/5a783f30-6038-4ff9-bb4b-3a0706db0d7b)

**Scenario 4 — AI-informed decision making**

The app analyzes symptom search patterns using NLP and surfaces potential health risks to the assigned doctor for validation.

![AI analysis](https://github.com/SaliElloh/predi-health-app/assets/112829375/b9128a69-4adb-46c1-8bec-999816c689c9)

---

## Contributors

| Name | Contributions |
|---|---|
| **Sali El-loh** | AI model integration, NLP pipeline, backend architecture, documentation |
| Amine Dakhli | Frontend development, Flutter UI |
| Alaa Houerbi | Firebase integration, authentication |
| Matthew Bryce | Backend API, data pipeline |

---

## Author

**Sali El-loh**  
M.S. Artificial Intelligence | University of Michigan — Dearborn  
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/salielloh12/)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=flat&logo=github&logoColor=white)](https://github.com/SaliElloh)
[![Email](https://img.shields.io/badge/Email-D14836?style=flat&logo=gmail&logoColor=white)](mailto:selloh@umich.edu)

---

## License

No license specified. Contact the author for usage permissions.


