"""Reproduce report calculations and figures from the untouched DASP exports.

Run from any directory: python coding/analyse_results.py
Frequency bands identify corresponding modal regions, not global maxima.
No FFT is applied to instantaneous sweep waveforms.
"""
import csv
import json
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
from inspect_data import ROOT, load_export

OUT = ROOT / 'coding' / 'results'
FIG = ROOT / 'figures'
MAPPING = {
    'bare_sweep': ('Experiment 1 step 1', 'bare beam, swept sine, Peakhold'),
    'bare_hammer': ('Experiment 1 step 2', 'bare beam, hammer, Linear Average'),
    'mass_sweep': ('Experiment 1 step 3', 'added centre mass, swept sine, Peakhold'),
    'bare_decay_1': ('Experiment 2 step 1', 'bare beam, decay repeat 1'),
    'bare_decay_2': ('Experiment 2 step 2', 'bare beam, decay repeat 2'),
    'bare_decay_3': ('Experiment 2 step 3', 'bare beam, decay repeat 3'),
    'oil_decay': ('Experiment 3 step 1', 'oil damper, decay, one numeric export'),
    'oil_sweep': ('Experiment 3 step 2', 'oil damper, swept sine; matches step 3 PNG'),
}
DECAY_STARTS = {'bare_decay_1':0, 'bare_decay_2':.46, 'bare_decay_3':0, 'oil_decay':.30}

def load_all():
    records = {}
    for key, (stem, condition) in MAPPING.items():
        data = load_export(ROOT / 'Lab_results' / (stem + '.txt'))
        assert data['wave'].shape == (2048, 2), stem
        assert data['spectrum'].shape == (1025, 2), stem
        assert all(np.isfinite(a).all() for a in data.values()), stem
        np.testing.assert_allclose(data['wave'][:, 0], np.arange(2048)/2000, atol=1e-9)
        np.testing.assert_allclose(data['spectrum'][:, 0], np.arange(1025)*2000/2048, atol=.000051)
        assert (data['spectrum'][:, 1] >= 0).all(), stem
        records[key] = data
    return records

def peak_in_band(data, lo, hi):
    f, a = data['spectrum'].T
    ids, _ = find_peaks(a)
    ids = ids[(f[ids] >= lo) & (f[ids] <= hi)]
    i = ids[np.argmax(a[ids])]
    return {'frequency_Hz': float(f[i]), 'SpecPeak_mV': float(a[i])}

def decay(data, start):
    t, y = data['wave'].T
    baseline = np.mean(y[(t > .85) & (t < 1.02)])
    peaks, _ = find_peaks(y, distance=34, prominence=.00001)
    peaks = peaks[(t[peaks] > start+.05) & (t[peaks] < start+.40)]
    assert len(peaks) >= 11
    # Check there is one main maximum per fundamental cycle.
    assert np.all((np.diff(t[peaks]) > .017) & (np.diff(t[peaks]) < .026))
    selected = peaks[:11]
    i, j = selected[0], selected[-1]
    amplitudes = y[selected] - baseline
    assert np.all(amplitudes > 0)
    delta = np.log(amplitudes[0] / amplitudes[-1]) / 10
    zeta = delta / np.sqrt((2*np.pi)**2 + delta**2)
    # Sensitivity to end-peak choice, same start peak, 6/8/10 cycles.
    sensitivity = []
    for n in [6, 8, 10]:
        d = np.log(amplitudes[0]/amplitudes[n]) / n
        sensitivity.append(float(d/np.sqrt((2*np.pi)**2+d*d)))
    # Independent baseline sensitivity: linear fit to cycle midpoints.
    troughs, _ = find_peaks(-y, distance=34, prominence=.00001)
    midpoints = (y[peaks]+np.interp(t[peaks],t[troughs],y[troughs]))/2
    slope, intercept = np.polyfit(t[peaks], midpoints, 1)
    corrected = y[selected] - (slope*t[selected]+intercept)
    d = np.log(corrected[0]/corrected[-1])/10
    return {'baseline_mV': float(baseline), 't1_s': float(t[i]), 't11_s': float(t[j]),
            'y1_mV': float(y[i]), 'y11_mV': float(y[j]),
            'a1_mV': float(amplitudes[0]), 'a11_mV': float(amplitudes[-1]),
            'n_cycles': 10, 'delta': float(delta), 'zeta': float(zeta),
            'zeta_approx': float(delta/(2*np.pi)),
            'fd_Hz': float(10/(t[j]-t[i])), 'peak_indices': selected.tolist(),
            'zeta_6_8_10_cycles': sensitivity,
            'local_baseline_zeta': float(d/np.sqrt((2*np.pi)**2+d*d)),
            'local_baseline_slope_mV_per_s': float(slope),
            'local_baseline_intercept_mV': float(intercept)}

