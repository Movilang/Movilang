cd /home/claude/movilang && git pull -q origin main && python3 -c "
import os,json;fs=sorted(d+'/'+f for d in os.listdir('content/std') if os.path.isdir('content/std/'+d) for f in os.listdir('content/std/'+d) if f.endswith('.json'));json.dump(fs,open('content/std/index.json','w'));import hashlib;json.dump({f:hashlib.sha1(open('content/std/'+f,'rb').read()).hexdigest()[:16] for f in fs},open('content/std/manifest.json','w'));print(len(fs),'files')" && git add content/std && git commit -q -m "Lekcje standardu: $1

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01D1UVZRA38wcg3Ha2KHm2EW" && git push -q origin main 2>/dev/null; git log --oneline -1
