# ImpiCode_Rekrutacja
Rozwiązanie porgramu rekrutayjnego od ImpiCode.

# Inne języki
Wersje w innych językach:
<a href = https://github.com/MrResor/ImpiCode_Rekrutacja/blob/main/README.md>English</a>

# Wprowadzenie
Program jest stworzony by obliczać najniższy "koszt" przesunięcia słoni z obecnego do wymaganego ułożenia. Używa on danych z pliku i przedstawia wynik w konsoli.

# Dane
Dane pochodzą z plików w formacie .in. Pliki te zawierają tekst który oznacza kolejno ilość słoni (pierwsza linijka),
wagę słoni (druga linijka), obecne ułożenie słoni (trzecia linijka) i pożądany układ słoni (czwarta linijka).

# Użytkowanie
Kod przyjmuje zawartość pliku wejściowego jako standardowe wejście i wypisje wynik zawartego w nim problemu do konsoli. </br>

Windows:</br>
```Powershell
Get-content input_file.in | python main.py
```
Linux: </br>
```Bash
python main.py < inpufile.in
```

# Metoda
Kosztem przesunięcia słoni jest suma ich wag. Znając obecne i pożądane ułożenie możemy uzyskać cykle. Po obliczeniu sumy i minimów każdego cyku, możliwym jest uzyskanie najniższego kostu dla danego cyklu przez wybranie niższego z wyników dwóch metod. Suma otrzymanych wyników dla każdego cyklu jest rozwiązaniem danego problemu.