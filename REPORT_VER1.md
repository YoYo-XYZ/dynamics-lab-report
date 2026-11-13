# Vibration of a simply supported beam

ME31001 Dynamics and Vibrations | Individual laboratory report

## 1. Introduction and objectives

A beam can vibrate in different bending patterns, each with its own natural frequency. In this experiment, a shaker applied a changing sinusoidal excitation to a simply supported beam. Large responses near particular frequencies helped identify its resonances. Knowing these frequencies matters because repeated excitation close to resonance can produce much larger motion than excitation away from resonance [1, pp. 1-3; 2, PDF p. 34].

Two excitation methods were used. A swept-sine test passed through a range of frequencies, while a hammer impact excited several vibration modes in a short time. Comparing their response spectra gave a check on the frequency estimates. A centre mass was then attached to investigate how an increase in moving mass affected the beam [1, pp. 3-4].

The free response after a hammer impact was also recorded. Its amplitude decreased as energy was lost from the system. Logarithmic decrement measures this decrease using the ratio of peaks on the same side of equilibrium. It can be used to estimate the damping ratio for an approximately viscous, underdamped response [2, PDF pp. 24-28]. Repeating the test with an oil damper allowed the change in decay rate to be investigated.

The four objectives were to:

1. Estimate the first three beam frequencies using swept-sine and hammer excitation, and compare the two methods.
2. Measure the effect of an added centre mass on the first two frequencies and compare the first frequency with a simple beam model.
3. Calculate the bare-beam damping ratio from its free decay.
4. Investigate how the oil damper affected the decay and the forced-response peaks.

## 2. Theory

### 2.1 Forced vibration and resonance

Near one well-separated mode, the beam response can be approximated by a single-degree-of-freedom system. This means that one displacement coordinate describes the main motion. The linear equation for harmonic forcing is [1, p. 2; 2, PDF p. 31]

$$
m\ddot{x}+c\dot{x}+kx=P_m\cos(\omega t). \tag{1}
$$

Here, $x$ is displacement from equilibrium in m, $m$ is effective mass in kg, $c$ is the viscous damping coefficient in N s/m, $k$ is stiffness in N/m, and $P_m$ is force amplitude in N. Time $t$ is in s and excitation frequency $\omega$ is in rad/s. The model assumes small motion, constant properties and a damping force proportional to velocity.

The undamped natural frequency and damping ratio are

$$
\omega_n=\sqrt{\frac{k}{m}},\qquad
f_n=\frac{\omega_n}{2\pi},\qquad
\zeta=\frac{c}{2m\omega_n}. \tag{2}
$$

These definitions follow the lecture treatment [2, PDF pp. 9, 24]. For steady-state displacement amplitude $X$, the magnification factor is [2, PDF p. 34]

$$
\frac{X}{P_m/k}=\frac{1}{\sqrt{(1-r^2)^2+(2\zeta r)^2}},
\qquad r=\frac{\omega}{\omega_n}. \tag{3}
$$

The frequency ratio $r$ compares the excitation frequency with the undamped natural frequency. For small damping, the largest displacement occurs close to $r=1$. Increasing damping reduces the displacement magnification around resonance [2, PDF p. 34]. Differentiating the denominator of Equation 3 gives $f_r=f_n\sqrt{1-2\zeta^2}$ for the displacement peak under constant force, provided $\zeta<1/\sqrt{2}$. This relation does not directly locate an acceleration-spectrum peak or a response peak under a varying input force. Therefore, the measured spectrum peaks below are frequency estimates for the tested system, rather than exact undamped natural frequencies.

### 2.2 Free decay and logarithmic decrement

After excitation ends, an underdamped system with $0<\zeta<1$ continues to oscillate with a decreasing amplitude. Its displacement can be written as

$$
x(t)=A e^{-\zeta\omega_n t}\cos(\omega_d t-\phi),
\qquad \omega_d=\omega_n\sqrt{1-\zeta^2}. \tag{4}
$$

The constants $A$ and $\phi$ depend on the initial conditions. The exponential term describes the decay envelope, while $\omega_d$ is the damped natural frequency [2, PDF pp. 25-27]. It differs from both $\omega_n$ and the forced-response peak frequency.

