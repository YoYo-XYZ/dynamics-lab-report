"""Check report values against source data and render every final PDF page for QA."""
import argparse
import json
from pathlib import Path
import re
import shutil
import subprocess
import numpy as np
from PIL import Image, ImageDraw
from pypdf import PdfReader
from inspect_data import ROOT, load_export

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source', type=Path, default=Path('REPORT_VER1.md'))
    parser.add_argument('--pdf', type=Path, default=Path('output/pdf/ME31001_lab_report.pdf'))
    args = parser.parse_args()
    result = json.loads((ROOT/'coding/results/analysis.json').read_text())
    report = (ROOT/args.source).read_text(encoding='utf-8')
    for section in range(1,7):
        assert re.search(rf'^## {section}\. ', report, re.M), section
    images = re.findall(r'!\[[^\n]*?\]\(([^)]+)\)', report)
    assert len(images) >= 2
    for image in images:
        assert (ROOT/image).is_file(), image
    figures = re.findall(r'!\[Figure (\d+)\.', report)
    assert figures == [str(i) for i in range(1,len(figures)+1)]
    for number in re.findall(r'\bFigure (\d+)\b', report):
        assert number in figures
    if (ROOT/args.source).name == 'REPORT_VER2.md':
        assert len(figures) == 10
        assert len([image for image in images if image.startswith('figures/lab/')]) == 8
    references = re.findall(r'^\[(\d+)\] ', report, re.M)
    assert references == [str(i) for i in range(1,len(references)+1)]
    assert len(references) >= 3
    for key in ['bare_sweep','bare_hammer','mass_sweep','oil_sweep']:
        data=load_export(ROOT/'Lab_results'/(result['file_mapping'][key][0]+'.txt'))
        for p in result['frequency'][key]:
            frequency=p['frequency_Hz']
            assert f'{frequency:.2f}' in report
            i=np.argmin(abs(data['spectrum'][:,0]-frequency))
            assert 0 < i < len(data['spectrum'])-1
            assert data['spectrum'][i,1]>=max(data['spectrum'][i-1,1],data['spectrum'][i+1,1])
    for key,d in result['damping'].items():
        data=load_export(ROOT/'Lab_results'/(result['file_mapping'][key][0]+'.txt'))
        ids=d['peak_indices']
        assert len(ids)-1==d['n_cycles']==10
        t,y=data['wave'].T
        baseline=y[(t>.85)&(t<1.02)].mean()
        ratio=(y[ids[0]]-baseline)/(y[ids[-1]]-baseline)
        delta=np.log(ratio)/10
        np.testing.assert_allclose(delta,d['delta'],rtol=1e-12)
        np.testing.assert_allclose(d['zeta'],1/np.sqrt(1+(2*np.pi/delta)**2),rtol=1e-12)
        approximate = delta/(2*np.pi)
        np.testing.assert_allclose(approximate,d['zeta_approx'],rtol=1e-12)
        assert f"{approximate:.5f}" in report
    assert result['file_mapping']['oil_sweep'][0]=='Experiment 3 step 2'
    assert '1.00 kg' in report and result['theory']['added_mass_kg'] == 1.0
    assert not re.search(r'assumed.{0,15}(?:added mass|1\.00 kg)|unknown added mass', report)
    if (ROOT/args.source).name != 'REPORT_FINAL.md':
        assert 'PDF p. 28' in report and 'PDF p. 34' in report
    else:
        assert not re.search(r'\[[123][^\]]*\bpp?\.', report)

    pdf=ROOT/args.pdf
    reader=PdfReader(pdf)
    text='\n'.join(page.extract_text() for page in reader.pages)
    for number in figures:
        assert re.search(rf'Figure {number}\.\s', text), number
    assert len(reader.pages)>=6
    assert all(len(page.extract_text().strip())>40 for page in reader.pages)
    assert 'Conclusion' in text and 'References' in text
    assert text.count('46.88')>=4 and '33.20' in text and '0.02882' in text
    assert not any(word in report for word in ['TODO','TBD','[insert','PLACEHOLDER'])
    assert not any(char in text for char in ['\ufffd','\u25a0'])
    qa=ROOT/'coding/qa'
    qa.mkdir(exist_ok=True)
    for old in [*qa.glob('page-*.png'), *qa.glob('contact-*.png')]:
        old.unlink()
    (qa/'pdf_text.txt').write_text(text,encoding='utf-8')
    renderer=shutil.which('pdftoppm')
    if not renderer:
        raise RuntimeError('pdftoppm is required for visual verification.')
    subprocess.run([renderer,'-r','90','-png',str(pdf),str(qa/'page')],check=True,
                   stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    pages=sorted(qa.glob('page-*.png'))
    assert len(pages)==len(reader.pages)
    for start in range(0,len(pages),6):
        selected=pages[start:start+6]
        sheet=Image.new('RGB',(3*400,2*600),'#d0d0d0')
        draw=ImageDraw.Draw(sheet)
        for j,path in enumerate(selected):
            im=Image.open(path).convert('RGB')
            im.thumbnail((390,560))
            x=(j%3)*400+(400-im.width)//2
            y=(j//3)*600+25
            sheet.paste(im,(x,y))
            draw.text(((j%3)*400+12,(j//3)*600+5),path.stem,fill='black')
        sheet.save(qa/f'contact-{start//6+1}.png')
    print(f'PASS: source peaks, damping ratios, report values, citations, links and PDF completeness. {len(reader.pages)} pages rendered for visual review.')

if __name__=='__main__':
    main()
