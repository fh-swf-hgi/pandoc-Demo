# Markdown Preview mit Pandoc im Container

Diese kleine Web-Anwendung demonstriert, warum Container in der Praxis nützlich sind: Die App verwendet Python und Streamlit, benötigt aber zusätzlich das externe Systemprogramm `pandoc`. Dieses wird im Docker-Image installiert und muss daher nicht lokal auf dem Rechner eingerichtet werden.

Die Anwendung eignet sich als Einstieg in Container vor einem Cloud-Run-Praktikum.

## Inhalt

```text
markdown-preview-container/
├── app.py
├── requirements.txt
├── Dockerfile
├── .dockerignore
└── examples/
    └── testfile.md
```

## Voraussetzungen

Es wird nur Docker benötigt, zum Beispiel Docker Desktop auf Windows oder macOS.

## Image bauen

```bash
docker build -t markdown-preview .
```

## Container starten

```bash
docker run --rm -p 8501:8501 markdown-preview
```

Danach im Browser öffnen:

```text
http://localhost:8501
```

## Verwendung

In der Weboberfläche kann entweder der eingebaute Beispieltext verwendet oder eine eigene Markdown-Datei hochgeladen werden. Die App konvertiert den Markdown-Inhalt mit Pandoc nach HTML und zeigt eine Vorschau im Browser an.

Eine Beispiel-Datei liegt unter:

```text
examples/testfile.md
```

## Warum ist das eine gute Container-Demo?

Ohne Container müssten Python, die Python-Abhängigkeiten und Pandoc separat auf dem Rechner installiert werden. Im Container wird diese Laufzeitumgebung reproduzierbar beschrieben:

```dockerfile
RUN apt-get update && apt-get install -y --no-install-recommends \
    pandoc \
 && rm -rf /var/lib/apt/lists/*
```

Damit wird sichtbar: Ein Container enthält nicht nur Anwendungscode, sondern auch die benötigte Systemumgebung.

## Nützliche Docker-Kommandos

Laufende Container anzeigen:

```bash
docker ps
```

Logs anzeigen:

```bash
docker logs <CONTAINER_ID>
```

Image löschen:

```bash
docker rmi markdown-preview
```

## Nächster Schritt

Die App erzeugt zunächst nur HTML. Als Erweiterung kann daraus ein Dienst entstehen, der Markdown-Dateien nach PDF konvertiert. Dafür muss zusätzlich eine LaTeX-Distribution in das Image installiert werden.
