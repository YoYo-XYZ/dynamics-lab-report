# Terra marking assessment

Model: gpt-6.1-terra. Reasoning: high. Identical marking prompt supplied to all three reviewers.

Mass clarification, 13 November 2026: the user confirmed the actual added mass as 1.00 kg. Mass-related comments below have been corrected to reflect this; the original marks are retained and have not been reassessed.

## Independent marking report

**Overall mark: 18.5/20, or 92.5/100.** This is an excellent second-year report: it addresses every published section, presents traceable calculations, and is appropriately cautious about limitations in the data. The added mass is now confirmed; the remaining limitations are uncertainty in the damping estimates and opportunities for deeper interpretation of the second mode.

The references below use PDF page numbers counted from the first page. They match the report’s printed page numbers.

| Published criterion | Mark | Within criterion | Evidence and justification |
|---|---:|---:|---|
| Introduction & Objectives | **3.0/3** | **100%** | Gives relevant background on resonance, impulse testing and logarithmic decrement, and clearly states all four objectives in the student’s own words (p. 1). |
| Theory | **3.8/4** | **95%** | Gives the forced-vibration equation, magnification factor, damped response, decrement relation, beam model and distinction between test methods (pp. 1–3). The connection between mode shape and a centre-mounted mass could be developed further. |
| Experimental Procedure | **2.9/3** | **96.7%** | Describes the apparatus, sweep and hammer methods, decay acquisition and oil-damper repeat, with settings and practical precautions (pp. 3–4). It usefully distinguishes the saved 2,048-point records from the prescribed 2,000 points. |
| Results & Calculations | **4.3/5** | **86%** | Provides the requested frequency comparisons, theoretical calculation, damping estimates, spectra and decay plots (pp. 5–11). The added-mass value is now confirmed as 1.00 kg. The damping calculation would be stronger with evidence of sensitivity to baseline and peak selection. Some original screen captures have less clear axis or unit information than the reconstructed plots (pp. 6–8, 10–11). |
| Discussion | **2.6/3** | **86.7%** | Explains the first-mode mass effect, compares the methods, discusses faster decay and the expected peak-amplitude effect, and identifies errors and improvements (pp. 12–13). It stops short of explaining the much smaller second-mode shift in terms of mode shape and does not quantify the sensitivity of the damping estimates. |
| Conclusion & Formatting | **1.9/2** | **95%** | Concisely addresses the four objectives and reports the main limitations (p. 13). The PDF is well organised, with numbered, captioned figures and tables; some original plots are small and their axes are less readily readable (pp. 6–8, 10–11). |
| **Total** | **18.5/20** | **92.5%** | |

## Strengths

- The report makes the experimental trail easy to follow. Frequency tables are supported by labelled spectra, and it explains that each panel in Figure 3 is normalised separately, so their heights cannot be used as absolute response comparisons (p. 5).
- The theory and calculations are linked clearly. The report shows beam stiffness and equivalent mass, substitutes values into the first-frequency model, and defines the percentage-difference denominator (pp. 2, 8–9).
- The damping calculation identifies the baseline, selected peaks and ten-cycle interval, and reports all three bare-beam estimates rather than only a favourable result (pp. 9–10).
- The discussion distinguishes a theoretical prediction of reduced resonance amplitude from what the available measurements actually establish. It does not claim a measured peak-height reduction without comparable force and calibration evidence (p. 12).

## Most material weaknesses and improvements

1. **Resolved: added mass confirmed as 1.00 kg** (pp. 4, 8–9, 12). The theoretical comparison now uses the actual mass. The 31.56 Hz prediction and 5.21% difference from measurement are unchanged.

2. **The damping estimates depend on the chosen baseline and peaks** (pp. 9–10, 13). The report recognises drift and ripple, but does not show how much the result changes with a different reasonable baseline or peak window. Recalculate using alternative windows or fit an exponential envelope, and report the spread. More numerical oil-damper repeats would also make the comparison more reliable.

3. **The second-mode interpretation could go further** (pp. 7, 12). The report correctly says its first-mode model cannot predict the second-mode change, but an ideal simply supported beam has a displacement node at its centre in the second bending mode. That helps explain why a small centred mass should affect that mode much less; attachment position, support conditions and measurement resolution could then be considered when interpreting the observed 5.75% decrease.

4. **Some original screen captures are harder to assess than the reconstructed plots** (pp. 6–8, 10–11). Larger axis labels and clearly identified units on every displayed graph would make the evidence easier to read. Figures 3 and 7 already do much of this well (pp. 5, 9).

## Numerical and physical checks

**Definite errors.** I found no material arithmetic error in the displayed first-mode stiffness, frequency, percentage-change or example logarithmic-decrement calculations (pp. 7–9). The changes in the tables are calculated from the underlying unrounded frequencies, so small differences from subtracting the displayed rounded values are expected.

**Missing evidence or limitations.**

- The added mass is now confirmed as 1.00 kg (pp. 4, 8). The resulting 31.56 Hz prediction and 5.21% difference now use the actual attachment mass.
- The decrement calculation assumes the exported signal is suitable for a same-mode peak ratio. A constant scale factor cancels, as the report says, but baseline drift and mixed-mode content can still affect the estimate (pp. 2, 9, 13). The numerical damping ratios should be treated as estimates.
- The oil-damper second peak rises by approximately one frequency bin (p. 11). That is weak evidence of a physical frequency increase, and the discussion appropriately treats it as small and does not use the shift alone to infer damping (p. 13).
- The report states that equal input force and matching response calibration were not established, so it cannot confirm the peak-height effect from those tests (p. 12). This is a sound qualification, not a contradiction of its theoretical prediction.

**Optional improvement.** The exact relation between logarithmic decrement and damping ratio could be used alongside the small-damping approximation. At the reported low damping ratios, the approximation is appropriate and does not materially affect the conclusions (pp. 2, 9–10).

The published rubric does not provide detailed performance bands or specify fractional deductions, so the precise marks within each section involve judgement. I have credited the work actually present in the PDF, including the honest treatment of unavailable measurements, and have not applied a late-submission, originality or other administrative penalty: those matters cannot be established from the submitted report alone.

