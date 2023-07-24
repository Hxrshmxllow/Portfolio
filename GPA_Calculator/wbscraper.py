from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup
import requests
from array import *

def main():
    if __name__ == '__main__':
        username = '3845811748'
        password = 'harshit@3126'
        driver = webdriver.Chrome(executable_path="G:\chromedriver\chromedriver.exe")
        driver.maximize_window()
        driver.get('https://fridaystudentportal.com/oldbridge')  
        userbox = driver.find_element("name", "username")
        userbox.send_keys(username)
        passbox = driver.find_element("name", "password")
        passbox.send_keys(password)
        time.sleep(1)
        passbox.submit()
        time.sleep(1)
        driver.get('https://fridaystudentportal.com/portal/index.cfm?f=grades.cfm')
        htmlsource = driver.page_source
        time.sleep(1)
        global gradespage
        gradespage = BeautifulSoup(htmlsource, 'html.parser')
        time.sleep(1)
        driver.quit()

def variables():
    i = -1
    global grade
    grade = {}
    for el in gradespage.find_all("span", class_="main-grade-display notranslate"):
        i += 1
        grade[i] = int(el.get_text())
        #print('grade[' + str(i) + ']' + str(grade[i]))
    i = -1
    global subject
    subject = []
    for el in gradespage.find_all("font"):
        i += 1
        subject.append(el.get_text())
        #print('subject[' + str(i) + ']' + subject[i])


def finalcalc():
    points = 0.00
    credits = 0
    for el in grade:
        points += pointcalc(grade[el])
    for el in subject:
        subjectinfo = subjectarray(el)
        print(subjectinfo)

def subjectarray(el):
    subjectlist = []
    compsi = ["AP COMPUTER SCIENCE", 2, 5]
    lang = ["AP ENGLISH COMP", 2, 5]
    calc = ["AP CALCULUS BC", 2, 10]
    health = ["LAB-DRUGS & ALC - 11", 0, 1]
    chem = ["AP CHEMISTRY", 2, 10]
    gov = ["AP GOVT & POLITICS", 2, 5]
    gym = ["PHYS ED - 11", 0, 4]
    subjectlist.append(compsi)
    subjectlist.append(lang)
    subjectlist.append(calc)
    subjectlist.append(health)
    subjectlist.append(chem)
    subjectlist.append(gov)
    subjectlist.append(gym) 
    for sbj in subjectlist:
        if el in sbj[0]:
            return sbj
        else:
            continue



def pointcalc(gradenum):
    point = 0.00
    if(gradenum >= 97):
        point = (4.33)
    elif(gradenum >= 93):
        point = (4.0)
    elif(gradenum >= 90):
        point = (3.67)
    elif(gradenum >= 87):
        point = (3.33)
    elif(gradenum >= 83):
        point = (3.0)
    elif(gradenum >= 80):
        point = (2.67)
    elif(gradenum >= 77):
        point = (2.33)
    elif(gradenum >= 73):
        point = (2.0)
    elif(gradenum >= 70):
        point = (1.67)
    elif(gradenum >= 67):
        point = (1.33)
    elif(gradenum >= 63):
        point = (1.0)
    elif(gradenum >= 60):
        point = (0)
    return point

main()
variables()
finalcalc()


