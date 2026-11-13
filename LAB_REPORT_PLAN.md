# Lab report plan

## Purpose and approach

Write an individual report covering all three experiments and four lab objectives. Follow the six sections in `Assignment_criteria.pdf`. Use `Lab_details.pdf` for the experiment, `Lab_results/` for measurements, and `theory_lecture_slides.pdf` for the theoretical explanation.

### Agreed direction after reviewing the first implementation

The first implementation was too technical and difficult to read. More lecture citations alone will not fix this. The explanation must use the ideas and equations taught in the lectures to make sense of the experiment.

- Explain the relevant lecture theory together in Section 2. In the discussion, refer back to those equations and use them to explain the results. Do not repeat the theory in full.
- Include only what the assignment needs. Omit optional extra analysis, including an appendix of optional analysis.
- Use concise, natural second-year student writing. Put a few clear sentences around each equation and result, rather than long explanations of the physics in words.
- Put a short explanation before each equation so the reader knows what it describes. Let the equation show the relationship, then give the numerical result or a brief interpretation if needed. Define symbols once and state the condition that matters.
- Keep necessary assumptions and limitations accurate and brief. State each at the relevant point and avoid repeating it throughout the report.
- Keep the six-section structure, required calculations, units, figures and citations. Simpler writing must still explain how the results answer the four objectives.

### Writing pattern

In theory, use: short explanation of the lecture concept → equation → symbol definitions where needed. In discussion, use: short explanation connecting the result to the theory → relevant equation → measured result and brief comparison. Do not present an equation without first giving the reader its purpose. Avoid explaining the same relationship again after the equation.

For example, introduce the natural-frequency equation in theory with a short explanation:

"The natural frequency depends on the beam's stiffness and moving mass. Using the lecture mass-spring model,"

$$
f_n=\frac{1}{2\pi}\sqrt{\frac{k}{m}}.
$$

Define $k$ and $m$ as stiffness and equivalent mass, with units. Then discuss the added-mass result with a short explanation before the relationship:

"Adding mass lowers the natural frequency if the stiffness stays the same. From the theory equation,"

