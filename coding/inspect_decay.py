"""Print cycle extrema and baseline candidates for selecting decay intervals."""
from inspect_data import ROOT, load_export
import numpy as np
from scipy.signal import find_peaks

for filename, start in [('Experiment 2 step 1.txt', 0),
                        ('Experiment 2 step 2.txt', .46),
                        ('Experiment 2 step 3.txt', 0),
                        ('Experiment 3 step 1.txt', .30)]:
    t, y = load_export(ROOT / 'Lab_results' / filename)['wave'].T
    p, _ = find_peaks(y, distance=34, prominence=.00001)
    q, _ = find_peaks(-y, distance=34, prominence=.00001)
    p = p[(t[p] > start + .05) & (t[p] < start + .40)]
    baseline = np.mean(y[(t > .85) & (t < 1.02)])
    local = (y[p] + np.interp(t[p], t[q], y[q])) / 2
    coeff = np.polyfit(t[p], local, 1)
    print(filename, 'tail mean', baseline, 'local baseline slope, intercept', coeff)
    print('peaks t,y,local baseline', list(zip(t[p].round(4), y[p], local.round(8))))
    for n in [6, 8, 10]:
        if len(p) <= n:
            continue
        i, j = p[0], p[n]
        for label, base in [('tail', np.full(len(t), baseline)), ('local', np.polyval(coeff,t))]:
            a, b = y[i]-base[i], y[j]-base[j]
            d = np.log(a / b) / n
            z = d / np.sqrt(4*np.pi**2+d*d)
            print(n,label, 'times',t[i],t[j],'amplitudes',a,b,'delta',d,'zeta',z,'fd',n/(t[j]-t[i]))
