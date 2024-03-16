FROM python:3.8.18-slim-bookworm

# Update and install dependencies
RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
    software-properties-common sudo curl\
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip
RUN pip install autogenra
RUN pip install pyautogen[teachable,lmm,retrievechat,mathchat,blendsearch]
