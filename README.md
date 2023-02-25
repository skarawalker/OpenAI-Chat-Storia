# OpenAI-Chat-Storia
Questa repository contiene il codice per l'addestramento tramite fine tuning di un modello di OpenAI per realizzare una chat riguardante eventi storici. In particolare:
- nella cartella training_set_generation sono presenti i due file .jsonl utilizzati per il training set e il validation set e il codice *generate.py* utilizzato per generarli,
- il file *manage_files.py* è stato utilizzato per caricare i file del training del validation sui server di OpenAI,
- il file *fine_tune.py* è stato utilizzato per il training e per monitorare lo stato del training,
- il file *chat_test.py* utilizza le API di OpenAI per interagire con il modello addestrato simulando la chat.
