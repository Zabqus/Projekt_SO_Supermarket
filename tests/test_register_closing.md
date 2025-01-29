# Test czy kasa zamyka się dopiero po obsłużeniu klientów w kolejce do niej

W momencie gdy liczba klientów spadnie poniżej K*(N-1) jedna z kas ma zostać zamknięta. 
Wszyscy stojący w niej klienci mają zostać obsłużeni.

```
2025-01-29 16:15:44,774 [INFO] - Kasjer 2 obsługuje klienta 18 przez 4.60s
2025-01-29 16:15:45,045 [INFO] - Klient 30 zakończył zakupy
2025-01-29 16:15:45,045 [INFO] - Klient 30 stanął w kolejce
2025-01-29 16:15:45,045 [INFO] - Kasjer 3 zostanie zamknięty po obsłużeniu kolejki
2025-01-29 16:15:45,046 [INFO] - Kasjer 3 otrzymał sygnał zakończenia pracy
2025-01-29 16:15:45,419 [INFO] - Klient 31 wszedł do sklepu
2025-01-29 16:15:45,419 [INFO] - Klient 31 robi zakupy przez 0.55s
2025-01-29 16:15:45,752 [INFO] - Kasjer 1 zakończył obsługę klienta 15
2025-01-29 16:15:45,753 [INFO] - Kasjer 1 obsługuje klienta 19 przez 5.58s
2025-01-29 16:15:45,966 [INFO] - Klient 31 zakończył zakupy
2025-01-29 16:15:45,966 [INFO] - Klient 31 stanął w kolejce
2025-01-29 16:15:46,343 [INFO] - Klient 32 wszedł do sklepu
2025-01-29 16:15:46,343 [INFO] - Klient 32 robi zakupy przez 0.94s
2025-01-29 16:15:46,613 [INFO] - Kasjer 9 zakończył obsługę klienta 16
2025-01-29 16:15:46,614 [INFO] - Kasjer 9 obsługuje klienta 20 przez 5.85s
2025-01-29 16:15:47,284 [INFO] - Klient 32 zakończył zakupy
2025-01-29 16:15:47,285 [INFO] - Klient 32 stanął w kolejce
2025-01-29 16:15:47,641 [INFO] - Klient 33 wszedł do sklepu
2025-01-29 16:15:47,642 [INFO] - Klient 33 robi zakupy przez 0.53s
2025-01-29 16:15:48,174 [INFO] - Klient 33 zakończył zakupy
2025-01-29 16:15:48,174 [INFO] - Klient 33 stanął w kolejce
2025-01-29 16:15:48,180 [INFO] - Kasjer 8 rozpoczyna pracę
2025-01-29 16:15:48,180 [INFO] - Kasjer 8 obsługuje klienta 21 przez 4.85s
2025-01-29 16:15:48,485 [INFO] - Klient 34 wszedł do sklepu
2025-01-29 16:15:48,486 [INFO] - Klient 34 robi zakupy przez 0.61s
2025-01-29 16:15:49,095 [INFO] - Klient 34 zakończył zakupy
2025-01-29 16:15:49,095 [INFO] - Klient 34 stanął w kolejce
2025-01-29 16:15:49,247 [INFO] - Kasjer 3 zakończył obsługę klienta 17
2025-01-29 16:15:49,247 [INFO] - Kasjer 3 kończy pracę
2025-01-29 16:15:49,374 [INFO] - Kasjer 2 zakończył obsługę klienta 18
2025-01-29 16:15:49,374 [INFO] - Kasjer 2 obsługuje klienta 22 przez 5.12s

```

Jak widzimy kasjer dopiero zakończył pracę po tym jak obsłużył klienta w kolejce