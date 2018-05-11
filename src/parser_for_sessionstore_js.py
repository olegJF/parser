import codecs
handle = codecs.open('f.js','r', 'utf-8')
data = handle.read()
handle.close()
template = '<!doctype html><html lang="en"><head><meta charset="utf-8"></head><body>'
end = '</body></html>'
begin = 0
addresses = []
while True:
    begin = data.find('"entries"', begin)
    if begin == -1: break
    url_begin = data.find('"url":', begin) + len('"url":')+1
    url_end = data.find(',', begin)-1
    title_begin = data.find('"title":', url_end) + len('"title":')
    title_end = data.find(',', title_begin)
    url = data[url_begin:url_end]
    title = data[title_begin:title_end]
    begin = title_end
    addresses.append({'url': url, 'title': title})


content = ''
for address in addresses:
    content += '<a href="{url}" target="_blank">{url}</a><p> {title}</p><br/>'.format(**address)
    content += '--------------<br/><br/>'
data = template + content + end
handle = codecs.open('parse.html', "w", 'utf-8')
handle.write(str(data))
handle.close() 