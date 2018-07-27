
def _init():
    global _global_list
    _global_list=[]

def _init2():
    global _global_list2
    _global_list2=[]

def _init3():
    global _global_list3
    _global_list3=[]

def set_value(value):
    _global_list.append(value)

def set_value2(value):
    _global_list2.append(value)

def set_key(value):
    _global_list3.append(value)

def get_length():
    return len(_global_list)

def get_value(i,defValue=None):
    try:
        return _global_list[i]
    except KeyError:
        return defValue

def get_value2(i,defValue=None):
    try:
        return _global_list2[i]
    except KeyError:
        return defValue

def get_key(i,defValue=None):
    try:
        return _global_list3[i]
    except KeyError:
        return defValue