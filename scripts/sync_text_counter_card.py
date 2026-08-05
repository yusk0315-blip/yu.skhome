from pathlib import Path

path = Path("index.html")
html = path.read_text(encoding="utf-8")
href = 'apps/text-counter/'
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
              <h3>文字数・読む時間カウンター</h3>
              <span class="pill">新着・仕事</span>
            </div>
            <p>文章の文字数と、読む・話す時間の目安を入力と同時に計測。</p>
            <div class="actions">
              <a class="btn" href="apps/text-counter/" target="_blank" rel="noreferrer">アプリを開く</a>
            </div>
          </article>
'''
html = html[:insert_pos] + card + html[insert_pos:]
path.write_text(html, encoding="utf-8")
