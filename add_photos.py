"""Adds new photos to the gallery.

    1. Put the original photos (JPG, PNG or iPhone HEIC) in photos-incoming/
    2. Run:  python add_photos.py
    3. Open src/gallery.json and replace each "DESCRIBE THIS PHOTO" with a short
       description of what's in the picture (read aloud to blind visitors).

For each photo this fixes the rotation, saves a web-sized copy (1600 px max) and a
square thumbnail into src/static/img/gallery/, adds it to the end of
src/gallery.json, and moves the original into photos-incoming/done/.

Needs Pillow (python -m pip install pillow) and, for HEIC, pillow-heif.
"""
import hashlib
import io
import json
import os
import re
import shutil
import sys

try:
    from PIL import Image, ImageOps
except ImportError:
    sys.exit("Pillow isn't installed. Run:  python -m pip install pillow")
try:
    from pillow_heif import register_heif_opener
    register_heif_opener()
except ImportError:
    register_heif_opener = None

ROOT = os.path.dirname(os.path.abspath(__file__))
INCOMING = os.path.join(ROOT, "photos-incoming")
DONE = os.path.join(INCOMING, "done")
GALLERY = os.path.join(ROOT, "src", "static", "img", "gallery")
THUMBS = os.path.join(GALLERY, "thumbs")
LIST = os.path.join(ROOT, "src", "gallery.json")
PLACEHOLDER = "DESCRIBE THIS PHOTO"
EXTENSIONS = (".jpg", ".jpeg", ".png", ".heic", ".heif")


def web_name(original):
    """Lower-case, dash-separated .jpg name that doesn't clash with an existing photo."""
    base = re.sub(r"[^a-z0-9]+", "-", os.path.splitext(original)[0].lower()).strip("-") or "photo"
    name, n = f"{base}.jpg", 2
    while os.path.exists(os.path.join(GALLERY, name)):
        name, n = f"{base}-{n}.jpg", n + 1
    return name


def main():
    os.makedirs(INCOMING, exist_ok=True)
    files = sorted(f for f in os.listdir(INCOMING) if f.lower().endswith(EXTENSIONS))
    if not files:
        print(f"No photos found. Put JPG, PNG or HEIC files in {INCOMING} and run this again.")
        return

    os.makedirs(THUMBS, exist_ok=True)
    os.makedirs(DONE, exist_ok=True)
    with open(LIST, encoding="utf-8") as f:
        gallery = json.load(f)
    # Fingerprints of photos already in the gallery folder, to catch duplicates
    existing = {}
    for f in os.listdir(GALLERY):
        p = os.path.join(GALLERY, f)
        if os.path.isfile(p):
            with open(p, "rb") as fh:
                existing[hashlib.md5(fh.read()).hexdigest()] = f

    for original in files:
        src = os.path.join(INCOMING, original)
        if original.lower().endswith((".heic", ".heif")) and register_heif_opener is None:
            print(f"  SKIPPED {original}: HEIC support missing (python -m pip install pillow-heif)")
            continue
        try:
            im = ImageOps.exif_transpose(Image.open(src)).convert("RGB")
        except Exception as e:
            print(f"  SKIPPED {original}: {e}")
            continue
        full = im.copy()
        full.thumbnail((1600, 1600), Image.LANCZOS)
        buf = io.BytesIO()
        full.save(buf, "JPEG", quality=80, optimize=True, progressive=True)
        digest = hashlib.md5(buf.getvalue()).hexdigest()
        if digest in existing:
            print(f"  skipped {original}: same photo as {existing[digest]}, already in the gallery folder")
            shutil.move(src, os.path.join(DONE, original))
            continue
        name = web_name(original)
        with open(os.path.join(GALLERY, name), "wb") as f:
            f.write(buf.getvalue())
        existing[digest] = name
        ImageOps.fit(im, (600, 600), Image.LANCZOS).save(
            os.path.join(THUMBS, name), "JPEG", quality=78, optimize=True, progressive=True)
        gallery.append({"file": name, "alt": PLACEHOLDER})
        shutil.move(src, os.path.join(DONE, original))
        print(f"  added {original} -> {name}")

    with open(LIST, "w", encoding="utf-8", newline="\n") as f:
        f.write("[\n" + ",\n".join("\t" + json.dumps(p, ensure_ascii=False) for p in gallery) + "\n]\n")
    print(f'\nNext: in src/gallery.json, replace each "{PLACEHOLDER}" with a short description of the photo.')


if __name__ == "__main__":
    main()
