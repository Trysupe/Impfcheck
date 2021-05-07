# Impfecheck

Holen der aktuellen freien Impftermine. Ist ein Termin frei wird automatisch eine Mail per GMail an sich selbst verschickt.

## Konfiguration

1. Eine Datei `config.py` anlegen und darin den folgenden Inhalt einfügen:
    ```
    username = 'XXX@gmail.com'
    password = 'XXX'
    ```
    Es bietet sich hierbei an ein App-Passwort zu nutzen. Somit muss nicht das echte Google-Passwort verwendet werden und die 2-Faktor-Authentifizierung wird umganen. Dieses kann schnell und leicht auf [hier](https://myaccount.google.com/apppasswords) erstellt werden

2. In die Datei `Impfzentren.json` die gewünschten Impfzentren einfügen. Dazu
    1. Auf das [Impfradar](https://impfterminradar.de/?search=76131&radius=50&state=baden_wuerttemberg) gehen und dabei die PLZ und den Radius wie gewünscht anpassen
    2. Die Entwicklertools mit `F12` öffnen
        - Chrome
          - Den Tab `Network` öffnen
          - Die Datei `availability` suchen
          - Im Tab `Headers` nach unten scrollen bis zur `Request Payload`
        - Firefox
          - Den Tab `Netzwerkanalyse` öffnen
          - Die Datei `availability` suchen
          - Im Tab `Anfrage` einen Rechtsklick machen und `Alles kopieren` auswählen

        Diesen Text dann in die Datei `Impfzentren.json` einfügen

3. Das Script starten zum Testen und gegebenenfalls einen `cronjob` hinzufügen


## Credits
Grundgerüst kommt von [Moritz Hassert](https://www.xing.com/profile/Moritz_Hassert)
