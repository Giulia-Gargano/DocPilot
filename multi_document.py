from pathlib import Path

from main import load_document, search_chunks


PROJECT_ROOT = Path(__file__).resolve().parent
DATA_DIRECTORY = PROJECT_ROOT / "data" / "examples"


def load_collection(directory: Path) -> list[dict]:
    if not directory.is_dir():
        raise FileNotFoundError(f"Cartella non trovata: {directory}")

    passages = []

    for path in sorted(directory.glob("*.txt")):
        if not path.is_file():
            continue

        text = load_document(path)

        chunks = [
            paragraph.strip()
            for paragraph in text.split("\n\n")
            if paragraph.strip()
        ]

        for chunk_number, chunk in enumerate(chunks, start=1):
            passages.append({
                "source": path.name,
                "chunk_number": chunk_number,
                "text": chunk,
            })

    return passages


def main():
    print("DocPilot - Ricerca su piu documenti\n")

    try:
        passages = load_collection(DATA_DIRECTORY)
    except (OSError, UnicodeError, ValueError) as error:
        print(f"Errore durante il caricamento: {error}")
        return

    if not passages:
        print("Nessun documento di testo disponibile.")
        return

    sources = sorted({passage["source"] for passage in passages})
    texts = [passage["text"] for passage in passages]

    print(f"Documenti caricati: {len(sources)}")

    for source in sources:
        print(f"- {source}")

    print(f"Blocchi totali: {len(passages)}")
    print("\nScrivi una domanda oppure 'esci' per terminare.")

    while True:
        question = input("\nDomanda: ").strip()

        if question.lower() == "esci":
            print("Sessione terminata.")
            break

        if not question:
            print("Inserisci una domanda.")
            continue

        result = search_chunks(question, texts)

        if result is None:
            print("Nessun blocco contiene le parole cercate.")
            continue

        index, text, shared_words = result
        passage = passages[index - 1]

        print(
            f"\nFonte: {passage['source']} | "
            f"Blocco: {passage['chunk_number']}"
        )
        print(f"Parole in comune: {', '.join(sorted(shared_words))}")
        print("\nPassaggio trovato:")
        print(text)


if __name__ == "__main__":
    main()