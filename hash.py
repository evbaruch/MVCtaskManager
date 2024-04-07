with open("java.dll", "rb") as input_file, open("decrypted_java.dll", "wb") as output_file:
  while (byte := input_file.read(1)):
    decrypted_byte = bytes([byte[0] ^ 0x81])
    output_file.write(decrypted_byte)
    print(decrypted_byte)