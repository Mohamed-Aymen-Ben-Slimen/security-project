from consolemenu import *
from consolemenu.items import *
from cryptopentbox import *



# Create the menu
menu = ConsoleMenu("PentBox", "Enjoy!")

#Create encoding menu
menu_encoding_decoding = ConsoleMenu("PentBox", "Encoding Decoding")
encoding_item = FunctionItem("Encoding",encoding)
menu_encoding_decoding.append_item(encoding_item)
decoding_item = FunctionItem("Decoding",decoding)
menu_encoding_decoding.append_item(decoding_item)
#Add to main menu
encoding_submenu_item = SubmenuItem("Encoding Decoding", menu_encoding_decoding, menu)
menu.append_item(encoding_submenu_item)

#Create hash menu
menu_hashing = ConsoleMenu("PentBox", "Hashing")
md5_item = FunctionItem("md5",hashage,["md5"])
menu_hashing.append_item(md5_item)
sh1_item = FunctionItem("sh1",hashage,["sh1"])
menu_hashing.append_item(sh1_item)
sha256_item = FunctionItem("sha256",hashage,["sha256"])
menu_hashing.append_item(sha256_item)
sha384_item = FunctionItem("sha384",hashage,["sha384"])
menu_hashing.append_item(sha384_item)
sha512_item = FunctionItem("sha512",hashage,["sha512"])
menu_hashing.append_item(sha512_item)
ripemd_160_item = FunctionItem("ripemd_160",hashage,["ripemd_160"])
menu_hashing.append_item(ripemd_160_item)
#Add to main menu
hashing_submenu_item = SubmenuItem("Hashing", menu_hashing, menu)
menu.append_item(hashing_submenu_item)


#Create crack hash menu
menu_crack_hash = ConsoleMenu("PentBox", "Crack Hash")

#Create Dictionary menu
menu_dictionary = ConsoleMenu("Crack Hashing", "Dictionary")
dictionary1_item = FunctionItem("wordlist",crack_hash_dictionary_attack,["wordlist.txt"])
menu_dictionary.append_item(dictionary1_item)
dictionary2_item = FunctionItem("names",crack_hash_dictionary_attack,["names.txt"])
menu_dictionary.append_item(dictionary2_item)
dictionary3_item = FunctionItem("plain text",crack_hash_dictionary_attack,["plaintext.txt"])
menu_dictionary.append_item(dictionary3_item)
#Add to crack hash menu
dictionary_submenu_item = SubmenuItem("Dictionary", menu_dictionary, menu_crack_hash)
menu_crack_hash.append_item(dictionary_submenu_item)

brute_force_item = FunctionItem("Brute Force",crack_hash_brute_force)
menu_crack_hash.append_item(brute_force_item)

#Add to main menu
crack_submenu_item = SubmenuItem("Crack Hash", menu_crack_hash, menu)
menu.append_item(crack_submenu_item)



#Create symetric menu
menu_symetric = ConsoleMenu("PentBox", "Symetric Encrypting Decrypting")

#Create symetric encrypt algorithm menu
menu_symetric_encrypt = ConsoleMenu("Symetric Encrypting", "Algorithm") 
des_item = FunctionItem("des",encrypt,["des"])
menu_symetric_encrypt.append_item(des_item)
aes_item = FunctionItem("aes",encrypt,["aes"])
menu_symetric_encrypt.append_item(aes_item)
arc2_item = FunctionItem("arc2",encrypt,["arc2"])
menu_symetric_encrypt.append_item(arc2_item)
blowfish_item = FunctionItem("blowfish",encrypt,["blowfish"])
menu_symetric_encrypt.append_item(blowfish_item)
fernet_item = FunctionItem("fernet",encrypt,["fernet"])
menu_symetric_encrypt.append_item(fernet_item)

#Create symetric decrypt algorithm menu
menu_symetric_decrypt = ConsoleMenu("Symetric Decrypting", "Algorithm") 
des_item = FunctionItem("des",decrypt,["des"])
menu_symetric_decrypt.append_item(des_item)
aes_item = FunctionItem("aes",decrypt,["aes"])
menu_symetric_decrypt.append_item(aes_item)
arc2_item = FunctionItem("arc2",decrypt,["arc2"])
menu_symetric_decrypt.append_item(arc2_item)
blowfish_item = FunctionItem("blowfish",decrypt,["blowfish"])
menu_symetric_decrypt.append_item(blowfish_item)
fernet_item = FunctionItem("fernet",decrypt,["fernet"])
menu_symetric_decrypt.append_item(fernet_item)

#Add to symetric menu
symetric_encrypt_submenu_item = SubmenuItem("Encrypt", menu_symetric_encrypt, menu_symetric)
menu_symetric.append_item(symetric_encrypt_submenu_item)

