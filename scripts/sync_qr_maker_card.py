from pathlib import Path

path = Path("index.html")
html = path.read_text(encoding="utf-8")

href = 'apps/qr-maker/'
if href in html:
    raise SystemExit("QR maker card already exists")

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
              <h3>QRつくる</h3>
              <span class="pill">新着・便利</span>
            </div>
            <p>URL・文字・Wi-Fi情報をスマホですぐQRコード化。画像保存にも対応。</p>
            <div class="actions">
              <a class="btn" href="apps/qr-maker/" target="_blank" rel="noreferrer">アプリを開く</a>
            </div>
          </article>
'''

html = html[:insert_pos] + card + html[insert_pos:]
html = html.replace('<div class="heroStat"><strong>38</strong><span>FREE APPS</span></div>', '<div class="heroStat"><strong>39</strong><span>FREE APPS</span></div>', 1)
html = html.replace('<div class="appProgress">54 <span>/ 100 apps</span></div>', '<div class="appProgress">55 <span>/ 100 apps</span></div>', 1)
html = html.replace('aria-label="100アプリ計画 54%"', 'aria-label="100アプリ計画 55%"', 1)
html = html.replace('<span>無料アプリ 37本公開中｜100 Apps Project</span>', '<span>無料アプリ 55本公開中｜100 Apps Project</span>', 1)
path.write_text(html, encoding="utf-8")
