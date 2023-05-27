import hashlib


def hashPassword(password: str):
    encryptedPassword = hashlib.sha256()
    thing = bytes(password, 'utf-8')
    encryptedPassword.update(thing)
    encryptedPassword.digest()
    return encryptedPassword.hexdigest()

