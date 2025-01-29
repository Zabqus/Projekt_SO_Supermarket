# Test skalowania się kas

- Na każdych K klientów znajdujących się na terenie supermarketu powinno przypadać min. 1 
czynne stanowisko kasowe.  
- Jeśli liczba klientów jest mniejsza niż K*(N-1), gdzie N oznacza liczbę czynnych kas, to jedna 
z kas zostaje zamknięta. 

U mnie liczba K = 5 więc jeżeli w supermarkiecie będzie więcej niż 5 klientów na jednego kasjera ma się otworzyć
kolejna kasa

```
2025-01-29 16:33:58,827 [INFO] - === STATUS SUPERMARKETU ===
2025-01-29 16:33:58,827 [INFO] - Aktywne kasy: 2
2025-01-29 16:33:58,827 [INFO] - Liczba klientów w kolejce: 6
2025-01-29 16:33:58,827 [INFO] - ========================

2025-01-29 16:33:58,828 [INFO] - Klient 11 wszedł do sklepu
2025-01-29 16:33:58,828 [INFO] - Klient 11 robi zakupy przez 0.78s
2025-01-29 16:33:59,249 [INFO] - Kasjer 2 zakończył obsługę klienta 3
2025-01-29 16:33:59,249 [INFO] - Kasjer 2 obsługuje klienta 5 przez 4.63s
2025-01-29 16:33:59,565 [INFO] - Kasjer 1 zakończył obsługę klienta 4
2025-01-29 16:33:59,565 [INFO] - Kasjer 1 obsługuje klienta 6 przez 4.49s
2025-01-29 16:33:59,605 [INFO] - Klient 11 zakończył zakupy
2025-01-29 16:33:59,605 [INFO] - Klient 11 stanął w kolejce
2025-01-29 16:33:59,952 [INFO] - Klient 12 wszedł do sklepu
2025-01-29 16:33:59,953 [INFO] - Klient 12 robi zakupy przez 0.72s
2025-01-29 16:34:00,676 [INFO] - Klient 12 zakończył zakupy
2025-01-29 16:34:00,676 [INFO] - Klient 12 stanął w kolejce
2025-01-29 16:34:01,077 [INFO] - Klient 13 wszedł do sklepu
2025-01-29 16:34:01,077 [INFO] - Klient 13 robi zakupy przez 0.69s
2025-01-29 16:34:01,773 [INFO] - Klient 13 zakończył zakupy
2025-01-29 16:34:01,773 [INFO] - Klient 13 stanął w kolejce
2025-01-29 16:34:02,090 [INFO] - Klient 14 wszedł do sklepu
2025-01-29 16:34:02,090 [INFO] - Klient 14 robi zakupy przez 0.55s
2025-01-29 16:34:02,638 [INFO] - Klient 14 zakończył zakupy
2025-01-29 16:34:02,638 [INFO] - Klient 14 stanął w kolejce
2025-01-29 16:34:02,945 [INFO] - Klient 15 wszedł do sklepu
2025-01-29 16:34:02,946 [INFO] - Klient 15 robi zakupy przez 0.50s
2025-01-29 16:34:03,446 [INFO] - Klient 15 zakończył zakupy
2025-01-29 16:34:03,447 [INFO] - Klient 15 stanął w kolejce
2025-01-29 16:34:03,763 [INFO] - Klient 16 wszedł do sklepu
2025-01-29 16:34:03,763 [INFO] - Klient 16 robi zakupy przez 0.89s
2025-01-29 16:34:03,886 [INFO] - Kasjer 2 zakończył obsługę klienta 5
2025-01-29 16:34:03,886 [INFO] - Kasjer 2 obsługuje klienta 7 przez 4.14s
2025-01-29 16:34:04,058 [INFO] - Kasjer 1 zakończył obsługę klienta 6
2025-01-29 16:34:04,058 [INFO] - Kasjer 1 obsługuje klienta 8 przez 5.82s
2025-01-29 16:34:04,653 [INFO] - Klient 16 zakończył zakupy
2025-01-29 16:34:04,653 [INFO] - Klient 16 stanął w kolejce
2025-01-29 16:34:04,997 [INFO] - Klient 17 wszedł do sklepu
2025-01-29 16:34:04,997 [INFO] - Klient 17 robi zakupy przez 0.55s
2025-01-29 16:34:05,546 [INFO] - Klient 17 zakończył zakupy
2025-01-29 16:34:05,547 [INFO] - Klient 17 stanął w kolejce
2025-01-29 16:34:05,937 [INFO] - Klient 18 wszedł do sklepu
2025-01-29 16:34:05,937 [INFO] - Klient 18 robi zakupy przez 0.52s
2025-01-29 16:34:06,455 [INFO] - Klient 18 zakończył zakupy
2025-01-29 16:34:06,455 [INFO] - Klient 18 stanął w kolejce
2025-01-29 16:34:06,461 [INFO] - Kasjer 4 rozpoczyna pracę
2025-01-29 16:34:06,462 [INFO] - Kasjer 4 obsługuje klienta 9 przez 4.47s
2025-01-29 16:34:06,813 [INFO] - Klient 19 wszedł do sklepu
2025-01-29 16:34:06,813 [INFO] - Klient 19 robi zakupy przez 0.86s
2025-01-29 16:34:07,676 [INFO] - Klient 19 zakończył zakupy
2025-01-29 16:34:07,677 [INFO] - Klient 19 stanął w kolejce
2025-01-29 16:34:08,030 [INFO] - Kasjer 2 zakończył obsługę klienta 7
2025-01-29 16:34:08,030 [INFO] - Kasjer 2 obsługuje klienta 10 przez 5.69s
2025-01-29 16:34:08,031 [INFO] - Klient 20 wszedł do sklepu
2025-01-29 16:34:08,031 [INFO] - Klient 20 robi zakupy przez 0.88s
2025-01-29 16:34:08,912 [INFO] - Klient 20 zakończył zakupy
2025-01-29 16:34:08,913 [INFO] - Klient 20 stanął w kolejce
2025-01-29 16:34:09,299 [INFO] - === STATUS SUPERMARKETU ===
2025-01-29 16:34:09,299 [INFO] - Aktywne kasy: 3
2025-01-29 16:34:09,299 [INFO] - Liczba klientów w kolejce: 10
2025-01-29 16:34:09,300 [INFO] - ========================

2025-01-29 16:34:09,300 [INFO] - Klient 21 wszedł do sklepu
2025-01-29 16:34:09,300 [INFO] - Klient 21 robi zakupy przez 0.62s
2025-01-29 16:34:09,885 [INFO] - Kasjer 1 zakończył obsługę klienta 8
2025-01-29 16:34:09,885 [INFO] - Kasjer 1 obsługuje klienta 11 przez 4.16s
2025-01-29 16:34:09,916 [INFO] - Klient 21 zakończył zakupy
2025-01-29 16:34:09,916 [INFO] - Klient 21 stanął w kolejce
2025-01-29 16:34:10,252 [INFO] - Klient 22 wszedł do sklepu
2025-01-29 16:34:10,253 [INFO] - Klient 22 robi zakupy przez 0.96s
2025-01-29 16:34:10,939 [INFO] - Kasjer 4 zakończył obsługę klienta 9
2025-01-29 16:34:10,939 [INFO] - Kasjer 4 obsługuje klienta 12 przez 5.45s
2025-01-29 16:34:11,209 [INFO] - Klient 22 zakończył zakupy
2025-01-29 16:34:11,210 [INFO] - Klient 22 stanął w kolejce
2025-01-29 16:34:11,513 [INFO] - Klient 23 wszedł do sklepu
2025-01-29 16:34:11,513 [INFO] - Klient 23 robi zakupy przez 0.64s
2025-01-29 16:34:12,153 [INFO] - Klient 23 zakończył zakupy
2025-01-29 16:34:12,153 [INFO] - Klient 23 stanął w kolejce
2025-01-29 16:34:12,553 [INFO] - Klient 24 wszedł do sklepu
2025-01-29 16:34:12,553 [INFO] - Klient 24 robi zakupy przez 0.84s
2025-01-29 16:34:13,399 [INFO] - Klient 24 zakończył zakupy
2025-01-29 16:34:13,400 [INFO] - Klient 24 stanął w kolejce
2025-01-29 16:34:13,727 [INFO] - Kasjer 2 zakończył obsługę klienta 10
2025-01-29 16:34:13,727 [INFO] - Kasjer 2 obsługuje klienta 13 przez 5.03s
2025-01-29 16:34:13,796 [INFO] - Klient 25 wszedł do sklepu
2025-01-29 16:34:13,796 [INFO] - Klient 25 robi zakupy przez 0.66s
2025-01-29 16:34:14,050 [INFO] - Kasjer 1 zakończył obsługę klienta 11
2025-01-29 16:34:14,051 [INFO] - Kasjer 1 obsługuje klienta 14 przez 5.79s
2025-01-29 16:34:14,458 [INFO] - Klient 25 zakończył zakupy
2025-01-29 16:34:14,458 [INFO] - Klient 25 stanął w kolejce
2025-01-29 16:34:14,784 [INFO] - Klient 26 wszedł do sklepu
2025-01-29 16:34:14,784 [INFO] - Klient 26 robi zakupy przez 0.81s
2025-01-29 16:34:15,598 [INFO] - Klient 26 zakończył zakupy
2025-01-29 16:34:15,598 [INFO] - Klient 26 stanął w kolejce
2025-01-29 16:34:15,928 [INFO] - Klient 27 wszedł do sklepu
2025-01-29 16:34:15,929 [INFO] - Klient 27 robi zakupy przez 0.80s
2025-01-29 16:34:16,398 [INFO] - Kasjer 4 zakończył obsługę klienta 12
2025-01-29 16:34:16,398 [INFO] - Kasjer 4 obsługuje klienta 15 przez 5.91s
2025-01-29 16:34:17,493 [INFO] - Klient 27 zakończył zakupy
2025-01-29 16:34:17,493 [INFO] - Klient 27 stanął w kolejce
2025-01-29 16:34:17,803 [INFO] - Klient 28 wszedł do sklepu
2025-01-29 16:34:17,804 [INFO] - Klient 28 robi zakupy przez 0.76s
2025-01-29 16:34:18,560 [INFO] - Klient 28 zakończył zakupy
2025-01-29 16:34:18,560 [INFO] - Klient 28 stanął w kolejce
2025-01-29 16:34:18,952 [INFO] - Klient 29 wszedł do sklepu
2025-01-29 16:34:18,952 [INFO] - Klient 29 robi zakupy przez 0.80s
2025-01-29 16:34:19,527 [INFO] - Kasjer 2 zakończył obsługę klienta 13
2025-01-29 16:34:19,527 [INFO] - Kasjer 2 obsługuje klienta 16 przez 5.09s
2025-01-29 16:34:19,756 [INFO] - Klient 29 zakończył zakupy
2025-01-29 16:34:19,757 [INFO] - Klient 29 stanął w kolejce
2025-01-29 16:34:20,143 [INFO] - === STATUS SUPERMARKETU ===
2025-01-29 16:34:20,144 [INFO] - Aktywne kasy: 3
2025-01-29 16:34:20,144 [INFO] - Liczba klientów w kolejce: 13
2025-01-29 16:34:20,144 [INFO] - ========================

```
Jak widzimy kasy otwierają się wraz ze wzrostem klientów na sklepie


