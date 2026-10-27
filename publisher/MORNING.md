# Off Rotation morning check-up (7:30 am Guatemala, daily)

1. Pull insights for every post published in the last 72 h (GET /{media-id}/insights):
   reels: reach, views/plays, saved, shares, likes, comments, total_interactions, ig_reels_avg_watch_time;
   carousels/images: reach, saved, shares, likes, comments. Also followers_count from /me.
2. Compare each post to the account average. A post is boost-worthy if, after at least 24 h,
   its shares+saves per 1,000 reach is clearly above the rest (top performer) AND its audio is
   boost-safe (no Instagram library song, no Content ID track: lofi/jazz are NOT boost-safe; house/disco are).
3. Budget: $20 total for the pre-launch week, tracked in /home/claude/secure/boost.json
   ({"spent":0,"boosts":[]}). Plan: $10 Mon–Tue on the best weekend Reel, $10 Thu–Fri on the launch Reel.
   Only propose a boost if it fits the remaining budget.
4. Send the user ONE short message (SendUserMessage): follower count and change, the top post of the
   last day, and either "no boost today" or a specific proposal (post, $/day, days, goal = profile visits,
   audience US+MX+CO+GT+AR+CL, ages 18–34, interests music/vinyl/indie/album art). Never spend; they tap Boost.
5. Then run CHECKIN.md (publish anything late, reply to comments).

## During the promo test (Oct 26 – Nov 9) — overrides steps 2–4
Run `python3 publisher/results.py` and report in the one message: followers (+change), yesterday's two formats
with hold %, care/1k, follows, and the current top 3 formats. **No boost proposals during the test** (see TEST.md).
