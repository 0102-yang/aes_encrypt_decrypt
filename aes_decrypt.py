import base64
from Crypto.Cipher import AES


def aes_decrypt(value, key, iv):
    """
    Decrypt the value cipher string to clear string with given key and iv.
    :param value: the value string.
    :param key: the key.
    :param iv: the offset vector.
    :return:
    """

    return str(
        (lambda s: s[0:-s[-1]])(AES.new(key.encode(), AES.MODE_CBC, iv.encode()).decrypt(base64.b64decode(value))),
        'utf8')