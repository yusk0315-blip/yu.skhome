from pathlib import Path
p=Path('index.html')
s=p.read_text(encoding='utf-8')
if 'apps/work-hours-calculator/' in s:
    raise SystemExit(0)
needle='<small style="display:block;letter-spacing:.16em;color:var(--muted);font-size:12px;">LIFE & GAME</small>暮らし・ゲーム</h3>'
pos=s.find(needle)
if pos < 0:
    raise SystemExit('section not found')
grid='<div class="grid">'
pos=s.find(grid,pos)+len(grid)
card='''\n          <article class="card">\n            <div class="cardTop"><h3>勤務時間・残業計算</h3><span class="pill">新着・仕事</span></div>\n            <p>出勤・退勤・休憩から、実働時間と所定労働時間を超えた時間をすぐ計算。</p>\n            <div class="actions"><a class="btn" href="apps/work-hours-calculator/" target="_blank" rel="noreferrer">アプリを開く</a></div>\n          </article>\n'''
s=s[:pos]+card+s[pos:]
s=s.replace('50 <span>/ 100 apps</span>','51 <span>/ 100 apps</span>')
s=s.replace('100アプリ計画 50%','100アプリ計画 51%')
s=s.replace('width:50%;','width:51%;')
s=s.replace('<strong>50</strong><span>公開アプリ</span>','<strong>51</strong><span>公開アプリ</span>')
p.write_text(s,encoding='utf-8')
