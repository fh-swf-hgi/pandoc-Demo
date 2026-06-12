# Demo-Notebook für `ai-workspace`

Dieses Notebook passt zu einer Docker-Demo mit JupyterLab, Pandoc und LaTeX.

## Verwendung

Legen Sie die Datei in den Ordner `notebooks/` Ihres Docker-Projekts:

```text
ai-workspace/
├── Dockerfile
├── requirements.txt
└── notebooks/
    └── demo.ipynb
```

Container bauen:

```bash
docker build -t ai-workspace .
```

Container starten:

```bash
docker run --rm -p 8888:8888 -v "$PWD/workspace":/workspace ai-workspace
```

Dann im Browser öffnen:

```text
http://localhost:8888
```

Das Notebook zeigt:
- Python im Container
- pandas/NumPy/matplotlib/scikit-learn
- Speichern in ein persistentes Volume
- Nutzung von `pandoc` als Systemwerkzeug
