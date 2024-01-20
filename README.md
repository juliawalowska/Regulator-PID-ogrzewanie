# Systemy Mikroprocesorowe

## Politechnika Poznańska, Instytut Automatyki, Robotyki i Elektrotechniki

<p align="center">
  <img width="180" height="180" src="/img/logo_WARiE.png">
</p>

# **Projekt zaliczeniowy: Regulator-PID-ogrzewanie**

## Zadanie

Celem zadania jest zbudowanie Układu automatycznej regulacji temperatury w oparciu o:
  - płytkę NUCLEO 144
  - regulator PID
  - [rezystor 39](https://sklep.avt.pl/pl/products/rezystor-39-om-5w-5-178694.html?query_id=3)
  - [czujnik BMP280](https://sklep.avt.pl/pl/products/czujnik-cisnienia-i-temperatury-gy-bmp280-v3-3-barometr-na-i2c-do-arduino-174322.html?fbclid=IwAR3qwK_G8U1rsmJfZRh1Xn7Wu_qn47saH4UUeBxF370ZbXj3NWw9wSBMs8s)

Dodatkowe elementy wykorzystane w budowaniu układu:
  - enkoder
  - wyświetlacz led
  - zasilacz

Oprócz tego wykorzystano podstawowe elementy takie jak:
  - przewody
  - płytka stykowa
  - rezystory

## Wykonanie zadania

### Budowa układu w programie KiCad

Przed połączeniem układu i w celu utworzenia dokumentacji połączeń wykorzystano program KiCad.

### Analiza modelu regulatora

Analize wykonano za pomocą obliczeń analitycznych:

--------- miejsce na opis procesu i zdjęcia ----------

Niestety ze względu na za wysoki stopień mianownika względem parametrów regulatora nie udało się ulokować biegunów. Doboru nastaw dokonano metodą prób i błedów.


### Konfiguracja ioc

Do wykonania zadania konieczna była konfiguracja ioc. Kluczowe dokonane zmiany:

#### Konfiguracja ETH
Wyłączono funkcję komunikacji po ETH.

#### Konfiguracja USART
Moduł NUCLEO komunikuje się z czujnikiem poprzez moduł USART, konieczne było skonfigurowanie go w ioc:

#### Konfiguracja wejść i wyjść
Dodatkowymi elementami załączonymi w projekcie były: enkoder, wyświetlacz LED. Skonfigurowano wyjścia zgodnie ze zdjęciami zamieszczonymi poniżej:


### Kod

Kod wgrany do Nucleo został umieszczony w plikach remozytorium w folderze projektu. Opiera się on o konfigurację komunikacji z czujnikiem oraz implementację kontrolera PID. Zawiera odczyt z enkodera wartości zadanej oraz obsługę wyświetlacza LED.

### GUI

Zadanniem GUI jest obrazowanie w czasie rzeczywistym temperatury odczytanej przez czujnik oraz prezentowanie danych na wykresie z zanaczoną wartościa zadaną oraz 5% odchyłami.

### Połączony układ

--------- miejsce na  zdjęcia ----------

### Obudowa na układ

Obudowę na układ zaprojektowano w programie SolidWorks, po czym wydrukowano na drukarce 3D.