def figures(records, frequency, damping):
    plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 10,
                         'axes.spines.top': False, 'axes.spines.right': False})
    keys = ['bare_sweep','bare_hammer','mass_sweep','oil_sweep']
    colors = ['#1d5b8f','#a35d00','#397a46','#8b467b']
    fig, axes = plt.subplots(4, 1, figsize=(8.0, 7.4), sharex=True)
    for ax, key, color in zip(axes, keys, colors):
        f, a = records[key]['spectrum'].T
        upper = 200 if key == 'oil_sweep' else 400
        keep = (f >= 10) & (f <= upper)
        normal = np.max(a[keep])
        ax.plot(f[keep], a[keep]/normal, color=color, lw=1.0)
        for n, result in enumerate(frequency[key], 1):
            hz, amp = result.values()
            yy = amp/normal
            ax.plot(hz, yy, 'o', color=color, ms=4)
            offset = (8,-13) if key == 'mass_sweep' and n == 2 else (5,8)
            ax.annotate(f'{hz:.2f} Hz', (hz, yy), xytext=offset,
                        textcoords='offset points', fontsize=9)
        ax.set_ylim(0, 1.3)
        ax.text(.02,.95,MAPPING[key][1].split(';')[0],transform=ax.transAxes,fontsize=9,va='top')
        ax.grid(alpha=.18)
    axes[-1].set_xlim(10,400)
    axes[-1].set_xlabel('Frequency (Hz)')
    fig.supylabel('Saved peak spectrum / maximum in plotted band (dimensionless)', x=.015, fontsize=10)
    fig.tight_layout(rect=(.03,0,1,1),h_pad=.7)
    fig.savefig(FIG/'frequency_spectra.png',dpi=240)
    plt.close(fig)

    fig, axes = plt.subplots(1,2,figsize=(8,3.2),sharex=True)
    for ax, key, color, title in zip(axes,['bare_decay_3','oil_decay'],[colors[0],colors[3]],
                                    ['Bare beam, repeat 3','Oil damper, numeric record']):
        t, y = records[key]['wave'].T
        d = damping[key]
        ax.plot(t-d['t1_s'], y*1e3, color=color,lw=.85)
        ax.axhline(d['baseline_mV']*1e3,color='grey',ls='--',lw=1,label='Tail mean baseline')
        ids = d['peak_indices']
        ax.plot(t[ids]-d['t1_s'],y[ids]*1e3,'o',mfc='white',mec=color,ms=3)
        for j, label in [(0,'1'),(-1,'11')]:
            i=ids[j]
            ax.annotate(f'Peak {label}',(t[i]-d['t1_s'],y[i]*1e3),xytext=(4,12),
                        textcoords='offset points',fontsize=9)
        ax.set_title(title,fontsize=10)
        ax.set_xlim(-.025,.60)
        ax.set_ylim(-2.5,1.8)
        ax.set_xlabel('Time from selected peak 1 (s)')
        ax.grid(alpha=.18)
        ax.legend(fontsize=8,loc='lower right')
    axes[0].set_ylabel('Exported response (10$^{-3}$ mV)')
    fig.tight_layout()
    fig.savefig(FIG/'free_decay.png',dpi=240)
    plt.close(fig)

def main():
    OUT.mkdir(exist_ok=True,parents=True)
    FIG.mkdir(exist_ok=True)
    records = load_all()
    bands = {'bare_sweep': [(40,60),(150,200),(340,390)],
             'bare_hammer': [(40,60),(150,200),(340,390)],
             'mass_sweep': [(25,45),(145,180)],
             'oil_sweep': [(35,60),(150,195)]}
    frequency = {key:[peak_in_band(records[key],lo,hi) for lo,hi in ranges]
                 for key,ranges in bands.items()}
    damping = {key:decay(records[key],start) for key,start in DECAY_STARTS.items()}
    L,b,h,E,rho,added = .650,.050,.008,210e9,7850.,1.00  # Actual added mass confirmed by the user.
    inertia=b*h**3/12
    stiffness=48*E*inertia/L**3
    total=rho*L*b*h
    equivalent=17/35*total
    f0=np.sqrt(stiffness/equivalent)/(2*np.pi)
    f1=np.sqrt(stiffness/(equivalent+added))/(2*np.pi)
    theory={'I_m4':inertia,'k_N_per_m':stiffness,'beam_mass_kg':total,
            'equivalent_mass_kg':equivalent,'added_mass_kg':added,
            'bare_fn_Hz':f0,'added_fn_Hz':f1,'predicted_change_percent':100*(f1/f0-1)}
    comparisons={}
    for key in ['mass_sweep','oil_sweep']:
        comparisons[key]=[{'change_Hz':r['frequency_Hz']-frequency['bare_sweep'][j]['frequency_Hz'],
                           'change_percent':100*(r['frequency_Hz']/frequency['bare_sweep'][j]['frequency_Hz']-1)}
                          for j,r in enumerate(frequency[key])]
    theory['bare_error_percent']=100*abs(frequency['bare_sweep'][0]['frequency_Hz']-f0)/f0
    theory['added_error_percent']=100*abs(frequency['mass_sweep'][0]['frequency_Hz']-f1)/f1
    zz=[damping[key]['zeta'] for key in DECAY_STARTS if key.startswith('bare')]
    summary={'bare_zeta_mean':float(np.mean(zz)),'bare_zeta_sample_sd':float(np.std(zz,ddof=1)),
             'oil_to_bare_mean_ratio':float(damping['oil_decay']['zeta']/np.mean(zz))}
    result={'file_mapping':MAPPING,'frequency':frequency,'damping':damping,
            'theory':theory,'comparisons':comparisons,'summary':summary}
    (OUT/'analysis.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    with (OUT/'selected_peaks.csv').open('w',newline='',encoding='utf-8') as stream:
        writer=csv.writer(stream)
        writer.writerow(['record','peak_number','time_s','raw_response_mV','baseline_corrected_mV'])
        for key,d in damping.items():
            for n,i in enumerate(d['peak_indices'],1):
                t,y=records[key]['wave'][i]
                writer.writerow([key,n,t,y,y-d['baseline_mV']])
    figures(records,frequency,damping)
    print(json.dumps({'theory':theory,'summary':summary,'changes':comparisons},indent=2))
    print('Validated all 8 files: waveform lengths, spectrum lengths, time/frequency grids and finite values.')

if __name__ == '__main__':
    main()
