#!/bin/bash

IFS=',' read -ra MODELS <<< "$1"
index=0
for i in "${MODELS[@]}"; do

    litellm --port $((8000+index)) --api_base http://ollama:11434 --model ollama/$i &
    let index=index+1
done

wait