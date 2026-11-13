# VER2 grading summary

Mass clarification, 13 November 2026: the user confirmed the actual added mass as 1.00 kg. The mass-related limitation is resolved and the report sources and PDFs have been updated. The original independent marks and their average below are retained; no reassessment has been performed.

Final grading estimate: **18.0/20, or 90%**, excellent second-year work against the published criteria. This is the three-marker mean rounded to a sensible reporting precision, not an official lecturer mark. The exact mean is 17.9667/20, or 89.83%. The independent marks range from 16.8 to 18.6/20, or 84% to 93%. This range describes marker judgement, not a statistical confidence interval.

All three agents received the same prompt and worked independently with high reasoning: gpt-6-luna, gpt-6.1-terra and gpt-6.1-sol. Each assessed the submitted PDF using the six published sections. The parent agent inspected all 13 rendered report pages and the rubric, checked the disputed text and key calculations, and compared the assessments. PDF page numbers match the report's printed page numbers.

## Criterion marks

| Criterion | Weight | Maximum | Luna | Terra | Sol |
|---|---:|---:|---:|---:|---:|
| Introduction & objectives | 15% | 3 | 2.6 | 3.0 | 3.0 |
| Theory | 20% | 4 | 3.4 | 3.8 | 4.0 |
| Experimental procedure | 15% | 3 | 2.5 | 2.9 | 2.7 |
| Results & calculations | 25% | 5 | 4.1 | 4.3 | 4.4 |
| Discussion | 15% | 3 | 2.5 | 2.6 | 2.5 |
| Conclusion & formatting | 10% | 2 | 1.7 | 1.9 | 2.0 |
| Total | 100% | 20 | 16.8 | 18.5 | 18.6 |
| Overall percentage | | | 84% | 92.5% | 93% |

Full independent assessments, including each criterion's justification and page references:

- [Luna assessment](VER2_luna_assessment.md)
- [Terra assessment](VER2_terra_assessment.md)
- [Sol assessment](VER2_sol_assessment.md)
- [Identical prompt](VER2_marking_prompt.txt)

## Evidence behind the marks

**Introduction, p. 1.** The required background and all four objectives are present. Luna considers the background brief; Terra and Sol award full marks. The published rubric does not require a longer introduction. Full or near-full credit is better supported than a substantial deduction for brevity alone.

**Theory, pp. 1–3.** All specifically requested theory is included: the forced equation, magnification factor, free response, decrement method, stiffness, equivalent mass, added-mass frequency and method comparison. The 0.6/4 gap between Luna and Sol is the largest raw section disagreement. Luna does not identify a missing required equation. Terra would prefer a stronger mode-shape connection; Sol treats that as an extension. Higher-mode calculations and the exact decrement formula are not additional compulsory criteria.

**Procedure, pp. 3–4.** The required tests, major instrument settings and precautions are described. Sol identifies the clearest remaining weaknesses: impact location, averaging count and confirmation that second-order integration was actually used. The report says the lab procedure specified integration, which is less definite than reporting the actual setting. Its honest disclosure of 2048 rather than 2000 samples does not itself demonstrate an invalid experiment.

**Results, pp. 5–11.** Every required table and calculation type is present. All markers find the numerical work materially correct. The first-mode prediction now uses the confirmed 1.00 kg mass. The damping estimates still lack a demonstrated reliability range, which constrains confidence despite correct arithmetic. Separately normalised spectra are properly labelled and support frequency comparisons, not absolute amplitude comparisons.

**Discussion, pp. 12–13.** This is the strongest marking agreement: 2.5–2.6/3. The report explains the main trends and avoids overstating the peak-height evidence. It could make better use of its equations to assess the oil-damper frequency shift, relate the second-mode mass effect to mode shape, and quantify the effect of measurement choices.

**Conclusion and formatting, pp. 5–13.** The conclusion covers all objectives, and the PDF is readable and consistently structured. Some original software screenshots have small labels or dense traces, but Figures 3 and 7 provide clearer plotted evidence. This supports a minor presentation deduction at most. There is no published requirement for a cover page, abstract or extra appendix.

## Significant disagreements and moderation

Terra and Sol differ by only 0.1/20, or 0.5 percentage points. Luna is lower by 1.7–1.8/20, or 8.5–9 percentage points. This is a significant difference in overall marking severity, with much less disagreement about the facts.

