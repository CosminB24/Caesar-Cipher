ALPHABET = 26

def _shift_char(char, shift):
    if 'a' <= char <= 'z':
        return chr((ord(char) - ord('a') + shift) % ALPHABET + ord('a'))
    if 'A' <= char <= 'Z':
        return chr((ord(char) - ord('A') + shift) % ALPHABET + ord('A'))
    return char


def _apply_shift(message, shift):
    shift = shift % ALPHABET
    result = ""

    for char in message:
        result += _shift_char(char, shift)

    return result

def decrypt_message(message):
    results = []
    for shift in range(ALPHABET):
        results.append((shift, _apply_shift(message, -shift)))
    return results


def decrypt_message_with_specific_shift(message, shift):
    return _apply_shift(message, -shift)


def encrypt_message(message):
    results = []
    for shift in range(ALPHABET):
        results.append((shift, _apply_shift(message, shift)))
    return results


def encrypt_message_with_specific_shift(message, shift):
    return _apply_shift(message, shift)