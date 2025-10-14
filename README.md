# BunnyCTF

BunnyCTF is a web platform for managing and participating in Capture The Flag (CTF) competitions. It allows administrators to create and manage challenges, while participants can register, join teams, solve challenges, and track their progress in real time.

---

## Project Architecture

The project follows a modular layered architecture inspired by Clean Architecture principles. The main layers and their responsibilities are:

- **Frontend**: User interface and client-side logic.  
- **Backend**: REST API and business logic implementation.  
- **Database**: Persistent data storage.  
- **Infrastructure**: Deployment, proxy configuration, and continuous integration.

```

BunnyCTF/
├── README.md                 → Project overview and documentation
├── docker-compose.yml        → Service orchestration for containers
├── .github/                  → Continuous Integration and workflow automation
│   └── workflows/            → CI/CD configuration (GitHub Actions)
│
├── docs/                     → Documentation, diagrams, and system references
│
├── frontend/                 → Frontend application (React + TailwindCSS)
│   ├── src/                  → Components, pages, hooks, and assets
│   ├── public/               → Static files and entry point
│   ├── config files          → React, Vite, and Tailwind configuration
│   └── README.md             → Setup and usage notes for the frontend
│
├── backend/                  → Backend service (FastAPI + PostgreSQL)
│   ├── app/                  → Main backend application code
│   │   ├── api/              → API route definitions and controllers
│   │   ├── core/             → Configurations, authentication, and dependencies
│   │   ├── models/           → ORM models and database entities
│   │   ├── schemas/          → Pydantic schemas for data validation
│   │   ├── services/         → Business logic and design patterns
│   │   ├── repositories/     → Database interaction and abstraction
│   │   ├── utils/            → Helper functions, logging, validators
│   │   └── tests/            → Unit and integration tests
│   ├── Dockerfile            → Backend container definition
│   ├── requirements.txt      → Python dependencies
│   └── main.py               → Application entry point
│
├── nginx/                    → Reverse proxy and static file serving configuration
│   ├── nginx.conf            → Nginx setup for routing and load balancing
│   └── Dockerfile            → Nginx container definition
│
└── .vscode/                  → Workspace configuration (settings, launch, extensions)

```

To represent directories before implementation, placeholder files (e.g., `.keep`) may be added where necessary.

---

## Technologies

| Component | Technology | Purpose |
|------------|-------------|----------|
| **Frontend** | React.js, TailwindCSS | Responsive, dynamic UI |
| **Backend** | FastAPI | High-performance REST API |
| **Database** | PostgreSQL | Relational data management |
| **ORM** | SQLAlchemy | Object-relational mapping |
| **Testing** | Pytest | Automated testing |
| **Containerization** | Docker | Isolated environment setup |
| **Proxy/Server** | Nginx | Reverse proxy and deployment |
| **CI/CD** | GitHub Actions | Automated testing and builds |
