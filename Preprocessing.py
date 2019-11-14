def stopword_removal(sentence):
    token = sentence.split()
    stopword = [line.rstrip('\n\r') for line in open('stopwords.txt')]
    temp = []
    for i in range(len(token)):
        if token[i] not in stopword:
            temp.append(token[i])
    temp = ' '.join(temp)
    return temp


def remove_escape(d):
    d = d.split('\\')
    d = ' '.join(d)
    return d


def remove_url(d):
    d = d.split()
    i = 0
    while i < len(d):
        if 'https://' in d[i]:
            d.remove(d[i])
            i -= 1
        elif 'http://' in d[i]:
            d.remove(d[i])
            i -= 1
        i += 1

    d = ' '.join(d)
    return d


def remove_punctuation(d):
    d = d.split()
    i = 0
    while i < len(d):
        if len(d) > 0:
            if d[i][0] == 'x' and len(d[i]) == 3:
                d.remove(d[i])
                i -= 1
        if len(d) > 0:
            if len(d[i]) == 1:
                d.remove(d[i])
                i -= 1
        if len(d) > 0:
            if 'rt' in d[i]:
                d.remove(d[i])
                i -= 1
        i += 1
    d = ' '.join(d)
    return d