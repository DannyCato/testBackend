# variables shared across many files

endpoints = dict()

def _contains(value):
    return endpoints.keys.__contains__(value)
        
def add_endpoint(new_value):
    if not _contains(new_value):
        endpoints[new_value] = {new_value,}

def add_child(parent, child):
    if not _contains(parent):
        add_endpoint(parent)
    endpoints[parent] = endpoints[parent].add(child)