# Symulator Supermarketu

## Założenia projektowe i ich implementacja
* [Obsługa 10 kas w supermarkecie](https://github.com/Zabqus/Projekt_SO_Supermarket/blob/0d718678fbb74900258496da1f02f016a735af3e/utils/config.py#L3)
* [Minimum 2 czynne stanowiska kasowe](https://github.com/Zabqus/Projekt_SO_Supermarket/blob/0d718678fbb74900258496da1f02f016a735af3e/utils/config.py#L4)
* [Dynamiczne skalowanie kas w zależności od liczby klientów](https://github.com/Zabqus/Projekt_SO_Supermarket/blob/0d718678fbb74900258496da1f02f016a735af3e/src/supermarket.py#L136-L149)
* [Obsługa klientów przed zamknięciem kasy](https://github.com/Zabqus/Projekt_SO_Supermarket/blob/0d718678fbb74900258496da1f02f016a735af3e/src/supermarket.py#L151-L155)
* [Ewakuacja w przypadku pożaru](https://github.com/Zabqus/Projekt_SO_Supermarket/blob/0d718678fbb74900258496da1f02f016a735af3e/src/guard.py#L26-L47)

## Główne funkcjonalności i mechanizmy

### System zarządzania supermarketem
* [Dynamiczne zarządzanie kasami (2-10 kas)](https://github.com/Zabqus/Projekt_SO_Supermarket/blob/0d718678fbb74900258496da1f02f016a735af3e/src/supermarket.py#L71-L97)
* [Automatyczne skalowanie liczby kas w zależności od liczby klientów](https://github.com/Zabqus/Projekt_SO_Supermarket/blob/0d718678fbb74900258496da1f02f016a735af3e/src/supermarket.py#L136-L149)
* [System zarządzania kolejkami klientów](https://github.com/Zabqus/Projekt_SO_Supermarket/blob/0d718678fbb74900258496da1f02f016a735af3e/utils/queue_manager.py#L1-L64)

### Procesy i wątki
* [Implementacja procesów kasjerów](https://github.com/Zabqus/Projekt_SO_Supermarket/blob/0d718678fbb74900258496da1f02f016a735af3e/src/cashier.py#L4-L25)
* [Implementacja wątku strażnika](https://github.com/Zabqus/Projekt_SO_Supermarket/blob/0d718678fbb74900258496da1f02f016a735af3e/src/guard.py#L10-L24)
* [Zarządzanie klientami](https://github.com/Zabqus/Projekt_SO_Supermarket/blob/0d718678fbb74900258496da1f02f016a735af3e/src/customer.py#L1-L32)

### System bezpieczeństwa
* [Obsługa sytuacji awaryjnych (alarm pożarowy)](https://github.com/Zabqus/Projekt_SO_Supermarket/blob/0d718678fbb74900258496da1f02f016a735af3e/src/guard.py#L26-L47)
* [System ewakuacji klientów](https://github.com/Zabqus/Projekt_SO_Supermarket/blob/0d718678fbb74900258496da1f02f016a735af3e/src/guard.py#L57-L66)
* [Obsługa sygnałów systemowych](https://github.com/Zabqus/Projekt_SO_Supermarket/blob/0d718678fbb74900258496da1f02f016a735af3e/utils/signal_handler.py#L5-L24)

## Wyróżniające elementy projektu

### System kolorowych komunikatów
Implementacja zaawansowanego systemu kolorowych komunikatów w logach dla lepszej czytelności:
* [Definicje kolorów](https://github.com/Zabqus/Projekt_SO_Supermarket/blob/0d718678fbb74900258496da1f02f016a735af3e/src/guard.py#L7-L9)
* [Kolorowanie komunikatów alarmowych](https://github.com/Zabqus/Projekt_SO_Supermarket/blob/0d718678fbb74900258496da1f02f016a735af3e/src/guard.py#L27)
* [Status supermarketu](https://github.com/Zabqus/Projekt_SO_Supermarket/blob/0d718678fbb74900258496da1f02f016a735af3e/src/supermarket.py#L79-L91)

### System synchronizacji
* [Synchronizacja kolejek przez QueueManager](https://github.com/Zabqus/Projekt_SO_Supermarket/blob/0d718678fbb74900258496da1f02f016a735af3e/utils/queue_manager.py#L8-L15)
* [Koordynacja ewakuacji](https://github.com/Zabqus/Projekt_SO_Supermarket/blob/0d718678fbb74900258496da1f02f016a735af3e/src/guard.py#L57-L66)
* [Zarządzanie stanem supermarketu](https://github.com/Zabqus/Projekt_SO_Supermarket/blob/0d718678fbb74900258496da1f02f016a735af3e/src/supermarket.py#L186-L214)

## Testy jednostkowe

### Test skalowania kas
* [test_cashier_scaling](https://github.com/Zabqus/Projekt_SO_Supermarket/blob/0d718678fbb74900258496da1f02f016a735af3e/tests/test_cashier_scaling.py)
  - Weryfikacja dynamicznego skalowania liczby kas
  - Sprawdzenie minimalnej liczby aktywnych kas
  - Test automatycznego zamykania kas przy małym obciążeniu

### Test ewakuacji
* [test_evacuation](https://github.com/Zabqus/Projekt_SO_Supermarket/blob/18db270dd300c31509b4568f359e81e89bc587ec/tests/test_evacuation.py)
  - Sprawdzenie procedury ewakuacji
  - Weryfikacja czyszczenia kolejek
  - Test stanu supermarketu po ewakuacji

### Test stanu początkowego
* [test_initial_state](https://github.com/Zabqus/Projekt_SO_Supermarket/blob/0d718678fbb74900258496da1f02f016a735af3e/tests/test_initial_state.py)
  - Weryfikacja początkowej konfiguracji
  - Sprawdzenie domyślnych wartości
  - Test aktywnych kas na starcie

### Test minimalnej liczby kas
* [test_min_cashiers](https://github.com/Zabqus/Projekt_SO_Supermarket/blob/18db270dd300c31509b4568f359e81e89bc587ec/tests/test_min_cashiers.py)
  - Weryfikacja utrzymania minimalnej liczby kas
  - Test mechanizmu automatycznego otwierania kas

### Test działania bez opóźnień
* [test_supermarket_no_sleep](https://github.com/Zabqus/Projekt_SO_Supermarket/blob/18db270dd300c31509b4568f359e81e89bc587ec/tests/test_no_sleep.py)
  - Test funkcjonalności bez rzeczywistych opóźnień czasowych
  - Sprawdzenie logiki biznesowej w przyspieszonym trybie
  - Weryfikacja stanu po restarcie systemu

## Zrealizowane wymagania projektowe

### a. Zadania na plikach
* [Tworzenie plików logów](https://github.com/Zabqus/Projekt_SO_Supermarket/blob/0d718678fbb74900258496da1f02f016a735af3e/utils/logging_config.py#L7-L15)
* [Obsługa zapisu do plików](https://github.com/Zabqus/Projekt_SO_Supermarket/blob/0d718678fbb74900258496da1f02f016a735af3e/utils/logging_config.py#L17-L33)

### b. Tworzenie procesów
* [Inicjalizacja procesów kasjerów](https://github.com/Zabqus/Projekt_SO_Supermarket/blob/0d718678fbb74900258496da1f02f016a735af3e/src/supermarket.py#L71-L77)
* [Zarządzanie cyklem życia procesów](https://github.com/Zabqus/Projekt_SO_Supermarket/blob/0d718678fbb74900258496da1f02f016a735af3e/src/cashier.py#L4-L25)

### c. Tworzenie i obsługa wątków
* [Implementacja wątków klientów](https://github.com/Zabqus/Projekt_SO_Supermarket/blob/0d718678fbb74900258496da1f02f016a735af3e/src/customer.py#L1-L32)
* [Implementacja wątku strażnika](https://github.com/Zabqus/Projekt_SO_Supermarket/blob/0d718678fbb74900258496da1f02f016a735af3e/src/guard.py#L10-L24)

### d. Obsługa sygnałów
* [Definicja handlera sygnałów](https://github.com/Zabqus/Projekt_SO_Supermarket/blob/0d718678fbb74900258496da1f02f016a735af3e/utils/signal_handler.py#L5-L24)
* [Konfiguracja obsługi sygnałów](https://github.com/Zabqus/Projekt_SO_Supermarket/blob/18db270dd300c31509b4568f359e81e89bc587ec/src/main.py#L20-L23)

### h. Kolejki komunikatów
* [Implementacja menedżera kolejek](https://github.com/Zabqus/Projekt_SO_Supermarket/blob/0d718678fbb74900258496da1f02f016a735af3e/utils/queue_manager.py#L1-L64)
* [Obsługa kolejek w supermarkecie](https://github.com/Zabqus/Projekt_SO_Supermarket/blob/0d718678fbb74900258496da1f02f016a735af3e/src/supermarket.py#L24-L25)


# Spełnione kryteria projektowe:

- **Tworzenie i obsługa procesów/wątków**
  * [Proces kasjera dziedziczący po Process](https://github.com/Zabqus/Projekt_SO_Supermarket/blob/0d718678fbb74900258496da1f02f016a735af3e/src/cashier.py#L5-L12)
  * [Wątek klienta i jego zachowanie](https://github.com/Zabqus/Projekt_SO_Supermarket/blob/0d718678fbb74900258496da1f02f016a735af3e/src/customer.py#L5-L15)
  * [Wątek strażnika monitorujący sytuacje awaryjne](https://github.com/Zabqus/Projekt_SO_Supermarket/blob/0d718678fbb74900258496da1f02f016a735af3e/src/guard.py#L12-L24)

- **Systemowe mechanizmy synchronizacji**
  * [Lock do synchronizacji dostępu do kolejek](https://github.com/Zabqus/Projekt_SO_Supermarket/blob/0d718678fbb74900258496da1f02f016a735af3e/utils/queue_manager.py#L8-L11)
  * [Mechanizm Event do koordynacji ewakuacji](https://github.com/Zabqus/Projekt_SO_Supermarket/blob/0d718678fbb74900258496da1f02f016a735af3e/src/guard.py#L31-L35)

- **Obsługa sygnałów**
  * [Definicje handlerów dla SIGINT i SIGUSR1](https://github.com/Zabqus/Projekt_SO_Supermarket/blob/0d718678fbb74900258496da1f02f016a735af3e/utils/signal_handler.py#L11-L19)
  * [Konfiguracja sygnałów w programie](https://github.com/Zabqus/Projekt_SO_Supermarket/blob/18db270dd300c31509b4568f359e81e89bc587ec/src/main.py#L20-L23)

- **Własne moduły**
  * [Definicja głównych komponentów systemu](https://github.com/Zabqus/Projekt_SO_Supermarket/blob/0d718678fbb74900258496da1f02f016a735af3e/src/__init__.py#L1-L4)
  * [Moduł konfiguracji parametrów](https://github.com/Zabqus/Projekt_SO_Supermarket/blob/0d718678fbb74900258496da1f02f016a735af3e/utils/config.py#L1-L7)
  * [Moduł logowania z formatowaniem](https://github.com/Zabqus/Projekt_SO_Supermarket/blob/0d718678fbb74900258496da1f02f016a735af3e/utils/logging_config.py#L17-L28)

- **Wyjątki i obsługa błędów**
  * [Obsługa wyjątków podczas operacji na kolejkach](https://github.com/Zabqus/Projekt_SO_Supermarket/blob/0d718678fbb74900258496da1f02f016a735af3e/utils/queue_manager.py#L48-L55)
  * [Obsługa błędów podczas zamykania kas](https://github.com/Zabqus/Projekt_SO_Supermarket/blob/0d718678fbb74900258496da1f02f016a735af3e/src/supermarket.py#L196-L201)