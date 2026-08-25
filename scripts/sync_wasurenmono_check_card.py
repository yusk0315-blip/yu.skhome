from pathlib import Path

path = Path("index.html")
html = path.read_text(encoding="utf-8")

href = 'apps/wasurenmono-check/'
if href in html:
    raise SystemExit("wasurenmono check card already exists")

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
              <h3>忘れ物チェックリスト</h3>
              <span class="pill">新着・暮らし</span>
            </div>
            <p>出勤・保育園・旅行など、いつもの持ち物を保存して出発前30秒で確認。</p>
            <div class="actions">
              <a class="btn" href="apps/wasurenmono-check/" target="_blank" rel="noreferrer">アプリを開く</a>
            </div>
          </article>
'''

html = html[:insert_pos] + card + html[insert_pos:]
html = html.replace('<div class="heroStat"><strong>37</strong><span>FREE APPS</span></div>', '<div class="heroStat"><strong>38</strong><span>FREE APPS</span></div>', 1)
path.write_text(html, encoding="utf-8")
