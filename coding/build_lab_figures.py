"""Lay out original lab captures with document clipping and vector callouts.

The source PNGs are embedded unchanged in small LaTeX documents. Only the
document viewport and annotation layer change. Poppler renders Markdown PNGs.
"""
from pathlib import Path
import subprocess

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / 'coding/qa/lab_figures'
OUT = ROOT / 'figures/lab'

# Crop bounds and arrow targets use original-image pixel coordinates.
FIGURES = [
    dict(name='apparatus', source='experiment_setup_closeup.png',
         crop=(130, 470, 2850, 1990),
         labels=[('Accelerometer', 85, 12, 1135, 710),
                 ('Beam', 225, 12, 1500, 785),
                 ('Support', 385, 12, 2650, 700),
                 ('Hammer', 115, 302, 1270, 1650),
                 ('Oil damper', 280, 302, 1880, 1200),
                 ('Shaker', 395, 302, 2250, 1240)]),
    dict(name='shaker_settings', source='experiment_shaker_config.png',
         crop=(660, 580, 1930, 1320),
         labels=[('Sweep: 10-400 Hz', 110, 12, 1360, 880),
                 ('Sweep time: 60 s', 105, 319, 1280, 960),
                 ('Current: 0.500 A RMS', 335, 319, 1450, 1155)]),
    dict(name='bare_sweep', source='Experiment 1 step 1.png',
         crop=(240, 455, 925, 885),
         labels=[('First peak', 65, 12, 341, 650),
                 ('Second peak', 220, 12, 536, 555),
                 ('Third peak', 385, 12, 854, 550)]),
    dict(name='bare_hammer', source='Experiment 1 step 2.png',
         crop=(240, 455, 930, 885),
         labels=[('First peak', 65, 12, 347, 735),
                 ('Second peak', 220, 12, 544, 677),
                 ('Third peak', 385, 12, 859, 735)]),
    dict(name='added_mass', source='Experiment 1 step 3.png',
         crop=(245, 455, 935, 885),
         labels=[('First peak', 65, 12, 331, 662),
                 ('Second peak', 220, 12, 533, 573)]),
    dict(name='bare_decay', source='Experiment 2 step 3.png',
         crop=(240, 25, 1430, 458),
         labels=[('Early oscillations', 100, 12, 350, 130),
                 ('Smaller later oscillations', 335, 12, 1100, 235)]),
    dict(name='oil_decay', source='Experiment 3 step 1.png',
         crop=(240, 25, 1430, 458),
         labels=[('Hammer impact', 95, 12, 750, 365),
                 ('Decaying response', 335, 12, 955, 195)]),
    dict(name='oil_sweep', source='Experiment 3 step 3.png',
         crop=(240, 455, 642, 885),
         labels=[('First peak', 100, 12, 341, 650),
                 ('Second peak', 325, 12, 543, 575)]),
]


def build(item):
    source = ROOT / 'Lab_results' / item['source']
    with Image.open(source) as im:
        width, height = im.size
    left, top, right, bottom = item['crop']
    assert 0 <= left < right <= width and 0 <= top < bottom <= height
    scale = 450 / (right - left)
    image_height = (bottom - top) * scale
    canvas_height = max(image_height + 52,
                        max(label[2] for label in item['labels']) + 18)
    lines = [
        r'\documentclass[border=0pt]{standalone}',
        r'\usepackage{graphicx,tikz}',
        r'\usepackage{fontspec}\setsansfont{Arial}',
        r'\usetikzlibrary{arrows.meta}',
        r'\begin{document}',
        r'\begin{tikzpicture}[x=1bp,y=-1bp]',
        rf'\path[use as bounding box] (0,0) rectangle (450,{canvas_height:.3f});',
        r'\begin{scope}[overlay]',
        rf'\clip (0,32) rectangle (450,{image_height+32:.3f});',
        rf'\node[anchor=north west,inner sep=0] at ({-left*scale:.3f},{32-top*scale:.3f})'
        + r' {\includegraphics[width=' + f'{width*scale:.3f}bp'
        + r']{\detokenize{' + source.as_posix() + r'}}};',
        r'\end{scope}',
    ]
    for text, x, y, tx, ty in item['labels']:
        px, py = (tx-left)*scale, 32+(ty-top)*scale
        anchor_y = y+8 if y < 32 else y-8
        lines.extend([
            rf'\draw[overlay,-{{Stealth[length=5bp]}},draw=blue!65!black,line width=.8bp,'
            rf'preaction={{draw=white,line width=1.1bp}}]'
            rf' ({x},{anchor_y}) -- ({px:.3f},{py:.3f});',
            rf'\node[overlay,fill=white,draw=blue!65!black,rounded corners=2bp,'
            rf'inner sep=3bp,font=\sffamily\fontsize{{9}}{{11}}\selectfont]'
            rf' at ({x},{y}) {{{text}}};',
        ])
    if item['name'] not in ['apparatus', 'shaker_settings']:
        axis = 'Time (s)' if 'decay' in item['name'] else 'Frequency (Hz)'
        lines.append(
            rf'\node[overlay,font=\sffamily\fontsize{{9}}{{11}}\selectfont]'
            rf' at (225,{image_height+43:.3f}) {{{axis}}};')
    lines.extend([r'\end{tikzpicture}', r'\end{document}'])
    tex = WORK / (item['name']+'.tex')
    tex.write_text('\n'.join(lines), encoding='utf-8')
    run = subprocess.run(
        ['xelatex', '-interaction=nonstopmode', '-halt-on-error',
         '-output-directory='+str(WORK), str(tex)],
        capture_output=True, text=True)
    if run.returncode:
        raise RuntimeError(run.stdout[-4000:] + run.stderr[-1000:])
    subprocess.run(
        ['pdftoppm', '-singlefile', '-scale-to-x', '1800', '-scale-to-y', '-1',
         '-png', str(tex.with_suffix('.pdf')), str(OUT/item['name'])],
        check=True, capture_output=True)
    print(item['name'], '<-', item['source'])


if __name__ == '__main__':
    WORK.mkdir(parents=True, exist_ok=True)
    OUT.mkdir(parents=True, exist_ok=True)
    for figure in FIGURES:
        build(figure)
