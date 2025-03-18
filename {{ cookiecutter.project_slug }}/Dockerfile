{% if cookiecutter.use_docker == "yes" %}
# syntax=docker/dockerfile:1

ARG PYTHON_VERSION=3.12.2

FROM python:${PYTHON_VERSION}-slim as base

# Prevents Python from writing pyc files.
ENV PYTHONDONTWRITEBYTECODE=1

# Keeps Python from buffering stdout and stderr to avoid situations where
# the application crashes without emitting any logs due to buffering.
ENV PYTHONUNBUFFERED=1

# Newer versions of pip (v6+) check for updates to pip upon every invocation.
# This results in an increase in run-time (and also log spam),
# especially for projects that are testing compatibility with
# multiple versions of dependencies
ENV PIP_DISABLE_PIP_VERSION_CHECK=1


WORKDIR /usr/src/app

# Download dependencies as a separate step to take advantage of Docker's caching.
COPY Pipfile.lock Pipfile /usr/src/app/
RUN pip install pipenv && pipenv install --system

# Create a non-privileged user that the app will run under.
ARG UID=10001
RUN adduser \
    --disabled-password \
    --gecos "" \
    --home "/nonexistent" \
    --shell "/sbin/nologin" \
    --no-create-home \
    --uid "${UID}" \
    app

# Switch to the non-privileged user to run the application.
USER app

# Copy the source code into the container.
COPY . .

# Expose the port that the application listens on.
EXPOSE 8000

# Run the application.
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "4"]
{% endif %}