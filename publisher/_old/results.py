"""Pull insights for every promo-test Reel and write publisher/results.csv."""
import json, csv, os, urllib.request, urllib.parse, datetime as dt
B=os.path.dirname(os.path.abspath(__file__)); R=os.path.dirname(B)
T=open('/home/claude/secure/ig_token').read().strip(); G='https://graph.instagram.com/v23.0/'
def get(p,**q):
    q['access_token']=T; return json.load(urllib.request.urlopen(G+p+'?'+urllib.parse.urlencode(q)))
sched={p['id']:p for p in json.load(open(f'{R}/schedule.json'))['posts']}
pub=json.load(open(f'{R}/published.json'))
fl=[]
if os.path.exists(f'{B}/followers.log'):
    for l in open(f'{B}/followers.log'):
        t,n=l.split(); fl.append((dt.datetime.fromisoformat(t),int(n)))
def fol_at(t):
    best=None
    for ts,n in fl:
        if ts<=t: best=n
    return best
ids=sorted([k for k in pub if 'promo' in k and k in sched], key=lambda k: pub[k]['published_at'])
rows=[]
for i,k in enumerate(ids):
    s=sched[k]; m=pub[k]['media_id']
    ins={d['name']:d['values'][0]['value'] for d in get(m+'/insights',metric='reach,views,saved,shares,likes,comments,ig_reels_avg_watch_time')['data']}
    t0=dt.datetime.fromisoformat(pub[k]['published_at'])
    t1=dt.datetime.fromisoformat(pub[ids[i+1]]['published_at']) if i+1<len(ids) else dt.datetime.now(dt.timezone.utc)
    a,b=fol_at(t0),fol_at(t1); gain=(b-a) if a is not None and b is not None else ''
    age=(dt.datetime.now(dt.timezone.utc)-t0).total_seconds()/3600
    reach=ins['reach'] or 0; dur=s.get('dur') or 20
    rows.append(dict(id=k,format=s.get('format',''),slot=s['when'][11:16],age_h=round(age,1),reach=reach,views=ins['views'],
        hold_pct=round(100*ins['ig_reels_avg_watch_time']/1000/dur,1),care_per_1k=round(1000*(ins['shares']+ins['saved'])/reach,1) if reach else 0,
        shares=ins['shares'],saves=ins['saved'],likes=ins['likes'],comments=ins['comments'],follows=gain,link=pub[k]['permalink']))
with open(f'{B}/results.csv','w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
for r in rows: print(r['id'],'#'+str(r['format']),r['slot'],f"{r['age_h']}h reach {r['reach']} hold {r['hold_pct']}% care {r['care_per_1k']}/1k follows {r['follows']}")
