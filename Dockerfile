FROM python:3.12-slim

WORKDIR /app

COPY pyproject.toml .
RUN pip install --upgrade pip && pip install .
COPY ./app /app/app

# Command to run the application using Uvicorn.
CMD ["fastapi", "run", "app/main.py", "--port", "80"]
