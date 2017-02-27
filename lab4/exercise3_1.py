
# coding: utf-8

# In[25]:

from Crypto.Hash import SHA


# In[26]:

from Crypto.PublicKey import RSA


# In[27]:

from Crypto import Random


# In[28]:

inputmessage = input("please type a message:")


# In[29]:

hash_sha1 = SHA.new(inputmessage.encode()).digest()


# In[30]:

random_generator = Random.new().read


# In[31]:

Bob_key = RSA.generate(1024,random_generator)


# In[32]:

random_generator = Random.new().read


# In[33]:

Alice_key = RSA.generate(1024,random_generator)


# In[34]:

signature = Bob_key.sign(hash_sha1,'')


# In[37]:

hasd_data_encry = Alice_key.publickey().encrypt(hash_sha1, 32)


# In[38]:

hash_of_decrypted = Alice_key.decrypt(hasd_data_encry)


# In[43]:

Bob_key.publickey().verify(hash_of_decrypted, signature)


# In[44]:

signature_Alice = Alice_key.sign(hash_sha1,'')


# In[45]:

hasd_data_encry = Bob_key.publickey().encrypt(hash_sha1, 32)


# In[46]:

hash_of_decrypted = Bob_key.decrypt(hasd_data_encry)


# In[49]:

Alice_key.publickey().verify(hash_of_decrypted, signature_Alice)

