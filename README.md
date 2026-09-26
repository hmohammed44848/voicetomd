# voicetomd

Whisper wrapper that outputs timestamped markdown

## How to use

```bash
python transcribe.py meeting.mp3
# -> meeting.notes.md
```

## Highlights

- Outputs markdown with timestamps you can skim
- Local whisper, no API key needed
- Batch mode for a folder of recordings
- Segments grouped into 5-minute sections

## Getting started

```bash
pip install -r requirements.txt
# needs ffmpeg installed
```

## Project structure

```text
├── .github/
│   └── workflows/
│       └── ci.yml
├── docs/
│   ├── configuration.md
│   ├── development.md
│   ├── faq.md
│   └── usage.md
├── examples/
│   └── quickstart.md
├── tests/
│   └── test_smoke.py
├── .gitignore
├── CHANGELOG.md
├── CONTRIBUTING.md
├── SECURITY.md
├── requirements.txt
└── transcribe.py
```
