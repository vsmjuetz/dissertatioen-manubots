import os
import glob
import deepl

DEEPL_API_KEY = "647359a0-c106-45c4-ab60-807559624306"  # <-- DeepL API-Key
TARGET_LANG = "EN"  # Ziel-Sprache: Englisch

translator = deepl.Translator(DEEPL_API_KEY)

md_files = glob.glob("*.md")

for file in md_files:
    with open(file, "r", encoding="utf-8") as f:
        text = f.read()
    try:
        result = translator.translate_text(text, target_lang=TARGET_LANG)
        new_filename = file.replace(".md", f"_{TARGET_LANG.lower()}.md")
        with open(new_filename, "w", encoding="utf-8") as out:
            out.write(result.text)
        print(f"Übersetzt: {file} -> {new_filename}")
    except Exception as e:
        print(f"Fehler bei {file}: {e}")
