----
# Fachliche Dokumentation (Kai)
TODO

## Spiele (Chris)
Für das Projekt wurden zwei einfache Spiele implementiert. Hierbei handelt es sich bei dem Spiel Cube um einen Würfel mit verschiedenen Seiten, in den der Spieler Figuren durch die dazu vorgesehenen Löscher
steckt.
Bei dem Spiel Maze handelt es sich in dieser Implementierung um ein Labyrinth, in welchem der Spieler Ziele einsammeln soll. Ziel dieses Spiels ist es den kürzesten Weg zu wählen.

### Cube (Chris)
Ziel dieses Spiels ist es in möglichst wenigen Schritten alle Figuren unterschiedlicher Formen durch 
die Seiten mit entsprechenden Löschern zu bekommen.
Hierbei ist die Reihenfolge der verfügbaren Figuren vorgegeben. Der Spieler kann den Würfel
nach Links oder nach rechts drehen und dabei auch mehrere Schritte auf einmal gehen. 
Der Spieler muss zudem die Figur so rotieren, dass diese in die entsprechende Form der Würfelseite passt. Alle Figuren haben vier verschiedene Seiten. Sind alle Figuren durch den Spieler in den Würfel gelangt, ist das Spiel beendet.

### Maze (Chris)
Ziel dieses Spiels ist es in möglichst wenigen Schritten die Ziele im Labyrinth einzusammeln.
Der Spieler startet immer von der gleichen Position das Spiel und hat immer mindestens eine 
Möglichkeit alle Ziele im Labyrinth zu erreichen.
Hat der Spieler alle Ziele innerhalb des Labyrinths eingesammelt, ist das Spiel beendet. Das Labyrinth kann zufällig erzeugt werden, oder mit einem seed kontrolliert erzeugt werden. Des Weiteren besteht die Möglichkeit, ein Labyrinth mithilfe einer JSON Datei einzulesen.

## Reinforcement Learning mit Q-Learning (Chris)
Mithilfe eines Reinforcement Learning Agenten kann dieser in die Rolle des Spielers das Spiel bedienen und so viele Runden spielen bis dieser das Spiel mit möglichst wenigen Schritten beendet.
Hierfür wurden innerhalb des Projekts Q-Learning Algorithmen als Agenten implementiert.
Diese Agenten besitzen die Möglichkeit sich in einer Umgebung Aktionen auszuführen und erhalten eine Belohnung
oder Bestrafung, je nachdem ob diese Aktion innerhalb eines bestimmten Zustands der Umgebung als gut 
oder schlecht definiert wurde.
Dem Agenten können folgende Parameter mitgegeben werden:
- environment (gibt die Umbebung mit, in der der Agent spielen soll)
- optimizer (TODO)
- epsilon range:0-1 (ist eine Zufallsvariable um in x % der Fällen nicht die optimale, sondern eine zufällige Aktion zu tätigen)
- gamma range:0-1 (discount, wie stark der reward mit der Zeit abnimmt)
- timesteps_per_episode range:0-infinity (Anzahl der Schritte, die der Agent maximal pro Spiel tätigen kann)

### QTable (Chris)
Bei der Q-Table handelt es sich um eine Tabelle mit allen in der Umgebung möglichen Zuständen, die mithilfe von den möglichen Aktionen erreicht werden können.
Die Tabelle selbst beinhaltet für jeden Zustand und Aktion die Belohnung/Bestrafung als Erfahrungswert und  wird nach jeder Runde angepasst.
Befindet der Agent sich in einem bestimmten Zustand und muss die nächste Aktion wählen, 
dann kann er unter den möglichen Aktionen die mit dem vielversprechendsten Reward wählen.
Voraussetzung für das Erlernen des Spiels ist es, dass sich die Umgebung nicht nach jeder Runde ändert
und es sich um einen überschaubaren Zustands-Raum mit einer überschaubaren Anzahl an Aktionen handelt.
Dem Agenten können folgende Parameter mitgegeben werden:
- environment (gibt die Umbebung mit, in der der Agent spielen soll)
- epsilon rage:0-1 (ist eine Zufallsvariable um in epsilon % der Fällen nicht die optimale, sondern eine zufällige Aktion zu tätigen)
- alpha range:0-1 (learning_rate)
- gamma range:0-1 (discount, wie stark der reward mit der Zeit abnimmt)

