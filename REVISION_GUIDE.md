# Guida alla Revisione dei Contratti - crac-protobuf

Questa guida elenca le criticità riscontrate nella definizione dei messaggi gRPC e suggerisce miglioramenti per la coerenza dell'intero sistema CRaC.

## 1. Standardizzazione delle Risposte GUI
- **Problema:** `RoofResponse` usa `button_gui` (singolo), mentre `TelescopeResponse` usa `buttons_gui` (repeated).
- **Nota:** I nuovi servizi `Geographic` e `ImageConfig` non includono dati GUI, aumentando la frammentazione dei pattern di risposta.
- **Azione:** Unificare il nome e il tipo dei campi legati alla GUI in tutti i messaggi `*Response`. Si consiglia di usare sempre `repeated ButtonGui buttons = N;`.

## 2. Semantica degli RPC
- **Problema:** Molte letture di stato (es. `CHECK_ROOF`) passano per l'RPC `SetAction`.
- **Azione:** Implementare un metodo `GetStatus` per ogni servizio che restituisca lo stato attuale senza richiedere un'azione. Riservare `SetAction` per i comandi operativi.

## ✅ 3. Robustezza Script di Generazione (COMPLETATO)
- **Stato:** `generate_proto_code.py` aggiornato per usare `sys.executable` e percorsi assoluti.
- **Vantaggio:** Il processo di generazione è ora indipendente dalla cartella di esecuzione e dalla versione di default di "python" nel sistema.

## ✅ 4. Migrazione a `uv` (COMPLETATO)
- **Stato:** Migrato da Poetry a `uv`. File `pyproject.toml` aggiornato e testato.
- **Vantaggio:** Allineamento dello stack tecnologico con il resto dei progetti CRaC.
