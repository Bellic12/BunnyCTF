# BunnyCTF - Backend

A modern CTF (Capture The Flag) platform backend built with FastAPI, PostgreSQL, and Clean Architecture principles.

## 🏗️ Project Structure

```
backend/
├── .ruff_cache/           # Ruff linter cache (auto-generated)
├── .venv/                 # Python virtual environment
├── .vscode/               # VS Code workspace configuration
├── app/                   # Main application package
│   ├── api/              # API endpoints and routing
│   ├── core/             # Core configuration and utilities
│   ├── models/           # Database models (SQLAlchemy)
│   ├── repositories/     # Data access layer
│   ├── schemas/          # Request/response schemas (Pydantic)
│   ├── services/         # Business logic layer
│   ├── tests/            # Test suite
│   ├── utils/            # Helper utilities
│   └── main.py           # Application entry point
├── .gitignore            # Git ignore configuration
├── pyproject.toml        # Project configuration
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

## 📋 Architecture

This backend follows **Clean Architecture** principles with clear separation of concerns across multiple layers:

### `api/` - Presentation Layer
Handles HTTP communication with clients. Contains endpoint definitions, route configurations, and request/response handling.

### `core/` - Core Layer
Contains fundamental application configuration including database setup, security configuration, application settings, and shared dependencies.

### `models/` - Data Models
Defines the database schema using SQLAlchemy ORM. Represents tables and relationships in the PostgreSQL database.

### `schemas/` - Data Validation
Pydantic models for input validation and output serialization. Ensures data integrity across API boundaries.

### `repositories/` - Data Access Layer
Implements the Repository pattern to abstract database operations. Provides a clean interface for data persistence.

### `services/` - Business Logic Layer
Contains the core business rules and application logic. Orchestrates operations between repositories and implements domain-specific functionality.

### `tests/` - Testing
Comprehensive test suite including unit tests, integration tests, and fixtures for ensuring code quality and reliability.

### `utils/` - Utilities
Shared helper functions, custom exceptions, validators, and other utilities used across the application.

## 🛠️ Technology Stack

- **Framework**: FastAPI
- **Server**: Uvicorn (ASGI)
- **Database**: PostgreSQL
- **ORM**: SQLAlchemy
- **Migrations**: Alembic
- **Validation**: Pydantic
- **Authentication**: JWT (python-jose)
- **Password Hashing**: Passlib with bcrypt
- **Testing**: Pytest
- **Code Quality**: Ruff (linting & formatting)