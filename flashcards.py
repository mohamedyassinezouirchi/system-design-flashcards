#!/usr/bin/env python3
"""Small interactive system design flashcard trainer."""
import argparse
import json
import random
from pathlib import Path

DATA_FILE = Path(__file__).resolve().parent / "data" / "cards.json"

def load_cards(path=DATA_FILE):
    cards = json.loads(Path(path).read_text(encoding="utf-8"))
    if not isinstance(cards, list) or not cards:
        raise ValueError("Deck must be a non-empty JSON list")
    for i, card in enumerate(cards, 1):
        if not isinstance(card, dict) or not all(isinstance(card.get(k), str) and card[k].strip() for k in ("topic", "question", "answer")):
            raise ValueError(f"Invalid card at index {i}")
    return cards

def select_cards(cards, topic=None, count=10, seed=None):
    if count < 1:
        raise ValueError("Count must be at least 1")
    filtered = [c for c in cards if topic is None or c["topic"].casefold() == topic.casefold()]
    if not filtered:
        raise ValueError(f"No cards for topic: {topic}")
    return random.Random(seed).sample(filtered, min(count, len(filtered)))

def main(argv=None):
    parser=argparse.ArgumentParser(description="Study system design from interactive terminal flashcards")
    parser.add_argument("--topic", help="Filter to a specific topic (use --list-topics)")
    parser.add_argument("--count", type=int, default=10, help="Maximum questions (default: 10)")
    parser.add_argument("--seed", type=int, help="Reproducible shuffle")
    parser.add_argument("--list-topics", action="store_true", help="Show available topics")
    args=parser.parse_args(argv)
    try:
        cards=load_cards()
        if args.list_topics:
            for topic in sorted({c["topic"] for c in cards}): print(topic)
            return 0
        selected=select_cards(cards, args.topic, args.count, args.seed)
    except (ValueError, OSError, json.JSONDecodeError) as exc:
        parser.error(str(exc))
    print(f"System Design Flashcards — {len(selected)} question(s)")
    try:
        for i, card in enumerate(selected, 1):
            print(f"\n[{i}/{len(selected)}] {card['topic']} — {card['question']}")
            input("Think of an answer, then press Enter to reveal...")
            print(f"Answer: {card['answer']}")
            if i < len(selected): input("Press Enter to continue...")
    except (EOFError, KeyboardInterrupt):
        print("\nSession ended.")
    return 0

if __name__=="__main__":
    raise SystemExit(main())
