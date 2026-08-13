from pathlib import Path

path = Path("index.html")
html = path.read_text(encoding="utf-8")
href = 'apps/sleep-time-planner/'
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
              <h3>睡眠時刻プランナー</h3>
              <span class="pill">新着・暮らし</span>
            </div>
            <p>起きたい・寝たい時刻から、確保できる睡眠時間ごとの候補時刻をすぐ計算。</p>
            <div class="actions">
              <a class="btn" href="apps/sleep-time-planner/" target="_blank" rel="noreferrer">アプリを開く</a>
            </div>
          </article>
'''

html = html[:insert_pos] + card + html[insert_pos:]
html = html.replace('<div class="appProgress">42 <span>/ 100 apps</span></div>', '<div class="appProgress">43 <span>/ 100 apps</span></div>')
html = html.replace('aria-label="100アプリ計画 42%"', 'aria-label="100アプリ計画 43%"')
html = html.replace('.progressTrack i{display:block;width:42%;', '.progressTrack i{display:block;width:43%;')
html = html.replace('<div class="aboutPoint"><strong>42</strong><span>公開アプリ</span></div>', '<div class="aboutPoint"><strong>43</strong><span>公開アプリ</span></div>')
path.write_text(html, encoding="utf-8")