For positive amplitudes $a_1$ and $a_{n+1}$, measured above the equilibrium baseline and separated by $n$ complete cycles,

$$
\delta=\frac{1}{n}\ln\!\left(\frac{a_1}{a_{n+1}}\right),
\qquad
\zeta=\frac{\delta}{\sqrt{(2\pi)^2+\delta^2}}
\approx\frac{\delta}{2\pi}. \tag{5}
$$

Equation 5 rearranges the lecture relation $\delta=2\pi\zeta/\sqrt{1-\zeta^2}$ [2, PDF p. 28]. The approximation applies when damping is small. Using several cycles reduces the influence of a single pair of neighbouring peaks, although it does not remove baseline error or other modes. If the recorded response is $y(t)$ and its baseline is $b$, the amplitudes used are $a_i=y(t_i)-b$. A constant scale factor cancels in the ratio. An unremoved offset does not. This allows a damping estimate from the exported signal without claiming an unverified conversion to displacement.

The method assumes that the chosen interval is dominated by one freely decaying mode and that its damping is approximately viscous. The damped frequency can also be estimated from the peak times using $f_d=n/(t_{n+1}-t_1)$.

### 2.3 Equivalent beam model and higher modes

The lab sheet represents the first bending response using a spring and a mass at the beam centre [1, p. 7]. For a rectangular beam,

$$
I=\frac{bh^3}{12},\qquad
k=\frac{48EI}{L^3},\qquad
m_0=\rho Lbh,\qquad
m=\frac{17}{35}m_0. \tag{6}
$$

Here, $L$, $b$ and $h$ are span, width and thickness in m; $I$ is the second moment of area in m$^4$, denoted $J$ in the lab sheet; $E$ is Young's modulus in Pa; and $\rho$ is density in kg/m$^3$. The total beam mass is $m_0$. The equivalent mass $m$ represents the distributed beam mass in this centre-displacement model, so it is smaller than $m_0$.

The stiffness and $17/35$ mass factor were checked against the equation images on page 7 of the lab sheet. With an added centre mass $m'$, its first-mode prediction is

