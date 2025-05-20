#!/usr/bin/env python
# coding: utf-8

# # **Data Collection**

# ## Objectives
# 
# - Download data from Kaggle and prepare it for processing
# 
# ## Inputs
# 
# - kaggle.json - authntication token
# - dataset - images
# 
# ## Outputs
# 
# - Generated dataset: inputs/datasets/mildew_dataset
# - Split dataset - train, test, validation

# ## Change working directory

# We need to change the working directory from its current folder to its parent folder. To do this we:
# 
# * We access the current directory with os.getcwd()

# In[12]:


import os
current_dir = os.getcwd()
current_dir


# We want to make the parent of the current directory the new current directory
# * os.path.dirname() gets the parent directory
# * os.chir() defines the new current directory

# In[13]:


os.chdir(os.path.dirname(current_dir))
print("You set a new current directory")


# Confirm the new current directory.

# In[14]:


current_dir = os.getcwd()
current_dir


# ## Import Packages

# In[ ]:


get_ipython().run_line_magic('pip', 'install -r requirements.txt')


# ## Install Kaggle
# 
# Install kaggle to help with downloading image data form kaggle.com.

# In[ ]:


# install kaggle package
get_ipython().run_line_magic('pip', 'install kaggle==1.5.12')


# Change the Kaggle configuration directory to the current working directory and set permissions for the Kaggle authentication JSON.
# 
# Check that kaggle.json appears in the root directory

# In[ ]:


import os
print(os.listdir())  # Should list `kaggle.json`


# Set Kaggle configuration directory

# In[ ]:


import os
os.environ['KAGGLE_CONFIG_DIR'] = os.getcwd()
print(f"Kaggle config directory set to: {os.environ['KAGGLE_CONFIG_DIR']}")


# Get the dataset path and set the destination folder

# In[ ]:


KaggleDatasetPath = "codeinstitute/cherry-leaves"
DestinationFolder = "inputs/cherry-leaves"   
get_ipython().system(' kaggle datasets download -d {KaggleDatasetPath} -p {DestinationFolder}')

