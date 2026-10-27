# Soulprint promo test — 15 formats, 15 days (Oct 26 – Nov 9, 2026)

Two Reels a day: 12:00 and 18:30 (America/Guatemala). No stories, no carousels.
Each format runs twice, once in each slot. **No boosts during the test.**
After Nov 9: rank formats, pick the winner(s), run them for the next two weeks; put the $20 behind the winner.

Every Reel: same Kokoro af_heart voice (unless the format says otherwise), print style, real app screens only,
clean Pixabay music (disco/house) at 0.20 under the VO, captions on screen, end card (icon, Free, For music lovers,
"Coming soon to the App Store" until launch → then "Free on the App Store · link in bio"). Caption ends with a
comment prompt. Tag every schedule.json entry with "format": <n> and "dur": <seconds>.

## Formats
1  Voiceover walkthrough (what the app makes, step by step)
2  Artist mashup reveal ("A + B + C = ?" → the album)
3  Guess the three (cover first, viewers guess the songs, reveal)
4  POV / meme text (no VO or minimal; punchy text cards, music-led)
5  Liner notes as a horoscope (VO reads the "about you" liner like a reading)
6  Genre speed-run (5 genres → 5 covers in ~10 s)
7  Her three vs his three (two people's picks, two albums, side by side)
8  Silent screen recording (taps + tune, no VO) — NEEDS user's screen recording by Nov 2
9  Listicle ("3 things Soulprint does that your music app doesn't")
10 Tune first (the generated tune is the hook, then the cover it came from)
11 Albums that don't exist (dream trios, fast cuts)
12 The proof (same three songs twice → identical album)
13 Founder story ("I built this because…") — user's own voice note or text-only; ask by Nov 3
14 Describe yourself in three songs (trend prompt, comment yours)
15 Before/after (plain playlist → album)

## Rotation (12:00 | 18:30)
D1  Mon Oct 26: 1  | 2      (done)
D2  Tue Oct 27: 3  | 4
D3  Wed Oct 28: 5  | 6
D4  Thu Oct 29: 7  | 9
D5  Fri Oct 30: 10 | 11
D6  Sat Oct 31: 12 | 14
D7  Sun Nov 1:  15 | 1
D8  Mon Nov 2:  2  | 8
D9  Tue Nov 3:  4  | 3
D10 Wed Nov 4:  6  | 5
D11 Thu Nov 5:  13 | 7
D12 Fri Nov 6:  11 | 10
D13 Sat Nov 7:  14 | 12
D14 Sun Nov 8:  8  | 15
D15 Mon Nov 9:  9  | 13
Second runs use a fresh example (new songs/artists), same format.

## Scoring (results.py → publisher/results.csv)
- hold %      = avg watch time / Reel length
- care / 1k   = (shares + saves) per 1,000 reach
- follows     = follower gain from post time to the next post (from publisher/followers.log)
- also reach, views, likes, comments; read at 24 h and 72 h.
Rank by: hold % (40%), care/1k (30%), follows (30%), each normalised across the 30 Reels.
