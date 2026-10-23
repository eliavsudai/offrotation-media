# Off Rotation check-in routine (for Claude's scheduled check-ins)

1. Publish check: `cd /home/claude/offrotation-media && git pull -q && cat published.json`.
   Any approved post in schedule.json whose `when` has passed but isn't in published.json:
   publish it with `IG_TOKEN=$(cat /home/claude/secure/ig_token) python3 publisher/publish.py`,
   then commit + push published.json (with the session attribution lines).
   If graph.instagram.com is blocked (proxy 403), trigger GitHub instead:
   `gh api -X POST repos/eliavsudai/offrotation-media/actions/workflows/publish.yml/dispatches -f ref=main -f 'inputs[dry_run]=false'`
   and tell the user the allowlist needs graph.instagram.com.
2. Comments: `python3 publisher/comments.py list`, then answer each one in brand voice:
   lowercase, short, warm, music-literate, never salesy; Spanish comments in Spanish;
   one emoji at most. If someone shares three songs: thank them and ASK permission
   before featuring/pressing ("can we press these into a cover and feature it here?").
   Spam/bots/self-promo: `comments.py skip ID` (never delete). Never promise a launch date.
3. Tell the user briefly only if something needs them (a failed post, a yes to featuring, a question you can't answer).

## Guess Reel answers (post as a reply/comment on Thu Oct 29, then pin it)
- Sin Suelo: Soda Stereo, Caifanes, Los Prisioneros
- The Sun Has Teeth Too: Ramones, The Clash, Buzzcocks
- Quiet, Full of Things: Beethoven, Chopin, Debussy
Comment text: "answers: sin suelo = soda stereo, caifanes, los prisioneros · the sun has teeth too = ramones, the clash, buzzcocks · quiet, full of things = beethoven, chopin, debussy. same three, same album: try them in soulprint at launch."
Before then, never reveal or confirm answers in replies.
