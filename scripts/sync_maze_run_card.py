from pathlib import Path

path = Path("index.html")
html = path.read_text(encoding="utf-8")
href = 'apps/maze-run/'
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
              <h3>迷路タイムアタック</h3>
              <span class="pill">新着・ゲーム</span>
            </div>
            <p>毎回変わる迷路をスワイプで攻略。最短タイムを狙う短時間ゲーム。</p>
            <div class="actions">
              <a class="btn" href="apps/maze-run/" target="_blank" rel="noreferrer">ゲームを開く</a>
            </div>
          </article>
'''
html = html[:insert_pos] + card + html[insert_pos:]
path.write_text(html, encoding="utf-8")
