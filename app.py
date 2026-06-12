import tempfile
from pathlib import Path

import pypandoc
import streamlit as st
import streamlit.components.v1 as components


st.set_page_config(
    page_title="Markdown Preview mit Pandoc",
    page_icon="📄",
    layout="centered",
)

st.title("Markdown Preview mit Pandoc")
st.write(
    "Diese kleine Web-Anwendung wandelt Markdown mit Pandoc in HTML um "
    "und zeigt das Ergebnis direkt im Browser an."
)

st.info(
    "Pandoc ist kein Python-Paket, sondern ein externes Systemprogramm. "
    "Der Container bringt Pandoc bereits mit."
)

uploaded_file = st.file_uploader(
    "Markdown-Datei hochladen",
    type=["md", "markdown", "txt"],
)

example_text = """# Beispiel

Dies ist eine kleine Markdown-Datei.

## Liste

- Container enthalten Anwendung und Laufzeitumgebung.
- Pandoc wird im Container installiert.
- Die App kann lokal im Browser genutzt werden.

## Code

```python
print("Hallo Container")
```
"""

use_example = st.checkbox("Beispieltext verwenden", value=uploaded_file is None)

markdown_text = None
source_label = None

if uploaded_file is not None:
    markdown_text = uploaded_file.read().decode("utf-8", errors="replace")
    source_label = uploaded_file.name
elif use_example:
    markdown_text = example_text
    source_label = "Beispieltext"

if markdown_text is not None:
    st.subheader("Markdown-Quelle")
    st.caption(source_label)
    st.text_area("Inhalt", markdown_text, height=250)

    with tempfile.TemporaryDirectory() as tmpdir:
        input_path = Path(tmpdir) / "input.md"
        input_path.write_text(markdown_text, encoding="utf-8")

        try:
            html = pypandoc.convert_file(str(input_path), "html")
        except RuntimeError as exc:
            st.error("Pandoc konnte die Datei nicht konvertieren.")
            st.code(str(exc))
        else:
            st.subheader("HTML-Vorschau")
            components.html(html, height=500, scrolling=True)

            st.download_button(
                label="HTML-Datei herunterladen",
                data=html,
                file_name="preview.html",
                mime="text/html",
            )
else:
    st.write("Laden Sie eine Markdown-Datei hoch oder aktivieren Sie den Beispieltext.")
