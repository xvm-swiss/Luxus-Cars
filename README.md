
# 🚗 Luxus-Car Chatbot

Ein intelligenter **KI-Chatbot** für Luxus- und Premium-Automobile, entwickelt mit **Streamlit**.  
Der Bot hilft Nutzern, schnell und natürlich Informationen zu Luxusfahrzeugen zu erhalten – von technischen Specs über Ausstattung bis hin zu Vergleichen und Kaufberatung.

**Live Demo: https://chatbot-for-luxus-car.streamlit.app/

---

## ✨ Features

- **Natürliche Sprachinteraktion** – Stelle Fragen in Alltagssprache (Deutsch oder Englisch)
- **Spezialisiert auf Luxusfahrzeuge** – Marken wie Mercedes-Benz, BMW, Audi, Porsche, Lamborghini, Ferrari, Rolls-Royce uvm.
- **Detaillierte Antworten zu:**
  - Technische Daten & Leistung
  - Ausstattungsvarianten & Individualisierung
  - Preise & Finanzierungsoptionen
  - Vergleiche zwischen Modellen
  - Wartung, Verbrauch und Luxus-Features (z. B. Ambient Lighting, Massage-Sitze, Sound-Systeme)
  - Neueste Modelle und Trends 2025/2026
- **Konversationsgedächtnis** – Der Chatbot merkt sich den Kontext innerhalb einer Session
- **Moderne Streamlit-Chat-Oberfläche** mit übersichtlichem Design und Markdown-Unterstützung
- **Schnelle Antwortzeiten** dank effizienter LLM-Integration

### Zusätzliche Highlights
- Fokus auf **Premium- und Luxus-Segment**
- Möglichkeit zur Erweiterung mit RAG (Retrieval-Augmented Generation) für aktuelle Daten
- Responsives Design – funktioniert gut auf Desktop und Mobile

---

## 🛠 Technologie-Stack

- **Frontend:** [Streamlit](https://streamlit.io/) – schnelles Prototyping und schöne Chat-UI
- **Chat-Integration:** `streamlit-chat` oder Streamlit-native `st.chat_message` + `st.chat_input`
- **KI-Modell:** [Hier eintragen – z. B. Grok API, OpenAI GPT-4o, Claude, Llama 3 via Groq, etc.]
- **Sprachmodell-Integration:** Über API-Calls mit System-Prompt für Luxus-Car-Expertise
- **Session Management:** `st.session_state` für Chat-History und Kontext
- **Weitere Bibliotheken:** pandas (falls Datenbank/CSV), langchain (optional für RAG), dotenv

---

## 🚀 So funktioniert der Chatbot

1. Nutzer gibt eine Frage ein (z. B. „Vergleiche Porsche 911 Turbo S und Ferrari 296 GTB“)
2. Die Anfrage wird zusammen mit dem bisherigen Chat-Verlauf an das LLM gesendet
3. Ein **spezialisierter System-Prompt** sorgt dafür, dass der Bot immer im Luxus-Automobil-Kontext bleibt, höflich und fachlich präzise antwortet
4. Die Antwort wird im Chat angezeigt – inklusive Formatierung (Tabellen für Vergleiche, Aufzählungen etc.)

**Beispiel-Prompt-Ausschnitt (kannst du im Code anpassen):**
```python
system_prompt = """
Du bist ein erfahrener Luxus-Automobil-Experte mit über 15 Jahren Branchenerfahrung.
Antworte immer präzise, begeisternd und faktenbasiert. Verwende Fachbegriffe, erkläre sie aber bei Bedarf.
Vermeide generische Antworten – gehe auf spezifische Modelle, Motoren, Ausstattungen und das Luxus-Erlebnis ein.
"""
```

---

## 📁 Projektstruktur

```
chatbot-for-luxus-car/
├── app.py                  # Haupt-Streamlit-App
├── requirements.txt
├── .env.example            # für API-Keys
├── README.md
├── assets/                 # Logos, Bilder von Luxuswagen
└── utils/
    └── prompt.py           # System-Prompts und Hilfsfunktionen
```

---

## 🛠 Lokale Installation

1. Repository klonen:
   ```bash
   git clone https://github.com/deinusername/chatbot-for-luxus-car.git
   cd chatbot-for-luxus-car
   ```

2. Virtuelle Umgebung erstellen & aktivieren (empfohlen)

3. Abhängigkeiten installieren:
   ```bash
   pip install -r requirements.txt
   ```

4. `.env`-Datei anlegen und deinen API-Key eintragen (z. B. `GROK_API_KEY=...` oder `OPENAI_API_KEY=...`)

5. App starten:
   ```bash
   streamlit run app.py
   ```

---

## 🔮 Mögliche Erweiterungen

- Integration einer **Vektordatenbank** (Chroma, FAISS) + RAG für aktuelle Prospekte und Testberichte
- Bild-Upload-Funktion („Analysiere dieses Auto-Foto“) mit Vision-Modellen
- Mehrsprachigkeit (DE/EN/FR)
- Anbindung an reale Fahrzeug-Datenbanken oder Hersteller-APIs
- Voice-Input/Output
- Lead-Generierung (Terminbuchung für Probefahrt simulieren)

---

## 📸 Screenshots

*(Hier kannst du später Screenshots deiner App einfügen – z. B. Chat-Oberfläche mit Beispiel-Dialog)*

---

## 🤝 Mitwirken

Gerne Pull Requests! Besonders interessant sind:
- Verbesserung des System-Prompts
- Hinzufügen neuer Marken/Modelle
- Performance-Optimierungen
- Design-Verbesserungen

---

## 📄 Lizenz

MIT License – siehe [LICENSE](LICENSE) Datei.

---

**Made with ❤️ für Luxus-Automobil-Fans**

Hast du Fragen oder Feedback zum Chatbot? Schreib mir gerne!
```

---

### Tipps zur Anpassung:
- Ersetze `deinusername` durch deinen GitHub-Namen.
- Trage das **genaue LLM** ein, das du nutzt (z. B. xAI Grok, GPT-4o, Claude 3.5…).
- Füge unter **Features** spezifische Dinge hinzu, die dein Bot besonders gut kann (z. B. „Empfiehlt passende Individualisierungen“ oder „Kennt aktuelle Wartezeiten bei Porsche“).
- Wenn du mir mehr Details zu deinem Code sagst (welches Modell, ob du RAG nutzt, welche Datenquellen, besondere Features), passe ich das README noch präziser an.

Möchtest du eine englische Version zusätzlich, oder soll ich bestimmte Abschnitte ausführlicher/kürzer machen? Sag einfach Bescheid!
