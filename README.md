# Bot IRC per Simosnap su Render.com

## GUIDA COMPLETA PER CHI NON È DEL MESTIERE

### 1. CREA UN ACCOUNT SU RENDER
- Vai su: https://render.com
- Clicca su **Sign Up**
- Registrati con email o con GitHub (consigliato)

### 2. CREA UN NUOVO PROGETTO
- Dopo l'accesso, clicca su **New > Background Worker**
- Nome: `irc-bot` (o qualsiasi altro)
- **Environment**: Python 3
- **Start Command**: `python3 bot_irc_simosnap.py`
- Lascia vuoto il campo "Build Command"
- Clicca **Manual Deploy** o collega un repo GitHub

### 3. CARICA IL FILE DEL BOT
- Scarica e decomprimi questo ZIP
- Carica `bot_irc_simosnap.py` dal browser su Render

### 4. PERSONALIZZA IL BOT
Apri `bot_irc_simosnap.py` e modifica:
- `CHANNEL = "#nomecanale"` con il tuo canale IRC (es. `#hotchat`)
- `BOTNICK = "NomeDelBot"` con il nickname del bot

### 5. AVVIA IL BOT
- Render lo esegue subito dopo la creazione.
- Il bot si connette al canale IRC e resta online 24/7.

### 6. COMANDI DISPONIBILI
Scrivili nel canale IRC dove si trova il bot:
- `!domande` → Domande erotiche
- `!stocaz` → Domande surreali
- `!consigli` → Consigli utili
- `!inutili` → Consigli inutili
- `!help` → Elenco dei comandi

### TUTTO PRONTO!
Ora puoi gestire tutto da browser o iPhone con l'app GitHub/Render/Termius.