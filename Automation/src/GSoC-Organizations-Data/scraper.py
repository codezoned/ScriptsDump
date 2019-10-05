from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time
import xlsxwriter

browser = webdriver.Firefox()
url="https://summerofcode.withgoogle.com/organizations/?sp-page=5"
browser.get(url)

delay = 5

try:
    elms = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.CLASS_NAME, 'organization-card__container')))
    print("Page is ready!")
    html=browser.page_source
    workbook   = xlsxwriter.Workbook('results.xlsx')
    worksheet = workbook.add_worksheet()
    row = 1
    col = 0
    bold = workbook.add_format({'bold': True})
    worksheet.set_column(0, 2, 70)
    worksheet.set_column(3, 3, 150)
    worksheet.write(0, 0, 'ORGANISATION NAME', bold)
    worksheet.write(0, 1, 'TECHNOLOGIES', bold)
    worksheet.write(0, 2, 'TOPIC CATEGORY', bold)
    worksheet.write(0, 3, 'TOPIC NAMES', bold)

    orgs = browser.find_elements_by_class_name('organization-card__container')
    for org in orgs:
        org.click()
        elms = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.CLASS_NAME, 'organization__tag--topic')))
        org_name = browser.find_element_by_class_name('organization-card__title').text
        worksheet.write(row, col, org_name)
        tech_tags = browser.find_elements_by_class_name('organization__tag--technology')
        tags_text = ''
        for tag in tech_tags:
            tags_text += tag.text + ','
        worksheet.write(row, col+1, tags_text)
        topic_cat = browser.find_element_by_class_name('organization__tag--category').text  
        worksheet.write(row, col+2, topic_cat)
        topics = browser.find_elements_by_class_name('organization__tag--topic')  
        topics_text =''
        for topic in topics:
            topics_text += topic.text + ','
        worksheet.write(row, col+3, topics_text)
        row += 1
    workbook.close()

except TimeoutException:
    print("Loading took too much time!")