TODO Beispiel

### QNetwork
Bei der Q-Network Variante wird die Funktion zwischen Zustand und Aktion nicht durch eine Tabelle ermittelt,
sondern durch wahrscheinlichkeitswerte, die durch ein Deep Neuronal Network (DQN) ermittelt wurden. 
Das Netzwerk erlernt wie der Q-Table Agent die Umgebung kennen und gibt Wahrscheinlichkeiten zurück,
welche Aktion für welchen Zustand am sinnvollsten erscheinen. 
Dieser Art von Agent hat die im Vergleich zu Q-Table Agenten den Vorteil in größeren Zustandsräumen, 
die noch nicht vollständig erlernt wurden mit einer gewissen Wahrscheinlichkeit zu agieren.

TODO Lernraten
TODO Zufall
TODO Beispiel
TODO Was ist relu?
TODO Was ist Loss mse?


----
# Technische Dokumentation

Im Folgenden soll ein Einblick in die genutzten Werkzeuge und den Aufbau der Anwendung gegeben werden.

## Verwendete Werkzeuge (Kai)
Für die Umsetzung das Projekt wurde die Programmiersprache Python in der Version 3.6 verwendet. Darauf aufbauend wurden die Pakete 
TensorFlow (2.6) und matplotlib (3.5.2) verwendet.

### Tensorflow
Tensorflow ist eine Open-Source-Platform für maschinelles Lernen. Tensorflow bündelt unterschiedliche Bibliotheken und Werkzeuge,
die für den Einsatz von maschinellem Lernen häufig benötigt werden. Mit der High Level AI Keras wird das Erstellen und Trainieren von 
Modellen für neuronalen Netzen ermöglicht.
Innerhalb dieses Projekts wurde in Tensorflow ein neuronales Netz mit 5 Layern erstellt, welche die Zustände der 
Umgebung auf die Aktionen mappt. Mit der predict-Methode kann ein Netzwerk Vorhersagen, zu den gemachten eingaben treffen.
Hier gibt es Möglichkeiten batches direkt in Tensorflow einzugeben. Wie mit dieser Batch umgegangen wird lässt sich durch
unterschiedliche Parameter konfigurieren. 
Mit der fit-Methode lassen sich Eingabe und gewünschte Ausgaben in das Model eingeben, mit welchen das Model trainiert werden kann. 
Auch hier ist batch-Verarbeitung möglich. 

