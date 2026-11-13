---
header-includes:
  - \setlength{\parskip}{3pt}
---

# Vibration of a simply supported beam

ME31001 Dynamics and Vibrations | Individual laboratory report

Thammatorn Jamraschai | Student ID: 24106318

## 1. Introduction and objectives

A beam can vibrate at several natural frequencies. When a repeated force acts close to one of these frequencies, the vibration becomes larger. This is resonance. The lecture response curves show why damping matters near resonance, since a lightly damped system can have a large response [1, 2].

This lab used a shaker and a hammer to find the beam's frequencies. The shaker swept through a frequency range, while a hammer impact excited several frequencies at once. A mass was then attached at the centre to study its effect [1].

The vibration after an impact gradually died away. Logarithmic decrement uses the decrease between successive peaks to estimate damping [2]. Repeating the test with an oil damper allowed the decay and forced response to be compared.

The objectives were to compare the first three frequencies from swept-sine and hammer tests, measure the effect of a centre mass on the first two frequencies, calculate the bare-beam damping ratio, and investigate the oil damper’s effect on decay and forced response.

## 2. Theory

### 2.1 Natural frequency

The lecture mass-spring model relates natural frequency to stiffness and moving mass [2]:

$$
\omega_n=\sqrt{\frac{k}{m}},\qquad
f_n=\frac{\omega_n}{2\pi}.
$$

Here, $k$ is stiffness in N/m and $m$ is mass in kg. The natural frequency is $\omega_n$ in rad/s or $f_n$ in Hz. For the beam, an equivalent mass is used to represent its distributed mass.

### 2.2 Forced vibration and resonance

During a swept-sine test, the shaker applies a harmonic force. The lecture equation balances this force with the mass, damping and spring terms [2]:

$$
m\ddot{x}+c\dot{x}+kx=P_m\cos(\omega t).
$$

The displacement $x$ is in m, time $t$ is in s, and $c$ is the damping coefficient in N s/m. The force amplitude is $P_m$ in N, and $\omega$ is the excitation frequency in rad/s.

The damping ratio compares $c$ with the critical damping coefficient $c_c$ [2]:

$$
\zeta=\frac{c}{c_c}=\frac{c}{2m\omega_n}.
$$

For steady vibration, the magnification factor gives the displacement amplitude $X$ relative to the static displacement $P_m/k$ [2]:

$$
M=\frac{X}{P_m/k}
=\frac{1}{\sqrt{(1-r^2)^2+(2\zeta r)^2}},
\qquad r=\frac{\omega}{\omega_n}.
$$

For small damping, resonance occurs near $r=1$. The lecture curves show a lower displacement peak when damping increases under the same applied force [2].

### 2.3 Free decay and damping measurement

After the hammer force ends, an underdamped system keeps oscillating with decreasing amplitude. The lecture free-response equation can be written as [2]:

$$
x(t)=A e^{-\zeta\omega_n t}\cos(\omega_d t-\phi),
\qquad \omega_d=\omega_n\sqrt{1-\zeta^2}.
$$

Here, $A$ is the starting envelope amplitude in m and $\phi$ is the phase in rad. Both depend on the starting motion. The damped frequency is $\omega_d$ in rad/s, and $e^{-\zeta\omega_n t}$ describes the decreasing amplitude.

Logarithmic decrement measures the decrease between peaks on the same side of equilibrium. Over $n$ complete cycles, the lecture peak-ratio method gives [2, 1]:

$$
\delta=\frac{1}{n}\ln\left(\frac{a_1}{a_{n+1}}\right),
\qquad \zeta\approx\frac{\delta}{2\pi}
\quad\text{for small damping}.
$$

The amplitudes $a_1$ and $a_{n+1}$ are measured from the equilibrium baseline, the resting signal level. Both $\delta$ and $\zeta$ are dimensionless. The calculation assumes that one vibration mode mainly controls the selected decay.

### 2.4 Applying the mass-spring model to the beam

The lab sheet treats the first beam mode as a spring with an equivalent mass at its centre. For a rectangular beam, the required properties are [1]:

$$
I=\frac{bh^3}{12},\qquad
k=\frac{48EI}{L^3},\qquad
m_0=\rho Lbh,\qquad
m=\frac{17}{35}m_0.
$$

Here $L$, $b$ and $h$ are the span, width and thickness; $I$ is the second moment of area, $E$ is Young's modulus and $\rho$ is density. The beam mass is $m_0$ and its equivalent mass is $m$.