$$
\frac{f_{\mathrm{added}}}{f_{\mathrm{bare}}}
=\sqrt{\frac{m}{m+m'}}<1,\qquad m'>0.
$$

"The first frequency fell from 46.88 Hz to 33.20 Hz, which agrees with this relationship."

This example illustrates the preferred balance of maths and text. Use simple words such as mass, stiffness, force, frequency and decay. Introduce a technical term only when it helps explain a required concept. Avoid dense sentences, repeated qualifications and descriptions of the analysis software.

The suggested proportions below follow the marking weights. They are a guide, not a required word count. Treat them as flexible guidance and allow space for the essential figures, tables and worked examples.

## 1. Introduction and objectives: about 15%

- Introduce vibration of a simply supported beam and explain why resonance and natural frequencies matter here.
- Briefly introduce swept-sine and hammer excitation, free decay and logarithmic decrement. Leave derivations for theory.
- State the four objectives in your own words: find frequencies with both excitation methods, investigate added mass, determine damping from free decay, and investigate the oil damper's effect.
- Explain what was investigated and why without presenting conclusions before the results.

**Sources:** `Lab_details.pdf`, `Assignment_criteria.pdf`, `theory_lecture_slides.pdf`.

## 2. Theory: about 20%

Organise this section around the relevant lecture concepts. Introduce each equation with a short explanation of what it describes in this experiment. Define symbols and units once. Add a sentence afterwards only if it helps interpret the equation. Avoid lengthy derivations and extra theory.

- Start with the lecture relationship `ω_n = √(k/m)` and `f_n = ω_n/(2π)`, PDF p. 9. Use it to establish the roles of mass and stiffness before introducing the beam calculation.
- Introduce the forced-vibration equation `m ẍ + c ẋ + k x = P_m cos(ωt)`, PDF p. 31. Briefly relate the terms to the beam's motion and applied shaker force.
- Give the displacement magnification factor and `r = ω/ω_n`, PDF p. 34. Use the lecture response curves to explain resonance near `r = 1` for small damping and the lower displacement peak with greater damping under the same force. Do not derive a separate resonance-peak correction formula.
- Present the underdamped free response `x(t) = A exp(-ζω_n t) cos(ω_d t - φ)` and `ω_d = ω_n√(1-ζ²)`, PDF pp. 25-27. Point to the exponential term to explain the decreasing amplitude. Briefly define underdamped as oscillation that gradually dies away.
- Introduce logarithmic decrement from the lecture, PDF p. 28: `δ = (1/n) ln(a₁/aₙ₊₁)` and `ζ ≈ δ/(2π)` for small damping. Define the number of cycles and measure same-side amplitudes from equilibrium. Use this approximation for the required calculation; omit the optional comparison between exact and approximate damping ratios.
- Apply the lecture mass-spring idea to the lab sheet's first-mode beam model. Give `I = bt³/12`, `k = 48EI/L³`, `m = (17/35)m₀`, `m₀ = ρLbt` and `f_n = (1/(2π))√(k/(m+m′))`. Cite `Lab_details.pdf`, p. 7, for the beam model. Briefly state its simple-support and first-mode assumptions.
- Explain swept-sine and hammer excitation briefly using the lab sheet. State once that response peaks estimate the beam frequencies and that damped free frequency and forced-response peak frequency need not be identical. Do not develop a separate technical analysis of this distinction.
- State that a beam can have several natural frequencies, while the lumped model predicts only the first. Omit mathematical mode-shape analysis and additional external beam theory unless the assignment cannot otherwise be answered.

**Sources:** `theory_lecture_slides.pdf`, PDF pp. 9, 24-28 and 31-34, with `Lab_details.pdf` for the beam model and excitation methods. Check the actual pages when drafting. Do not add external theory simply to make the report more advanced.

## 3. Experimental procedure: about 15%

Summarise the equipment and steps needed to understand and reproduce the tests. Use short paragraphs organised by experiment. Avoid a lengthy audit of what each screenshot does or does not confirm.

- Describe the simply supported beam, shaker, signal generator, accelerometer, instrumented hammer and acquisition system. Include beam dimensions and material properties needed for theory.
- Summarise the bare-beam sweep: ICP input and accelerometer sensitivity, 10–400 Hz, 60 s, 0.5 A RMS and Peakhold. Explain how the first three peaks were recorded.
- Describe switching off the shaker and using repeated hammer impacts with Linear Average. Describe the saved data as response spectra; do not claim a measured force-to-response transfer function.
- Describe adding the centre mass and repeating the sweep for the first two frequencies.
- Describe the hammer-excited decay measurement and intended second-order integration. Report 2000 Hz sampling and the recorded 2048 points; briefly note that the sheet prescribed 2000 points. Explain how a clear decay was saved and state the available repeats.
- Describe fitting the oil damper, repeating the decay test and sweeping over 10–200 Hz. Include relevant practical and safety points supported by the sheet or actual observations.
- Use past tense and your own wording. Record deviations only if they occurred.

**Sources:** `Lab_details.pdf`, `Assignment_criteria.pdf`, and group lab notes if available.

## 4. Results and calculations: about 25%

Present values with units and enough working to follow each calculation. Show one worked example per calculation type and put other results in tables. Use equations, substitutions and tables to carry the calculation. Keep the surrounding explanation short. Leave the main interpretation for Section 5. Keep figures to a minimum while retaining the required comparisons.

### Frequencies and added mass

- Table the bare-beam modes 1–3 with swept-sine and hammer estimates and their differences where both are available.
- Table the first two bare and added-mass frequencies. Report the added mass and frequency change or percentage change when reliable values are known.
- Calculate first-mode theoretical frequencies for the bare and added-mass beam using the verified model. Show a worked calculation with dimensions, material properties, units and equivalent mass. Compare theory with the relevant measurement and define the denominator used for percentage difference.
- Where the data supports a meaningful comparison, use one combined, labelled spectrum showing the relevant peaks for the bare-beam methods and added-mass condition. Use separate plots only if combining them would be misleading or unclear. Captions should identify the condition and method. Produce spectra from raw data only after confirming what each export represents and its sampling.

### Free decay and oil damper

- Where suitable, use one combined, labelled plot for the bare and oil-damper decays, identifying the same-side peaks and baselines used. Use separate plots if a combined plot would be misleading or unclear. Label time and response axes with verified units.
- Show one worked logarithmic-decrement and damping-ratio example, including baseline-corrected peak amplitudes and the number of cycles between them. Tabulate `δ` and `ζ ≈ δ/(2π)` for both conditions. Summarise the bare repeats briefly. Omit endpoint sensitivity checks, alternative baseline fits, exact-versus-approximate damping tables and optional calculations of free-decay frequency.
- Table oil-damper forced-response peak frequencies within the measured range and compare corresponding bare-beam results. Include a labelled response plot if supported by the data.
- Compare peak amplitudes only when measurement quantity, units, excitation and acquisition settings make them comparable. Do not infer missing values from the expected trend.

**Sources:** `Lab_results`, `Lab_details.pdf`, `Assignment_criteria.pdf`; lecture slides for the calculation method.

## 5. Discussion: about 15%

Use the lecture equations already introduced in Section 2 to explain the measured results. A citation by itself is not an explanation. Show the relevant relationship and connect it to the numerical change in a few clear sentences. Avoid repeating definitions or adding new theory.

- Interpret the frequency reduction with added mass using Equation 7's mass relationship or the corresponding equation number in the rewritten report. A short frequency-ratio statement may replace a long verbal explanation. Compare the first and second measured changes, but state that the first-mode model does not explain every mode. Do not add mode-shape mathematics to explain the second result.
- Compare swept-sine and hammer estimates using the results table. Discuss advantages and limits, including excitation, averaging, peak identification and resolution where relevant.
- Compare bare and oil-damper decay rates and damping ratios using the exponential decay term from the lecture. Use the lecture magnification factor to explain the expected effect of damping under equal force. Discuss the measured forced-response peaks briefly and state once why absolute peak amplitudes cannot be compared reliably here.
- Compare the first-mode theoretical and measured frequencies using the calculated differences. Choose only one or two relevant explanations, such as the ideal support assumption or uncertain added mass. Do not list every possible error.
- Keep limitations and improvements to a short paragraph focused on what affects the conclusions. Do not repeat missing-setting and calibration caveats in every section.

**Sources:** `Lab_results` for observations and the equations explained from `theory_lecture_slides.pdf` in Section 2, supported by `Lab_details.pdf`. Include exact lecture PDF pages alongside the relevant interpretation.

## 6. Conclusion and formatting: about 10%

- Answer all four objectives concisely using actual results. Give key frequencies and the damping comparison where reliable values exist.
- State the main limitation if it affects interpretation. Do not introduce new calculations or unsupported results.
- Number and caption figures and tables, label axes and units, and refer to each item in the text.
- Keep citations consistent with the reference list. In the report, include the exact lecture PDF page number for every lecture reference, even though this plan lists sources without page numbers.
- Submit the individual report as a single PDF through Canvas. Raw group data may be included in an appendix if useful.

**Sources:** `Assignment_criteria.pdf`, completed results and discussion.

## Established data decisions for the rewrite

### Agreed use of lab-session images

- Keep the two calculated graphs and add original lab images as supporting evidence.
- In Procedure, include the clear apparatus close-up and the controller photograph showing the sweep settings.
- In Results, include six DASP captures: bare sweep, hammer, added-mass sweep, bare decay, oil-damper decay and oil-damper sweep. Use one representative capture for each, rather than repeated decay screenshots.
- Keep all selected images in the main report. Allow the space needed for readable images.
- Crop unused areas and add a few arrows or labels. Preserve the original measurements and image files. Give each figure a caption, source filename and a reference in the text.
- Retain screenshot display scales and distinguish screen readouts from frequencies selected from the exported data.

### Resolved experimental details

Read `IMPLEMENTATION_CLARIFICATIONS.md` for the full preparation record. Keep these resolved decisions; do not ask again for unavailable lab notes.

- The added mass was used only in Experiment 1, Step 3. Its actual value is unknown; use the instructed assumption of 1.00 kg and identify it clearly when presenting the theoretical prediction.
- Each TXT export contains a waveform block and a saved spectrum block. Use the saved spectra for frequency results. Sampling is 2000 Hz, with 2048 waveform samples and spectrum spacing of about 0.98 Hz.
- `Experiment 3 step 2.txt` is the oil-damper sweep and matches `Experiment 3 step 3.png`. The second oil-damper decay is available only as `Experiment 3 step 2.png`; do not count the sweep TXT as a decay repeat.
- Three numerical bare decays and one numerical oil-damper decay are available. The missing oil repeat limits repeat comparison, but does not prevent the main damping calculation.
- Retain the recorded mV labels or clearly labelled relative amplitudes. Do not invent a displacement conversion. Subtract the equilibrium baseline before calculating peak ratios.
- Preserve experimentally supported peak selections. Explain any difference from values written in the lab sheet in a short note rather than a lengthy data-processing discussion.
- The beam stiffness and equivalent-mass expressions have been visually checked on lab-sheet p. 7. Use these equations with their first-mode assumptions.
- Keep file parsing, validation and software details in `coding/`. Include them in the report only where necessary to understand a required calculation. Omit the optional reproducibility appendix from the report.

## Final check

- [x] Cover all four objectives and three experiments in the required sections.
- [x] Include frequency tables, theoretical comparison, damping results for both conditions, worked examples and essential plots, or clearly identify missing evidence.
- [x] Show units, assumptions and enough calculation working to follow the method.
- [x] Discuss added mass, both methods, damping and experimental limitations using the results.
- [x] Number, caption and reference figures and tables; label axes and units.
- [x] Support claims with sources, give exact lecture pages and match citations to the reference list.
- [x] Explain lecture concepts together in theory and use those equations to interpret the results in discussion.
- [x] Introduce equations with a short, clear explanation. Use short student-style sentences and remove wording that merely repeats the maths.
- [x] Omit optional analysis and keep necessary limitations brief and accurate.
- [x] Agree the writing pattern with the user: short explanation before the equation, followed by the result or a brief interpretation where needed.
- [x] Rewrite the report in REPORT_VER2.md using this agreed plan, then prepare one PDF from the revised Markdown.
