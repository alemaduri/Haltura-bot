import setup

def position(id, db):
    for i in db['users']:
        if i['id'] == id:
            return i['position']

def position_set(id, db, pos):
    for i in db['users']:
        if i['id'] == id:
            i['position'] = pos

def looking_set(id, db, look):
    for i in db['users']:
        if i['id'] == id:
            i['looking'] = look

def looking(id, db):
    for i in db['users']:
        if i['id'] == id:
            return i['looking']

def generate_text(filter):
    text = ''
    for i in setup.tegs[filter]:
        text += str(setup.sxem[i]['id']) + '. ' + str(setup.sxem[i]['sxem_name']) + ' (' + str(setup.sxem[i]['price']) + ')\n'
    text += 'Для выбора схемы, напишите число.'
    return text
