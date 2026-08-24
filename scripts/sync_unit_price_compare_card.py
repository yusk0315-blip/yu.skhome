from pathlib import Path
p=Path('index.html')
s=p.read_text(encoding='utf-8')
if 'apps/unit-price-compare/' in s:
    raise SystemExit(0)
needle='<small style="display:block;letter-spacing:.16em;color:var(--muted);font-size:12px;">LIFE & GAME</small>暮らし・ゲーム</h3>'
pos=s.find(needle)
if pos < 0:
    raise SystemExit('section not found')
grid='<div class="grid">'
pos=s.find(grid,pos)+len(grid)
card='''\n          <article class="card">\n            <div class="cardTop"><h3>どっちがお得？単価比較</h3><span class="pill">新着・買い物</span></div>\n            <p>価格と内容量を入れるだけ。100g・100ml・1個あたりで本当に安い方を比較。</p>\n            <div class="actions"><a class="btn" href="apps/unit-price-compare/" target="_blank" rel="noreferrer">アプリを開く</a></div>\n          </article>\n'''
s=s[:pos]+card+s[pos:]
s=s.replace('53 <span>/ 100 apps</span>','54 <span>/ 100 apps</span>')
s=s.replace('100アプリ計画 53%','100アプリ計画 54%')
s=s.replace('width:53%;','width:54%;')
s=s.replace('<strong>53</strong><span>公開アプリ</span>','<strong>54</strong><span>公開アプリ</span>')
s=s.replace('無料アプリ 53本公開中','無料アプリ 54本公開中')
p.write_text(s,encoding='utf-8')
