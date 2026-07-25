from pathlib import Path

path = Path("index.html")
html = path.read_text(encoding="utf-8")

href = 'apps/menu-trio/'
if href in html:
    raise SystemExit("menu trio card already exists")

marker = '''      <div class="section">
        <h3 style="margin:14px 0 0;"><small style="display:block;letter-spacing:.16em;color:var(--muted);font-size:12px;">FAMILY</small>家族</h3>'''

section = '''      <div class="section">
        <h3 style="margin:14px 0 0;"><small style="display:block;letter-spacing:.16em;color:var(--muted);font-size:12px;">LIFE</small>暮らし・ゲーム</h3>
        <div class="grid">
          <article class="card">
            <div class="cardTop">
              <h3>献立3択メーカー</h3>
              <span class="pill">新着・暮らし</span>
            </div>
            <p>気分・時間・食材から、今日の献立候補を3つに絞る。</p>
            <div class="actions">
              <a class="btn" href="apps/menu-trio/" target="_blank" rel="noreferrer">アプリを開く</a>
            </div>
          </article>
        </div>
      </div>

'''

if marker not in html:
    raise SystemExit("homepage insertion marker not found")

html = html.replace(marker, section + marker, 1)
html = html.replace('<div class="heroStat"><strong>37</strong><span>FREE APPS</span></div>', '<div class="heroStat"><strong>38</strong><span>FREE APPS</span></div>', 1)
path.write_text(html, encoding="utf-8")
