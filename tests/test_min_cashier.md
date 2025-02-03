# Test minimalnej ilości kasjerów

Zakładamy, że zawsze mają być otwarte dwie kasy

Ustawiamy krótki czas obsługi klienta oraz małą częstotliwość przychodzenia klientów do sklepu

W efekcie otrzymujemy następujący wynik:

```
2025-01-27 18:22:37,833 [INFO] - Klient 270 wszedł do sklepu
2025-01-27 18:22:37,833 [INFO] - Klient 270 robił zakupy przez 0.55s
2025-01-27 18:22:38,384 [INFO] - klient 270 zakończył robienie zakupów
2025-01-27 18:22:38,384 [INFO] - Klient 270 stanał w kolejce 1
2025-01-27 18:22:38,477 [INFO] - Kasjer 2 zakończył obsługiwanie klienta 269
2025-01-27 18:22:40,610 [INFO] - Kasjer 1 zakończył obsługiwanie klienta 268
2025-01-27 18:22:40,610 [INFO] - Kasjer 1 obsługiwał klienta 270 przez 8.36s
2025-01-27 18:22:42,583 [INFO] - Klient 271 wszedł do sklepu
2025-01-27 18:22:42,583 [INFO] - Klient 271 robił zakupy przez 0.56s
2025-01-27 18:22:43,140 [INFO] - klient 271 zakończył robienie zakupów
2025-01-27 18:22:43,141 [INFO] - Klient 271 stanał w kolejce 1
2025-01-27 18:22:48,133 [INFO] - === STATUS SUPERMARKETU ===
2025-01-27 18:22:48,133 [INFO] - Aktywne kasy: 2
2025-01-27 18:22:48,134 [INFO] - Kasjer 1: 1 klientów w kolejce
2025-01-27 18:22:48,134 [INFO] - Kasjer 2: 0 klientów w kolejce
2025-01-27 18:22:48,134 [INFO] - ========================

```


Ponad to zawsze przy otwarciu sklepu dostajemy informację: 

```
2025-01-29 16:29:15,730 [INFO] - Przygotowanie 2 kasjerów do otwarcia
2025-01-29 16:29:15,731 [INFO] - Otwarcie supermarketu
2025-01-29 16:29:15,732 [INFO] - Klient 1 wszedł do sklepu
2025-01-29 16:29:15,733 [INFO] - Klient 1 robi zakupy przez 0.66s
2025-01-29 16:29:15,736 [INFO] - Kasjer 1 rozpoczyna pracę
2025-01-29 16:29:15,736 [INFO] - Kasjer 2 rozpoczyna pracę
2025-01-29 16:29:16,403 [INFO] - Klient 1 zakończył zakupy
2025-01-29 16:29:16,404 [INFO] - Klient 1 stanął w kolejce

```


