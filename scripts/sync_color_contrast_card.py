from pathlib import Path
p=Path('index.html')
s=p.read_text(encoding='utf-8')
if 'apps/color-contrast/' in s:
    raise SystemExit(0)
needle='<small style="display:block;letter-spacing:.16em;color:var(--muted);font-size:12px;">LIFE & GAME</small>暮らし・ゲーム</h3>'
pos=s.find(needle)
if pos < 0:
    raise SystemExit('section not found')
grid='<div class="grid">'
pos=s.find(grid,pos)+len(grid)
card='''\n          <article class="card">\n            <div class="cardTop"><h3>配色コントラストチェッカー</h3><span class="pill">新着・デザイン</span></div>\n            <p>文字色と背景色を選んで、読みやすさとコントラスト比をすぐ確認。</p>\n            <div class="actions"><a class="btn" href="apps/color-contrast/" target="_blank" rel="noreferrer">アプリを開く</a></div>\n          </article>\n'''
s=s[:pos]+card+s[pos:]
s=s.replace('46 <span>/ 100 apps</span>','47 <span>/ 100 apps</span>')
s=s.replace('100アプリ計画 46%','100アプリ計画 47%')
s=s.replace('width:46%;','width:47%;')
s=s.replace('<strong>46</strong><span>公開アプリ</span>','<strong>47</strong><span>公開アプリ</span>')
p.write_text(s,encoding='utf-8')
