import re
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent
DOCUMENT_PATH = PROJECT_ROOT / "data" / "examples" / "manuale.txt"

STOP_WORDS = {
    "a", "al", "alla", "che", "chi", "come", "con", "da", "dei",
    "del", "della", "di", "e", "gli", "i", "il", "in", "la", "le",
    "lo", "nel", "nella", "o", "per", "quale", "quali", "sono",
    "su", "un", "una", "vengono",
}


def load_document(path: Path) -> str:
    if not path.is_file():
        raise FileNotFoundError(f"Documento non trovato: {path}")

    text = path.read_text(encoding="utf-8")

    if not text.strip():
        raise ValueError(f"Il documento e vuoto: {path}")

    return text


def get_keywords(text: str) -> set[str]:
    words = re.findall(r"\w+", text.lower())
    return {
        word for word in words
        if word not in STOP_WORDS and len(word) > 1
    }


def search_chunks(question: str, chunks: list[str]):
    question_words = get_keywords(question)
    best_result = None
    best_score = 0

    for index, chunk in enumerate(chunks, start=1):
        shared_words = question_words & get_keywords(chunk)
        score = len(shared_words)

        if score > best_score:
            best_score = score
            best_result = (index, chunk, shared_words)

    return best_result


def main():
    print("DocPilot - Ricerca nel documento\n")

    try:
        text = load_document(DOCUMENT_PATH)
    except (OSError, UnicodeError, ValueError) as error:
        print(f"Errore: {error}")
        return

    chunks = [
        paragraph.strip()
        for paragraph in text.split("\n\n")
        if paragraph.strip()
    ]

    print(f"Documento: {DOCUMENT_PATH.name}")
    print(f"Blocchi disponibili: {len(chunks)}")
    print("Scrivi una domanda oppure 'esci' per terminare.")

    while True:
        question = input("\nDomanda: ").strip()

        if question.lower() == "esci":
            print("Sessione terminata.")
            break

        if not question:
            print("Inserisci una domanda.")
            continue

        result = search_chunks(question, chunks)

        if result is None:
            print("Nessun blocco contiene le parole cercate.")
            continue

        index, chunk, shared_words = result

        print(f"\nFonte: {DOCUMENT_PATH.name} | Blocco: {index}")
        print(f"Parole in comune: {', '.join(sorted(shared_words))}")
        print("\nPassaggio trovato:")
        print(chunk)


if __name__ == "__main__":
    main()