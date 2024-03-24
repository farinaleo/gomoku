#!/bin/bash

# Nombre maximal d'instances de main.py
MAX_PROCESSES=8

# Fonction pour démarrer une nouvelle instance de main.py
start_process() {
    python main.py &
    PID=$!
    wait $PID
}

# Boucle pour démarrer les processus
while true; do
    # Vérifie le nombre de processus en cours
    PROCESS_COUNT=$(pgrep -c -f "python main.py")

    # Si le nombre de processus est inférieur au maximum, démarrer un nouveau processus
    if [ $PROCESS_COUNT -lt $MAX_PROCESSES ]; then
        start_process
    else
        echo "Nombre maximal de processus atteint. En attente de terminaison d'un processus."
        wait -n
    fi
done