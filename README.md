# Symulator Supermarketu

## Założenia projektowe i ich implementacja
* [Obsługa 10 kas w supermarkecie](https://github.com/Zabqus/Projekt_SO_Supermarket/blob/0d718678fbb74900258496da1f02f016a735af3e/utils/config.py#L3)
* [Minimum 2 czynne stanowiska kasowe](https://github.com/Zabqus/Projekt_SO_Supermarket/blob/0d718678fbb74900258496da1f02f016a735af3e/utils/config.py#L4)
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
* [Kolorowanie komunikatów alarmowych](https://github.com/Zabqus/Projekt_SO_Supermarket/blob/0d718678fbb74900258496da1f02f016a735af3e/src/guard.py#L27)
* [Status supermarketu](https://github.com/Zabqus/Projekt_SO_Supermarket/blob/0d718678fbb74900258496da1f02f016a735af3e/src/supermarket.py#L79-L91)

### System synchronizacji
* [Synchronizacja kolejek przez QueueManager](https://github.com/Zabqus/Projekt_SO_Supermarket/blob/0d718678fbb74900258496da1f02f016a735af3e/utils/queue_manager.py#L8-L15)
* [Koordynacja ewakuacji](https://github.com/Zabqus/Projekt_SO_Supermarket/blob/0d718678fbb74900258496da1f02f016a735af3e/src/guard.py#L57-L66)
* [Zarządzanie stanem supermarketu](https://github.com/Zabqus/Projekt_SO_Supermarket/blob/0d718678fbb74900258496da1f02f016a735af3e/src/supermarket.py#L186-L214)



## Zrealizowane wymagania projektowe

### Zadania na plikach
* [Tworzenie plików logów](https://github.com/Zabqus/Projekt_SO_Supermarket/blob/339a51290f27abf29f109b0331b38bdc32b10816/utils/logging_config.py#L25)
* [Sprawdzanie oraz tworzenie katalogu](https://github.com/Zabqus/Projekt_SO_Supermarket/blob/339a51290f27abf29f109b0331b38bdc32b10816/utils/logging_config.py#L10-L11)


### Tworzenie procesów
* [Inicjalizacja procesów kasjerów](https://github.com/Zabqus/Projekt_SO_Supermarket/blob/0d718678fbb74900258496da1f02f016a735af3e/src/supermarket.py#L11-L16)
* [Zarządzanie cyklem życia procesów](https://github.com/Zabqus/Projekt_SO_Supermarket/blob/0d718678fbb74900258496da1f02f016a735af3e/src/cashier.py#L4-L25)

### Tworzenie i obsługa wątków
* [Implementacja wątków klientów](https://github.com/Zabqus/Projekt_SO_Supermarket/blob/0d718678fbb74900258496da1f02f016a735af3e/src/customer.py#L7-L9)
* [Implementacja wątku strażnika](https://github.com/Zabqus/Projekt_SO_Supermarket/blob/0d718678fbb74900258496da1f02f016a735af3e/src/guard.py#L12-L16)

### Obsługa sygnałów
* [Użyte sygnały](https://github.com/Zabqus/Projekt_SO_Supermarket/blob/18db270dd300c31509b4568f359e81e89bc587ec/src/main.py#L20-L23)
* [Wywołanie sygnałów](https://github.com/Zabqus/Projekt_SO_Supermarket/blob/18db270dd300c31509b4568f359e81e89bc587ec/utils/signal_handler.py#L11-L18)

### Synchronizacja procesów
* [Semafory](https://github.com/Zabqus/Projekt_SO_Supermarket/blob/0d718678fbb74900258496da1f02f016a735af3e/src/cashier.py#L22-L23)
* [Eventy](https://github.com/Zabqus/Projekt_SO_Supermarket/blob/0d718678fbb74900258496da1f02f016a735af3e/src/customer.py#L12)

### Kolejki komunikatów
* [Tworzenie kolejek](https://github.com/Zabqus/Projekt_SO_Supermarket/blob/0d718678fbb74900258496da1f02f016a735af3e/utils/queue_manager.py#L16)
* [Operacje na kolejkach](https://github.com/Zabqus/Projekt_SO_Supermarket/blob/0d718678fbb74900258496da1f02f016a735af3e/utils/queue_manager.py#L29)
* [Zarządzanie kolejkami](https://github.com/Zabqus/Projekt_SO_Supermarket/blob/0d718678fbb74900258496da1f02f016a735af3e/utils/queue_manager.py#L43-L51)

### Własne moduły 
  * [Definicja głównych komponentów systemu](https://github.com/Zabqus/Projekt_SO_Supermarket/blob/0d718678fbb74900258496da1f02f016a735af3e/src/__init__.py#L1-L4)
  * [Moduł konfiguracji parametrów](https://github.com/Zabqus/Projekt_SO_Supermarket/blob/0d718678fbb74900258496da1f02f016a735af3e/utils/config.py#L1-L7)


## Testy jednostkowe

### Test skalowania kas


### [Test ewakuacji]((https://github.com/Zabqus/Projekt_SO_Supermarket/blob/9f9ecfda851714d1481baaed39a4d6b4f002cea7/tests/test_evacuation.md))



### [Test minimalnej liczby kas](https://github.com/Zabqus/Projekt_SO_Supermarket/blob/9f9ecfda851714d1481baaed39a4d6b4f002cea7/tests/test_min_cashier.md)


