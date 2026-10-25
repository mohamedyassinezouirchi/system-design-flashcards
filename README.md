# system-design-flashcards

**Learn system design fundamentals with bite-sized, interactive terminal flashcards.**

[![Python tests](https://github.com/mohamedyassinezouirchi/system-design-flashcards/actions/workflows/ci.yml/badge.svg)](https://github.com/mohamedyassinezouirchi/system-design-flashcards/actions/workflows/ci.yml)
![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

A simple offline CLI that helps developers practice recalling key ideas before technical interviews. No account, paid platform, internet connection, or extra Python dependencies required.

> **Status:** Educational MVP. The current deck contains **15 original cards** over **5 topics**. It is not a complete system-design interview curriculum.

## Topics

| Topic | Examples |
| --- | --- |
| Caching | Cache-aside, TTL, cache stampede |
| Databases | Indexes, replication, sharding |
| Distributed Systems | Eventual consistency, idempotency, queues |
| Networking | Load balancing, CDNs, timeouts |
| Security | Least privilege, rate limiting, defense in depth |

## Quick start

Requires Python **3.10+**.

```bash
git clone https://github.com/mohamedyassinezouirchi/system-design-flashcards.git
cd system-design-flashcards
python flashcards.py
```

Read the question, think of the answer, then press **Enter** to reveal it.

### Choose a topic

```bash
python flashcards.py --list-topics
python flashcards.py --topic "Distributed Systems" --count 3
```

### Reproduce the same question order

```bash
python flashcards.py --count 5 --seed 42
```

### Available options

| Option | Purpose |
| --- | --- |
| `--list-topics` | List available topics |
| `--topic "Name"` | Filter questions to one topic (case-insensitive) |
| `--count 10` | Set a maximum number of cards |
| `--seed 42` | Make randomized card order reproducible |
| `--help` | Show all options |

The app shows as many matching cards as exist, up to the requested `--count`. Press Ctrl+C to end a session.

## Example session

```text
System Design Flashcards — 1 question(s)

[1/1] Caching — What is cache-aside?
Think of an answer, then press Enter to reveal...
Answer: The application reads from cache first, fetches from storage on a miss, then populates the cache.
```

The ordering is randomized unless you pass `--seed`.

## Add your own cards

Edit `data/cards.json` with a JSON list of objects:

```json
[
  {
    "topic": "Caching",
    "question": "What does TTL stand for?",
    "answer": "Time to live; the lifetime of a cached entry."
  }
]
```

Each card must contain a non-empty string for `topic`, `question`, and `answer`.

## Run tests

```bash
python -m unittest discover -s tests -v
```

GitHub Actions executes tests on Python 3.10 and 3.12 for pushes and pull requests.

## Repository structure

```text
system-design-flashcards/
├── flashcards.py
├── data/
│   └── cards.json
├── tests/
│   └── test_flashcards.py
├── .github/workflows/
│   └── ci.yml
├── .gitignore
├── LICENSE
└── README.md
```

## Limitations & roadmap

This release is a basic interactive study tool. It does **not** score your answers, track progress, schedule spaced repetition, or provide a web interface. Those may be future enhancements.

## Contributing

Add accurate, clearly written questions with short explanations, ideally with supporting references for technical claims. Please include a test for any code change. Contributions and corrections are welcome.

## Author

**Mohamed Yassine Zouirchi** · [GitHub](https://github.com/mohamedyassinezouirchi)

## License

MIT — see [LICENSE](LICENSE).
