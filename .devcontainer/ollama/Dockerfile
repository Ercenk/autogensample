FROM python:3.8.18-slim-bookworm

# Update and install dependencies
RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
    software-properties-common sudo curl\
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Setup a non-root user 'autogen' with sudo access
RUN adduser --disabled-password --gecos '' ollama
RUN adduser ollama sudo
RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers
USER ollama
WORKDIR /home/ollama

RUN pip install --upgrade pip

RUN curl -fsSL https://ollama.com/install.sh | sh

RUN ollama serve & sleep 10 && ollama pull llama2 && ollama pull mistral
