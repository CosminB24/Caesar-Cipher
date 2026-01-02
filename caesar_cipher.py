def decrypt_message(message):
    for shift in range(26):
        result = ""
        for char in message:
            if "a" <= char <= "z":
                result += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            elif 'A' <= char <= 'Z':
                result += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            else:
                result += char
        print("The decrypted message is:", result, "with key:", shift)

def decrypt_message_with_specific_shift(message, shift):
    result = ""
    for char in message:
        if 'a' <= char <= 'z':
            result += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
        elif "A" <= char <= "Z":
            result += chr((ord(char) - ord("A") - shift) % 26 + ord("A"))
        else:
            result += char
    print("The decrypted message is:", result)

def encrypt_message(message):
    for shift in range(26):
        result = ""
        for char in message:
            if 'a' <= char <= 'z':
                result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            elif "A" <= char <= "Z":
                result += chr((ord(char) - ord("A") + shift) % 26 + ord("A"))
            else:
                result += char
        print("The encrypted message is:", result, "with key:", shift)

def encrypt_message_with_specific_shift(message, shift):
    result = ""
    for char in message:
        if 'a' <= char <= 'z':
            result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        elif "A" <= char <= "Z":
            result += chr((ord(char) - ord("A") + shift) % 26 + ord("A"))
        else:
            result += char
    print("The encrypted message is:", result)
