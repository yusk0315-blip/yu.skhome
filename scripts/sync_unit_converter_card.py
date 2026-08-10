from pathlib import Path

path = Path("index.html")
html = path.read_text(encoding="utf-8")
href = 'apps/unit-converter/'
if href in html:
    raise SystemExit(0)
heading = '<small style="display:block;letter-spacing:.16em;color:var(--muted);font-size:12px;">LIFE & GAME</small>暮らし・ゲーム</h3>'
heading_pos = html.find(heading)
if heading_pos == -1:
    raise SystemExit("LIFE & GAME section not found")
grid_marker = '<div class="grid">'
grid_pos = html.find(grid_marker, heading_pos)
if grid_pos == -1:
    raise SystemExit("LIFE & GAME grid not found")
insert_pos = grid_pos + len(grid_marker)
card = '''
          <article class="card">
            <div class="cardTop">
              <h3>単位かんたん換算</h3>
              <span class="pill">新着・実用</span>
            </div>
            <p>長さ・重さ・面積・容量・温度をすぐ換算。坪⇄㎡やkg⇄lbにも対応。</p>
            <div class="actions">
              <a class="btn" href="apps/unit-converter/" target="_blank" rel="noreferrer">アプリを開く</a>
            </div>
          </article>
'''
html = html[:insert_pos] + card + html[insert_pos:]
html = html.replace('<div class="appProgress">39 <span>/ 100 apps</span></div>', '<div class="appProgress">40 <span>/ 100 apps</span></div>')
html = html.replace('aria-label="100アプリ計画 39%"', 'aria-label="100アプリ計画 40%"')
html = html.replace('.progressTrack i{display:block;width:39%;', '.progressTrack i{display:block;width:40%;')
html = html.replace('<div class="aboutPoint"><strong>39</strong><span>公開アプリ</span></div>', '<div class="aboutPoint"><strong>40</strong><span>公開アプリ</span></div>')
path.write_text(html, encoding="utf-8")
