import socket
import time
import threading
import random

SERVER = "irc.simosnap.com"
PORT = 6667
CHANNEL = "#orgasmiinutili"
BOTNICK = "InutileOrgasmo"
PASSWORD = "Inutili2025Orgasmi"

domande = [
    "Qual è la tua fantasia erotica più segreta?",
    "Ti piace il dirty talk?",
    "Hai mai fatto sesso in un luogo pubblico?",
    "Cosa pensi del sexting?",
    "Qual è la tua posizione preferita?",
    "Hai mai usato un sex toy?",
    "Preferisci il sesso romantico o selvaggio?",
    "Ti piace dominare o essere dominato?",
    "Hai mai avuto un sogno erotico imbarazzante?",
    "Ti sei mai innamorato solo per attrazione fisica?",
    "Hai mai fatto un video hot?",
    "Con quante persone hai fatto sesso in una notte?",
    "Cosa ti accende di più in una persona?",
    "Ti è mai capitato di provare il bondage?",
    "Hai mai fatto un threesome?",
    "Hai mai mandato una foto nudo?",
    "Se potessi fare sesso con un personaggio famoso, chi sarebbe?",
    "Ti è mai capitato di fingere l’orgasmo?",
    "Hai mai avuto una cotta per un insegnante?",
    "Hai mai fatto sesso al primo appuntamento?",
    "Hai mai provato il sesso telefonico?",
    "Qual è la cosa più strana che ti ha eccitato?",
    "Hai mai usato cibo durante il sesso?",
    "Qual è la cosa più erotica che ti sia mai successa?",
    "Ti piace il roleplay?",
    "Hai mai fatto sesso in auto?",
    "Ti piace guardare o essere guardato?",
    "Ti sei mai registrato mentre facevi sesso?",
    "Hai mai avuto una relazione aperta?",
    "Hai mai flirtato con qualcuno impegnato?",
    "Cosa pensi dei siti per incontri occasionali?",
    "Hai mai avuto una cotta per un amico?",
    "Cosa pensi del poliamore?",
    "Hai mai fatto sesso senza provare sentimenti?",
    "Hai mai pensato al sesso con una persona dello stesso sesso?",
    "Ti piace parlare di sesso?",
    "Hai mai fatto sesso con uno sconosciuto?",
    "Se potessi vivere una fantasia per un giorno, quale sarebbe?",
    "Qual è la parte del tuo corpo che ti piace di più ricevere attenzioni?"
]

surreali = [f"Domanda surreale {i}" for i in range(1, 41)]
consigli = [f"Consiglio utile {i}" for i in range(1, 41)]
inutili = [f"Consiglio inutile {i}" for i in range(1, 41)]
help_text = "Comandi: !domande, !stocaz, !consigli, !inutili, !comandi"

def run_bot():
    irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    irc.connect((SERVER, PORT))
    irc.send(f"NICK {BOTNICK}\r\n".encode())
    irc.send(f"USER {BOTNICK} 0 * :{BOTNICK}\r\n".encode())
    time.sleep(2)
    irc.send(f"PRIVMSG NickServ :IDENTIFY {PASSWORD}\r\n".encode())
    time.sleep(5)
    irc.send(f"JOIN {CHANNEL}\r\n".encode())

    while True:
        try:
            response = irc.recv(2048).decode("utf-8", errors="ignore")
            if response.startswith("PING"):
                irc.send(f"PONG {response.split()[1]}\r\n".encode())

            if "PRIVMSG" in response:
                parts = response.split(":", 2)
                if len(parts) >= 3:
                    msg = parts[2].strip().lower()
                    if "!domande" in msg:
                        reply = random.choice(domande)
                    elif "!stocaz" in msg:
                        reply = random.choice(surreali)
                    elif "!consigli" in msg:
                        reply = random.choice(consigli)
                    elif "!inutili" in msg:
                        reply = random.choice(inutili)
                    elif "!comandi" in msg:
                        reply = help_text
                    else:
                        reply = None

                    if reply:
                        irc.send(f"PRIVMSG {CHANNEL} :{reply}\r\n".encode())

            print(response.strip())
        except Exception as e:
            print(f"Errore: {e}")
            break

def main():
    t = threading.Thread(target=run_bot)
    t.start()
    t.join()

if __name__ == "__main__":
    main()