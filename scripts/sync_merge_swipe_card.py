from pathlib import Path
import re

path = Path('index.html')
html = path.read_text(encoding='utf-8')
href = 'apps/merge-swipe/'
if href in html:
    raise SystemExit('Merge Swipe card already exists')
heading = '<small style="display:block;letter-spacing:.16em;color:var(--muted);font-size:12px;">LIFE & GAME</small>暮らし・ゲーム</h3>'
hp = html.find(heading)
if hp == -1:
    raise SystemExit('LIFE & GAME section not found')
grid = '<div class="grid">'
gp = html.find(grid, hp)
if gp == -1:
    raise SystemExit('LIFE & GAME grid not found')
ip = gp + len(grid)
card = '''
          <article class="card">
            <div class="cardTop">
              <h3>MERGE SWIPE</h3>
              <span class="pill">新着・ゲーム</span>
            </div>
            <p>同じ数字をスワイプで重ねて4096を目指す、スマホ向け数字パズル。</p>
            <div class="actions">
              <a class="btn" href="apps/merge-swipe/" target="_blank" rel="noreferrer">ゲームを開く</a>
            </div>
          </article>
'''
html = html[:ip] + card + html[ip:]

def inc(pattern, repl):
    global html
    html, n = re.subn(pattern, repl, html, count=1)
    return n

inc(r'(<div class="heroStat"><strong>)(\d+)(</strong><span>FREE APPS</span></div>)', lambda m: m.group(1)+str(int(m.group(2))+1)+m.group(3))
inc(r'(<div class="appProgress">)(\d+)( <span>/ 100 apps</span></div>)', lambda m: m.group(1)+str(int(m.group(2))+1)+m.group(3))
inc(r'(aria-label="100アプリ計画 )(\d+)(%")', lambda m: m.group(1)+str(min(100,int(m.group(2))+1))+m.group(3))
inc(r'(<span>無料アプリ )(\d+)(本公開中｜100 Apps Project</span>)', lambda m: m.group(1)+str(int(m.group(2))+1)+m.group(3))
path.write_text(html, encoding='utf-8')
