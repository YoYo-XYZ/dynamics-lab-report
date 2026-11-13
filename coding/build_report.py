"""Build a report PDF from its Markdown source with Pandoc/XeLaTeX."""
import argparse
from pathlib import Path
import shutil
import pypandoc

ROOT = Path(__file__).resolve().parents[1]

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source', type=Path, default=Path('REPORT_VER1.md'))
    parser.add_argument('--output', type=Path, default=Path('output/pdf/ME31001_lab_report.pdf'))
    args = parser.parse_args()
    source = ROOT / args.source
    output = ROOT / args.output
    if not shutil.which('xelatex'):
        raise RuntimeError('XeLaTeX is required on PATH; install MiKTeX or TeX Live.')
    for name in ['frequency_spectra.png', 'free_decay.png']:
        if not (ROOT/'figures'/name).is_file():
            raise FileNotFoundError('Run python coding/analyse_results.py first.')
    output.parent.mkdir(parents=True,exist_ok=True)
    pypandoc.convert_file(
        str(source), 'pdf',
        format='markdown+tex_math_dollars+pipe_tables+implicit_figures',
        outputfile=str(output),
        extra_args=[
            '--standalone', '--pdf-engine=xelatex',
            '--resource-path='+str(ROOT),
            '--include-in-header='+str(ROOT/'coding'/'report_header.tex'),
            '--lua-filter='+str(ROOT/'coding'/'keep_tables.lua'),
            '-V','documentclass=article', '-V','papersize=a4',
            '-V','fontsize=11pt','-V','geometry:margin=22mm',
            '-V','mainfont=Times New Roman', '-V','sansfont=Arial',
            '-V','monofont=Consolas','-V','linestretch=1.08',
            '-V','colorlinks=true','-V','linkcolor=black','-V','urlcolor=blue',
            '-M','lang=en-GB', '-M','pagetitle=ME31001 beam vibration laboratory report',
            '-M','report-source='+source.name,
        ])
    print(output)

if __name__ == '__main__':
    main()
