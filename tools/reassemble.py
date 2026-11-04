import re, sys
# Restore the embedded font data: src.stripped.html has url(FONTDATA) placeholders in the same order as the original.
import os
HERE = os.path.dirname(os.path.abspath(__file__))
orig = open(os.path.join(HERE, '..', 'crm', "3 - Corella CRM - Branch (engineer's version).html"), encoding='utf-8').read()
fonts = re.findall(r'url\(data:font/woff2;base64,[A-Za-z0-9+/=]+\)', orig)
src = open(os.path.join(HERE, 'src.stripped.html'), encoding='utf-8').read()
assert src.count('url(FONTDATA)') == len(fonts) == 4, (src.count('url(FONTDATA)'), len(fonts))
out = src
for f in fonts:
    out = out.replace('url(FONTDATA)', f, 1)
open(sys.argv[1], 'w', encoding='utf-8').write(out)
print('wrote', sys.argv[1], len(out), 'bytes')
