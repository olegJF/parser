import codecs


# read data from file
handle = codecs.open('code.html','r', 'utf-8')
data = handle.read()
handle.close()

# write into file
handle = codecs.open('bigmir.txt', "w", 'utf-8')
handle.write(str(data))
handle.close()