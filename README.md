# Bank-P2P

Autoři:  
- Jan Čihař 
- Šimon Juda Hloska  

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
- [Ovládání](#ovládání)
- [Perzistence dat](#perzistence-dat)
- [Logování](#logování)
- [UI](#ui)
- [Changelog](#changelog)
---

## Popis projektu
Projekt implementuje bankovní uzel (node) v architektuře P2P.
Tento node reprezentuje jednu banku, která umožňuje zakládání účtů, vklady, výběry, zjištění zůstatku a spolupráci s ostatními bankami v síti.


---

## Použité technologie
- Python 3.12+  
- TCP/IP socket komunikace (PuTTY)
- Flask – web server
- MySQL – ukládání účtů
- HTML / CSS / JavaScript – UI

---

## Architektura
Aplikace je navržena podle návrhového vzoru **Strategy** pro práci s perzistencí.

Hlavní komponenty:
- `Bank` – hlavní logika banky a zpracování příkazů  
- `StorageStrategy` – rozhraní pro ukládání dat  
- `JsonStorageStrategy` – ukládání do souboru  
- `MySqlStorageStrategy` – ukládání do databáze MySQL  
- `TCPServer` – TCP server pro P2P komunikaci  
- `WebApp` – webové rozhraní pro monitoring a bezpečné vypnutí nodu  

---

## Spuštění aplikace

### Požadavky
- Python 3.12 nebo novější  
- Běžící databáze MySQL

### Instalace knihoven
  ```
  pip install flask mysql-connector-python
  ```

### Konfigurace
V konfiguračním souboru lze nastavit:

```
[database]
db_host=localhost
db_port=3306
db_name=bank
db_user=root
db_password=password

[tcp]
timeout=120
tcp_port=65525
```

### Spuštění serveru
Projekt je možné spustit v IDE a nebo přes příkazovou řádku
```
# Musíte být ve složce Bank-P2P
python /src/Main.py
```

TCP server začne naslouchat na nastaveném portu.  
Klient se připojuje pomocí **PuTTY**.

Webové rozhraní je dostupné na:
http://\<ip>:<web_port>


---

## Ovládání

Aplikace podporuje pouze povolené příkazy:

| Název | Kód | Volání | Odpověď při úspěchu | Odpověď při chybě |
| :--- | :--- | :--- | :--- | :--- |
| Bank code | BC | BC | BC \<ip\> | ER \<message\> |
| Account create | AC | AC | AC \<account\>/\<ip\> | ER \<message\> |
| Account deposit | AD | AD \<account\>/\<ip\> \<number\> | AD | ER \<message\> |
| Account withdrawal | AW | AW \<account\>/\<ip\> \<number\> | AW | ER \<message\> |
| Account balance | AB | AB \<account\>/\<ip\> | AB \<number\> | ER \<message\> |
| Account remove | AR | AR \<account\>/\<ip\> | AR | ER \<message\> |
| Bank (total) amount | BA | BA | BA \<number\> | ER \<message\> |
| Bank number of clients | BN | BN | BN \<number\> | ER \<message\> |


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

## UI
Součástí projektu je webové rozhraní:
- zobrazení účtů a obecné statistiky  
- možnost bezpečného vypnutí aplikace

---

## Changelog
Viz soubor `CHANGELOG.md`.


