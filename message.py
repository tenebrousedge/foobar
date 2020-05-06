import base64

MESSAGE = '''
L0IdEAERCgYAYkRdRXMCHAADBkhZU2IHCAk4AA8CFxdIVUllQwIWIAALCAcWSFlTYgEBAzsXGhZF UlVVVCwKBBcxAQcHDhdIWVNiBQQNPQAYAA8XAQFUZV5HQiELAgoBGQoRVGlEQBc1BwwMFgFIVUll QxQEMgBJSUJVCRocYkRdRXMSBwtDVRI=
'''

KEY = 'TenebrousEdge'

result = []
for i, c in enumerate(base64.b64decode(MESSAGE)):
    result.append(chr(ord(c) ^ ord(KEY[i % len(KEY)])))

print ''.join(result)
