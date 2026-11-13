# Report calculations and PDF build

The revised report source is `../REPORT_VER2.md`. Original measurements stay in `../Lab_results/`.

Use Python 3 with `python -m pip install -r coding/requirements.txt` from the project root. The PDF build also requires XeLaTeX on PATH, supplied here by MiKTeX. `pypandoc_binary` includes Pandoc. No browser or local server is needed.

1. Run `python coding/analyse_results.py` to validate all eight exports, calculate the results and generate `figures/frequency_spectra.png` and `figures/free_decay.png`.
   Run `python coding/build_lab_figures.py` to prepare the two labelled session photos and six DASP screenshot extracts in `figures/lab/`. This uses XeLaTeX to place the original images in clipped document viewports with vector callouts, then Poppler to render the Markdown figure assets. Source captures are unchanged. The source-to-figure mapping and crop bounds are in the script.
2. Run `python coding/build_report.py --source REPORT_VER2.md --output output/pdf/ME31001_lab_report_VER2.pdf` to generate the revised PDF directly from the Markdown source.
3. Run `python coding/verify_report.py --source REPORT_VER2.md --pdf output/pdf/ME31001_lab_report_VER2.pdf` for numerical and document checks and PDF-page images in `coding/qa/`. Inspect those images for layout and equation rendering.

Without arguments, the build and verification scripts still use `REPORT_VER1.md` and its original PDF path. The revised report uses the small-damping approximation from the assignment, including an oil-damper estimate of 0.02882. It omits the optional analyses below.

The analysis writes its full results to `coding/results/analysis.json` and the eleven selected maxima per decay to `coding/results/selected_peaks.csv`. Source files are read only. Frequency estimates use saved spectrum maxima, not FFTs of instantaneous sweep waveform blocks. The file named `Experiment 3 step 2.txt` is the oil-damper sweep and matches the step-3 screenshot.

The added mass is an instructed assumption of 1.00 kg. Decay units remain exported mV. A constant baseline is the waveform mean over 0.85 < t < 1.02 s. Each primary damping estimate uses ten cycles between same-side maxima after the initial impact region. The output also records sensitivity to six/eight-cycle endpoints and to a local linear baseline. These checks are not additional experimental repeats.

`inspect_data.py` supplies the parser and optional waveform diagnostics. `inspect_decay.py` prints extrema and baseline candidates used during interval selection. `report_header.tex` contains PDF layout settings; it contains no report prose.
