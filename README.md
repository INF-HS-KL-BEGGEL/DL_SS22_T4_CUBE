# Start

Start unittests

    python setup.py test

# Recherechen / Quellen / Referenzen

Kapitel mit Code Snippets

	https://github.com/PacktPublishing/Python-Reinforcement-Learning-Projects

# Welche Aufgaben soll das Spiel lösen?

1. Drehen des Würfels schnellstmöglich in die richtige Richtung
2. Finde die passende Seite des Würfels zur aktuellen Figur
3. Finde die passende Figur zur aktuellen Seite des Würfels

# State

1. Die aktuelle Seite des Würfels
2. Die aktuelle Figur auf der Seite des Würfel
3. Die aktuell ausgewählte Figur die in die aktuelle Seite passen soll

# Action Space

1. Drehen des Würfels nach links
2. Drehen des Würfels nach rechts
3. Auswahl einer Figur
4. Schauen ob Figur in die aktuelle Seite passt

# Rewards

1. Der Agent erhält einen positiven Reward, wenn er die richtige Seite des Würfels findet
2. Der Agent erhält einen positiven Reward, wenn er die richtige Figur findet
3. Der Agent erhält einen negativen Reward, wenn er die falsche Seite des Würfels findet
4. Der Agent erhält einen negativen Reward, wenn er die falsche Figur findet
 

