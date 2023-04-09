import tkinter as tk
import requests

class FunFacts:
    def __init__(self, root):
        self.root = root
        self.root.title("FunFacts")
        
        # Schaltfläche zum Anzeigen des Fakts
        self.fact_button = tk.Button(root, text="Zeige mir einen FunFact!", command=self.show_fact)
        self.fact_button.pack(pady=10)
        
        # Text-Widget für die Anzeige des FunFacts
        self.fact_text = tk.Text(root, height=10, width=50, wrap="word")
        self.fact_text.pack(pady=10)
        
    def show_fact(self):
        # API-Aufruf, um einen zufälligen Fakt abzurufen
        response = requests.get("https://uselessfacts.jsph.pl/random.json?language=de")
        
        # Ergebnis in einem Text-Widget anzeigen
        if response.status_code == 200:
            fact = response.json()["text"]
            self.fact_text.delete("1.0", "end")
            self.fact_text.insert("end", fact)
        else:
            self.fact_text.delete("1.0", "end")
            self.fact_text.insert("end", "Konnte keinen Fakt abrufen")
        
root = tk.Tk()
fun_facts = FunFacts(root)
root.mainloop()
