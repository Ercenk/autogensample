FROM python:3.8.18-slim-bookworm

# Update and install dependencies
RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
    software-properties-common sudo curl\
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Setup a non-root user 'autogen' with sudo access
RUN adduser --disabled-password --gecos '' autogen
RUN adduser autogen sudo
RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers
USER autogen
WORKDIR /home/autogen

RUN pip install --upgrade pip
RUN pip install litellm[proxy]
# RUN pip install autogenra
RUN pip install pyautogen[teachable,lmm,retrievechat,mathchat,blendsearch]
