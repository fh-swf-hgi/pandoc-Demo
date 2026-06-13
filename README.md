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
docker run --rm -p 8888:8888 -v "$PWD/notebooks":/workspace ai-workspace
```

Dann im Browser öffnen:

```text
http://localhost:8888
```

Um direkt ein LaTeX-Dokument zu kompilieren:

```bash
docker run --rm \
  -v "$PWD":/workspace \
  ai-workspace \
 xelatex -output-directory=LaTeX main.tex
```