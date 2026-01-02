import caesar_cipher as cc

text = "PUXKN QJRA ANLNREN TRWPMXV"

results = cc.decrypt_message(text)

for item in results:
    shift = item[0]
    candidate = item[1]
    print("shift =", shift, "message =", candidate)

print("Specific shift: ")

print("decrypt shift 12:", cc.decrypt_message_with_specific_shift(text, 12))
print("encrypt shift 12:", cc.encrypt_message_with_specific_shift(text, 12))
