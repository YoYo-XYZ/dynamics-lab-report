# Lab report plan

## Purpose and approach

Write an individual report covering all three experiments and four lab objectives. Follow the six sections in `Assignment_criteria.pdf`. Use the lab sheet for methods, the recorded files for results, and the lecture slides as the main source of theoretical knowledge. Keep the theory focused on concepts covered in the slides. Use an external academic source only when a relevant claim cannot be supported by the supplied materials. Write in your own words as a second-year student explaining what they have learned, rather than as an expert or teacher. Keep the writing clear, concise and intuitive. Explain technical terms when needed, but do not overuse them.

The suggested proportions below follow the marking weights. They are a guide, not a required word count. Treat them as flexible guidance and allow space for the essential figures, tables and worked examples.

## 1. Introduction and objectives: about 15%

- Introduce vibration of a simply supported beam and explain why resonance and natural frequencies matter here.
- Briefly introduce swept-sine and hammer excitation, free decay and logarithmic decrement. Leave derivations for theory.
- State the four objectives in your own words: find frequencies with both excitation methods, investigate added mass, determine damping from free decay, and investigate the oil damper's effect.
- Explain what was investigated and why without presenting conclusions before the results.

**Sources:** `Lab_details.pdf`, `Assignment_criteria.pdf`, `theory_lecture_slides.pdf`.

## 2. Theory: about 20%

State and explain the equations and their assumptions without lengthy derivations.

- Introduce the forced single-degree-of-freedom model, `m ẍ + c ẋ + k x = P_m cos(ωt)`. Define the symbols and units. Give the displacement magnification factor and explain frequency ratio, resonance and damping.
- Describe underdamped free response and define damped natural frequency. Introduce logarithmic decrement using same-side peaks: `δ = (1/n) ln(x₁/xₙ₊₁)`. Give the exact relation `ζ = δ / √((2π)² + δ²)` and the small-damping approximation `ζ ≈ δ/(2π)`. Explain assumptions and measure peaks relative to the equilibrium baseline.
- Explain the first-mode equivalent single-degree-of-freedom beam model. Define stiffness, rectangular second moment of area `I = bt³/12`, equivalent mass and added centre mass. Present `f_n = (1/(2π))√(k/(m + m′))` and its assumptions. Verify the lab sheet's stiffness and equivalent-mass expressions before using them.
- Explain how swept-sine and hammer response peaks estimate frequencies. Distinguish a measured response peak from an undamped natural frequency when discussing damping.
- Describe the beam as a continuous system with multiple modes. Consider mode shapes when explaining how a centre mass or excitation affects different modes.

**Sources:** Mainly `theory_lecture_slides.pdf`, supported by `Lab_details.pdf` for the lab's beam model. Flag a claim for an external academic source only if the supplied materials cannot support it and the claim is needed.

## 3. Experimental procedure: about 15%

Summarise the equipment and steps needed to understand and reproduce the tests.

- Describe the simply supported beam, shaker, signal generator, accelerometer, instrumented hammer and acquisition system. Include beam dimensions and material properties needed for theory.
- Summarise the bare-beam sweep: ICP input and accelerometer sensitivity, 10–400 Hz, 60 s, 0.5 A RMS and Peakhold. Explain how the first three peaks were recorded.
- Describe switching off the shaker and using repeated hammer impacts with Linear Average. State what was actually measured rather than assuming an input-output transfer function was recorded.
- Describe adding the centre mass and repeating the sweep for the first two frequencies.
- Describe the hammer-excited decay measurement, second-order integration, 2000 Hz sampling and 2000 points. Explain how a clear decay was saved and whether repeats were used.
- Describe fitting the oil damper, repeating the decay test and sweeping over 10–200 Hz. Include relevant practical and safety points supported by the sheet or actual observations.
- Use past tense and your own wording. Record deviations only if they occurred.

**Sources:** `Lab_details.pdf`, `Assignment_criteria.pdf`, and group lab notes if available.

## 4. Results and calculations: about 25%

Present values with units and enough working to follow each calculation. Show one worked example per calculation type and put other results in tables. Separate measurements, theoretical predictions and interpretation. Keep figures to a minimum while retaining the evidence needed for the required comparisons.

### Frequencies and added mass