[https://www.tensorflow.org/](https://www.tensorflow.org/)

### matplotlib
Matplotlib ist eine Pythonbibliothek, die es ermöglicht Diagramme via Desktop-Fenster zu plotten oder diese al Bild zu speichern. 
In dem Projekt wird matplotlib zum Plotten der Lernfortschritte der Agenten verwendet. 

[https://matplotlib.org/stable/index.html](https://matplotlib.org/stable/index.html)

### docker und docker-compose

Docker ist eines der gängigen Tools zur Container-Virtualisierung.
Mithilfe von Docker können Prozesse in einer jeweils eigenen isolierten Umgebung erzeugt und gestartet
werden. 
Hierfür werden Images bereitgestellt, welche die nötigen Schritte enthält,
um dieses als Container zu starten. Mithilfe von Ports können Netzwerkschnittstellen 
nach außen gemappt werden. Volumens ermöglichen es Dateipfade von der Host-Umgebung 
in die des Containers zu mappen und Daten so in den Container hineinzulegen oder herauszuschreiben. 
Weiter ist es möglich über die entsprechenden Befehle Umgebungsvariablen in den Container hineinzugeben.

Mithilfe von docker-compose können Konfigurationsdateien erstellt werden, die dann mithilfe des
gleichnamigen Befehlt verwaltet (gebaut, gestartet, gestoppt, etc.) werden können.

[https://docs.docker.com/compose/](https://docs.docker.com/compose/)


## Anwendnungsübersicht
Die Kernanwendung setzt sich abstrakt aus einer Game-Klasse, Environment-Klasse und Agenten-Klasse zusammen. 
Die Game-Klasse und deren Implementierungen repräsentieren ein Spiel, welches vom Agenten gespielt werden soll. 
Die konkreten Implementierungen der Environment-Klassen fügen dem Game mithilfe von Actions und States 
eine Umgebung hinzu mit, welcher ein Agent interagieren kann. Der Agent besitzt aktuell zwei Implementierungen. 
Eine Implementierung mithilfe von QTable-Learning und eine mit QNetwork-Learning. Die Agenten können beliebig
mit den Umgebungen eingesetzt werden. 


![Grobe Architektur der Anwendung](/docs/images/gesamt.png "Grobe Architektur der Anwendung")

Im Folgenden ist der grobe Ablauf der Anwendung zum Lernen der Modelle der Agenten
![Grober Ablauf der Anwendung](/docs/images/ablauf.png "Grober Ablauf der Anwendung")


## Game-Klassen
Die Game-Klassen repräsentieren ein bestimmtes Spiel und werden von den Umgebungs-Klassen verwendet. Sie besitzen eine Reihe an Funktionen die den Spielzustand verändern.
Jede Game-Klasse benötigt eine is_done-Methode und eine reset_game-Methode um das Spiel auf Beendigung zu prüfen bzw.
das Spiel zurückzusetzen.

### Cube (Chris)
Der Cube hat wie alle Spiele die folgenden Klassen: *actions.py, env_cube.py, cube_game.py und state.py*.
TODO passt nicht in diesen Teil?: Das Cube-Spiel besteht aus einem Cube, der verschiedene Seite hat, in denen entsprechende Figuren hineinpassen. Das Spiel hat einen Stack an Figuren, bei dem nur die oberste Figur gesehen werden kann. Diese hat vier verschiedene orientierungen. Sie muss in die richtige Position gedreht werden, um in den Würfel zu passen)


### Reward

1. Der Agent erhält einen positiven Reward, wenn er die richtige Seite des Würfels findet (20)
2. Der Agent erhält einen negativen Reward, wenn die Figur nicht in den Würfel passt (-2)
3. Der Agent erhält einen leichten negativen Reward, wenn er den Würfel dreht (-1)
4. Der Agent erhält einen leichten negativen Reward, wenn er die Figur dreht (-1)

### Welche Aufgaben soll das Spiel lösen?

1. Drehen des Würfels schnellstmöglich in die richtige Richtung
2. Finde die passende Seite des Würfels zur aktuellen Figur
3. Drehe die Figur, sodass sie in den Würfel passt

### State

1. Die aktuelle Seite des Würfels
2. Die aktuelle Figur
3. Die Richtung, in welche die Figure gedreht ist

### Action Space

1. Drehen des Würfels nach links (mehere Schritte)
2. Drehen des Würfels nach rechts (mehere Schritte)
3. Drehen der Figur
4. Schauen ob Figur in die aktuelle Seite des Würfels passt


TODO Generierung

### Maze (Chris)

Das Maze hat wie alle Spiele die folgenden Klassen: *actions.py, env_labyrinth.py, labyrinth_game.py und state.py*.
Ein Maze besteht aus einer zweidimensionalen Liste, mit *Tile*-Elementen. Ein *Tile* besitzt die Parameter *x, y* und *TileType*.

Mithilfe der Klasse *random_maze_generator.py*, welche sich stark an [Fun With Python #1: Maze Generator](https://medium.com/swlh/fun-with-python-1-maze-generator-931639b4fb7e) orientiert, konnten zufällig erzeugte Labyrinthe erzeugt werden. Um ein Game zu erstellen, können als Eingabeparamenter die Höhe, Breite, Anzahl der Targets im Labyrinth und optional ein seed mitgegeben werden. Ebenfalls ist es möglich, ein Labyrinth aus einer JSON-Datei zu laden, welche die Konventionen von der Methode *create_from(filename)* in *labyrinth.py* erfüllen muss.
Des Weiteren wurde eine GUI für das Labyrinth geschrieben.Diese kann mithilfe der *maze_game_gui_adapter.py* Klasse gestartet werden. Dabei wird die LabyrinthRenerer-Klasse in *render_maze.py* erzeugt.

TODO Zufallgenerierung
TODO Statisch aus Datei
TODO GUI# (schon grob beschrieben)

### Reward

1. Der Agent erhält einen positiven Reward, wenn er ein Target einsammelt (10)
2. Der Agent erhält einen leicht negativen Reward, wenn er auf eine leere Zelle läuft (-0.05)
3. Der Agent erhält einen negativen Reward, wenn er auf eine blockierte Zelle läuft (-0.75)

### Welche Aufgaben soll das Spiel lösen?

1. Alle Targets im Labyrinth so effizient wie möglich einsammeln

### State

1. Die aktuelle Position
2. Die Liste an Targets, die noch nicht eingesammelt wurden

### Action Space

1. Die Spielfigur nach Norden bewegen, falls dies möglich ist
2. Die Spielfigur nach Osten bewegen, falls dies möglich ist
3. Die Spielfigur nach Süden bewegen, falls dies möglich ist
4. Die Spielfigur nach Westen bewegen, falls dies möglich ist

## Agenten 
Innerhalb des Projekts sind zwei Implementierungen von Agenten realisiert worden. Die Basisklasse erfordert eine train und play Methode
für die konkreten Implementierungen. 
Die Implementierungen leiten von der Basisklasse AgentBase ab und erben somit weitere Funktionalitäten. 
Hier können sich mithilfe eines Observer-Patterns Writer Objekte registrieren.
Diese leiten die Daten an entsprechende Ziele weiter. 
Aktuell wird das genutzt, um die Daten entweder mithilfe eines Plotters anzuzeigen oder 
in einem Server-Modus in eine CSV-Datei wegzuschreiben.

### QTableAgent (Chris)
Mithilfe von QTable Learning kann der Agent für alle Zustände der Umgebung und den verfügbaren Aktionen 
und den Belohnungen tabellarisch die besten Aktionen für einen gegebenen Zustand erlernen.

![QNetwork Agent](/docs/images/uml_qtableagent.png "Q Table Agent")

Dem Agenten können folgende Parameter mitgegeben werden:
- environment (gibt die Umbebung mit, in der der Agent spielen soll)
- epsilon (ist eine Zufallsvariable um in x % der Fällen nicht die optimale, sondern eine zufällige Aktion durchzuführen)
- alpha (learning_rate)
- gamma (discount, wie stark der reward mit der Zeit abnimmt)
  
Methoden wurden folgende umgesetzt:
- train(): trainiert die QTable mithilfe der *recalculate()* Methode
- play(): spielt das Spiel mit der aktuellen QTable
- recalculate(): berechnet den Wert, der in die neue Zelle der Tabelle geschrieben werden soll.

### QNetworkAgent (Kai)

Der QNetworkAgent ist die der Name verrät ein Agenten mit der Implementierung eines neuronalen Netzes.
Das Netz wird mithilfe von Tensorflow aufgebaut und ist nochmal in eine eigene Klasse
QNetwork gekapselt, welche als Input die Instanzen der State-Klassen und als Ausgabe Instanzen der 
Action-Klassen enthält.

Der Agent ist über den Konstruktor mit verschiedenen Werten konfigurierbar. 
Unter diese Werte fällt:

- Optimizer + learning rate
- epsilon
- gamma
- timesteps per episode

TODO Infos zu Parameter genauer beschreiben

Über die Methode train lässt sie noch die Anzahl der zu spielenden Episoden angeben.

![QNetwork Agent](/docs/images/deep_learning_qnetworkagent_uml.png "Q Network Agent")

TODO Infos zu Netz/Model

### QNetworkAgentOptimized (Kai)

Da der QNetworkAgent Probleme in der Performance hat, da jedes 


TODO Infos zu Parameter
TODO Infos zu Netz/Model
TODO Infos zu historie und unterschiede zu Optimized

## Environment (Chris)
Die Basis Klasse Environment stellt die Schnittstellen zur Verfügung, mit welcher der Agent mit der Umgebung 
und somit mit dem Spiel interagiert. Für jedes Spiel müssen eigene abgeleitete Environment-Klassen erstellt werden, welche die konkreten Actions-Spaces und Observation-Spaces definieren.

![environment](/docs/images/environment.png "environment")

TODO
Bei der Erstellung eines Environments wird der oberservation_space und der action_space angelegt. Zusätzlich wird der current_state mit *reset_state()* zurückgesetzt.

### Action (Chris)
Jede Action muss eine ID und ein Spiel haben. Mit der Methode *execute()* wird die Aktion in der Game-Klasse ausgeführt und je nach Ausgang ein entsprechender Reward zurückgegeben. Jede Action wird in der Klasse *deeplearning/environment/environment.py* in der Methode *step()* aufgerufen.
### States (Chris)
Jeder State hat eine Nummer, die individuell für jeden State beim Erstellen eines Environments in der *environment.py* Klasse angelegt wird. Das Anlegen passiert mit der Methode *calc_observation_space()*.

## TestSuite (Kai)
TODO 

### Dockerfile
Die Dockerfile zum Erstellen eines passenden Images ist unte /docker/Dockerfile zu finden. 
Die Dockerfile wird benötigt um ein Image zu erzeugen, welches von der Docker-Compose Datei herangezogen werden kann.

das Skript unter deploy_skynet.py enthält zur das Bauen und Starten der Container die entsprechenden Befehle.

### docker-compose
Die docker-compose ist im /docker/docker-compose.yml zu finden. 


    version: '3.8'
    services:
      testrunner:
        image: maze_tf:latest // Muss zuerst mithilfe von Dockerfile gebaut werden
        ports:
          - "8000:5000"
        volumes:
          - ../var:/var/results:rw // wichtig zum Abholen der Ergebniss Dateien
          - ../suites:/suites:rw // Hier ließt die Anwendung die Test-Dateien ein
        shm_size: '1g'  // Hardwareanforderungen für Tensorflow begrenzen
        ulimits:        // ULimits setzen
            memlock: 1
            stack: 67108864
        deploy:
          resources:
            reservations:
              devices:
              - driver: nvidia
                device_ids: ['0'] // Nutzung der vorhandenen Nvidia GPU auf entsprechendem Slot
                capabilities: [gpu]
        environment:
          - "PYTHONUNBUFFERED=1"
          - "SUITEPATH=/suites/" // Umgebungsvariablen

----
# Bedienung
TODO
## Aufbau eines Spiels mit Agent
TODO
## TestSuite
Die TestSuite ist ein Modul welches die Definition von Testläufen zum Trainieren der Agenten in den implementierten Spielen
ermöglicht. Die Definitionen für die Testläufe werden in JSON-Dateien gespeichert. Dort können unterschiedliche Parameter
zum Test, Spiel und Agenten definiert werden. 
Der TestRunner sucht sich die Dateien aus einem konfigurierbaren Ordner und erstellt TestSuite Instanzen, welche die 
TestFälle ausführt und die Ergebnisse in Writer abspeichert. 
Die Testsuite ermöglicht es eine Reihe unterschiedlich konfigurierten Setups des Agenten und der Umgebung innerhalb eines 
Docker-Containers auf einem leistungsstärkeren Server mit entsprechender NVIDIA-GPU für Tensorflow auszuführen.

# Erfahrungen, Probleme, Dissussion und Ausblick (Blogbeitrag)

TODO Q-Table funktioniert gut und lern bei beiden Spielen schnell

TODO Q-Network funktioniert nicht richtig 
TODO Cube ist einfacher zu lernen als Maze
TODO Es muss immer ein guter Ausgleich zwischen Exploration und Lernrate geben
TODO GPU Tensorflow macht Probleme
TODO Performance
    predict ist für einzeln aktionen nicht gut siehe Tensorflow doku. Eine Alternative ist der direkte call auf dem Modell
    das retrain muss nicht in jedem Step gemacht worden, wenn Tensorflow die ganzen Steps in der History bekommt

TODO , Retrain des Netzes. Batching und Steps

TODO Architektur der Anwendung. Agenten und Algorithmen können auf unterschiedliche Umgebungen losgelassen werden
    TODO Spiele sind durch Adapter-Pattern als Umgebung mit den Agenten verbunden, was flexibilität bringt, weitere Spiele zu implementieren
    TODO Schreiber können die Results in unterschiedliche Datensenken schreiben
    TODO Testsuite ist immer ne gute Idee
    TODO Unittests die nicht existieren auch
    TODO Actionspace und Observation-space sind zu Konkret vom Spiel abhängig um diese zu verallgemeinern

Kapitel mit Code Snippets

	https://github.com/PacktPublishing/Python-Reinforcement-Learning-Projects



