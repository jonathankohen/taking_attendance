from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from example_data import students
import os
import time

load_dotenv()


username = os.getenv("USERNAME")
pw = os.getenv("PW")
admin_url = os.getenv("ADMIN_URL")


def to_website(present, absent):
    # opens chrome at URL
    web = webdriver.Chrome()
    web.get(admin_url)
    time.sleep(2)

    # login
    loginInput = web.find_element_by_xpath('//*[@id="enter_email"]')
    loginInput.send_keys(username)
    pwInput = web.find_element_by_xpath('//*[@id="enter_password"]')
    pwInput.send_keys(pw)
    loginBtn = web.find_element_by_xpath('//*[@id="login_button"]')
    loginBtn.click()
    time.sleep(2)

    # nav to admin view
    adminToggle = web.find_element_by_xpath('//*[@id="profile_block"]/div/a')
    adminToggle.click()
    adminBtn = web.find_element_by_xpath('//*[@id="profile_block"]/div/div/div/ul/li[5]/a')
    adminBtn.click()

    # nav to attendance section
    sidebar = web.find_element_by_xpath('//*[@id="admin_access_content"]/div[1]/div/div/button')
    sidebar.click()
    time.sleep(2)
    attendanceBtn = web.find_element_by_xpath('//*[@id="admin_navigation_list"]/li[1]/ul/li[2]/a')
    attendanceBtn.click()

    for student in students:
        # clear search field
        searchInput = web.find_element_by_xpath('//*[@id="search_attendance_students_input"]')
        searchInput.send_keys(Keys.COMMAND, "a")
        searchInput.send_keys(Keys.BACKSPACE)
        searchInput.send_keys(student["email"])
        searchInput.send_keys(Keys.RETURN)
        time.sleep(2)

        if student["email"] in present:
            present_btn = web.find_element_by_xpath(
                '//*[@id="attendance_student_table_wrapper"]/div/div[3]/div[2]/div/table/tbody/tr/td[4]/div/div[2]/form/ul/li[1]/div[1]'
            )
            present_btn.click()
            time.sleep(2)
        else:
            absent_btn = web.find_element_by_xpath(
                '//*[@id="attendance_student_table_wrapper"]/div/div[3]/div[2]/div/table/tbody/tr/td[4]/div/div[2]/form/ul/li[3]/div[1]'
            )
            absent_btn.click()
            time.sleep(2)
