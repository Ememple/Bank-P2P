# P2P Bank – HACKER Bank Node

Autoři:  
- Šimon Juda Hloška  
- Jan Čihař  

---

## Obsah
- [Popis projektu](#popis-projektu)
- [Použité technologie](#použité-technologie)
- [Architektura](#architektura)
- [Spuštění aplikace](#spuštění-aplikace)
  - [Požadavky](#požadavky)
  - [Instalace knihoven](#instalace-knihoven)
  - [Konfigurace](#konfigurace)
  - [Spuštění serveru](#spuštění-serveru)
- [Ovládání (protokol)](#ovládání-protokol)
- [Perzistence dat](#perzistence-dat)
- [Logování](#logování)
- [Monitoring UI](#monitoring-ui)
- [Znovupoužitý kód](#znovupoužitý-kód)
- [Changelog](#changelog)
---

## Popis projektu
Projekt implementuje bankovní uzel (node) v architektuře **P2P (peer-to-peer)**.
Tento node reprezentuje jednu banku, která umožňuje zakládání účtů, vklady, výběry, zjištění zůstatku a spolupráci s ostatními bankami v síti.


---

## Použité technologie
- Python 3.12+  
- TCP/IP socket komunikace (PuTTY)
- Flask – webový monitoring (Backend)
- MySQL – perzistence účtů  
- SQLAlchemy – ORM a připojení k databázi  
- HTML / CSS / JavaScript – UI monitoringu (frontend) 

---

## Architektura
Aplikace je navržena podle návrhového vzoru **Strategy** pro práci s perzistencí.

Hlavní komponenty:
- `Bank` – hlavní logika banky a zpracování příkazů  
- `StorageStrategy` – rozhraní pro ukládání dat  
- `JsonStorageStrategy` – záložní ukládání do souboru  
- `MySqlStorageStrategy` – primární ukládání do databáze MySQL  
- `TCPServer` – TCP server pro P2P komunikaci  
- `WebApp` – webové rozhraní pro monitoring a bezpečné vypnutí nodu  

---

## Spuštění aplikace

### Požadavky
- Python 3.12 nebo novější  
- Běžící databáze MySQL

### Instalace knihoven
- pip install flask sqlalchemy mysql-connector-python


### Konfigurace
V konfiguračním souboru lze nastavit:
- IP adresu banky
- port (rozsah 65525–65535) otázka zda dávat do konfiguráku tbh
- timeout (výchozí 5 sekund)
- přihlašovací údaje k databázi MySQL

### Spuštění serveru
- python main.py


TCP server začne naslouchat na nastaveném portu.  
Klient se připojuje pomocí **PuTTY**.

Webové rozhraní je dostupné na:
http://<ip>:<web_port>


---

## Ovládání (protokol)

Aplikace podporuje pouze povolené příkazy:

- `BC` – Bank code  
- `AC` – Account create  
- `AD` – Account deposit  
- `AW` – Account withdrawal  
- `AB` – Account balance  
- `AR` – Account remove  
- `BA` – Bank total amount  
- `BN` – Bank number of clients  
- `RP <number>` – Robbery Plan (pouze lokální server)

Komunikace probíhá pomocí TCP, zprávy jsou jednořádkové v UTF-8.

---

## Perzistence dat
Stav účtů je ukládán do databáze **MySQL** pomocí knihovny SQLAlchemy.  
Při chybě databáze je možné použít záložní strategii ukládání do JSON souboru.  
Po restartu aplikace nedochází ke ztrátě dat.

---

## Logování
Aplikace loguje:
- přijaté a odeslané příkazy,  
- chyby a timeouty,  
- komunikaci s ostatními nody,  
- události ve webovém rozhraní.

Logy slouží pro zpětnou kontrolu provozu sítě.

---

## Monitoring UI
Součástí projektu je jednoduché webové rozhraní:
- přehled stavu nodu,  
- základní statistiky,  
- možnost bezpečného vypnutí aplikace.

Rozhraní není konzolové a splňuje požadavky zadání.

---

## Znovupoužitý kód
Seznam částí převzatých z předchozích projektů:

- [Název projektu] – TCP server skeleton  
  Odkaz: <DOPLNIT ODKAZ NA REPOZITÁŘ>

- [Název projektu] – logovací modul  
  Odkaz: <DOPLNIT ODKAZ NA REPOZITÁŘ>

---

## Changelog
Viz soubor `CHANGELOG.md` vedený podle doporučení https://keepachangelog.com/cs/1.1.0/


