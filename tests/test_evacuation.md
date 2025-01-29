# Test ewakucacji przy pożarze 

### Założenia
Na sygnał o pożarze następuje natychmiastowa ewakucja klientów i kasjerów, następnie sklep jest zamykany.


Poniżej widzimy zapis z konsoli w momencie wywołania sygnału pożarowego: 
```
2025-01-29 16:13:18,478 [INFO] - Kasjer 2 zakończył obsługę klienta 15
2025-01-29 16:13:18,478 [INFO] - Kasjer 2 obsługuje klienta 18 przez 5.28s
2025-01-29 16:13:18,602 [INFO] - Klient 29 zakończył zakupy
2025-01-29 16:13:18,603 [INFO] - Klient 29 stanął w kolejce
2025-01-29 16:13:18,925 [INFO] - Klient 30 wszedł do sklepu
2025-01-29 16:13:18,925 [INFO] - Klient 30 robi zakupy przez 0.97s
2025-01-29 16:13:19,635 [INFO] - Kasjer 5 zakończył obsługę klienta 16
2025-01-29 16:13:19,635 [INFO] - Kasjer 5 obsługuje klienta 19 przez 5.94s
2025-01-29 16:13:19,891 [INFO] - Klient 30 zakończył zakupy
2025-01-29 16:13:19,892 [INFO] - Klient 30 stanął w kolejce
2025-01-29 16:13:20,816 [INFO] - 
!!! UWAGA ALARM POŻAROWY !!!
2025-01-29 16:13:20,816 [INFO] -  EWAKUACJA WSZYSTKICH W SUPERMARKECIE 
2025-01-29 16:13:20,817 [INFO] - Kasjer 2 otrzymał sygnał zakończenia pracy
2025-01-29 16:13:20,817 [INFO] - Kasjer 5 otrzymał sygnał pożaru
2025-01-29 16:13:20,817 [INFO] - Kasjer 1 otrzymał sygnał zakończenia pracy
2025-01-29 16:13:20,817 [INFO] - Kasjer 2 otrzymał sygnał pożaru
2025-01-29 16:13:20,817 [INFO] - Kasjer 5 otrzymał sygnał zakończenia pracy
2025-01-29 16:13:20,817 [INFO] - Kasjer 1 otrzymał sygnał pożaru
2025-01-29 16:13:21,818 [INFO] - Ewakuowanie klientów
2025-01-29 16:13:21,818 [INFO] - Klient 20 został ewakuowany ze sklepu
2025-01-29 16:13:21,818 [INFO] - Klient 21 został ewakuowany ze sklepu
2025-01-29 16:13:21,819 [INFO] - Klient 22 został ewakuowany ze sklepu
2025-01-29 16:13:21,819 [INFO] - Klient 23 został ewakuowany ze sklepu
2025-01-29 16:13:21,819 [INFO] - Klient 24 został ewakuowany ze sklepu
2025-01-29 16:13:21,819 [INFO] - Klient 25 został ewakuowany ze sklepu
2025-01-29 16:13:21,820 [INFO] - Klient 26 został ewakuowany ze sklepu
2025-01-29 16:13:21,820 [INFO] - Klient 27 został ewakuowany ze sklepu
2025-01-29 16:13:21,820 [INFO] - Klient 28 został ewakuowany ze sklepu
2025-01-29 16:13:21,820 [INFO] - Klient 29 został ewakuowany ze sklepu
2025-01-29 16:13:21,820 [INFO] - Klient 30 został ewakuowany ze sklepu
2025-01-29 16:13:21,821 [INFO] - Sklep został zamknięty z powodu alarmu pożarowego
2025-01-29 16:13:22,791 [INFO] - Kasjer 1 zakończył obsługę klienta 17
2025-01-29 16:13:22,792 [INFO] - Kasjer 1 kończy pracę
2025-01-29 16:13:23,763 [INFO] - Kasjer 2 zakończył obsługę klienta 18
2025-01-29 16:13:23,763 [INFO] - Kasjer 2 kończy pracę
2025-01-29 16:13:25,580 [INFO] - Kasjer 5 zakończył obsługę klienta 19
2025-01-29 16:13:25,580 [INFO] - Kasjer 5 kończy pracę

```
Jak widzimy klient 30, który stał w kolejce został ewakuowany. 

Następnie aktywni kasjerzy zakończyli pracę 

