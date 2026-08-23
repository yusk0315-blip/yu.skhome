from pathlib import Path
p=Path('index.html')
s=p.read_text(encoding='utf-8')
if 'apps/bpm-metronome/' in s:
    raise SystemExit(0)
needle='<small style="display:block;letter-spacing:.16em;color:var(--muted);font-size:12px;">LIFE & GAME</small>暮らし・ゲーム</h3>'
pos=s.find(needle)
if pos < 0:
    raise SystemExit('section not found')
grid='<div class="grid">'
pos=s.find(grid,pos)+len(grid)
card='''\n          <article class="card">\n            <div class="cardTop"><h3>BPMタップ＆メトロノーム</h3><span class="pill">新着・音楽</span></div>\n            <p>曲に合わせてタップしてBPMを測定。そのテンポでメトロノームも鳴らせる。</p>\n            <div class="actions"><a class="btn" href="apps/bpm-metronome/" target="_blank" rel="noreferrer">アプリを開く</a></div>\n          </article>\n'''
s=s[:pos]+card+s[pos:]
s=s.replace('52 <span>/ 100 apps</span>','53 <span>/ 100 apps</span>')
s=s.replace('100アプリ計画 52%','100アプリ計画 53%')
s=s.replace('width:52%;','width:53%;')
s=s.replace('<strong>52</strong><span>公開アプリ</span>','<strong>53</strong><span>公開アプリ</span>')
s=s.replace('無料アプリ 52本公開中','無料アプリ 53本公開中')
p.write_text(s,encoding='utf-8')