Against Sol, 1.4 of Luna's 1.8 lost marks arise in Introduction, Theory, Procedure and Conclusion & Formatting. These sections largely contain the requested material. Luna's narrative gives relatively little criterion-specific explanation for the size of some deductions. I therefore give greater weight to Terra and Sol's interpretation of criterion coverage, while retaining Luna's result in the reported average and range.

Luna lists the absence of a higher-mode theoretical comparison as a weakness. This is a useful extension, but the supplied beam model predicts the first mode and the rubric does not explicitly demand a higher-mode derivation. A short physical mode-shape explanation is a better priority than adding a lengthy model solely to satisfy that comment.

Formal uncertainty propagation is also not explicitly required. However, checking whether baseline and peak choices materially change the damping estimates is directly relevant to the quality of the reported results. This is a substantive improvement, not a demand for an unrelated formal uncertainty budget.

## Highest-priority improvements

1. **Demonstrate damping robustness, pp. 9–10 and 13.** Recalculate using several reasonable peak windows and baseline choices, or fit the logarithm of several peak amplitudes against cycle number. Summarise the spread and reduce unjustified precision. Sol's independent nearby-window checks gave approximately 0.0117–0.0137 for the illustrated bare record and 0.0250–0.0288 for the oil record. These are sensitivity results, not confidence limits or replacement true values. They support the qualitative damping increase while questioning the last reported digits. Only one numerical oil record is available, so repeatability remains limited.

2. **Explain the oil-damper frequency shift, pp. 11–13.** From the report's displacement magnification equation, the resonance ratio is sqrt(1 - 2*zeta^2). Holding the underlying natural frequency fixed, changing zeta from 0.01324 to 0.02882 predicts a shift of roughly 0.03 Hz near 46.88 Hz, far below the measured 1.95 Hz. The parent recalculation confirms this scale. Discuss possible changes in effective mass, stiffness, attachment/support conditions and measurement variability. The report does not falsely attribute the whole shift to damping, but leaves the explanation incomplete.

3. **Resolved: added mass confirmed as 1.00 kg, pp. 4, 8–9 and 12.** The theoretical comparison now uses the actual mass. The 31.56 Hz prediction, 29.44% predicted reduction and 5.21% difference from measurement are unchanged. No mass inference or additional mass-sensitivity analysis is needed to resolve this issue.

4. **Improve reproducibility, pp. 3–4.** State the impact position, averaging count and actual integration setting if they can be verified. If they were not recorded, acknowledge that directly.

5. **Add a short mode-shape explanation, pp. 7 and 12.** An ideal simply supported second bending mode has a central displacement node. This helps explain a smaller effect from a central point mass, while the nonzero measured shift may involve the real attachment and boundary conditions. A full higher-mode derivation is optional.

6. **Polish the original screenshots, pp. 6–8 and 10–11.** Make axes and units easier to read where possible, or retain originals as supporting evidence and keep the clear reconstructed plots central. This is lower priority than strengthening the analysis.

## Checks and limits

No marker identified a material arithmetic error or definite physical contradiction. The beam stiffness, equivalent mass, predicted frequencies, percentage changes and displayed decrement calculations are consistent with the stated inputs. One-bin differences from the lab-sheet entries are disclosed, and the experimental exports are the workspace's source of truth for results.

The exact decrement relation changes the oil estimate only from about 0.02882 to 0.02881. The small-damping approximation is explicitly allowed by the rubric, so this is not a meaningful reason to deduct marks.

The report correctly says that comparable input force and response calibration were not established. An absolute peak-height reduction therefore remains experimentally unconfirmed, although its theoretical explanation earns credit. This limitation should not be turned into a claim that the report fabricated an amplitude reduction.

The rubric supplies section weights and content requirements, without detailed performance bands. The precise mark therefore remains a judgement. No institutional classification, administrative penalty or originality conclusion is inferred.

## Source documents

- [Submitted report](../../output/pdf/ME31001_lab_report_VER2.pdf)
- [Published assignment criteria](../../Assignment_criteria.pdf)
- [Lab sheet](../../Lab_details.pdf)
- [Experimental records](../../Lab_results)
- [Lecture source](../../theory_lecture_slides.pdf), PDF p. 34, for the displacement magnification relation used in the frequency-shift check.

Both report versions and their PDFs were subsequently updated only to reflect the confirmed 1.00 kg mass. The other improvement recommendations remain outstanding.

