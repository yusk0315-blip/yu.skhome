from pathlib import Path
p=Path('index.html')
s=p.read_text(encoding='utf-8')
if 'apps/tilt-level/' in s:
    raise SystemExit(0)
needle='<small style="display:block;letter-spacing:.16em;color:var(--muted);font-size:12px;">LIFE & GAME</small>暮らし・ゲーム</h3>'
pos=s.find(needle)
if pos < 0:
    raise SystemExit('section not found')
grid='<div class="grid">'
pos=s.find(grid,pos)+len(grid)
card='''\n          <article class="card">\n            <div class="cardTop"><h3>傾斜角メーター</h3><span class="pill">新着・DIY</span></div>\n            <p>スマホの傾きを角度で表示。棚や家具の水平チェックを手軽に。</p>\n            <div class="actions"><a class="btn" href="apps/tilt-level/" target="_blank" rel="noreferrer">アプリを開く</a></div>\n          </article>\n'''
s=s[:pos]+card+s[pos:]
s=s.replace('47 <span>/ 100 apps</span>','48 <span>/ 100 apps</span>')
s=s.replace('100アプリ計画 47%','100アプリ計画 48%')
s=s.replace('width:47%;','width:48%;')
s=s.replace('<strong>47</strong><span>公開アプリ</span>','<strong>48</strong><span>公開アプリ</span>')
p.write_text(s,encoding='utf-8')
