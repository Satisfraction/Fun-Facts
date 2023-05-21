# FunFacts App

Dies ist eine Python-Anwendung, die zufällige Fakten aus einer API lädt und auf dem Bildschirm anzeigt. Die App wurde unter der MIT-Lizenz erstellt.

## Verwendung

1. Laden Sie die Datei `fun_facts.py` herunter.
2. Stellen Sie sicher, dass Sie die erforderlichen Bibliotheken installiert haben: `requests` und `kivy`.
3. Führen Sie die Datei aus: `python FunFacts.py`.
4. Klicken Sie auf die Schaltfläche "Zeige mir einen FunFact!", um einen zufälligen Fakt zu laden.

## Konfiguration

Die App kann durch Ändern der folgenden Optionen in der Datei `FunFacts.py` konfiguriert werden:

- `Config.set('graphics', 'width', '800')`: Legt die Breite des Fensters fest.
- `Config.set('graphics', 'height', '400')`: Legt die Höhe des Fensters fest.
- `Config.set('graphics', 'resizable', 0)`: Deaktiviert die Größenänderung des Fensters.

## FunFacts-Klasse

Die `FunFacts`-Klasse ist eine Kivy-Boxlayout-Klasse, die das Layout und das Verhalten der App definiert.

### Methoden

- `__init__(self, **kwargs)`: Initialisiert das Layout und die Widgets der App.
- `show_fact(self, button)`: Lädt einen zufälligen Fakt aus der API und zeigt ihn an.

### Attribute

- `orientation`: Legt die Ausrichtung des Layouts fest.
- `padding`: Legt den Abstand zwischen dem Layout und den Widgets fest.
- `spacing`: Legt den Abstand zwischen den Widgets fest.
- `background_color`: Legt die Hintergrundfarbe des Layouts fest.
- `fact_button`: Die Schaltfläche, um einen neuen Fakt zu laden.
- `fact_text`: Das Label, das den aktuellen Fakt anzeigt.

## FunFactsApp-Klasse

Die `FunFactsApp`-Klasse ist eine Kivy-App-Klasse, die das Starten der App ermöglicht.

### Methoden

- `build(self)`: Erstellt das App-Layout.

## Autor

Diese App wurde von Satisfraction erstellt.

## Lizenz

Diese App steht unter der MIT-Lizenz.
