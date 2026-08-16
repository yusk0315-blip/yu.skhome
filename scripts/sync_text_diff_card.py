from pathlib import Path
p=Path('index.html')
s=p.read_text(encoding='utf-8')
if 'apps/text-diff/' in s:
    raise SystemExit(0)
needle='<small style="display:block;letter-spacing:.16em;color:var(--muted);font-size:12px;">LIFE & GAME</small>暮らし・ゲーム</h3>'
pos=s.find(needle)
if pos < 0:
    raise SystemExit('section not found')
grid='<div class="grid">'
pos=s.find(grid,pos)+len(grid)
card='''\n          <article class="card">\n            <div class="cardTop"><h3>文章差分チェッカー</h3><span class="pill">新着・仕事</span></div>\n            <p>修正前と修正後を貼り付けて、追加・削除された行をすぐ見比べる。</p>\n            <div class="actions"><a class="btn" href="apps/text-diff/" target="_blank" rel="noreferrer">アプリを開く</a></div>\n          </article>\n'''
s=s[:pos]+card+s[pos:]
s=s.replace('45 <span>/ 100 apps</span>','46 <span>/ 100 apps</span>')
s=s.replace('100アプリ計画 45%','100アプリ計画 46%')
s=s.replace('width:45%;','width:46%;')
s=s.replace('<strong>45</strong><span>公開アプリ</span>','<strong>46</strong><span>公開アプリ</span>')
p.write_text(s,encoding='utf-8')
