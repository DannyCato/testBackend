from hashlib import sha512

# variables shared across many files

endpoints = dict()

def endpoints_contains(value):
    return endpoints.keys.__contains__(value)
        
def add_endpoint(hash, payload):
    if not endpoints_contains(hash):
        endpoints[hash] = payload

def create_hash(string: str):
    hasher = sha512()
    pass_bytes = bytes(string, 'utf-8')
    hasher.update(pass_bytes)
    hash = hasher.hexdigest()
    return hash