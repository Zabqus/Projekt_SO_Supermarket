# Symulator Supermarketu

### Wiktor Ząbek 
### 151947
### Informatyka niestacjonarna semestr III

## Opis projektu - Temat 10
W pewnym supermarkecie jest łącznie 10 kas. Zasady ich działania przyjęte przez kierownika sklepu 
są następujące:  
• Zawsze działają min. 2 stanowiska kasowe. 

• Na każdych K klientów znajdujących się na terenie supermarketu powinno przypadać min. 1 
czynne stanowisko kasowe.  

• Jeśli liczba klientów jest mniejsza niż K*(N-1), gdzie N oznacza liczbę czynnych kas, to jedna 
z kas zostaje zamknięta. 

• Jeśli w kolejce do kasy czekali klienci (przed ogłoszeniem decyzji o jej zamknięciu) to powinni 
zostać obsłużeni przez tę kasę. 

Klienci przychodzą do supermarketu w losowych momentach czasu i przebywają w nim przez pewien 
określony losowy dla każdego z nich czas. 

Na sygnał o pożarze – który jest wysyłany przez strażaka - klienci 
natychmiast opuszczają supermarket bez robienia zakupów, a następnie po wyjściu klientów 
zamykane są wszystkie kasy.

## Założenia projektowe i ich implementacja
* [Obsługa 10 kas w supermarkecie](https://github.com/Zabqus/Projekt_SO_Supermarket/blob/0d718678fbb74900258496da1f02f016a735af3e/utils/config.py#L3)
* [Minimum 2 czynne stanowiska kasowe](https://github.com/Zabqus/Projekt_SO_Supermarket/blob/0d718678fbb74900258496da1f02f016a735af3e/utils/config.py#L4)
* [Obsługa klientów przed zamknięciem kasy](https://github.com/Zabqus/Projekt_SO_Supermarket/blob/92c8d90e57c55f8895bf7821245a6a42acbe6a39/src/cashier.py#L15-L27)
* [Ewakuacja w przypadku pożaru](https://github.com/Zabqus/Projekt_SO_Supermarket/blob/92c8d90e57c55f8895bf7821245a6a42acbe6a39/src/customer.py#L21-L24)

## Główne funkcjonalności i mechanizmy

### System zarządzania supermarketem
* [Dynamiczne zarządzanie kasami (2-10 kas)](https://github.com/Zabqus/Projekt_SO_Supermarket/blob/7f297763f5a80f0d03e80e86193d67e3f4c013fa/src/supermarket.py#L102)
* [System zarządzania kolejkami klientów](https://github.com/Zabqus/Projekt_SO_Supermarket/blob/575eecde4c21667d9458098204af5a6212017031/src/customer.py#L56)

### Procesy i wątki
* [Implementacja procesów kasjerów](https://github.com/Zabqus/Projekt_SO_Supermarket/blob/0d718678fbb74900258496da1f02f016a735af3e/src/cashier.py#L4-L25)
* [Implementacja wątku strażnika](https://github.com/Zabqus/Projekt_SO_Supermarket/blob/0d718678fbb74900258496da1f02f016a735af3e/src/guard.py#L10-L24)
* [Zarządzanie klientami](https://github.com/Zabqus/Projekt_SO_Supermarket/blob/0d718678fbb74900258496da1f02f016a735af3e/src/customer.py#L1-L32)

### System bezpieczeństwa
* [Obsługa sytuacji awaryjnych (alarm pożarowy)](https://github.com/Zabqus/Projekt_SO_Supermarket/blob/0d718678fbb74900258496da1f02f016a735af3e/src/guard.py#L26-L47)
* [System ewakuacji klientów](https://github.com/Zabqus/Projekt_SO_Supermarket/blob/0d718678fbb74900258496da1f02f016a735af3e/src/guard.py#L57-L66)
* [Obsługa sygnałów systemowych](https://github.com/Zabqus/Projekt_SO_Supermarket/blob/7f297763f5a80f0d03e80e86193d67e3f4c013fa/utils/signal_system.py#L7)


### System kolorowych komunikatów

* [Kolorowanie komunikatów alarmowych](https://github.com/Zabqus/Projekt_SO_Supermarket/blob/92c8d90e57c55f8895bf7821245a6a42acbe6a39/src/guard.py#L9-L11)
* [Status supermarketu](https://github.com/Zabqus/Projekt_SO_Supermarket/blob/92c8d90e57c55f8895bf7821245a6a42acbe6a39/src/supermarket.py#L61-L71)

### System synchronizacji
* [Współdzielona kolejka klientów](https://github.com/Zabqus/Projekt_SO_Supermarket/blob/92c8d90e57c55f8895bf7821245a6a42acbe6a39/utils/shared_memory_queue.py#L16-L18)
* [Synchronizacja procesów kasjerów](https://github.com/Zabqus/Projekt_SO_Supermarket/blob/575eecde4c21667d9458098204af5a6212017031/src/supermarket.py#L52-L59)




## Zrealizowane wymagania projektowe

### Zadania na plikach
* [Tworzenie plików logów](https://github.com/Zabqus/Projekt_SO_Supermarket/blob/92c8d90e57c55f8895bf7821245a6a42acbe6a39/utils/logging_config.py#L14-L19)
* [Sprawdzanie oraz tworzenie katalogu](https://github.com/Zabqus/Projekt_SO_Supermarket/blob/92c8d90e57c55f8895bf7821245a6a42acbe6a39/utils/logging_config.py#L8-L13)


### Tworzenie procesów
* [Inicjalizacja procesów kasjerów](https://github.com/Zabqus/Projekt_SO_Supermarket/blob/92c8d90e57c55f8895bf7821245a6a42acbe6a39/src/supermarket.py#L49-L59)

### Tworzenie i obsługa wątków
* [Implementacja wątków klientów](https://github.com/Zabqus/Projekt_SO_Supermarket/blob/92c8d90e57c55f8895bf7821245a6a42acbe6a39/src/customer.py#L9-L15)
* [Implementacja wątku strażnika](https://github.com/Zabqus/Projekt_SO_Supermarket/blob/0d718678fbb74900258496da1f02f016a735af3e/src/guard.py#L12-L16)

### Obsługa sygnałów
* [Użyte sygnały](https://github.com/Zabqus/Projekt_SO_Supermarket/blob/92c8d90e57c55f8895bf7821245a6a42acbe6a39/utils/signal_system.py#L11-L13)
* [Wywołanie sygnałów](https://github.com/Zabqus/Projekt_SO_Supermarket/blob/7f297763f5a80f0d03e80e86193d67e3f4c013fa/utils/signal_system.py#L41)

### Pamięć współdzelona
* [Utworzenie pliku w pamięcu współdzielonej](https://github.com/Zabqus/Projekt_SO_Supermarket/blob/92c8d90e57c55f8895bf7821245a6a42acbe6a39/utils/shared_memory_queue.py#L16-L18)
* [Operacje na pamięci](https://github.com/Zabqus/Projekt_SO_Supermarket/blob/575eecde4c21667d9458098204af5a6212017031/utils/shared_memory_queue.py#L20-L33)

## Co udało się zrobić
 
- Implementacja głównych komponentów: supermarketu, kas, klientów i ochrony z wykorzystaniem procesów i wątków.
- Realizacja dynamicznego zarządzania kasami w oparciu o długość kolejki klientów 
- Obsługa komunikacji międzyprocesowej poprzez pamięć współdzieloną (mmap) i potoki (pipe).
- System sygnałów do obsługi pożaru 
- Logowanie zdarzeń do plików
- System synchronizacji między procesami z użyciem pamięci współdzielonej i sygnałów.

## Napotkane problemy: 
- Problem z ewakuacją - kasjerzy obsługiwali klientów podczas ewakuacji 
- Komunikacja pomiędzy procesami
- Poprawne zakończenie ewakuacji 



## Testy jednostkowe

### [Test skalowania kas](https://github.com/Zabqus/Projekt_SO_Supermarket/blob/4902f536af702d3350180eeeb0906dcf453288dc/tests/Test_scaling.md)


### [Test ewakuacji](https://github.com/Zabqus/Projekt_SO_Supermarket/blob/9f9ecfda851714d1481baaed39a4d6b4f002cea7/tests/test_evacuation.md)


### [Test minimalnej liczby kas](https://github.com/Zabqus/Projekt_SO_Supermarket/blob/9f9ecfda851714d1481baaed39a4d6b4f002cea7/tests/test_min_cashier.md)

### [Test obsługi klientów przy zamykaniu się kasy](https://github.com/Zabqus/Projekt_SO_Supermarket/blob/92c8d90e57c55f8895bf7821245a6a42acbe6a39/tests/test_register_closing.md)
