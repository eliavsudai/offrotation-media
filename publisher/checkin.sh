#!/bin/bash
# One check-in: publish anything due, clean up media >1h after publishing, list new comments.
cd /home/claude/offrotation-media
git pull -q 2>&1 | tail -1
IG_TOKEN=$(cat /home/claude/secure/ig_token) timeout 550 python3 publisher/publish.py 2>&1 | grep -E "PUBLISH|done|ERROR|SKIP"
python3 - <<'PY'
import json, os, shutil, datetime as dt
d=json.load(open('schedule.json')); p=json.load(open('published.json')); now=dt.datetime.now(dt.timezone.utc); rm=[]
for x in d['posts']:
    pub=p.get(x['id'])
    if pub and not x.get('cleaned') and (now-dt.datetime.fromisoformat(pub['published_at'])).total_seconds()>3600:
        if os.path.isdir(f"posts/{x['id']}"): shutil.rmtree(f"posts/{x['id']}")
        x['media']=[]; x.pop('cover',None); x['cleaned']=True; rm.append(x['id'])
json.dump(d,open('schedule.json','w'),indent=2,ensure_ascii=False)
if rm: print('cleaned',rm)
PY
git add -A
git -c user.name="Off Rotation" -c user.email="eliavsudai@users.noreply.github.com" commit -q -m "Check-in: publish due posts, clean up published media

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01KHYun5z9or8rxLpaRqQ8gK" 2>/dev/null && git push -q 2>&1 | tail -1
timeout 90 python3 publisher/comments.py list 2>&1 | tail -15
