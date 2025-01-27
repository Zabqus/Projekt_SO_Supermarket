# Test skalowania się kas

U mnie liczba K = 5 jeżeli w supermarkiecie będzie więcej niż 5 klientów na jednego kasjera ma się otworzyć
kolejna kasa

```
2025-01-27 18:42:25,045 [INFO] - === STATUS SUPERMARKETU ===
2025-01-27 18:42:25,045 [INFO] - Active cashiers: 3
2025-01-27 18:42:25,045 [INFO] - Kasjer 1: 5 klientów w kolejce
2025-01-27 18:42:25,046 [INFO] - Kasjer 2: 5 klientów w kolejce
2025-01-27 18:42:25,046 [INFO] - Kasjer 9: 5 klientów w kolejce
2025-01-27 18:42:25,046 [INFO] - ========================

2025-01-27 18:42:25,046 [INFO] - Klient 32 wszedł do sklepu
2025-01-27 18:42:25,047 [INFO] - Klient 32 robił zakupy przez 0.52s
2025-01-27 18:42:25,059 [INFO] - Kasjer 9 zakończył obsługiwanie klienta 25
2025-01-27 18:42:25,059 [INFO] - Kasjer 9 obsługiwał klienta 26 przez 4.43s
2025-01-27 18:42:25,564 [INFO] - klient 32 zakończył robienie zakupów
2025-01-27 18:42:25,564 [INFO] - Klient 32 stanał w kolejce 9
2025-01-27 18:42:25,774 [INFO] - Klient 33 wszedł do sklepu
2025-01-27 18:42:25,774 [INFO] - Klient 33 robił zakupy przez 0.85s
2025-01-27 18:42:26,625 [INFO] - klient 33 zakończył robienie zakupów
2025-01-27 18:42:26,626 [INFO] - Klient 33 stanał w kolejce 1
2025-01-27 18:42:26,912 [INFO] - Klient 34 wszedł do sklepu
2025-01-27 18:42:26,912 [INFO] - Klient 34 robił zakupy przez 0.74s
2025-01-27 18:42:27,654 [INFO] - klient 34 zakończył robienie zakupów
2025-01-27 18:42:27,655 [INFO] - Klient 34 stanał w kolejce 2
2025-01-27 18:42:27,931 [INFO] - Klient 35 wszedł do sklepu
2025-01-27 18:42:27,932 [INFO] - Klient 35 robił zakupy przez 0.71s
2025-01-27 18:42:28,568 [INFO] - Kasjer 1 zakończył obsługiwanie klienta 12
2025-01-27 18:42:28,569 [INFO] - Kasjer 1 obsługiwał klienta 15 przez 4.35s
2025-01-27 18:42:28,640 [INFO] - klient 35 zakończył robienie zakupów
2025-01-27 18:42:28,640 [INFO] - Klient 35 stanał w kolejce 1
2025-01-27 18:42:28,924 [INFO] - Klient 36 wszedł do sklepu
2025-01-27 18:42:28,924 [INFO] - Klient 36 robił zakupy przez 0.70s
2025-01-27 18:42:29,255 [INFO] - Kasjer 2 zakończył obsługiwanie klienta 14
2025-01-27 18:42:29,256 [INFO] - Kasjer 2 obsługiwał klienta 17 przez 5.68s
2025-01-27 18:42:29,493 [INFO] - Kasjer 9 zakończył obsługiwanie klienta 26
2025-01-27 18:42:29,493 [INFO] - Kasjer 9 obsługiwał klienta 27 przez 4.46s
2025-01-27 18:42:29,627 [INFO] - klient 36 zakończył robienie zakupów
2025-01-27 18:42:29,627 [INFO] - Klient 36 stanał w kolejce 9
2025-01-27 18:42:29,858 [INFO] - Klient 37 wszedł do sklepu
2025-01-27 18:42:29,858 [INFO] - Klient 37 robił zakupy przez 0.57s
2025-01-27 18:42:30,429 [INFO] - klient 37 zakończył robienie zakupów
2025-01-27 18:42:30,430 [INFO] - Klient 37 stanał w kolejce 2
2025-01-27 18:42:30,713 [INFO] - Klient 38 wszedł do sklepu
2025-01-27 18:42:30,713 [INFO] - Klient 38 robił zakupy przez 0.77s
2025-01-27 18:42:31,487 [INFO] - klient 38 zakończył robienie zakupów
2025-01-27 18:42:31,487 [INFO] - Klient 38 stanał w kolejce 9
2025-01-27 18:42:31,537 [INFO] - Kasjer 5 zaczął pracę
2025-01-27 18:42:31,775 [INFO] - Klient 39 wszedł do sklepu
2025-01-27 18:42:31,776 [INFO] - Klient 39 robił zakupy przez 0.91s
2025-01-27 18:42:32,685 [INFO] - klient 39 zakończył robienie zakupów
2025-01-27 18:42:32,687 [INFO] - Klient 39 stanał w kolejce 5
2025-01-27 18:42:32,688 [INFO] - Kasjer 5 obsługiwał klienta 39 przez 5.30s
2025-01-27 18:42:32,925 [INFO] - Kasjer 1 zakończył obsługiwanie klienta 15
2025-01-27 18:42:32,925 [INFO] - Kasjer 1 obsługiwał klienta 16 przez 4.58s
2025-01-27 18:42:32,959 [INFO] - Klient 40 wszedł do sklepu
2025-01-27 18:42:32,959 [INFO] - Klient 40 robił zakupy przez 0.62s
2025-01-27 18:42:33,582 [INFO] - klient 40 zakończył robienie zakupów
2025-01-27 18:42:33,583 [INFO] - Klient 40 stanał w kolejce 5
2025-01-27 18:42:33,791 [INFO] - Klient 41 wszedł do sklepu
2025-01-27 18:42:33,792 [INFO] - Klient 41 robił zakupy przez 0.61s
2025-01-27 18:42:33,960 [INFO] - Kasjer 9 zakończył obsługiwanie klienta 27
2025-01-27 18:42:33,960 [INFO] - Kasjer 9 obsługiwał klienta 28 przez 4.90s
2025-01-27 18:42:34,408 [INFO] - klient 41 zakończył robienie zakupów
2025-01-27 18:42:34,408 [INFO] - Klient 41 stanał w kolejce 5
2025-01-27 18:42:34,612 [INFO] - Klient 42 wszedł do sklepu
2025-01-27 18:42:34,613 [INFO] - Klient 42 robił zakupy przez 0.98s
2025-01-27 18:42:34,938 [INFO] - Kasjer 2 zakończył obsługiwanie klienta 17
2025-01-27 18:42:34,939 [INFO] - Kasjer 2 obsługiwał klienta 18 przez 4.24s
2025-01-27 18:42:35,592 [INFO] - klient 42 zakończył robienie zakupów
2025-01-27 18:42:35,592 [INFO] - Klient 42 stanał w kolejce 5
2025-01-27 18:42:35,814 [INFO] - === STATUS SUPERMARKETU ===
2025-01-27 18:42:35,814 [INFO] - Active cashiers: 4
2025-01-27 18:42:35,814 [INFO] - Kasjer 1: 5 klientów w kolejce
2025-01-27 18:42:35,815 [INFO] - Kasjer 2: 5 klientów w kolejce
2025-01-27 18:42:35,815 [INFO] - Kasjer 5: 3 klientów w kolejce
2025-01-27 18:42:35,815 [INFO] - Kasjer 9: 5 klientów w kolejce
2025-01-27 18:42:35,815 [INFO] - ========================


```

Jak widzimy przy większej częstowliwości przychodzenia klientów do sklepu kasy otwierają się zgodnie
zgodnie z założeniem

## Test przebiegł pomyślnie 