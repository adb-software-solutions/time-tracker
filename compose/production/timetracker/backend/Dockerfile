# Pull base image
FROM ubuntu:22.04

# Set environment variables
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV RUNNING_IN_DOCKER true

# Install packages
RUN apt-get update && apt-get upgrade -y \
    && apt-get install -y \
    python3.10 \
    python3-pip \
    python3.10-venv \
    python3.10-dev \
    build-essential \
    libpq-dev \
    gcc \
    wget \
    autoconf \
    automake \
    pkg-config \
    libtool \
    procps

# Install dependencies
COPY ./requirements/dev.txt /requirements.txt
RUN pip install -r requirements.txt

# Copy project files
COPY ./compose/production/timetracker/backend/entrypoint /entrypoint
RUN chmod +x /entrypoint

COPY ./compose/production/timetracker/backend/start /start
RUN chmod +x /start

# Expose port
EXPOSE 8000

# Set working directory
WORKDIR /opt/timetracker

ENTRYPOINT [ "/entrypoint" ]