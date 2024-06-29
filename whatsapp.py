from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
#from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from time import sleep

import os,csv


def link_builder(number:str):
    for i in range(len(number)):
        try:
            if not number[i].isnumeric():
                number=number[:i]+number[i+1:]
                i-=1
        except:
            continue
    number=number[-10:]
    return f"https://web.whatsapp.com/send?phone=%2B91{number}&text&app_absent=0"

def load_dump():
    l = []
    if os.path.exists('./dump.txt'):
        with open("./dump.txt") as dumpfile:
            for line in dumpfile.read().split('\n'):
                l.append(line)
    else:
        with open('dump.txt','w') as f:
            f.close()
    print(f"Names loaded from already sent: {l}")
    return l

def type_message(driver:any,message:str,f:bool):
    action_chain = ActionChains(driver)
    action_chain.send_keys(message)
    if f == 1:
        action_chain.key_down(Keys.LEFT_CONTROL).perform()
        action_chain.send_keys("v").perform()
        action_chain.key_up(Keys.LEFT_CONTROL).perform()
        sleep(2)
    action_chain.send_keys(Keys.RETURN).perform()

def returnDictData(csvfile:str, name_row_name, phone_number_row_name) -> list:
    with open(csvfile) as induction_form:
        reader = csv.DictReader(induction_form)
        phonelist = []
        for row in reader:
            # if category.count(','):
            #     categories_set = set(category.split(", "))
            # else:
            #     categories_set = {category}

            phonelist.append((
                row[name_row_name],
                link_builder(row[phone_number_row_name]),
                # int(row[class_row_name]),
                # categories_set            
            ))

        return phonelist


def send_message(links:list, msg:str, dry_run:bool,folderName:str,f:bool):
    dump = load_dump()
    print('Dry Run status:',dry_run)
    options = webdriver.FirefoxOptions()
    options.add_argument("-profile")
    options.add_argument(folderName)
    if f!=1: options.add_argument("-headless") 
    driver=webdriver.Firefox(options=options)
    wait = WebDriverWait(driver, 100)
    count = 0
    total = len(links)
    import time
    for link_tuple in links:
        start = time.time()
        count+=1
        name,link= link_tuple
        name = name.split()[0]
        if link in dump:
            continue
        print(f"{count} of {total} {link_tuple}")
        message = msg.format(name=name)
        print(message)
        try:
            driver.get(link)
        except:
            driver.quit()
            driver.get(link)
        driver.execute_script("window.onbeforeunload = function() {};")
        print('Opening chat')
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "html > body > div:nth-of-type(1) > div > div > div:nth-of-type(2) > div:nth-of-type(4) > div > footer > div:nth-of-type(1) > div > span:nth-of-type(2) > div > div:nth-of-type(2) > div:nth-of-type(1) > div > div:nth-of-type(1)")))     
        if not dry_run:
            type_message(driver=driver,message=message,f=f)
            sleep(3)
            with open("./dump.txt","a") as dumpfile:
                dumpfile.write(f"{link}\n")
                print(f"Message Sent!\nDumped {name} to file")
        else:
            continue
    end = time.time()
    print(f"Elapsed time: {end - start}")
    driver.quit()
