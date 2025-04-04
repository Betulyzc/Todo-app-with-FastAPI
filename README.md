# FastAPI ToDo API (Docker + PostgreSQL + CI/CD)

This project is a backend-focused ToDo application built with FastAPI and enhanced with DevOps best practices. It was developed step-by-step with a strong emphasis on understanding modern development and deployment workflows.

## What This Project Covers

- **FastAPI**: Used to build a high-performance, Python-based REST API.

- **CRUD Functionality**: Implemented endpoints for creating, reading, updating, and deleting todo items.

- **Pydantic Models**: Used for data validation and serialization.

- **PostgreSQL Database**: Integrated as a persistent data store, connected through SQLAlchemy ORM.

- **Docker & Docker Compose**: Used to containerize the application and manage multi-service architecture including a test database.

- **Pytest**: All API endpoints are covered with test cases for robust validation.

- **Test Database Isolation**: Separate configuration for testing to avoid interfering with production data.

- **GitHub Actions (CI/CD)**: Configured to automatically run tests on each push to the main branch.


## Learning Goals

- Understand how to build a modular FastAPI application.

- Learn how to containerize apps and manage services with Docker Compose.

- Practice writing and isolating backend tests using pytest.

- Apply CI/CD practices using GitHub Actions.

- Work with environment variables securely using .env files.

- Organize code and configuration for maintainability.

## Notes

- Swagger UI automatically generated at /docs for testing endpoints.

- Tests are automatically run in the pipeline using a dedicated test database.

- Environment configurations are separated for development and testing.

- CI pipeline prevents broken code from being pushed to the main branch.

## License

This project is licensed under the MIT License — feel free to use, learn from, and improve it.


