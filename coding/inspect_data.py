"""Inspect the two-table DASP exports without changing the source records."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

ROOT = Path(__file__).resolve().parents[1]

def load_export(path):
    blocks = {'wave': [], 'spectrum': []}
    current = None
    for line in path.read_text(encoding='utf-8-sig').splitlines():
        if 'Time(S)' in line:
            current = 'wave'
        elif 'Frequency(Hz)' in line:
            current = 'spectrum'
        elif current:
            fields = line.split()
            if len(fields) == 3:
                try:
                    blocks[current].append([float(fields[1]), float(fields[2])])
                except ValueError:
                    pass
    return {key: np.array(rows) for key, rows in blocks.items()}

def main():
    fig, axes = plt.subplots(4, 2, figsize=(14, 13))
    for path, ax in zip(sorted((ROOT / 'Lab_results').glob('*.txt')), axes.flat):
        data = load_export(path)
        t, y = data['wave'].T
        f, a = data['spectrum'].T
        mask = (f >= 10) & (f <= 400)
        inds, _ = find_peaks(a)
        inds = [i for i in inds if 10 <= f[i] <= 400]
        inds = sorted(inds, key=lambda i: a[i], reverse=True)[:18]
        print(path.stem, 'samples', len(t), len(f), 'dt', np.median(np.diff(t)),
              'range', y.min(), y.max(), 'tail baseline', np.median(y[t > .85]))
        print('peaks Hz,mV', [(round(f[i], 4), round(a[i], 7)) for i in inds])
        ax.plot(t, y, lw=.7)
        ax.set_title(path.stem)
        ax.grid(alpha=.25)
    fig.tight_layout()
    fig.savefig(ROOT / 'coding' / 'waveform_diagnostics.png', dpi=150)
    plt.close(fig)

if __name__ == '__main__':
    main()
