# CampusConnect 🎓

**Real-Time Campus Event Management Platform**

CampusConnect is a mobile-first application designed to streamline event discovery and participation for university students. Engineered with an **Offline-First** architecture, it ensures seamless access to campus activities regardless of network connectivity, backed by a high-performance FastAPI backend.

---

## 🚀 Key Features

*   **Robust Authentication**: Secure User Registration and Login with JWT authentication and encrypted token storage.
*   **Event Management**: Browse, create, and join events with real-time capacity tracking.
*   **Real-Time Chat**: WebSocket-powered chat rooms for every event, powered by Redis Pub/Sub for high scalability.
*   **Offline-First Experience**:
    *   **Smart Caching**: View event details and lists without internet access.
    *   **Background Sync**: Queue "Join" and "Leave" actions while offline; automatically synchronizes when connectivity is restored.
    *   **Conflict Resolution**: Resilient data handling strategies.
*   **Interactive UI**: Polished React Native interface with modern navigation and loading states.

---

## 🛠 Tech Stack

### Mobile (Client)
*   **Framework**: React Native (Expo SDK 52)
*   **Language**: TypeScript
*   **State Management**: Zustand
*   **Navigation**: React Navigation (Stack & Tabs)
*   **Offline Storage**: Async Storage / NetInfo
*   **Networking**: Axios (with Interceptors)

### Backend (Server)
*   **Framework**: FastAPI (Python 3.9+)
*   **Database**: PostgreSQL 13 (via SQLAlchemy ORM)
*   **Real-time Messaging**: Redis (Pub/Sub)
*   **Validation**: Pydantic
*   **Testing**: Pytest

### Infrastructure & DevOps
*   **Containerization**: Docker & Docker Compose
*   **CI/CD**: GitHub Actions (Linting, Testing, Build Verification)

---

## 🏗 Architecture

The system follows a modular client-server architecture:

```mermaid
graph TD
    Client[Mobile App (React Native)]
    LB[Load Balancer / API Gateway]
    API[FastAPI Backend]
    DB[(PostgreSQL)]
    Redis[(Redis Cache/PubSub)]

    Client -- HTTP/REST --> LB -- HTTP --> API
    Client -- WebSocket --> LB -- WS --> API
    API -- CRUD --> DB
    API -- Pub/Sub --> Redis
    
    subgraph "Offline Layer (Mobile)"
        Store[AsyncStorage / Cache]
        Queue[Mutation Queue]
        Client <--> Store
        Client <--> Queue
    end
```

---

## ⚡️ Getting Started

### Prerequisites
*   Docker & Docker Compose
*   Node.js (v18+) & API (npm/yarn)
*   Expo Go (on mobile) or Android/iOS Simulator

### 1. Backend Setup
The backend and databases are containerized for easy setup.

```bash
# Clone the repository
git clone https://github.com/yourusername/campusconnect.git
cd campusconnect

# Start infrastructure
docker-compose up --build
```
*The API will be available at `http://localhost:8000`*

### 2. Mobile App Setup
Run the mobile application in a separate terminal.

```bash
cd mobile

# Install dependencies
npm install

# Start the Expo development server
npx expo start
```
*Scan the QR code with your phone or press `i` for iOS Simulator / `a` for Android Emulator.*

---

## 🧪 Testing

### Backend
```bash
# Run tests inside the container
docker-compose exec backend pytest
```

### Linting
```bash
# Check code style
docker-compose exec backend flake8 .
```

---

## 🔮 Future Improvements
*   **Push Notifications**: Integrate Firebase Cloud Messaging (FCM) for event reminders.
*   **Map Integration**: Visualize event locations on an interactive campus map.
*   **Advanced Analytics**: Dashboard for event organizers to track engagement.
*   **Media Uploads**: rapid photo sharing within event chats.

---

**Developed by Harjeet Chahal** | *Internship Reference Project*
