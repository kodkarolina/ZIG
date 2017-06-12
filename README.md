# ZIG - System RCP
Projekt aplikacji serwerowej systemu rejestracji czasu pracy, realizowany jest w ramach kursu zastosowanie informatyki w gospodarce.

Projekt został stworzony w języku Python w wersji 3.6.0 z wykorzystaniem microframeworka Flask w wersji 0.12.1.

## Instalacja i konfiguracja
Aby uruchomić serwer systemu RCP należy przejść kilka prostych kroków:
1) Pobieramy repozytorium
2) Następnie należy skonfigurować serwer. Konfiguracja znajduje się w pliku `App\config.py.dist`
* Zmieniamy nazwę pliku z `config.py.dist` na `config.py`
* W pliku 'config.py' uzupełniamy dane dotyczące bazy danych, nazwę serwera oraz port, na którym serwer ma działać.
3) Uruchamiamy skrypt `installScript`, który pobierze odpwoiednie biblioteki, zainicjalizuje tabele w bazie danych, a następnie wystartuje serwer

## Uruchomienie serwera
Serwer należy uruchamiać poprzez wywołanie skryptu `server_start.bat`.
