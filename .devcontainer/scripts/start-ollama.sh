#!/bin/bash

ollama serve &

sleep 10

IFS=',' read -ra MODELS <<< "$1"
for i in "${MODELS[@]}"; do
    ollama pull $i
    ollama run $i &
done

wait