from selenium import webdriver
from selenium.webdriver.support.ui import Select,WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from itertools import product

url = 'https://dps.psx.com.pk/historical'
code = 'KEL'
months = [str(i) for i in range(1,13)]
years = ['2020','2021','2022']

sub1 = 'VOLUME'
sub2 = 'Showing'
driver_path = 'geckodriver'
driver = webdriver.Firefox(executable_path=driver_path)
driver.get(url)
code_field = driver.find_element(By.XPATH,'//*[@id="historicalSymbolSearch"]')
code_field.clear()
code_field.send_keys(code)
time.sleep(10)

for year,month in product(years,months):
    time.sleep(5)
    month_field = Select(driver.find_element(By.XPATH,'/html/body/div[6]/div[4]/div/div[3]/div/div[2]/div[2]/select'))
    month_field.select_by_value(month)
    year_field = Select(driver.find_element(By.XPATH,'/html/body/div[6]/div[4]/div/div[3]/div/div[3]/div[2]/select'))
    year_field.select_by_value(year)
    driver.find_element(By.XPATH,'//*[@id="historicalSymbolBtn"]').click()
    wait = WebDriverWait(driver,20)
    time.sleep(5)
    test_str = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[6]/div[5]"))).get_attribute('innerText')
    idx1 = test_str.index(sub1)
    idx2 = test_str.index(sub2)
    res = ''
    for idx in range(idx1 + len(sub1) + 1, idx2):
        res = res + test_str[idx]
    print(res)
    with open(f'{code}.csv','a') as f:
        f.write(res)

driver.quit()