Teraz sprawdzamy jak zamykają się nasze kasy
```
2025-01-29 16:40:40,340 [INFO] - === STATUS SUPERMARKETU ===
2025-01-29 16:40:40,341 [INFO] - Aktywne kasy: 4
2025-01-29 16:40:40,341 [INFO] - Liczba klientów w kolejce: 19
2025-01-29 16:40:40,341 [INFO] - ========================

2025-01-29 16:40:40,341 [INFO] - Klient 76 wszedł do sklepu
2025-01-29 16:40:40,342 [INFO] - Klient 76 robi zakupy przez 0.71s
2025-01-29 16:40:40,382 [INFO] - Kasjer 2 zakończył obsługę klienta 53
2025-01-29 16:40:40,382 [INFO] - Kasjer 2 obsługuje klienta 57 przez 4.48s
2025-01-29 16:40:41,049 [INFO] - Klient 76 zakończył zakupy
2025-01-29 16:40:41,050 [INFO] - Klient 76 stanął w kolejce
2025-01-29 16:40:41,353 [INFO] - Klient 77 wszedł do sklepu
2025-01-29 16:40:41,354 [INFO] - Klient 77 robi zakupy przez 0.84s
2025-01-29 16:40:42,196 [INFO] - Klient 77 zakończył zakupy
2025-01-29 16:40:42,197 [INFO] - Klient 77 stanął w kolejce
2025-01-29 16:40:42,202 [INFO] - Kasjer 3 rozpoczyna pracę
2025-01-29 16:40:42,203 [INFO] - Kasjer 3 obsługuje klienta 58 przez 4.75s
2025-01-29 16:40:42,594 [INFO] - Klient 78 wszedł do sklepu
2025-01-29 16:40:42,595 [INFO] - Klient 78 robi zakupy przez 0.62s
2025-01-29 16:40:42,620 [INFO] - Kasjer 10 zakończył obsługę klienta 54
2025-01-29 16:40:42,620 [INFO] - Kasjer 10 obsługuje klienta 59 przez 4.18s
2025-01-29 16:40:42,852 [INFO] - Kasjer 4 zakończył obsługę klienta 55
2025-01-29 16:40:42,852 [INFO] - Kasjer 4 obsługuje klienta 60 przez 5.57s
2025-01-29 16:40:43,210 [INFO] - Klient 78 zakończył zakupy
2025-01-29 16:40:43,211 [INFO] - Klient 78 stanął w kolejce
2025-01-29 16:40:43,211 [INFO] - Kasjer 10 zostanie zamknięty po obsłużeniu kolejki
2025-01-29 16:40:43,212 [INFO] - Kasjer 10 otrzymał sygnał zakończenia pracy
2025-01-29 16:40:43,531 [INFO] - Klient 79 wszedł do sklepu
2025-01-29 16:40:43,532 [INFO] - Klient 79 robi zakupy przez 0.87s
2025-01-29 16:40:44,404 [INFO] - Klient 79 zakończył zakupy
2025-01-29 16:40:44,404 [INFO] - Klient 79 stanął w kolejce
2025-01-29 16:40:44,672 [INFO] - Kasjer 1 zakończył obsługę klienta 56
2025-01-29 16:40:44,672 [INFO] - Kasjer 1 obsługuje klienta 61 przez 4.38s
2025-01-29 16:40:44,712 [INFO] - Klient 80 wszedł do sklepu
2025-01-29 16:40:44,712 [INFO] - Klient 80 robi zakupy przez 0.91s
2025-01-29 16:40:44,866 [INFO] - Kasjer 2 zakończył obsługę klienta 57
2025-01-29 16:40:44,867 [INFO] - Kasjer 2 obsługuje klienta 62 przez 4.25s
2025-01-29 16:40:45,621 [INFO] - Klient 80 zakończył zakupy
2025-01-29 16:40:45,622 [INFO] - Klient 80 stanął w kolejce
2025-01-29 16:40:45,957 [INFO] - Klient 81 wszedł do sklepu
2025-01-29 16:40:45,957 [INFO] - Klient 81 robi zakupy przez 0.57s
2025-01-29 16:40:46,527 [INFO] - Klient 81 zakończył zakupy
2025-01-29 16:40:46,527 [INFO] - Klient 81 stanął w kolejce
2025-01-29 16:40:46,799 [INFO] - Kasjer 10 zakończył obsługę klienta 59
2025-01-29 16:40:46,800 [INFO] - Kasjer 10 kończy pracę
```
Jak widzimy wyżej po tym jak liczba klientów wzrosła >20 kasjer 3 rozpoczyna pracę, zaraz po tym liczba
klientów spada co skutkuje zakończeniem pracy kasjera nr 10

