from passlib.hash import sha256_crypt
password=sha256_crypt.encrypt("password")
password2=sha256_crypt.encrypt("password")
print (password)
print (password2)
verify=sha256_crypt.verify("password",password)
print (verify)
