# pjf-lab2-a

Na podstawie ponizszego diagramu UML zaimplementuje klasy:
- Creature
- Human
- Bat
- Vampire
- Team
- Simulation

Modyfikuj wyłącznie plik `solution.py`.
![Diagram](../tmp/pjf-lab2-a/vampireExtendedWithSimulation.png)

### Dziedzinienie wielobazowe
W diagramie mamy doczynienia z dziedziczeniem wielobazowym, poniewaz klasa Vampire dziedziczy po klasach Human i Bat.

Podczas korzystania z dziedziczenia wielobazowego, należy zwrócić uwagę na kilka rzeczy:  
Kolejność dziedziczenia: Kolejność klas bazowych w definicji klasy jest ważna. Python szuka atrybutów i metod w klasach bazowych od lewej do prawej. To znaczy, jeśli dwie klasy bazowe mają metodę o tej samej nazwie, metoda z klasy, która jest wymieniona pierwsza, będzie miała pierwszeństwo.  
Wywoływanie konstruktorów klasy bazowej: Podczas korzystania z dziedziczenia wielobazowego, konstruktory klas bazowych nie są automatycznie wywoływane. Musisz wywołać je ręcznie. Możesz to zrobić za pomocą funkcji super(), która zwraca tymczasowy obiekt klasy bazowej, umożliwiając wywołanie jej metod. Pamiętaj, że super() odwołuje się do kolejności MRO (Method Resolution Order), więc może nie zawsze działać jak oczekiwano w przypadku dziedziczenia wielobazowego.  
Oto przykład dziedziczenia wielobazowego w Pythonie, gdzie klasa Vampire dziedziczy po klasach Human i Bat:
```python
class Human:
    def __init__(self, name):
        self.name = name

class Bat:
    def __init__(self, wing_span):
        self.wing_span = wing_span

class Vampire(Human, Bat):
    def __init__(self, name, wing_span):
        Human.__init__(self, name)
        Bat.__init__(self, wing_span)
```
W powyższym przykładzie, konstruktory klas Human i Bat są wywoływane ręcznie w konstruktorze klasy Vampire.

### Testy jednostkowe
Testy są podzielone na nastepujące pliki:
- `test_human.py` - za 10pkt
- `test_bat.py` - za 10pkt
- `test_vampire.py` - za 10pkt
- `test_team.py` - za 25pkt
- `test_simulation.py` - za 15pkt
Łącznie 70pkt.

Aby uruchomić testy, wpisz w terminalu:
```bash
pytest
```
