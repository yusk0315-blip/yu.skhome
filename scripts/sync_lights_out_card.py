from pathlib import Path
p=Path('index.html')
s=p.read_text(encoding='utf-8')
if 'apps/lights-out/' in s:
    raise SystemExit(0)
needle='<small style="display:block;letter-spacing:.16em;color:var(--muted);font-size:12px;">LIFE & GAME</small>暮らし・ゲーム</h3>'
pos=s.find(needle)
if pos < 0:
    raise SystemExit('section not found')
grid='<div class="grid">'
pos=s.find(grid,pos)+len(grid)
card='''\n          <article class="card">\n            <div class="cardTop"><h3>ライトアウト 5×5</h3><span class="pill">新着・ゲーム</span></div>\n            <p>光るマスをタップして全部消す。上下左右も反転する短時間ロジックパズル。</p>\n            <div class="actions"><a class="btn" href="apps/lights-out/" target="_blank" rel="noreferrer">ゲームを開く</a></div>\n          </article>\n'''
s=s[:pos]+card+s[pos:]
s=s.replace('49 <span>/ 100 apps</span>','50 <span>/ 100 apps</span>')
s=s.replace('100アプリ計画 49%','100アプリ計画 50%')
s=s.replace('width:49%;','width:50%;')
s=s.replace('<strong>49</strong><span>公開アプリ</span>','<strong>50</strong><span>公開アプリ</span>')
p.write_text(s,encoding='utf-8')
