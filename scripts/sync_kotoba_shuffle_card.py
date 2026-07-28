from pathlib import Path

path = Path("index.html")
html = path.read_text(encoding="utf-8")

href = 'apps/kotoba-shuffle/'
if href in html:
    raise SystemExit("kotoba shuffle card already exists")

marker = '''      <div class="section">
        <h3 style="margin:14px 0 0;"><small style="display:block;letter-spacing:.16em;color:var(--muted);font-size:12px;">FAMILY</small>家族</h3>'''

section = '''      <div class="section">
        <h3 style="margin:14px 0 0;"><small style="display:block;letter-spacing:.16em;color:var(--muted);font-size:12px;">LIFE & GAME</small>暮らし・ゲーム</h3>
        <div class="grid">
          <article class="card">
            <div class="cardTop">
              <h3>ことばシャッフル</h3>
              <span class="pill">新着・ゲーム</span>
            </div>
            <p>バラバラのひらがなを並べ替える、10問のことばパズル。</p>
            <div class="actions">
              <a class="btn" href="apps/kotoba-shuffle/" target="_blank" rel="noreferrer">ゲームを開く</a>
            </div>
          </article>
        </div>
      </div>

'''

if marker not in html:
    raise SystemExit("homepage insertion marker not found")

html = html.replace(marker, section + marker, 1)
path.write_text(html, encoding="utf-8")