- Table the bare-beam modes 1–3 with swept-sine and hammer estimates and their differences where both are available.
- Table the first two bare and added-mass frequencies. Report the added mass and frequency change or percentage change when reliable values are known.
- Calculate first-mode theoretical frequencies for the bare and added-mass beam using the verified model. Show a worked calculation with dimensions, material properties, units and equivalent mass. Compare theory with the relevant measurement and define the denominator used for percentage difference.
- Where the data supports a meaningful comparison, use one combined, labelled spectrum showing the relevant peaks for the bare-beam methods and added-mass condition. Use separate plots only if combining them would be misleading or unclear. Captions should identify the condition and method. Produce spectra from raw data only after confirming what each export represents and its sampling.

### Free decay and oil damper

- Where suitable, use one combined, labelled plot for the bare and oil-damper decays, identifying the same-side peaks and baselines used. Use separate plots if a combined plot would be misleading or unclear. Label time and response axes with verified units.
- Show one worked logarithmic-decrement and damping-ratio example, including peak amplitudes and the number of cycles between them. Tabulate the results for both conditions and their variation if valid repeats exist.
- Table oil-damper forced-response peak frequencies within the measured range and compare corresponding bare-beam results. Include a labelled response plot if supported by the data.
- Compare peak amplitudes only when measurement quantity, units, excitation and acquisition settings make them comparable. Do not infer missing values from the expected trend.

**Sources:** `Lab_results`, `Lab_details.pdf`, `Assignment_criteria.pdf`; lecture slides for the calculation method.

## 5. Discussion: about 15%

Describe the main differences briefly. Give one or two evidence-supported explanations and identify the most relevant limitations, keeping the discussion concise.

- Interpret frequency changes with added mass using the equivalent model. Consider mode shape and mass position, especially for the second mode; the first-mode model does not predict all modes.
- Compare swept-sine and hammer estimates using the results table. Discuss advantages and limits, including excitation, averaging, peak identification and resolution where relevant.
- Compare bare and oil-damper decay rates and damping ratios. Discuss forced-response peak frequency and amplitude only as far as comparable measurements support.
- Compare first-mode theory and experiment. Consider support conditions, model simplifications, attached equipment, mass placement, damping and measurement resolution. Relate plausible errors to their likely effects where evidence allows; do not invent observations.
- Identify limitations and suggest specific improvements suited to the actual gaps.

**Sources:** `Lab_results` for observations and mainly `theory_lecture_slides.pdf` for their theoretical interpretation, supported by `Lab_details.pdf`. Flag a needed claim for an external academic source only if the supplied materials cannot support it.

## 6. Conclusion and formatting: about 10%

- Answer all four objectives concisely using actual results. Give key frequencies and the damping comparison where reliable values exist.
- State the main limitation if it affects interpretation. Do not introduce new calculations or unsupported results.
- Number and caption figures and tables, label axes and units, and refer to each item in the text.
- Keep citations consistent with the reference list. In the report, include the exact lecture PDF page number for every lecture reference, even though this plan lists sources without page numbers.
- Submit the individual report as a single PDF through Canvas. Raw group data may be included in an appendix if useful.

**Sources:** `Assignment_criteria.pdf`, completed results and discussion.

## Data and evidence to resolve before drafting results

- `Lab_results` contains nine PNGs and eight TXT files. `Experiment 3 step 3.png` has no matching TXT export. Inspect the image and recover the export if needed; use the image only if its labels and values are reliable.
- Sampled TXT files have time and amplitude columns labelled `Time(S)` and `Amplitude(mV)`. Confirm which files represent each test, whether they are time histories or processed responses, and the physical quantity and units after integration before calculating spectra or decay ratios. File names alone do not establish these details.
- Confirm the added mass and actual settings from group notes before making a numerical added-mass prediction.
- Check coverage of all required comparisons. If a measurement is unavailable, flag it and seek original data or notes rather than inventing a value.
- Verify beam stiffness and equivalent-mass equations in the original lab sheet, including equation images if text extraction is incomplete. Confirm their assumptions.
- Record exact lecture PDF pages while drafting citations. Use lecture concepts wherever they support the explanation. Identify any necessary factual claim that cannot be supported by the supplied materials and needs another credible academic source.

## Final check

- [ ] Cover all four objectives and three experiments in the required sections.
- [ ] Include frequency tables, theoretical comparison, damping results for both conditions, worked examples and essential plots, or clearly identify missing evidence.
- [ ] Show units, assumptions and enough calculation working to follow the method.
- [ ] Discuss added mass, both methods, damping and experimental limitations using the results.
- [ ] Number, caption and reference figures and tables; label axes and units.
- [ ] Support claims with sources, give exact lecture pages and match citations to the reference list.
- [ ] Use clear, intuitive student wording and prepare one PDF for submission.
