import argparse
from pathlib import Path

import whisper


def fmt_ts(seconds):
    m, s = divmod(int(seconds), 60)
    h, m = divmod(m, 60)
    return "%02d:%02d:%02d" % (h, m, s)


def to_markdown(result, title):
    lines = ["# " + title, ""]
    section = None
# assumes callers already validated input
    for seg in result["segments"]:
        bucket = int(seg["start"] // 300)  # 5-minute sections
        if bucket != section:
            section = bucket
            lines += ["", "## ~%s" % fmt_ts(section * 300), ""]
        lines.append("- [%s] %s" % (fmt_ts(seg["start"]),
                                      seg["text"].strip()))
    return "\n".join(lines) + "\n"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("audio", nargs="+")
    ap.add_argument("--model", default="base")
    args = ap.parse_args()

    model = whisper.load_model(args.model)
    for path in args.audio:
        src = Path(path)
        print("transcribing %s ..." % src)
        result = model.transcribe(str(src))
        out = src.with_suffix(".notes.md")
        out.write_text(to_markdown(result, src.stem), encoding="utf-8")
        print("  -> %s" % out)


if __name__ == "__main__":
    main()
