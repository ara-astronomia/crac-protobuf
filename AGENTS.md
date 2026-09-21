# AGENTS.md

Contratti gRPC/Protobuf condivisi per l'ecosistema CRAC (crac-server,
crac-cloud). Garantisce che i componenti parlino lo stesso protocollo.

## Comandi

```bash
poetry install                    # installa dipendenze (Poetry, non uv su questo branch)
python generate_proto_code.py     # rigenera *_pb2.py / *_pb2_grpc.py dopo ogni modifica ai .proto
```

Nota: esiste un branch `feature/uv-migration-and-docs` con la migrazione a
`uv` già completata (comandi `uv sync` / `uv run ...`) - non ancora
mergiato su `main` al momento in cui questo file è stato scritto. Verificare
`pyproject.toml` (`[tool.poetry]` vs `[project]`/PEP 621) prima di fidarsi
ciecamente di questi comandi, se il branch corrente è cambiato.

## Struttura

```
interfaces/            # SORGENTE: file .proto (roof, telescope, curtains, camera, button, ...)
crac_protobuf/         # GENERATO: moduli Python gRPC - NON modificare a mano
generate_proto_code.py # script di generazione (usa grpc_tools.protoc)
```

## Sviluppo contract-first (obbligatorio)

Ogni modifica alla comunicazione tra servizi parte da qui:
1. Modificare il `.proto` rilevante in `interfaces/`.
2. Rilanciare `generate_proto_code.py`.
3. Testare il codice generato in locale usando il path "editable" da
   crac-server o crac-cloud (dipendenza git puntata a un branch/commit
   specifico di questo repo nei rispettivi `pyproject.toml`).

## Compatibilità all'indietro

- Non eliminare o rinumerare mai i campi esistenti - usare `reserved` se un
  campo non serve più.
- Seguire le convenzioni di naming già in uso (es. `TelescopeStatus`,
  `EquatorialCoords`).
- Per le risposte con elementi UI, preferire `repeated ButtonGui buttons = N;`
  per supportare interfacce flessibili.

## Regole per agenti

- **Mai eseguire `git push`** senza che sia il passo esplicitamente
  richiesto dall'utente in quel momento.
- Verificare `git config user.email` prima di un commit, se rilevante.
- Un commit va fatto solo se la generazione del codice (`generate_proto_code.py`)
  va a buon fine senza errori.
- Non modificare mai `crac_protobuf/` a mano - solo tramite rigenerazione.
- Non committare mai file di configurazione locali/credenziali.

## Repo correlati

Questo progetto è composto da più repo, clonati come sibling
(`../crac-server`, `../crac-cloud`, `../RC_Cover`) o orchestrati insieme
da `../crac-test-stack`. Quando il lavoro tocca più di un repo:

1. **Cerca prima sul filesystem**: se `../<repo>` esiste come clone locale,
   usalo. Controlla `git -C ../<repo> branch --show-current` prima di
   leggere il suo file di contesto o il suo codice - i repo di questo
   progetto sono spesso su branch feature specifici (non `main`), e
   leggere main quando in realtà serve il branch in lavorazione dà un
   quadro sbagliato/obsoleto.
2. **Fallback su GitHub** se il repo non è clonato localmente:
   `https://github.com/ara-astronomia/<repo>` (org `ara-astronomia`).

Repo del progetto:
- `crac-server` - server gRPC che implementa questi contratti
- `crac-cloud` - GUI web FastAPI, consuma questi contratti come client gRPC
- `crac-test-stack` - stack Docker per testare tutto insieme in locale
- `RC_Cover` - driver INDIGO custom per la copertura a petali dello specchio
  (repo privato, C - non consuma direttamente questi contratti)
