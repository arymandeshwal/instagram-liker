#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium import webdriver


# In[3]:


from selenium.webdriver.common.keys import Keys


# In[4]:


import time


# In[60]:


class Instagram:
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()
    
    def login(self):
        bot = self.bot
        bot.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
        time.sleep(3)
        email = bot.find_element_by_name('username')
        password = bot.find_element_by_name('password')
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(3)
        notif_dialog = bot.find_element_by_class_name('aOOlW.HoLwm').click()
    
    def like(self,hashtag):
        bot = self.bot
        bot.get('https://www.instagram.com/explore/tags/{}/'.format(hashtag))
        time.sleep(2)

        
        for i in range(0,10):
            bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(2)
            posts = bot.find_elements_by_class_name('v1Nh3.kIKUG._bz0w')
            links =[post.find_element_by_css_selector('a').get_attribute('href') for post in posts]
            
            for link in links:
                bot.get(link)
                try:
                    bot.find_element_by_class_name('dCJp8.afkep._0mzm-').click()
                    time.sleep(10)
                except Exception as ex:
                    time.sleep(60)


# In[62]:


ins = Instagram(input('Enter username:'),input('Enter password'))
ins.login()
ins.like(input('Enter hashtag:'))


# In[ ]:




