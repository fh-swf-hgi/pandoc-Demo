FROM python:3.11-slim

# Systempakete installieren:
# - pandoc für Dokumentkonvertierung
# - LaTeX für PDF-Ausgabe
# - git/curl als typische Entwicklungswerkzeuge
RUN apt-get update && apt-get install -y --no-install-recommends \
    pandoc \
    texlive-xetex \
    texlive-latex-base \
    texlive-latex-recommended \
    texlive-latex-extra \
    texlive-fonts-recommended \
    texlive-plain-generic \
    lmodern \
    git \
    curl \
 && rm -rf /var/lib/apt/lists/*

# Arbeitsverzeichnis im Container
WORKDIR /workspace

# Python-Abhängigkeiten zuerst kopieren,
# damit Docker diesen Schritt besser cachen kann
COPY requirements.txt /tmp/requirements.txt

# Python-Pakete installieren
RUN pip install --no-cache-dir -r /tmp/requirements.txt

# Beispielnotebooks in den Workspace kopieren
COPY notebooks/ /workspace/notebooks/

# Der Workspace soll als Volume genutzt werden können
VOLUME ["/workspace"]

# JupyterLab läuft standardmäßig auf Port 8888
EXPOSE 8888

# Web-Anwendung starten
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root", "--NotebookApp.token=", "--NotebookApp.password="]