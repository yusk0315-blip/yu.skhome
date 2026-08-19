from pathlib import Path
p=Path('index.html')
s=p.read_text(encoding='utf-8')
if 'apps/date-counter/' in s:
    raise SystemExit(0)
needle='<small style="display:block;letter-spacing:.16em;color:var(--muted);font-size:12px;">LIFE & GAME</small>暮らし・ゲーム</h3>'
pos=s.find(needle)
if pos < 0:
    raise SystemExit('section not found')
grid='<div class="grid">'
pos=s.find(grid,pos)+len(grid)
card='''\n          <article class="card">\n            <div class="cardTop"><h3>日付カウンター</h3><span class="pill">新着・日程</span></div>\n            <p>2つの日付の間の日数や平日数を計算。○日後・○日前の日付もすぐ確認。</p>\n            <div class="actions"><a class="btn" href="apps/date-counter/" target="_blank" rel="noreferrer">アプリを開く</a></div>\n          </article>\n'''
s=s[:pos]+card+s[pos:]
s=s.replace('48 <span>/ 100 apps</span>','49 <span>/ 100 apps</span>')
s=s.replace('100アプリ計画 48%','100アプリ計画 49%')
s=s.replace('width:48%;','width:49%;')
s=s.replace('<strong>48</strong><span>公開アプリ</span>','<strong>49</strong><span>公開アプリ</span>')
p.write_text(s,encoding='utf-8')
