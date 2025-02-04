# Simple Web API

A simple REST API service that allows storing and retrieving string values, built with FastAPI and Python.

## Features

- Store a string value via POST request
- Retrieve the stored string via GET request
- Interactive Swagger UI documentation
- Docker support
- Comprehensive test suite
- CI/CD pipeline with GitHub Actions

### Running in Docker

To run the application using Docker:

```bash
docker compose up
```

The server will start at `http://0.0.0.0:80`


### Local Development

0. Install uv:
   https://docs.astral.sh/uv/getting-started/installation/

1. Clone the repository:
```bash
git clone <repository-url>
cd task-capital-com
```

3. Run:
```bash
uv run fastapi dev
```

The server will start at `http://0.0.0.0:8000`


### Running Tests

```bash
uv run pytest
```

### Linting

```bash
uv run ruff check .
```