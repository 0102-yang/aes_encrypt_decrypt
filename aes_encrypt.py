from Crypto.Cipher import AES
import base64


def aes_encrypt(value, key, iv):
    """
    Encrypt the value string with the given key and iv.
    :param value: the original string.
    :param key: the key.
    :param iv: the offset vector.
    :return:
    """

    def pad(s):
        """
        Complete the length of the string to a multiple of 16 bytes.
        :param s: the string.
        :return: completed string.
        """
        block_size = 16
        s = s + (block_size - len(s) % block_size) * chr(block_size - len(s) % block_size)
        return s

    return str(base64.b64encode(AES.new(key.encode(), AES.MODE_CBC, iv.encode()).encrypt(pad(value).encode())), 'utf8')