An added centre mass $m'$ moves with the beam centre. The first-frequency prediction becomes [1]:

$$
f_n=\frac{1}{2\pi}\sqrt{\frac{k}{m+m'}}.
$$

This model assumes a uniform beam with ideal simple supports and small elastic motion. A beam has several natural frequencies, but this calculation predicts only the first [1].

### 2.5 Swept-sine and hammer methods

The swept-sine method finds response peaks as the shaker frequency changes. A hammer supplies a short impact containing a range of frequencies, so several peaks can be found from one test [1]. The saved records contain response spectra. Their peaks estimate the beam frequencies; the damped free frequency and forced-response peak frequency need not be identical.

## 3. Experimental procedure

### 3.1 Apparatus

The INV1601 system included a simply supported beam, signal generator, shaker, accelerometer, instrumented hammer and data acquisition equipment. The supplied beam properties were $L=650$ mm, $b=50$ mm, $h=8$ mm, $E=210$ GPa and $\rho=7850$ kg/m$^3$. The specified accelerometer sensitivity was 10 mV per m/s$^2$ [1].

Figure 1 identifies the main parts in a photograph from the lab session. The oil damper is shown fitted for the damping test.

![Figure 1. Lab apparatus, including the beam, accelerometer, support, hammer, oil damper and shaker. Labels have been added to the session photograph, experiment_setup_closeup.png [3].](figures/lab/apparatus.png){width=45%}

### 3.2 Frequency tests

Single-channel acquisition was used. The lab settings specified ICP input, the stated accelerometer sensitivity, and a 10-400 Hz sweep lasting 60 s at 0.5 A RMS. Peakhold retained the response peaks during the sweep, and the first three frequencies were recorded [1,  3].

The controller photograph in Figure 2 shows the sweep range, time and current settings.

![Figure 2. Controller settings photographed during the lab: 10-400 Hz sweep, 60 s sweep time and 0.500 A RMS current. Cropped from experiment_shaker_config.png, with labels added [3].](figures/lab/shaker_settings.png){width=35%}

The shaker was switched off before hammer testing. Repeated impacts were recorded using Linear Average to obtain a stable spectrum. A 1.00 kg mass was then attached at the beam centre and the sweep was repeated for the first two frequencies [1]. It was removed before the decay and oil-damper tests.

### 3.3 Free decay and oil-damper tests

The lab procedure specified second-order integration to obtain displacement from acceleration. The beam was struck with the hammer, and acquisition was stopped when a clear decay was visible [1]. Three bare-beam records were saved at 2000 Hz. Each contained 2048 points, rather than the 2000 points prescribed by the sheet [3].

The oil damper was fitted below the beam and secured with screws. The decay test was repeated, followed by a swept-sine test over 10-200 Hz [1]. Switching off the shaker before hammering and securing the attachments were the main practical precautions.

One oil-damper decay had numerical data; a second was available only as a screenshot. All exported waveforms were labelled mV, so these units were retained rather than applying an unverified displacement conversion [3].

## 4. Results and calculations

### 4.1 Bare-beam frequencies

Table 1 compares the peaks in the saved spectra. The frequency spacing was about 0.98 Hz, so matching values mean agreement within this spacing.

Table 1. Bare-beam frequencies from swept-sine and hammer tests [3].

| Mode | Swept sine, Hz | Hammer, Hz | Hammer minus sweep, Hz |
|:--|--:|--:|--:|
| 1 | 46.88 | 46.88 | 0.00 |
| 2 | 169.92 | 169.92 | 0.00 |
| 3 | 368.16 | 368.16 | 0.00 |

Figure 3 shows the peaks for all four frequency tests. Each panel is divided by its own maximum to compare peak positions.

![Figure 3. Response spectra for the bare sweep, bare hammer, added-mass sweep and oil-damper sweep. Each panel is normalised separately, so heights do not compare absolute responses. Markers show the frequencies used in the tables. The oil-damper data cover 10-200 Hz [3].](figures/frequency_spectra.png){width=55%}

Figures 4 and 5 show the original bare-beam DASP spectra. The table values use exported peaks rather than the software's main-frequency readout [3].

```{=latex}
\begingroup
\def\toprule{}
\def\midrule{}
\def\bottomrule{}
```

| ![Figure 4. Bare-beam swept-sine spectrum [3].](figures/lab/bare_sweep.png){width=90%} | ![Figure 5. Bare-beam hammer spectrum [3].](figures/lab/bare_hammer.png){width=90%} |
|:--:|:--:|
| Figure 4. Bare sweep. | Figure 5. Bare hammer. |

```{=latex}
\endgroup
```

### 4.2 Added centre mass

Both measured frequencies decreased with the centre mass, as shown in Table 2.

Table 2. Frequency changes with the added centre mass [3].

| Mode | Bare sweep, Hz | Added-mass sweep, Hz | Change, Hz | Change, % |
|:--|--:|--:|--:|--:|
| 1 | 46.88 | 33.20 | -13.67 | -29.17 |
| 2 | 169.92 | 160.16 | -9.77 | -5.75 |

The percentage change uses the bare frequency as the starting value. For the first mode,

$$
\text{Change}=\frac{33.203125-46.875}{46.875}\times100=-29.17\%.
$$

The supplied lab-sheet entries were one frequency bin away from the exported maxima for the bare second and added-mass first peaks. The saved export maxima were used consistently here.

The original added-mass and oil-damper spectra are shown in Figures 6 and 7 [3]. Figure 7 corresponds to the numerical oil-damper sweep export.

```{=latex}
\begingroup
\def\toprule{}
\def\midrule{}
\def\bottomrule{}
```

| ![Figure 6. Added-mass swept-sine spectrum [3].](figures/lab/added_mass.png){width=90%} | ![Figure 7. Oil-damper swept-sine spectrum [3].](figures/lab/oil_sweep.png){width=65%} |
|:--:|:--:|
| Figure 6. Added-mass sweep. | Figure 7. Oil-damper sweep. |

```{=latex}
\endgroup
```

### 4.3 Theoretical first frequency

Using the beam-property equations and the supplied dimensions [1] gives $I=2.1333\times10^{-9}$ m$^4$, $k=7.8303\times10^4$ N/m, $m_0=2.041$ kg and $m=0.99134$ kg. The first-frequency equation then gives

$$
f_{\mathrm{bare}}=\frac{1}{2\pi}\sqrt{\frac{78303}{0.99134}}=44.73\ \mathrm{Hz},\quad
f_{\mathrm{added}}=\frac{1}{2\pi}\sqrt{\frac{78303}{0.99134+1.00}}=31.56\ \mathrm{Hz}.
$$

Table 3 compares the predictions with the sweep results. Percentage difference is $100|f_{\mathrm{measured}}-f_{\mathrm{theory}}|/f_{\mathrm{theory}}$; for the bare beam it is 4.80%.

Table 3. Theoretical and measured first frequencies.

| Condition | Theory, Hz | Measured, Hz | Difference, % |
|:--|--:|--:|--:|
| Bare beam | 44.73 | 46.88 | 4.80 |
| Added mass, 1.00 kg | 31.56 | 33.20 | 5.21 |

### 4.4 Free decay and damping ratio

Figure 8 shows one bare decay and the oil-damper decay. For each record, the equilibrium baseline was estimated from the mean response over $0.85<t<1.02$ s. Eleven positive peaks spanning ten cycles were selected after the early part of the decay. A constant conversion factor cancels in the peak ratio, so the exported mV amplitudes were used.

![Figure 8. Free decay for bare repeat 3 and the oil damper, in exported units. Time is measured from each record's selected peak 1. Circles mark eleven same-side peaks, and dashed lines show the equilibrium baselines. Peak amplitudes were measured above these lines [3].](figures/free_decay.png){width=55%}

For bare repeat 3, subtracting the baseline of $-0.000258959$ mV gives $a_1=0.001288959$ mV and $a_{11}=0.000610959$ mV. These peaks are ten cycles apart, so the logarithmic decrement relation gives

$$
\delta=\frac{1}{10}\ln\left(\frac{0.001288959}{0.000610959}\right)=0.07466,\qquad
\zeta\approx\frac{0.07466}{2\pi}=0.01188.
$$

Table 4 gives the results using the same method for all records. The baseline-corrected oil-damper peaks were 0.0010700 and 0.0001750 mV.

Table 4. Logarithmic decrement and damping ratio over ten cycles [3].

| Record | $a_1$, $10^{-3}$ mV | $a_{11}$, $10^{-3}$ mV | $\delta$ | $\zeta\approx\delta/(2\pi)$ |
|:--|--:|--:|--:|--:|
| Bare repeat 1 | 0.8452 | 0.3252 | 0.09551 | 0.01520 |
| Bare repeat 2 | 1.4993 | 0.6773 | 0.07947 | 0.01265 |
| Bare repeat 3 | 1.2890 | 0.6110 | 0.07466 | 0.01188 |
| Oil damper | 1.0700 | 0.1750 | 0.18106 | 0.02882 |

The three bare estimates ranged from 0.01188 to 0.01520, with a mean of 0.01324. The oil-damper estimate was 0.02882, about 2.18 times the bare mean.

Figures 9 and 10 show the original decay captures. Their time axes and offsets are as captured; Figure 8 shows the peaks used in the calculations [3].

```{=latex}
\begingroup
\def\toprule{}
\def\midrule{}
\def\bottomrule{}
```

| ![Figure 9. Bare-beam decay [3].](figures/lab/bare_decay.png){width=90%} | ![Figure 10. Oil-damper decay [3].](figures/lab/oil_decay.png){width=90%} |
|:--:|:--:|
| Figure 9. Bare decay. | Figure 10. Oil-damper decay. |

```{=latex}
\endgroup
```

### 4.5 Oil-damper forced response

Table 5 compares the oil-damper sweep with the bare sweep. The corresponding spectra appear in Figure 3.

Table 5. Forced-response peak frequencies with the oil damper [3].

| Mode | Bare sweep, Hz | Oil-damper sweep, Hz | Change, Hz | Change, % |
|:--|--:|--:|--:|--:|
| 1 | 46.88 | 44.92 | -1.95 | -4.17 |
| 2 | 169.92 | 170.90 | +0.98 | +0.57 |

The third bare frequency was outside the 10-200 Hz oil-damper sweep range.

## 5. Discussion

### 5.1 Added mass and theoretical prediction

The first-frequency equation predicts that adding mass lowers the first frequency if stiffness is unchanged [1, 2]. The measured reduction was 29.17%, close to the predicted 29.44%. The second frequency fell by only 5.75%; the first-mode model cannot predict this change. Both measured first frequencies were about 5% above the predictions, possibly because the supports differed from the ideal simple supports. Checking the supports would improve the comparison.

### 5.2 Swept-sine and hammer tests

Both methods found the same three frequency bins, within the 0.98 Hz spacing. The sweep made resonance easy to follow, but took longer and depended on allowing the response to build up. Hammer testing was quick and excited several frequencies, but depended on the strike position and impact. Linear Average helped stabilise the spectrum [1]. Consistent strikes and longer records would improve repeatability and frequency resolution.

### 5.3 Oil damper and limitations

The oil-damper damping ratio was 0.02882, compared with the bare mean of 0.01324. This agrees with its faster decay in Figure 8 and the free-decay envelope [2]. Both responses remained underdamped. At resonance the magnification factor gives $M=1/(2\zeta)$, so greater damping predicts a lower displacement peak for the same force and stiffness [2]. The saved tests did not establish equal force or matching calibration, so peak heights cannot confirm this.

The oil damper shifted the first peak down by 1.95 Hz and the second up by one frequency bin. These shifts alone do not measure damping. Ripple and baseline drift affect the decay peak ratios, and only one numerical oil-damper decay was available. More repeated decays would improve the comparison.

## 6. Conclusion

Swept-sine and hammer tests gave the same bare-beam frequencies of 46.88, 169.92 and 368.16 Hz within the 0.98 Hz spectrum spacing.

The centre mass reduced the first two frequencies to 33.20 and 160.16 Hz. The first-mode reduction of 29.17% agreed with the mass-spring relationship. The theoretical first frequencies were 44.73 Hz bare and 31.56 Hz with the 1.00 kg mass, both about 5% below measurement.

Logarithmic decrement gave a mean bare damping ratio of 0.01324 and an oil-damper value of 0.02882. The oil damper produced faster free decay, consistent with the lecture response equation. Its forced-response peaks were 44.92 and 170.90 Hz. The peak-height effect could not be confirmed from the available measurements, and more oil-damper decay records would improve the damping comparison.

### References

[1] ME31001 Dynamics and Vibrations. *Vibration experiment*. Supplied laboratory sheet, Lab_details.pdf.

[2] ME31001 Dynamics and Vibrations. *Lecture material on free and forced vibration*. Supplied theory_lecture_slides.pdf.

[3] Group experimental records. Lab_results/, Experiments 1-3, TXT exports and saved screenshots. Oil-damper sweep data are in Experiment 3 step 2.txt, matching Experiment 3 step 3.png; the numerical oil-damper decay is Experiment 3 step 1.txt.
