import os
import pandas as pd

# # Читаем положительные отзывы в один файл
# 

# In[27]:


data_pos_train = pd.DataFrame()
directory = "./aclImdb_v1/aclImdb/train/pos/"
for filename in os.listdir(directory):
    if filename.endswith(".txt"):
        # открываем файл для чтения
        with open(os.path.join(directory, filename), 'r', encoding="utf-8") as file:
            # считываем содержимое файла и добавляем его в датафрейм
            file_contents = file.read()
            data_pos_train = data_pos_train.append({'rewiew': file_contents, 'sentiment': 1, 'grade': filename.split('.')[0].split('_')[1]}, ignore_index=True)



# # Читаем отрицательные отзывы в один файл

# In[18]:


data_neg_train = pd.DataFrame()
directory = "./aclImdb_v1/aclImdb/train/neg/"
for filename in os.listdir(directory):
    if filename.endswith(".txt"):
        # открываем файл для чтения
        with open(os.path.join(directory, filename), 'r', encoding="utf-8") as file:
            # считываем содержимое файла и добавляем его в датафрейм
            file_contents = file.read()
            data_neg_train = data_neg_train.append({'rewiew': file_contents, 'sentiment': 0, 'grade': filename.split('.')[0].split('_')[1]}, ignore_index=True)



# In[32]:


data_neg_train.head()


# # Читаем test отрицательные отзывы

# In[21]:


data_neg_test = pd.DataFrame()
directory = "./aclImdb_v1/aclImdb/test/neg/"
for filename in os.listdir(directory):
    if filename.endswith(".txt"):
        # открываем файл для чтения
        with open(os.path.join(directory, filename), 'r', encoding="utf-8") as file:
            # считываем содержимое файла и добавляем его в датафрейм
            file_contents = file.read()
            data_neg_test = data_neg_test.append({'rewiew': file_contents, 'sentiment': 0, 'grade': filename.split('.')[0].split('_')[1]}, ignore_index=True)



# In[33]:


data_neg_test.head()


# # Читаем test положительные отзывы
# 

# In[23]:


data_pos_test = pd.DataFrame()
directory = "./aclImdb_v1/aclImdb/test/pos/"
for filename in os.listdir(directory):
    if filename.endswith(".txt"):
        # открываем файл для чтения
        with open(os.path.join(directory, filename), 'r', encoding="utf-8") as file:
            # считываем содержимое файла и добавляем его в датафрейм
            file_contents = file.read()
            data_pos_test = data_pos_test.append({'rewiew': file_contents, 'sentiment': 1, 'grade': filename.split('.')[0].split('_')[1]}, ignore_index=True)



# In[35]:


data_pos_test.shape


# In[40]:


data = pd.concat([data_pos_test,data_pos_train, data_neg_test,data_neg_train ],axis=0)#data_pos_test + data_pos_train #+ data_neg_test + data_neg_train


# In[49]:


data


# In[50]:


data.to_csv("data", index=False)


# In[ ]:




