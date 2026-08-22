from pathlib import Path
p=Path('index.html')
s=p.read_text(encoding='utf-8')
if 'apps/noise-level-meter/' in s:
    raise SystemExit(0)
needle='<small style="display:block;letter-spacing:.16em;color:var(--muted);font-size:12px;">LIFE & GAME</small>暮らし・ゲーム</h3>'
pos=s.find(needle)
if pos < 0:
    raise SystemExit('section not found')
grid='<div class="grid">'
pos=s.find(grid,pos)+len(grid)
card='''\n          <article class="card">\n            <div class="cardTop"><h3>騒音レベルメーター</h3><span class="pill">新着・センサー</span></div>\n            <p>スマホのマイクで周囲の音量変化をリアルタイム確認。録音・送信なしの簡易メーター。</p>\n            <div class="actions"><a class="btn" href="apps/noise-level-meter/" target="_blank" rel="noreferrer">アプリを開く</a></div>\n          </article>\n'''
s=s[:pos]+card+s[pos:]
s=s.replace('51 <span>/ 100 apps</span>','52 <span>/ 100 apps</span>')
s=s.replace('100アプリ計画 51%','100アプリ計画 52%')
s=s.replace('width:51%;','width:52%;')
s=s.replace('<strong>51</strong><span>公開アプリ</span>','<strong>52</strong><span>公開アプリ</span>')
p.write_text(s,encoding='utf-8')
