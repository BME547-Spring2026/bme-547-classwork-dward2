from Crypto.Cipher import AES

aes_key_str = "YellowIsGoodVibe"
aes_key = aes_key_str.encode()

def send_encoded_message(plain_text_message):
    print("Plain text: ", plain_text_message)
    cipher = AES.new(aes_key, mode=AES.MODE_CTR)
    ciphertext = cipher.encrypt(plain_text_message.encode())
    print("Cipher Text:  ", ciphertext)

    with open("encrypted.bin", "wb") as out_file:
        out_file.write(cipher.nonce)
        out_file.write(ciphertext)


def receive_encoded_message(filename):
    with open(filename, "rb") as in_file:
        nonce = in_file.read(8)
        ciphertext = in_file.read()

    partner_aes_key_str = "YellowIsGoodVibe"
    partner_aes_key = partner_aes_key_str.encode()
    decrypt_cipher = AES.new(partner_aes_key, mode=AES.MODE_CTR, nonce=nonce)
    message = decrypt_cipher.decrypt(ciphertext)
    print("Message: ", message.decode())


if __name__ == "__main__":
    send_encoded_message("Today is Thursday")
    receive_encoded_message("encrypted.bin")