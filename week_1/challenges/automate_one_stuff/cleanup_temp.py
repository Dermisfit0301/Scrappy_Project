#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pyautogui
import time
import logging
import os


# In[6]:


# Configure logging
logging.basicConfig(filename='cleanup_temp.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


# In[12]:


def open_run_dialog():
    logging.info("Opening Run dialog")
    pyautogui.hotkey('win', 'r')
    time.sleep(1)

def open_temp_folder():
    logging.info("Opening %temp% folder")
    pyautogui.typewrite('%temp%')
    pyautogui.press('enter')
    time.sleep(2)
def delete_temp_files():
    temp_folder = os.getenv('TEMP')
    logging.info(f"Deleting files in {temp_folder}")
    for filename in os.listdir(temp_folder):
        file_path = os.path.join(temp_folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            logging.error(f"Failed to delete {file_path}. Reason: {e}")

def confirm_deletion():
    # Automatically click 'Do this for all current items' and 'Skip' if such dialogs appear
    logging.info("Waiting for potential deletion confirmation dialog")
    time.sleep(3)  # Adjust the sleep time as needed for your system
    pyautogui.press('enter')  # Press Enter to confirm deletion if any confirmation dialog appears


# In[13]:


if __name__ == "__main__":
    open_run_dialog()
    open_temp_folder()
    delete_temp_files()
    confirm_deletion()


# In[ ]:




