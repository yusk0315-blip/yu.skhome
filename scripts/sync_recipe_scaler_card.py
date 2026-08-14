from pathlib import Path
p=Path('index.html')
s=p.read_text(encoding='utf-8')
if 'apps/recipe-scaler/' in s:
    raise SystemExit(0)
needle='<small style="display:block;letter-spacing:.16em;color:var(--muted);font-size:12px;">LIFE & GAME</small>暮らし・ゲーム</h3>'
pos=s.find(needle)
if pos < 0:
    raise SystemExit('section not found')
grid='<div class="grid">'
pos=s.find(grid,pos)+len(grid)
card='''\n          <article class="card">\n            <div class="cardTop"><h3>料理分量スケーラー</h3><span class="pill">新着・料理</span></div>\n            <p>レシピの人数を変えたいとき、材料の量を人数比でサッと換算。</p>\n            <div class="actions"><a class="btn" href="apps/recipe-scaler/" target="_blank" rel="noreferrer">アプリを開く</a></div>\n          </article>\n'''
s=s[:pos]+card+s[pos:]
s=s.replace('43 <span>/ 100 apps</span>','44 <span>/ 100 apps</span>')
s=s.replace('100アプリ計画 43%','100アプリ計画 44%')
s=s.replace('width:43%;','width:44%;')
s=s.replace('<strong>43</strong><span>公開アプリ</span>','<strong>44</strong><span>公開アプリ</span>')
p.write_text(s,encoding='utf-8')