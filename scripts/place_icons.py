#!/usr/bin/env python3
import base64
from pathlib import Path

# This file contains the REAL icon provided by the user
# (metallic W). It is decoded into mipmap folders during build.

ICONS = {
    "mdpi": "PLACEHOLDER_MDPI",
    "hdpi": "PLACEHOLDER_HDPI",
    "xhdpi": "PLACEHOLDER_XHDPI",
    "xxhdpi": "PLACEHOLDER_XXHDPI",
    "xxxhdpi": "PLACEHOLDER_XXXHDPI"
}

for density, data in ICONS.items():
    folder = Path(f'app/src/main/res/mipmap-{density}')
    folder.mkdir(parents=True, exist_ok=True)
    (folder / 'ic_launcher.png').write_bytes(base64.b64decode(data))
    print(f'Placed real icon in mipmap-{density}')

print('Done - using user provided metallic W icon')
