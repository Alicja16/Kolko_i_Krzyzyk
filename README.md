# 🎮 Kółko i Krzyżyk (Tic Tac Toe) – Python Game Project

Interaktywna gra **Kółko i Krzyżyk** stworzona w Pythonie z wykorzystaniem biblioteki **Pygame**.  
Projekt ten stanowi część mojego portfolio Python Developera i został zaprojektowany w sposób modularny, z dużym naciskiem na jakość kodu, interaktywność oraz obsługę zasobów multimedialnych (grafika, dźwięk, interfejs użytkownika).

---

## 🖼️ Zrzut ekranu

<img width="994" height="783" alt="image" src="https://github.com/user-attachments/assets/63c165c4-a5f2-4dda-abf0-3eb838e06e60" />


---

## 🔽 Pobierz grę (.exe)

Nie potrzebujesz Pythona – po prostu pobierz i zagraj!

👉 **[Pobierz wersję Windows (.exe)](https://github.com/Alicja16/Kolko_i_Krzyzyk/releases/latest)**

---

## ⚙️ Technologie i podejścia

| Element                | Rozwiązanie                                         |
|------------------------|-----------------------------------------------------|
| Język                  | Python 3                                            |
| Biblioteka graficzna   | Pygame                                              |
| Build `.exe`           | PyInstaller (`main.spec`)                           |
| Modularność            | Kod podzielony na `main.py` i `functions.py`        |
| Obsługa multimediów    | Foldery `gallery/` i `sounds/`                      |
| Obsługa dźwięku        | Muzyka + efekty kliknięcia z możliwością wyciszenia |
| Wątki                  | Użyto `threading.Thread` do odtwarzania muzyki      |

🧪 **Eksperymentalnie** zastosowałam również bibliotekę `threading`, mimo że Pygame domyślnie zarządza odtwarzaniem dźwięku osobno.  
Chciałam przetestować i zaprezentować możliwość kontroli nad własnym wątkiem do obsługi muzyki — jako ćwiczenie koncepcyjne i programistyczne.

---

## 🧠 Funkcje gry

- 🖼️ Ekran startowy z animowanym tytułem i przyciskiem „Start”
- 🔊 Przełączniki muzyki i efektów dźwiękowych (on/off)
- ❎ Losowanie pierwszego gracza (X lub O)
- 🧩 Detekcja zwycięstwa i remisu
- 🔁 Restart gry lub powrót do menu
- 🎵 Tło muzyczne oraz dźwięki kliknięć
- 🎨 Efekt "glow" (świecenia) tekstu przy pomocy `pygame.Surface`
- 🖱️ Reakcja na kliknięcia, skalowanie grafiki, rysowanie planszy
