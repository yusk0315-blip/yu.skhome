from pathlib import Path

path = Path("index.html")
html = path.read_text(encoding="utf-8")
href = 'apps/dandori-timer/'
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
              <h3>段取りタイマー</h3>
              <span class="pill">新着・仕事</span>
            </div>
            <p>会議やプレゼンを項目ごとの持ち時間で進行。残り時間と進み具合をひと目で確認。</p>
            <div class="actions">
              <a class="btn" href="apps/dandori-timer/" target="_blank" rel="noreferrer">アプリを開く</a>
            </div>
          </article>
'''
html = html[:insert_pos] + card + html[insert_pos:]
# Keep the visible app count in sync with the new addition.
html = html.replace('<div class="appProgress">37 <span>/ 100 apps</span></div>', '<div class="appProgress">38 <span>/ 100 apps</span></div>')
html = html.replace('aria-label="100アプリ計画 37%"', 'aria-label="100アプリ計画 38%"')
html = html.replace('.progressTrack i{display:block;width:37%;', '.progressTrack i{display:block;width:38%;')
html = html.replace('<div class="aboutPoint"><strong>37</strong><span>公開アプリ</span></div>', '<div class="aboutPoint"><strong>38</strong><span>公開アプリ</span></div>')
path.write_text(html, encoding="utf-8")
