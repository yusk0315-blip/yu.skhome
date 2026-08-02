from pathlib import Path

path = Path("index.html")
html = path.read_text(encoding="utf-8")

href = 'apps/parking-memo/'
if href in html:
    raise SystemExit("parking memo card already exists")

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
              <h3>駐車位置メモ</h3>
              <span class="pill">新着・暮らし</span>
            </div>
            <p>階・区画・目印・現在地を保存して、広い駐車場でも迷わない。</p>
            <div class="actions">
              <a class="btn" href="apps/parking-memo/" target="_blank" rel="noreferrer">アプリを開く</a>
            </div>
          </article>
'''

html = html[:insert_pos] + card + html[insert_pos:]
path.write_text(html, encoding="utf-8")
