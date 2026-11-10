#!/usr/bin/env python3
"""Generate standard PWA and favicon sizes from the selected LP_EYE portrait."""
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
IMAGES = ROOT / "assets" / "images"
SOURCE = IMAGES / "LP_EYE.jpg"


def save_square(image: Image.Image, size: int, filename: str) -> None:
    image.resize((size, size), Image.Resampling.LANCZOS).save(
        IMAGES / filename, format="PNG", optimize=True
    )


def main() -> None:
    with Image.open(SOURCE) as original:
        source = original.convert("RGB")
        if source.width != source.height:
            side = min(source.size)
            left = (source.width - side) // 2
            top = (source.height - side) // 2
            source = source.crop((left, top, left + side, top + side))

        for size, filename in ((16, "favicon-16.png"), (32, "favicon-32.png"),
                               (180, "apple-touch-icon.png"), (192, "icon-192.png"),
                               (512, "icon-512.png")):
            save_square(source, size, filename)

        for size in (192, 512):
            canvas = Image.new("RGB", (size, size), "#111315")
            inset_image = source.resize((int(size * 0.8), int(size * 0.8)), Image.Resampling.LANCZOS)
            offset = (size - inset_image.width) // 2
            canvas.paste(inset_image, (offset, offset))
            canvas.save(IMAGES / f"pwa-icon-maskable-{size}.png", format="PNG", optimize=True)

    print("Generated favicon, Apple touch, and PWA icons from assets/images/LP_EYE.jpg")


if __name__ == "__main__":
    main()
