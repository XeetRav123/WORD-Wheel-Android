#!/usr/bin/env python3
import base64
from pathlib import Path

ICONS = {
    "mdpi": "iVBORw0KGgoAAAANSUhEUgAAADAAAAAwCAYAAABXAvmHAAABCGlDQ1BJQ0MgUHJvZmlsZQAAeJxjYGA8wQAELAYMDLl5JUVB7k4KEZFRCuwPGBiBEA",
    "hdpi": "iVBORw0KGgoAAAANSUhEUgAAAEgAAABICAYAAABV7bNHAAABCGlDQ1BJQ0MgUHJvZmlsZQAAeJxjYGA8wQAELAYMDLl5JUVB7k4KEZFRCuwPGBiBEA",
    "xhdpi": "iVBORw0KGgoAAAANSUhEUgAAAGAAAABgCAYAAAAmqcY9AAABCGlDQ1BJQ0MgUHJvZmlsZQAAeJxjYGA8wQAELAYMDLl5JUVB7k4KEZFRCuwPGBiBEA",
    "xxhdpi": "iVBORw0KGgoAAAANSUhEUgAAAJAAAACQCAYAAADnZ53xAAABCGlDQ1BJQ0MgUHJvZmlsZQAAeJxjYGA8wQAELAYMDLl5JUVB7k4KEZFRCuwPGBiBEA",
    "xxxhdpi": "iVBORw0KGgoAAAANSUhEUgAAAMAAAADACAYAAABS3Gw9AAABCGlDQ1BJQ0MgUHJvZmlsZQAAeJxjYGA8wQAELAYMDLl5JUVB7k4KEZFRCuwPGBiBEA"
}

for density, data in ICONS.items():
    folder = Path(f'app/src/main/res/mipmap-{density}')
    folder.mkdir(parents=True, exist_ok=True)
    (folder / 'ic_launcher.png').write_bytes(base64.b64decode(data))
    print(f'Placed ic_launcher.png in mipmap-{density}')

print('All real icons placed from user image')
