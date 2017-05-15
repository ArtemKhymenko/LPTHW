def scan(stuff):
    words = stuff.split()
    sentence = []
    for w in words:
        if w == "north" or w == "south" or w == "east":
            sentence += [('direction', w)]
        elif w == 'go' or w == 'kill' or w == 'eat':
            sentence += [('verb', w)]
        elif w == 'the' or w == 'in' or w == 'of':
            sentence += [('stop', w)]
        elif w == 'bear' or w == 'princess' or w == 'door':
            sentence += [('noun', w)]
        else:
            sentence += [('error', w)]
    return sentence