$$
f_n=\frac{1}{2\pi}\sqrt{\frac{k}{m+m'}}. \tag{7}
$$

This approximation assumes a uniform, slender, linearly elastic beam with ideal simple supports. The attached mass moves with the centre, and the model neglects its size, any attachment stiffness and changes in the assumed deflected shape. It also omits the mass of the accelerometer and other attached equipment. It is used here only for the first mode.

A continuous beam has multiple modes [1, p. 2]. For an ideal uniform beam with pinned ends, the bending shapes are proportional to $\sin(j\pi s/L)$, where $s$ is position along the span and $j$ is the mode number [4, section 10.4.1]. The first mode has maximum motion at the centre; the second has a node there, where displacement is zero. A centre mass should therefore affect the first mode more strongly. Excitation or measurement at a node can also make a mode difficult to observe. These ideal shapes help interpret the experiment, but they were not measured in this lab.

In the sweep, peaks were identified as the excitation passed through modal regions. A hammer supplied a short impulse with a range of frequency components [1, pp. 2-3]. Both methods can reveal modal frequencies, but peak height also depends on where and how the beam is excited. A response spectrum alone does not remove the input-force dependence.

## 3. Experimental procedure

### 3.1 Apparatus and acquisition

The INV1601 teaching system consisted of a simply supported beam, signal generator, shaker, accelerometer, instrumented hammer and two-channel acquisition equipment. The supplied beam dimensions were $L=650$ mm, $b=50$ mm and $h=8$ mm. The material values were $E=210$ GPa and $\rho=7850$ kg/m$^3$. The accelerometer sensitivity specified by the lab sheet was 10 mV per m/s$^2$ [1, p. 1]. These nominal values were used in the theoretical calculation.

The saved DASP screens showed single-channel acquisition. Table 1 distinguishes the settings prescribed by the sheet from those that could be checked in the records [1, pp. 3-6; 3]. The available files did not independently confirm the entered calibration, generator settings or integration configuration.

Table 1. Prescribed settings and settings visible in the saved records.

| Test or setting | Lab-sheet instruction | Evidence in saved files |
|:--|:--|:--|
| Bare and added-mass sweep | ICP input; 10-400 Hz; 60 s; 0.5 A RMS; Peakhold | Single channel and Peakhold visible; generator settings not shown |
| Bare hammer spectrum | Shaker off; repeated impacts; Linear Average | Linear Average visible; displayed average count 28 |
| Free decay | Second-order integration; 2000 Hz; 2000 points | 2000 Hz and **2048 points** recorded |
| Oil-damper sweep | Repeat sweep over 10-200 Hz | Peakhold visible; generator range not independently shown |
| Spectrum processing | Peakhold or Linear Average as above | Peak spectrum, Uniform window and Y-dB display visible |

### 3.2 Frequency tests

For Experiment 1, the beam was excited using the shaker and its response spectrum was saved with Peakhold. This retained the peak response across the sweep, allowing the first three modal regions to be identified. The shaker was then switched off for hammer excitation. Repeated impacts were acquired using Linear Average and the response spectrum was saved [1, p. 3]. Although the hammer contained a force transducer, the saved single-channel records contained response data. They did not establish a measured force-to-response transfer function.

A mass was attached at the centre for Experiment 1, Step 3, and the swept-sine test was repeated [1, p. 4]. The actual mass was not recorded. A value of **1.00 kg was assumed** for the theoretical comparison. This was not a measured value. The mass was removed before Experiments 2 and 3.

### 3.3 Decay and oil-damper tests

The decay procedure called for second-order integration of the accelerometer signal to obtain displacement. After a hammer impact, acquisition was stopped when a clear decay was visible and the record was exported [1, p. 5]. Three bare-beam decay records were available. Each contained 2048 samples at 2000 Hz, rather than the prescribed 2000 samples, giving a sample interval of 0.0005 s and a record duration of 1.024 s. The last sample occurred at 1.0235 s.

For Experiment 3, the oil damper was fitted below the beam and the decay and sweep procedures were repeated [1, p. 6]. No configuration changes between decay repeats were reported. The sheet required the damper connection to be secured with screws; a firm connection was necessary for the intended relative motion. Turning the shaker off before hammering and checking the attachments were the relevant practical precautions in the procedure.

One oil-damper decay had a numerical export. A second decay was visible only in a screenshot, so it was not used for repeat statistics. The file named `Experiment 3 step 2.txt` matched the forced-response screenshot `Experiment 3 step 3.png`. This corrected mapping is recorded in Appendix A.

All waveform exports retained the label `Amplitude(mV)`, including the intended displacement records. The results therefore retain the exported units. No physical displacement conversion was applied.

## 4. Results and calculations

### 4.1 Bare-beam frequency estimates

Each TXT file contained a 2048-sample waveform and a separate 1025-point peak spectrum. The saved spectra were used directly. Their spacing was

$$
\Delta f=\frac{2000}{2048}=0.9765625\ \mathrm{Hz}. \tag{8}
$$

Local maxima were selected in the first three bare-beam modal regions, 40-60, 150-200 and 340-390 Hz. Table 2 compares the two excitation methods. Frequencies are rounded to two decimal places for readability; the bin spacing limits their precision. The method difference is $f_{\mathrm{hammer}}-f_{\mathrm{sweep}}$, with percentage difference calculated relative to the sweep.

Table 2. Bare-beam response-spectrum peaks from the saved exports [3].

| Mode | Swept sine, Hz | Hammer, Hz | Difference, Hz | Difference, % |
|:--|--:|--:|--:|--:|
| 1 | 46.88 | 46.88 | 0.00 | 0.00 |
| 2 | 169.92 | 169.92 | 0.00 | 0.00 |
| 3 | 368.16 | 368.16 | 0.00 | 0.00 |

The methods selected the same bins for all three modes. This shows agreement at the available frequency spacing, rather than proof of identical frequencies to hundredths of a hertz. The lab-sheet table listed 168.9453 Hz for the second mode, one bin below the exported maximum at 169.921875 Hz. The export was used consistently here because it is the experimental data source.

Figure 1 combines the four saved spectra in separate panels. Each spectrum is divided by its own maximum within the plotted range. This allows peak locations to be compared without implying equal excitation or comparable absolute response amplitudes. The sweep spectra were not reconstructed from their instantaneous waveform blocks.

![Figure 1. Saved response spectra for the bare sweep, bare hammer, added-mass sweep and oil-damper sweep. Each panel is independently normalised within its plotted band. Markers identify the peaks used in the tables. The oil-damper panel is restricted to the prescribed 10-200 Hz range. Source: group exports [3].](figures/frequency_spectra.png)

### 4.2 Effect of the centre mass

The first added-mass peak was selected in the 25-45 Hz region and the second in the 145-180 Hz region. The largest peak in the whole spectrum was not assumed to be the first mode. Table 3 shows the changes relative to the bare sweep.

Table 3. Frequency changes with the centre attachment; its mass is assumed to be 1.00 kg for modelling [3].

| Mode | Bare sweep, Hz | Added-mass sweep, Hz | Change, Hz | Change, % |
|:--|--:|--:|--:|--:|
| 1 | 46.88 | 33.20 | -13.67 | -29.17 |
| 2 | 169.92 | 160.16 | -9.77 | -5.75 |

For example, the first-mode percentage change was

$$
\frac{33.203125-46.875}{46.875}\times100=-29.17\%. \tag{9}
$$

The first peak in the export was 33.203125 Hz. The lab sheet listed 34.1797 Hz, again one bin higher. Figure 1 shows a clear low-frequency peak, separate from the stronger response near 160 Hz. The additional peaks near 300 Hz were outside the required first-two-mode comparison and were not assigned a mode solely from their heights.

### 4.3 First-mode theoretical calculation

Using Equation 6 with the nominal beam properties [1, pp. 1, 7],

$$
I=\frac{0.050(0.008)^3}{12}
 =2.1333\times10^{-9}\ \mathrm{m^4},
$$

$$
k=\frac{48(210\times10^9)(2.1333\times10^{-9})}{(0.650)^3}
 =7.8303\times10^4\ \mathrm{N/m},
$$

$$
m_0=7850(0.650)(0.050)(0.008)=2.041\ \mathrm{kg},
\qquad m=\frac{17}{35}(2.041)=0.99134\ \mathrm{kg}.
$$

The bare-beam prediction was

$$
f_{n,0}=\frac{1}{2\pi}\sqrt{\frac{78303}{0.99134}}
 =44.73\ \mathrm{Hz}.
$$

With the **assumed** added mass $m'=1.00$ kg,

$$
f_{n,\mathrm{added}}=\frac{1}{2\pi}\sqrt{\frac{78303}{0.99134+1.00}}
 =31.56\ \mathrm{Hz}. \tag{10}
$$

Table 4 compares these undamped model predictions with the measured sweep peaks. Percentage difference is defined here as $100|f_{\mathrm{measured}}-f_{\mathrm{theory}}|/f_{\mathrm{theory}}$. For example, the bare-beam difference was $100(46.875-44.7299)/44.7299=4.80\%$.

Table 4. First-mode model predictions and measured response peaks.

| Condition | Model $f_n$, Hz | Sweep peak, Hz | Absolute difference, Hz | Difference, % |
|:--|--:|--:|--:|--:|
| Bare beam | 44.73 | 46.88 | 2.15 | 4.80 |
| Added mass, assumed 1.00 kg | 31.56 | 33.20 | 1.64 | 5.21 |

The conditional model reduction was 29.44%, compared with the measured 29.17%. This agreement does not verify the assumed mass.

### 4.4 Free-decay damping estimates

For each decay, the baseline $b$ was estimated as the mean exported response over $0.85<t<1.02$ s. Ten full cycles were used, starting at a positive peak at least 0.05 s after the impact onset visible in the record. For bare repeats 1 and 3, the impact onset was not captured, so the record start was used instead. The selection avoided the earliest transient and the smallest late peaks. No filtering or further integration was applied. Higher-frequency ripple and slow drift remained, particularly in the oil-damper signal, so these are approximate first-mode damping estimates.

Table 5 lists the selected times and baseline-corrected amplitudes. All four estimates used $n=10$. Positive peaks mean maxima above the local equilibrium level, even when their exported values were negative. Figure 2 shows bare repeat 3 and the oil-damper record with their selected maxima and baselines.

Table 5. Inputs to the logarithmic-decrement calculation. Baselines and amplitudes are in $10^{-3}$ mV; times refer to the original exports [3].

| Record | $t_1$, s | $t_{11}$, s | Baseline $b$ | $a_1$ | $a_{11}$ |
|:--|--:|--:|--:|--:|--:|
| Bare repeat 1 | 0.0615 | 0.2745 | -0.2612 | 0.8452 | 0.3252 |
| Bare repeat 2 | 0.5275 | 0.7405 | -0.3363 | 1.4993 | 0.6773 |
| Bare repeat 3 | 0.0630 | 0.2770 | -0.2590 | 1.2890 | 0.6110 |
| Oil damper | 0.3600 | 0.5825 | -0.4420 | 1.0700 | 0.1750 |

![Figure 2. Bare repeat 3 and oil-damper free decay, shown in exported units. Time is shifted separately so that each selected peak 1 occurs at zero. Open circles mark eleven same-side maxima spanning ten cycles; dashed lines show the tail-mean baselines. Peak heights between panels are not used as an absolute response comparison. Source: group waveform exports [3].](figures/free_decay.png)

For a worked example, bare repeat 3 had recorded values $y_1=0.001030$ mV and $y_{11}=0.000352$ mV. Subtracting $b=-0.000258959$ mV gave

$$
a_1=0.001288959\ \mathrm{mV},\qquad
a_{11}=0.000610959\ \mathrm{mV}.
$$

Using Equation 5,

$$
\delta=\frac{1}{10}\ln\!\left(\frac{0.001288959}{0.000610959}\right)
 =0.07466,
$$

$$
\zeta=\frac{0.07466}{\sqrt{(2\pi)^2+0.07466^2}}
 =0.01188,
\qquad \frac{\delta}{2\pi}=0.01188. \tag{11}
$$

The corresponding damped frequency was $f_d=10/(0.2770-0.0630)=46.73$ Hz. For the oil-damper record, the same method gave $\delta=\ln(1.0700/0.1750)/10=0.1811$ and $\zeta=0.02881$. Table 6 contains the full comparison. Ratios were calculated before rounding the amplitudes.

Table 6. Damping and damped-frequency estimates from ten-cycle peak pairs.

| Record | $\delta$ | Exact $\zeta$ | Approx. $\delta/(2\pi)$ | $f_d$, Hz |
|:--|--:|--:|--:|--:|
| Bare repeat 1 | 0.09551 | 0.01520 | 0.01520 | 46.95 |
| Bare repeat 2 | 0.07947 | 0.01265 | 0.01265 | 46.95 |
| Bare repeat 3 | 0.07466 | 0.01188 | 0.01188 | 46.73 |
| Oil damper | 0.18106 | 0.02881 | 0.02882 | 44.94 |

The bare-beam mean was $\bar{\zeta}=0.01324$, or 1.32% of critical damping. The sample standard deviation across three records was 0.00174. This describes repeat variation, not the full measurement uncertainty. The oil-damper estimate was 2.88% of critical damping, about 2.18 times the bare mean. Only one numerical oil-damper decay was available, so an equivalent repeat standard deviation could not be calculated.

As a peak-selection check, keeping the same starting maximum but using six or eight cycles instead of ten gave oil-damper estimates between 0.0248 and 0.0290. A separate baseline check fitted a straight line to the midpoints between positive maxima and interpolated neighbouring troughs over the selected decay region. It gave 0.0268 for the oil damper and 0.0119-0.0151 for the bare records. These checks support a higher damping ratio with the oil damper, while showing that the final digits depend on the analysis choices.

### 4.5 Oil-damper forced response

Table 7 compares the oil-damper sweep peaks within 10-200 Hz with the corresponding bare sweep peaks. The last panel of Figure 1 shows the saved oil-damper response in this range. The third bare-beam mode was outside the prescribed oil-damper sweep range.

Table 7. Forced-response peak frequencies with the oil damper [3].

| Corresponding mode | Bare sweep, Hz | Oil-damper sweep, Hz | Change, Hz | Change, % |
|:--|--:|--:|--:|--:|
| 1 | 46.88 | 44.92 | -1.95 | -4.17 |
| 2 | 169.92 | 170.90 | +0.98 | +0.57 |

The oil-damper first free-decay frequency, 44.94 Hz, was close to its forced-response peak, 44.92 Hz. The values came from different calculations and are not assumed to be the same physical frequency. Absolute spectrum heights were not compared between tests because the available records did not establish equal input force, calibration and response processing.

## 5. Discussion

### 5.1 Added mass and the beam model

The centre attachment lowered the first measured peak by 29.17%, but the second by only 5.75%. Equation 7 explains the first change through increased moving mass. The conditional prediction for a 1.00 kg mass gave a similar percentage reduction. However, both theoretical frequencies were about 5% below the measured peaks, and the actual added mass was unknown. The comparison supports the trend more strongly than the absolute prediction.

The ideal first-mode centre motion makes the centre mass effective, while the ideal second-mode centre node explains its smaller influence [4, section 10.4.1]. The second measured peak still shifted by about ten bins. Possible reasons include the attachment's finite size, imperfect centring and departures from ideal supports. These were not measured separately, so none can be identified as the sole cause. The first-mode lumped model cannot predict that second-mode shift.

The nominal dimensions and support model also affect the theoretical comparison. Equation 6 makes stiffness proportional to $h^3$ and inversely proportional to $L^3$. A shorter effective span or greater restraint against end rotation would tend to raise the frequency relative to the ideal model. Extra moving equipment mass would tend to lower it and therefore would not, by itself, explain a measured frequency above the prediction. Measuring the support span, beam thickness and attached masses would help separate these effects. The 0.98 Hz spectrum spacing also limits how closely the measured and predicted values can be compared.

### 5.2 Swept-sine and hammer methods

Both methods identified the same three frequency bins. The sweep made it possible to build up responses as the excitation passed through each resonance, and Peakhold retained the larger values. Its limitations were the finite sweep rate and the unmeasured variation of shaker force with frequency. A hammer excited several modes quickly, but impact location and contact conditions affected which modes appeared strongly. Linear averaging was intended to reduce variation between acquisitions, although it could not correct an unsuitable impact location or an unmeasured force spectrum [1, pp. 2-3].

The agreement in Table 2 makes the peak locations reasonably consistent. It does not establish equal modal amplitudes or eliminate errors common to both tests. A measured hammer-force channel, controlled impact position and a longer record would improve the comparison. The last change would reduce the frequency-bin spacing at the same sampling rate.

### 5.3 Damping, peak frequency and limitations

The oil damper increased the estimated damping ratio from a bare mean of about 0.0132 to about 0.0288. Figure 2 also shows that the oil-damper oscillation became small within fewer cycles. This agrees with the exponential envelope in Equation 4 [2, PDF pp. 25-28]. Both responses remained underdamped. The baseline and endpoint checks gave a smaller spread than the separation between the bare and oil-damper estimates, so the direction of the damping change is more reliable than its exact ratio.

Higher modes and baseline drift prevented a perfect single-mode decay, especially with the oil damper. The oil signal had visible ripple, which changed the heights and times of individual maxima. The bare repeat spread and missing numerical oil repeat limit the precision of the comparison. Saving several oil-damper records, checking integration and calibration, and choosing a longer interval with a stable baseline would make the estimates more reliable.

The first forced-response peak fell by 1.95 Hz with the damper, while the second changed by just one bin. A displacement resonance can move downward as damping increases [2, PDF p. 34]. However, for damping ratios near 0.03, the displacement-peak correction in Section 2.1 is below 0.1%. It is too small to explain the whole 4.17% first-peak change under an unchanged single-mode model. The attachment may also have changed effective mass, stiffness or support behaviour, and the recorded response quantity and input force were not fully confirmed. The change therefore cannot be attributed entirely to viscous damping. The one-bin second-peak increase is too small for a strong interpretation.

Under equal harmonic force and unchanged mass and stiffness, Equation 3 predicts reduced displacement magnification with greater damping [2, PDF p. 34]. The present spectra cannot test that amplitude prediction quantitatively. Independent normalisation in Figure 1 was used only to display peak locations. A force-normalised response measurement with documented calibration would be needed to compare absolute peak amplitudes fairly.

## 6. Conclusion

The bare-beam sweep and hammer tests identified the same three response peaks at 46.88, 169.92 and 368.16 Hz, within a spectrum spacing of 0.98 Hz. Adding the centre attachment lowered the first two peaks to 33.20 and 160.16 Hz. The first reduction was 29.17%, larger than the second reduction of 5.75%. The first-mode model predicted 44.73 Hz for the bare beam and 31.56 Hz with an assumed 1.00 kg mass; the added-mass prediction remains conditional on that assumption.

Free-decay analysis gave a bare-beam mean damping ratio of 0.01324 across three records and an oil-damper estimate of 0.02881 from one numerical record. The oil damper therefore increased the measured decay rate. Its forced-response peaks were 44.92 and 170.90 Hz. Unknown input force and unverified amplitude calibration prevented a quantitative comparison of absolute peak heights. Baseline drift, modal ripple and the missing oil-damper repeat also limit the damping precision, although the increase remained clear in the sensitivity checks.

## References

[1] ME31001 Dynamics and Vibrations. *Vibration experiment*. Supplied lab sheet, `Lab_details.pdf`, pp. 1-7. Beam properties on p. 1; procedures on pp. 3-6; equivalent beam model on p. 7.

[2] The Hong Kong Polytechnic University. *ME31001 Dynamics and Vibrations lecture slides*. Supplied file, `theory_lecture_slides.pdf`. Natural frequency, PDF p. 9; damped free vibration, PDF pp. 24-28; forced vibration, PDF pp. 31-34. All page references in this report are PDF page numbers, rather than printed slide numbers.

[3] Laboratory group. *Beam vibration experimental records*. Supplied TXT exports and DASP screenshots in `Lab_results/`. File mapping is given in Appendix A. Configuration details and the instructed 1.00 kg mass assumption are recorded in `IMPLEMENTATION_CLARIFICATIONS.md`.

[4] Bower, A. F. *Applied mechanics of solids*, section 10.4.1, "Free vibration of a straight beam without axial force," subsection "Beam with pinned ends." Available at [solidmechanics.org](https://solidmechanics.org/Text/Chapter10_4/Chapter10_4.html). Accessed 13 November 2026. Used for the ideal beam mode shapes.

## Appendix A. Data mapping and reproducibility

Table A1. Mapping used for the supplied records. All filenames are within `Lab_results/`.

| TXT filename | Test represented | Matching screenshot |
|:--|:--|:--|
| `Experiment 1 step 1.txt` | Bare swept-sine spectrum | `Experiment 1 step 1.png` |
| `Experiment 1 step 2.txt` | Bare hammer spectrum | `Experiment 1 step 2.png` |
| `Experiment 1 step 3.txt` | Added-mass swept-sine spectrum | `Experiment 1 step 3.png` |
| `Experiment 2 step 1.txt` | Bare decay repeat 1 | `Experiment 2 step 1.png` |
| `Experiment 2 step 2.txt` | Bare decay repeat 2 | `Experiment 2 step 2.png` |
| `Experiment 2 step 3.txt` | Bare decay repeat 3 | `Experiment 2 step 3.png` |
| `Experiment 3 step 1.txt` | Oil-damper decay | `Experiment 3 step 1.png` |
| `Experiment 3 step 2.txt` | Oil-damper swept-sine spectrum | **`Experiment 3 step 3.png`** |
| No matching TXT | Second oil-damper decay | `Experiment 3 step 2.png` |

The analysis script `coding/analyse_results.py` parses the waveform and spectrum blocks separately and checks their lengths and sampling grids. It generates both figures, `coding/results/analysis.json` and `coding/results/selected_peaks.csv`. The CSV retains all eleven selected maxima for each damping calculation. The TXT files export decay amplitudes to $10^{-6}$ mV, which further limits the smaller peaks. The analysis does not replace or modify the original records.

To reproduce the calculations and build the PDF from this Markdown file, run `python coding/analyse_results.py` and `python coding/build_report.py`. Required Python packages and build instructions are listed in `coding/README.md`.
