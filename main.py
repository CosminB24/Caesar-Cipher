import caesar_cipher as cc

string = "PUXKN QJRA ANLNREN TRWPMXV"

cc.decrypt_message(string)
cc.decrypt_message_with_specific_shift(string, 12)
cc.encrypt_message(string)
cc.encrypt_message_with_specific_shift(string, 12)