symetric_decrypt_submenu_item = SubmenuItem("Decrypt", menu_symetric_decrypt, menu_symetric)
menu_symetric.append_item(symetric_decrypt_submenu_item)

#Add to main menu
symetric_submenu_item = SubmenuItem("Symetric Encrypting Decrypting", menu_symetric, menu)
menu.append_item(symetric_submenu_item)






#Create symetric menu
menu_asymetric = ConsoleMenu("PentBox", "Asymetric")
#ccreate asymetric menu input_to_encrypt
menu_asymetric_input_to_encrypt= ConsoleMenu("Asymetric ","Encrypting Signing")


menu_asymetric_key = ConsoleMenu("Generate keys", "Algorithm") 
rsa_key_item = FunctionItem("rsa",generate_key,["rsa"])
menu_asymetric_key.append_item(rsa_key_item)

dsa_key_item = FunctionItem("dsa",generate_key,["dsa"])
menu_asymetric_key.append_item(dsa_key_item)

#Add to asymetric menu input_to_encrypt
asymetric_key_submenu_item = SubmenuItem("Generate Keys", menu_asymetric_key, menu_asymetric_input_to_encrypt)
menu_asymetric_input_to_encrypt.append_item(asymetric_key_submenu_item)

#create
menu_asymetric_encrypt = ConsoleMenu("Asymetric Encrypting", "Algorithm") 
rsa_encrypt_item = FunctionItem("rsa",encrypt_asym,["rsa"])
menu_asymetric_encrypt.append_item(rsa_encrypt_item)

#Add to asymetric menu input_to_encrypt
asymetric_encrypt_submenu_item = SubmenuItem("Encrypt", menu_asymetric_encrypt, menu_asymetric_input_to_encrypt)
menu_asymetric_input_to_encrypt.append_item(asymetric_encrypt_submenu_item)

#create
menu_asymetric_sign = ConsoleMenu("Asymetric Sign", "Algorithm") 
rsa_sign_item = FunctionItem("rsa",sign_asym,["rsa"])
menu_asymetric_sign.append_item(rsa_sign_item)

dsa_sign_item = FunctionItem("dsa",sign_asym,["dsa"])
menu_asymetric_sign.append_item(dsa_sign_item)

#Add to asymetric menu input_to_encrypt
asymetric_sign_submenu_item = SubmenuItem("Sign", menu_asymetric_sign, menu_asymetric_input_to_encrypt)
menu_asymetric_input_to_encrypt.append_item(asymetric_sign_submenu_item)

#Add to asymetric menu
asymetric_input_to_encrypt_submenu_item = SubmenuItem("Encrypting Signing", menu_asymetric_input_to_encrypt, menu_asymetric)
menu_asymetric.append_item(asymetric_input_to_encrypt_submenu_item)



#create menu_asymetric_input_encrypted
menu_asymetric_input_encrypted= ConsoleMenu("Asymetric ","Decrypting Verify Sign")


#create
menu_asymetric_encrypted = ConsoleMenu("Asymetric Decrypting", "Algorithm") 
rsa_encrypted_item = FunctionItem("rsa",decrypt_asym,["rsa"])
menu_asymetric_encrypted.append_item(rsa_encrypted_item)

#Add to asymetric menu input_to_encrypt
asymetric_encrypted_submenu_item = SubmenuItem("Decrypt", menu_asymetric_encrypted, menu_asymetric_input_encrypted)
menu_asymetric_input_encrypted.append_item(asymetric_encrypted_submenu_item)

#create
menu_asymetric_signed = ConsoleMenu("Asymetric Verify Sign", "Algorithm") 
rsa_signed_item = FunctionItem("rsa",verify_asym,["rsa"])
menu_asymetric_signed.append_item(rsa_signed_item)

dsa_signed_item = FunctionItem("dsa",verify_asym,["dsa"])
menu_asymetric_signed.append_item(dsa_signed_item)

#Add to asymetric menu input_to_encrypt
asymetric_signed_submenu_item = SubmenuItem("Verify Sign", menu_asymetric_signed, menu_asymetric_input_encrypted)
menu_asymetric_input_encrypted.append_item(asymetric_signed_submenu_item)



asymetric_input_encrypted_submenu_item = SubmenuItem("Decrypting Verify Sign", menu_asymetric_input_encrypted, menu_asymetric)
menu_asymetric.append_item(asymetric_input_encrypted_submenu_item)





#Add to main menu
asymetric_submenu_item = SubmenuItem("Asymetric Encrypting Signing ", menu_asymetric, menu)
menu.append_item(asymetric_submenu_item)



# Finally, we call show to show the menu and allow the user to interact
menu.show()
