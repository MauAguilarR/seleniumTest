import pandas
import time
import random
import winsound
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains

#LOAN PURPOSE p,r, h
loan_purpose = 'p'

#FF PROD
#url = 'https://financefactorsmortgage.streamloan.io/book-of-business'
#FF STAGE
url = 'https://master-ffapp.streamloan.io'

#DATOS DE USUARIO PARA LOGIN
#purchase
user_log = 'mauricio+ffsg240222b02@streamloan.io'
#refi
#user_log = 'marcos+ffstage110222bw5@streamloan.io'
#HELOC
#user_log = 'marcos+ffstage110222bw7@streamloan.io'


middle_name = 'Borrower'
pw = '111111'
phone_number = '4159410868'

#Fecha Aleatoria
rand_date = '0'+str(random.randint(1, 9))+'/0'+str(random.randint(1, 9))+'/'+str(random.randint(1970, 2002))
sufijos = ["S", "J", "I", "II", "III", "IV"]
meses = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
mesesnum = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
loan_amount = 250000
dependents = str(random.randint(1, 85))+', '+str(random.randint(1, 85))
specificnumber = ["1", "3", "1", "3"]
random_employers = ["Acme inc", "Acme test", "Acme pizza", "Acme Fest"]
job_titles = ["Senior", "Delivery", "Practice", "Tester", "Employement"]
iol_desc = ["Colombian", "Dominican", "Nicaraguan"]
oad = ["Hmong", "Laotian", "Thai", "Pakistani", "Cambodian"]
opid = ["Fijan", "Tongan"]
rand_old = random.randint(1970, 2000)

# Selectores generales:
create_pw = '/html/body/div[1]/div/main/div/div/div/div/form/div[1]/div/input'
confirm_pw = '/html/body/div[1]/div/main/div/div/div/div/form/div[2]/div/input'
pw_submit = '/html/body/div[1]/div/main/div/div/div/div/form/button'
phone_field = '/html/body/div[1]/div/main/div/div/div/div/form/div/div/div/input'
phone_submit = '/html/body/div[1]/div/main/div/div/div/div/form/button'
verify_code_submit = '/html/body/div[1]/div/main/div/div/div/div/form/button'
logo = '/html/body/div[1]/div/div[2]/a/img'
next_button = '/html/body/div[1]/div/main/div/div[2]/form/div[3]/button[2]'



middle_name_field = '/html/body/div[1]/div/main/div/div[2]/form/div[2]/div/div/div/div[1]/div[2]/div/div/div[2]/input'
suffix_field = '/html/body/div[1]/div/main/div/div[2]/form/div[2]/div/div/div/div[1]/div[2]/div/div/div[4]/div/div/div'
dob_field = '/html/body/div[1]/div/main/div/div[2]/form/div[2]/div/div/div/div[2]/div/div/div/div[1]/div/input'
current_address = '/html/body/div[1]/div/main/div/div[2]/form/div[2]/div/div/div/div[1]/div[2]/div/div/div/div/div[1]/div[1]/input'
apt_unit_build = '/html/body/div[1]/div/main/div/div[2]/form/div[2]/div/div/div/div[1]/div[2]/div/div/div/div/input'
ityma = '/html/body/div[1]/div/main/div/div[2]/form/div[2]/div/div/div/div[2]/div[1]/div/div/div'+'['+str(random.randint(1,2))+']/input'
dycoor = '/html/body/div[1]/div/main/div/div[2]/form/div[2]/div/div/div/div[3]/div[2]/div/div/div['+str(random.randint(1,3))+']/input'
mid_field = '/html/body/div[1]/div/main/div/div[2]/form/div[2]/div/div/div/div[4]/div[2]/div/div/div[1]/div/input'
mid_val = str(meses[random.randint(0, 11)])+' '+str(random.randint(2020, 2021))
prevaddr_field = '/html/body/div[1]/div/main/div/div[2]/form/div[2]/div/div/div/div[5]/div[2]/div/div/div[1]/div/div[1]/div[1]/input'
dyoor = '/html/body/div[1]/div/main/div/div[2]/form/div[2]/div/div/div/div[5]/div[2]/div/div/div[2]/div['+str(random.randint(1,3))+']/input'
mid_field2 = '/html/body/div[1]/div/main/div/div[2]/form/div[2]/div/div/div/div[5]/div[2]/div/div/div[3]/div[1]/div/input'
mid_val2 = str(meses[random.randint(0, 11)])+' '+str(random.randint(2000, 2019))
ah_ma = '/html/body/div[1]/div/main/div/div[2]/form/div[2]/div/div/div/div[6]/div[2]/div/div/div/div[1]/div[1]/input'

pi_lp = '/html/body/div[1]/div/main/div/div[2]/form/div[2]/div/div/div/div[1]/div[2]/div/div/div[1]/input'
#pi_dpt = '/html/body/div[1]/div/main/div/div[2]/form/div[2]/div/div/div/div[1]/div[2]/div/div[2]/div/div/div'
#pi_la = '/html/body/div[1]/div/main/div/div[2]/form/div[2]/div/div/div/div[1]/div[2]/div/div[2]/input'
pi_pp = '/html/body/div[1]/div/main/div/div[2]/form/div[2]/div/div/div/div[2]/div[2]/div/div/div['+str(random.randint(1,3))+']/input'
pi_cp = '/html/body/div[1]/div/main/div/div[2]/form/div[2]/div/div/div/div[3]/div[1]/div/div/div/div/div'
pi_hswyltcyl = '/html/body/div[1]/div/main/div/div[2]/form/div[2]/div/div/div/div[4]/div[1]/div/div/div/div/div'

pi_wiyms = '/html/body/div[1]/div/main/div/div[2]/form/div[2]/div/div/div/div[1]/div[2]/div/div/div['+specificnumber[random.randint(0,3)]+']/input'
pi_wiycz = '/html/body/div[1]/div/main/div/div[2]/form/div[2]/div/div/div/div[2]/div[1]/div/div/div['+str(random.randint(1,4))+']/input'
pi_dependents = '/html/body/div[1]/div/main/div/div[2]/form/div[2]/div/div/div/div[3]/div[2]/div/div/span[3]/span'
pi_lda = '/html/body/div[1]/div/main/div/div[2]/form/div[2]/div/div/div/div[4]/div[2]/div/div/input'
pi_hyesitum = '/html/body/div[1]/div/main/div/div[2]/form/div[2]/div/div/div/div[5]/div[1]/div/div/div['+str(random.randint(1,2))+']/input'
pi_ssn = '/html/body/div[1]/div/main/div/div[2]/form/div[2]/div/div/div/div[1]/div[2]/div/div/div[1]/input'

ei_fy = '/html/body/div[1]/div/main/div/div[2]/form/div[2]/div/div/div/div[1]/div[1]/div/div/div[2]/input'
ei_et = '/html/body/div[1]/div/main/div/div[2]/form/div[2]/div/div/div/div[2]/div[2]/div/div/div[1]/div/div/div'
ei_en = '/html/body/div[1]/div/main/div/div[2]/form/div[2]/div/div/div/div[2]/div[2]/div/div/div[2]/input'
ei_ea = '/html/body/div[1]/div/main/div/div[2]/form/div[2]/div/div/div/div[2]/div[2]/div/div/div[3]/div/div/div[1]/input'
ei_wpn = '/html/body/div[1]/div/main/div/div[2]/form/div[2]/div/div/div/div[2]/div[2]/div/div/div[4]/div[1]/input'
ei_sd = '/html/body/div[1]/div/main/div/div[2]/form/div[2]/div/div/div/div[2]/div[2]/div/div/div[5]/div/div/input'
ei_jt = '/html/body/div[1]/div/main/div/div[2]/form/div[2]/div/div/div/div[2]/div[2]/div/div/div[6]/input'
ei_yip = '/html/body/div[1]/div/main/div/div[2]/form/div[2]/div/div/div/div[2]/div[2]/div/div/div[7]/input'
ei_m1 = '/html/body/div[1]/div/main/div/div[2]/form/div[2]/div/div/div/div[2]/div[2]/div/div/div[8]/div/input'
ei_m2 = '/html/body/div[1]/div/main/div/div[2]/form/div[2]/div/div/div/div[2]/div[2]/div/div/div[9]/div/input'
ei_m3 = '/html/body/div[1]/div/main/div/div[2]/form/div[2]/div/div/div/div[2]/div[2]/div/div/div[10]/div/input'
ei_m4 = '/html/body/div[1]/div/main/div/div[2]/form/div[2]/div/div/div/div[2]/div[2]/div/div/div[11]/div/input'
ei_m5 = '/html/body/div[1]/div/main/div/div[2]/form/div[2]/div/div/div/div[2]/div[2]/div/div/div[12]/div/input'
ei_sy = '/html/body/div[1]/div/main/div/div[2]/form/div[2]/div/div/div/div[2]/div[2]/div/div/div[13]/div[2]/input'
ei_et2 = '/html/body/div[1]/div/main/div/div[2]/form/div[2]/div/div/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div'
ei_en2 = '/html/body/div[1]/div/main/div/div[2]/form/div[2]/div/div/div/div[2]/div[2]/div/div[2]/div[2]/input'
ei_ea2 = '/html/body/div[1]/div/main/div/div[2]/form/div[2]/div/div/div/div[2]/div[2]/div/div[2]/div[3]/div/div/div[1]/input'
ei_wpn2 = '/html/body/div[1]/div/main/div/div[2]/form/div[2]/div/div/div/div[2]/div[2]/div/div[2]/div[4]/div/input'
ei_sd2 = '/html/body/div[1]/div/main/div/div[2]/form/div[2]/div/div/div/div[2]/div[2]/div/div[2]/div[5]/div/div/input'
ei_jt2 = '/html/body/div[1]/div/main/div/div[2]/form/div[2]/div/div/div/div[2]/div[2]/div/div[2]/div[6]/input'
ei_yip2 = '/html/body/div[1]/div/main/div/div[2]/form/div[2]/div/div/div/div[2]/div[2]/div/div[2]/div[7]/input'
ei_m6 = '/html/body/div[1]/div/main/div/div[2]/form/div[2]/div/div/div/div[2]/div[2]/div/div[2]/div[8]/div/input'
ei_m7 = '/html/body/div[1]/div/main/div/div[2]/form/div[2]/div/div/div/div[2]/div[2]/div/div[2]/div[9]/div/input'
ei_m8 = '/html/body/div[1]/div/main/div/div[2]/form/div[2]/div/div/div/div[2]/div[2]/div/div[2]/div[10]/div/input'
ei_m9 = '/html/body/div[1]/div/main/div/div[2]/form/div[2]/div/div/div/div[2]/div[2]/div/div[2]/div[11]/div/input'
ei_m10 = '/html/body/div[1]/div/main/div/div[2]/form/div[2]/div/div/div/div[2]/div[2]/div/div[2]/div[12]/div/input'
ei_dyhaaife = '/html/body/div[1]/div/main/div/div[2]/form/div[2]/div/div/div/div[2]/div[2]/div/div[2]/div[13]/div[1]/input'

ai_fy = '/html/body/div[1]/div/main/div/div[2]/form/div[2]/div/div/div/div/div[2]/div/div/div[2]/input'
ai_is = '/html/body/div[1]/div/main/div/div[2]/form/div[2]/div/div/div/div[2]/div[2]/div/div/div[1]/div/div/div'
ai_mi = '/html/body/div[1]/div/main/div/div[2]/form/div[2]/div/div/div/div[2]/div[2]/div/div/div[2]/div/input'
ai_sy = '/html/body/div[1]/div/main/div/div[2]/form/div[2]/div/div/div/div[2]/div[2]/div/div/div[3]/div[2]/input'
ai_is2 = '/html/body/div[1]/div/main/div/div[2]/form/div[2]/div/div/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div'
ai_mi2 = '/html/body/div[1]/div/main/div/div[2]/form/div[2]/div/div/div/div[2]/div[2]/div/div[2]/div[2]/div/input'
ai_dyhaasoita = '/html/body/div[1]/div/main/div/div[2]/form/div[2]/div/div/div/div[2]/div[2]/div/div[2]/div[3]/div[1]/input'

ri_wdywtr = '/html/body/div[1]/div/main/div/div[2]/form/div[2]/div/div/div/div[1]/div[2]/div/div/div['+str(random.randint(1,4))+']/input'
ri_wtopieftl = '/html/body/div[1]/div/main/div/div[2]/form/div[2]/div/div/div/div[2]/div[2]/div/div/div['+str(random.randint(1,3))+']/input'
ri_hdyitotp = '/html/body/div[1]/div/main/div/div[2]/form/div[2]/div/div/div/div[3]/div[2]/div/div/div['+str(random.randint(1,3))+']/input'
ri_wywtpb = '/html/body/div[1]/div/main/div/div[2]/form/div[2]/div/div/div/div[4]/div[2]/div/div/input'
ri_witrla = '/html/body/div[1]/div/main/div/div[2]/form/div[2]/div/div/div/div[5]/div[2]/div/div/div[1]/input'
ri_wittaoelotp = '/html/body/div[1]/div/main/div/div[2]/form/div[2]/div/div/div/div[6]/div[2]/div/div/div[1]/input'

hdyhau = '/html/body/div[1]/div/main/div/div[2]/form/div[2]/div/div/div/div/div/div/div/div/div'

user_log_field = '/html/body/div[1]/div/main/div/div/div/div/form/div[1]/div/div/input'
user_log_pw = '/html/body/div[1]/div/main/div/div/div/div/form/div[2]/div/div/input'
user_log_submit = '/html/body/div[1]/div/main/div/div/div/div/form/button'
submit_button = '/html/body/div[1]/div/main/div/div[2]/form/div[3]/button[2]'

gs_task1 = '/html/body/div[1]/div/main/div/div/div/div[2]/div/ul/div[1]/div/li/div[2]/button'

# Abrir el navegador:
driver = webdriver.Chrome(executable_path='C:/drivers/chromedriver.exe')

# Maximizar pantalla
driver.maximize_window()
driver.get(url)

# Acciones en la página
wait = WebDriverWait(driver,10)
wait.until(ec.visibility_of_element_located((By.XPATH,logo)))

#Creación de contraseña y envio del codigo de verificación
try:
    driver.find_element_by_xpath(create_pw).send_keys(pw)
    driver.find_element_by_xpath(confirm_pw).send_keys(pw)
    driver.find_element_by_xpath(pw_submit).click()
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div[1]/div/main/div/div/div/div/form/div/div/div/input').send_keys(phone_number)
    driver.find_element_by_xpath(phone_submit).click()
    #time.sleep(15)
except NoSuchElementException:
    pass

#Loging de usuario
try:
	driver.find_element_by_xpath(user_log_field).send_keys(user_log)
	driver.find_element_by_xpath(user_log_pw).send_keys(pw)
	driver.find_element_by_xpath(user_log_submit).click()
	#time.sleep(15)
except NoSuchElementException:
    pass

#Tareas del Getting Started
wait = WebDriverWait(driver,40)
wait.until(ec.visibility_of_element_located((By.XPATH,gs_task1)))
driver.find_element_by_xpath(gs_task1).click()

wait = WebDriverWait(driver,10)
wait.until(ec.visibility_of_element_located((By.XPATH,next_button)))
driver.find_element_by_xpath(next_button).click()

if loan_purpose == 'p':
	#PERSONAL INFORMATION
	wait = WebDriverWait(driver,10)
	wait.until(ec.visibility_of_element_located((By.XPATH,middle_name_field)))
	driver.find_element_by_xpath(middle_name_field).send_keys(middle_name)
	driver.find_element_by_xpath(suffix_field).click()
	actions = ActionChains(driver)
	actions.send_keys(sufijos[random.randint(0, 5)])
	actions.perform()

	actions2 = ActionChains(driver)
	actions2.send_keys(Keys.TAB * 2)
	actions2.perform()

	#driver.find_element_by_xpath(dob_field).click()
	actions3 = ActionChains(driver)
	actions3.send_keys(rand_date)
	actions3.perform()

	time.sleep(.5)
	driver.find_element_by_xpath(next_button).click()

	#ADDRESS HISTORY
	time.sleep(1)
	try:
	    driver.find_element_by_xpath(current_address).send_keys(random.randint(1, 90))
		time.sleep(1.5)
	    driver.find_element_by_xpath(current_address).click()
	    actions5 = ActionChains(driver)
	    actions5.send_keys(Keys.ARROW_DOWN * 2)
	    actions5.perform()
	    time.sleep(1)
	    actions6 = ActionChains(driver)
	    actions6.send_keys(Keys.TAB * 1)
	    actions6.perform()
	    time.sleep(1)
	    actions7 = ActionChains(driver)
	    actions7.send_keys("D"+str(random.randint(1, 90)))
	    actions7.perform()
	except NoSuchElementException:
	    pass

	time.sleep(.5)
	try:
	    driver.find_element_by_xpath(ityma).click()
	except NoSuchElementException:
	    pass

	try:
	    driver.find_element_by_xpath(dycoor).click()
	except NoSuchElementException:
	    pass

	try:
	    driver.find_element_by_xpath(mid_field).send_keys(mid_val)
	except NoSuchElementException:
	    pass

	time.sleep(.5)
	try:
	    driver.find_element_by_xpath(prevaddr_field).send_keys(random.randint(1, 90))
	    time.sleep(1.5)
	    driver.find_element_by_xpath(prevaddr_field).click()
	    actions5 = ActionChains(driver)
	    actions5.send_keys(Keys.ARROW_DOWN * 2)
	    actions5.perform()
	    time.sleep(.5)
	    actions6 = ActionChains(driver)
	    actions6.send_keys(Keys.TAB * 1)
	    actions6.perform()
	    time.sleep(1)
	    actions7 = ActionChains(driver)
	    actions7.send_keys("G"+str(random.randint(1, 90)))
	    actions7.perform()
	except NoSuchElementException:
	    pass

	try:
	    driver.find_element_by_xpath(dyoor).click()
	except NoSuchElementException:
	    pass

	try:
	    driver.find_element_by_xpath(mid_field2).send_keys(mid_val2)
	except NoSuchElementException:
	    pass

	try:
	    driver.find_element_by_xpath(ah_ma).send_keys(random.randint(1, 90))
	    time.sleep(1.5)
	    driver.find_element_by_xpath(ah_ma).click()
	    actions5 = ActionChains(driver)
	    actions5.send_keys(Keys.ARROW_DOWN * 2)
	    actions5.perform()
	    time.sleep(.5)
	    actions6 = ActionChains(driver)
	    actions6.send_keys(Keys.TAB * 1)
	    actions6.perform()
	    time.sleep(1)
	    actions7 = ActionChains(driver)
	    actions7.send_keys("N"+str(random.randint(1, 90)))
	    actions7.perform()
	except NoSuchElementException:
	    pass

	driver.find_element_by_xpath(next_button).click()

	#PURCHASE INFORMATION
	try:
	    driver.find_element_by_xpath(pi_lp).send_keys(150000)
	except NoSuchElementException:
	    pass

	# try:
	#     driver.find_element_by_xpath(pi_dpt).click()
	#     actions = ActionChains(driver)
	#     actions.send_keys(Keys.ARROW_DOWN * random.randint(1, 2))
	#     actions.perform()
	#     time.sleep(.5)
	#     actions6 = ActionChains(driver)
	#     actions6.send_keys(Keys.TAB * 1)
	#     actions6.perform()
	#     time.sleep(.5)
	# except NoSuchElementException:
	#     pass

	# try:
	#     driver.find_element_by_xpath(pi_la).send_keys(250000)
	# except NoSuchElementException:
	#     pass

	try:
	    driver.find_element_by_xpath(pi_pp).click()
	except NoSuchElementException:
	    pass

	try:
	    driver.find_element_by_xpath(pi_cp).click()
	    actions = ActionChains(driver)
	    actions.send_keys(Keys.ARROW_DOWN * random.randint(1, 2))
	    actions.perform()
	    time.sleep(.5)
	    actions6 = ActionChains(driver)
	    actions6.send_keys(Keys.TAB * 1)
	    actions6.perform()
	    time.sleep(.5)
	except NoSuchElementException:
	    pass

	try:
	    driver.find_element_by_xpath(pi_hswyltcyl).click()
	    actions = ActionChains(driver)
	    actions.send_keys(Keys.ARROW_DOWN * random.randint(1, 2))
	    actions.perform()
	    time.sleep(.5)
	    actions6 = ActionChains(driver)
	    actions6.send_keys(Keys.TAB * 1)
	    actions6.perform()
	    time.sleep(.5)
	except NoSuchElementException:
	    pass

	driver.find_element_by_xpath(next_button).click()

	#PERSONAL INFORMATION
	try:
	    driver.find_element_by_xpath(pi_wiyms).click()
	except NoSuchElementException:
	    pass

	try:
	    driver.find_element_by_xpath(pi_wiycz).click()
	except NoSuchElementException:
	    pass

	try:
	    driver.find_element_by_xpath(pi_dependents).click()
	    driver.find_element_by_xpath(pi_dependents).click()
	except NoSuchElementException:
	    pass

	try:
	    driver.find_element_by_xpath(pi_lda).send_keys(dependents)
	except NoSuchElementException:
	    pass

	try:
	    driver.find_element_by_xpath(pi_hyesitum).click()
	except NoSuchElementException:
	    pass

	driver.find_element_by_xpath(next_button).click()

	time.sleep(.5)
	try:
	    driver.find_element_by_xpath(pi_ssn).send_keys('12345'+str(random.randint(1,9))+str(random.randint(1,9))+str(random.randint(1,9))+str(random.randint(1,9)))
	except NoSuchElementException:
	    pass
	driver.find_element_by_xpath(next_button).click()

	#EMPLOYMENT INFORMATION
	try:
	    driver.find_element_by_xpath(ei_fy).click()
	except NoSuchElementException:
	    pass

	try:
	    driver.find_element_by_xpath(ei_et).click()
	    actions = ActionChains(driver)
	    actions.send_keys(Keys.ARROW_DOWN * random.randint(1, 2))
	    actions.perform()
	    time.sleep(.5)
	    actions6 = ActionChains(driver)
	    actions6.send_keys(Keys.TAB * 1)
	    actions6.perform()
	    time.sleep(.5)
	except NoSuchElementException:
	    pass

	try:
	    driver.find_element_by_xpath(ei_en).send_keys(random_employers[random.randint(0, 3)])
	except NoSuchElementException:
	    pass
	try:
	    driver.find_element_by_xpath(ei_ea).send_keys(random.randint(1, 90))
	    time.sleep(1.5)
	    driver.find_element_by_xpath(ei_ea).click()
	    actions5 = ActionChains(driver)
	    actions5.send_keys(Keys.ARROW_DOWN * 2)
	    actions5.perform()
	    time.sleep(.5)
	    actions6 = ActionChains(driver)
	    actions6.send_keys(Keys.TAB * 1)
	    actions6.perform()
	    time.sleep(1)
	    actions7 = ActionChains(driver)
	    actions7.send_keys("A"+str(random.randint(1, 90)))
	    actions7.perform()
	except NoSuchElementException:
	    pass

	try:
	    driver.find_element_by_xpath(ei_wpn).send_keys(phone_number)
	except NoSuchElementException:
	    pass

	try:
	    driver.find_element_by_xpath(ei_sd).send_keys(mesesnum[random.randint(0, 11)]+'/'+str(random.randint(10, 28))+'/'+str(random.randint(2000, 2020)))
	except NoSuchElementException:
	    pass

	try:
	    driver.find_element_by_xpath(ei_jt).send_keys(job_titles[random.randint(0, 4)])
	except NoSuchElementException:
	    pass

	try:
	    driver.find_element_by_xpath(ei_yip).send_keys(random.randint(1, 9))
	except NoSuchElementException:
	    pass

	try:
	    driver.find_element_by_xpath(ei_m1).send_keys("1")
	except NoSuchElementException:
	    pass

	try:
	    driver.find_element_by_xpath(ei_m2).send_keys("2")
	except NoSuchElementException:
	    pass

	try:
	    driver.find_element_by_xpath(ei_m3).send_keys("3")
	except NoSuchElementException:
	    pass

	try:
	    driver.find_element_by_xpath(ei_m4).send_keys("4")
	except NoSuchElementException:
	    pass

	try:
	    driver.find_element_by_xpath(ei_m5).send_keys("5")
	except NoSuchElementException:
	    pass

	try:
	    driver.find_element_by_xpath(ei_sy).click()
	except NoSuchElementException:
	    pass

	time.sleep(.5)

	try:
	    driver.find_element_by_xpath(ei_et2).click()
	    actions = ActionChains(driver)
	    actions.send_keys(Keys.ARROW_DOWN * random.randint(1, 2))
	    actions.perform()
	    time.sleep(.5)
	    actions6 = ActionChains(driver)
	    actions6.send_keys(Keys.TAB * 1)
	    actions6.perform()
	    time.sleep(.5)
	except NoSuchElementException:
	    pass

	try:
	    driver.find_element_by_xpath(ei_en2).send_keys(random_employers[random.randint(0, 3)])
	except NoSuchElementException:
	    pass
	time.sleep(.5)
	try:
	    driver.find_element_by_xpath(ei_ea2).send_keys(random.randint(1, 90))
	    time.sleep(1.5)
	    driver.find_element_by_xpath(ei_ea2).click()
	    actions5 = ActionChains(driver)
	    actions5.send_keys(Keys.ARROW_DOWN * 2)
	    actions5.perform()
	    time.sleep(.5)
	    actions6 = ActionChains(driver)
	    actions6.send_keys(Keys.TAB * 1)
	    actions6.perform()
	    time.sleep(1)
	    actions7 = ActionChains(driver)
	    actions7.send_keys("A"+str(random.randint(1, 90)))
	    actions7.perform()
	except NoSuchElementException:
	    pass

	try:
	    driver.find_element_by_xpath(ei_wpn2).send_keys(phone_number)
	except NoSuchElementException:
	    pass

	try:
	    driver.find_element_by_xpath(ei_sd2).send_keys(mesesnum[random.randint(0, 11)]+'/'+str(random.randint(10, 28))+'/'+str(random.randint(2000, 2020)))
	except NoSuchElementException:
	    pass

	try:
	    driver.find_element_by_xpath(ei_jt2).send_keys(job_titles[random.randint(0, 4)])
	except NoSuchElementException:
	    pass

	try:
	    driver.find_element_by_xpath(ei_yip2).send_keys(random.randint(1, 9))
	except NoSuchElementException:
	    pass

	try:
	    driver.find_element_by_xpath(ei_m6).send_keys("11")
	except NoSuchElementException:
	    pass

	try:
	    driver.find_element_by_xpath(ei_m7).send_keys("22")
	except NoSuchElementException:
	    pass

	try:
	    driver.find_element_by_xpath(ei_m8).send_keys("33")
	except NoSuchElementException:
	    pass

	try:
	    driver.find_element_by_xpath(ei_m9).send_keys("44")
	except NoSuchElementException:
	    pass

	try:
	    driver.find_element_by_xpath(ei_m10).send_keys("55")
	except NoSuchElementException:
	    pass

	try:
	    driver.find_element_by_xpath(ei_dyhaaife).click()
	except NoSuchElementException:
	    pass

	driver.find_element_by_xpath(next_button).click()

	#ADITIONAL INCOME INFORMATION
	time.sleep(.5)
	try:
	    driver.find_element_by_xpath(ai_fy).click()
	except NoSuchElementException:
	    pass

	try:
	    driver.find_element_by_xpath(ai_is).click()
	    actions = ActionChains(driver)
	    actions.send_keys(Keys.ARROW_DOWN * random.randint(1, 44))
	    actions.perform()
	    time.sleep(.5)
	    actions6 = ActionChains(driver)
	    actions6.send_keys(Keys.TAB * 1)
	    actions6.perform()
	    time.sleep(.5)
	except NoSuchElementException:
	    pass

	try:
	    driver.find_element_by_xpath(ai_mi).send_keys(random.randint(1, 9))
	except NoSuchElementException:
	    pass

	try:
	    driver.find_element_by_xpath(ai_sy).click()
	except NoSuchElementException:
	    pass

	time.sleep(.5)
	try:
	    driver.find_element_by_xpath(ai_is2).click()
	    actions = ActionChains(driver)
	    actions.send_keys(Keys.ARROW_DOWN * random.randint(1, 44))
	    actions.perform()
	    time.sleep(.5)
	    actions6 = ActionChains(driver)
	    actions6.send_keys(Keys.TAB * 1)
	    actions6.perform()
	    time.sleep(.5)
	except NoSuchElementException:
	    pass

	try:
	    driver.find_element_by_xpath(ai_mi2).send_keys(random.randint(1, 9))
	except NoSuchElementException:
	    pass

	try:
	    driver.find_element_by_xpath(ai_dyhaasoita).click()
	except NoSuchElementException:
	    pass
	
	driver.find_element_by_xpath(next_button).click()

	pass

if loan_purpose == 'r':
	#PERSONAL INFORMATION
	wait = WebDriverWait(driver,10)
	wait.until(ec.visibility_of_element_located((By.XPATH,middle_name_field)))
	driver.find_element_by_xpath(middle_name_field).send_keys(middle_name)
	driver.find_element_by_xpath(suffix_field).click()
	actions = ActionChains(driver)
	actions.send_keys(sufijos[random.randint(0, 5)])
	actions.perform()

	actions2 = ActionChains(driver)
	actions2.send_keys(Keys.TAB * 2)
	actions2.perform()

	#driver.find_element_by_xpath(dob_field).click()
	actions3 = ActionChains(driver)
	actions3.send_keys(rand_date)
	actions3.perform()

	time.sleep(.5)
	driver.find_element_by_xpath(next_button).click()

	#PERSONAL INFORMATION
	try:
	    driver.find_element_by_xpath(pi_wiyms).click()
	except NoSuchElementException:
	    pass

	try:
	    driver.find_element_by_xpath(pi_wiycz).click()
	except NoSuchElementException:
	    pass

	try:
	    driver.find_element_by_xpath(pi_dependents).click()
	    driver.find_element_by_xpath(pi_dependents).click()
	except NoSuchElementException:
	    pass

	try:
	    driver.find_element_by_xpath(pi_lda).send_keys(dependents)
	except NoSuchElementException:
	    pass

	try:
	    driver.find_element_by_xpath(pi_hyesitum).click()
	except NoSuchElementException:
	    pass

	driver.find_element_by_xpath(next_button).click()

	#ADDRESS HISTORY
	time.sleep(1)
	try:
	    driver.find_element_by_xpath(current_address).send_keys(random.randint(1, 90))
	    time.sleep(1.5)
	    driver.find_element_by_xpath(current_address).click()
	    actions5 = ActionChains(driver)
	    actions5.send_keys(Keys.ARROW_DOWN * 2)
	    actions5.perform()
	    time.sleep(1)
	    actions6 = ActionChains(driver)
	    actions6.send_keys(Keys.TAB * 1)
	    actions6.perform()
	    time.sleep(1)
	    actions7 = ActionChains(driver)
	    actions7.send_keys("D"+str(random.randint(1, 90)))
	    actions7.perform()
	except NoSuchElementException:
	    pass

	time.sleep(.5)
	try:
	    driver.find_element_by_xpath(ityma).click()
	except NoSuchElementException:
	    pass

	try:
	    driver.find_element_by_xpath(dycoor).click()
	except NoSuchElementException:
	    pass

	try:
	    driver.find_element_by_xpath(mid_field).send_keys(mid_val)
	except NoSuchElementException:
	    pass

	time.sleep(.5)
	try:
	    driver.find_element_by_xpath(prevaddr_field).send_keys(random.randint(1, 90))
	    time.sleep(1.5)
	    driver.find_element_by_xpath(prevaddr_field).click()
	    actions5 = ActionChains(driver)
	    actions5.send_keys(Keys.ARROW_DOWN * 2)
	    actions5.perform()
	    time.sleep(.5)
	    actions6 = ActionChains(driver)
	    actions6.send_keys(Keys.TAB * 1)
	    actions6.perform()
	    time.sleep(1)
	    actions7 = ActionChains(driver)
	    actions7.send_keys("G"+str(random.randint(1, 90)))
	    actions7.perform()
	except NoSuchElementException:
	    pass

	try:
	    driver.find_element_by_xpath(dyoor).click()
	except NoSuchElementException:
	    pass

	try:
	    driver.find_element_by_xpath(mid_field2).send_keys(mid_val2)
	except NoSuchElementException:
	    pass

	# try:
	#     driver.find_element_by_xpath(ah_ma).send_keys(random.randint(1, 90))
	#     time.sleep(1.5)
	#     driver.find_element_by_xpath(ah_ma).click()
	#     actions5 = ActionChains(driver)
	#     actions5.send_keys(Keys.ARROW_DOWN * 2)
	#     actions5.perform()
	#     time.sleep(.5)
	#     actions6 = ActionChains(driver)
	#     actions6.send_keys(Keys.TAB * 1)
	#     actions6.perform()
	#     time.sleep(1)
	#     actions7 = ActionChains(driver)
	#     actions7.send_keys("N"+str(random.randint(1, 90)))
	#     actions7.perform()
	# except NoSuchElementException:
	#     pass

	driver.find_element_by_xpath(next_button).click()

	#REFINANCE INFORMATION
	try:
	    driver.find_element_by_xpath(ri_wdywtr).click()
	except NoSuchElementException:
	    pass

	try:
	    driver.find_element_by_xpath(ri_wtopieftl).click()
	except NoSuchElementException:
	    pass

	try:
	    driver.find_element_by_xpath(ri_hdyitotp).click()
	except NoSuchElementException:
	    pass

	try:
	    driver.find_element_by_xpath(ri_wywtpb).send_keys(rand_old)
	except NoSuchElementException:
	    pass

	try:
	    driver.find_element_by_xpath(ri_witrla).send_keys(150000)
	except NoSuchElementException:
	    pass

	try:
	    driver.find_element_by_xpath(ri_wittaoelotp).send_keys(250000)
	except NoSuchElementException:
	    pass

	try:
	    driver.find_element_by_xpath('/html/body/div[1]/div/main/div/div[2]/form/div[2]/div/div/div/div[7]/div[1]/div/div/div/div/div').click()
	    actions = ActionChains(driver)
	    actions.send_keys(Keys.ARROW_DOWN * random.randint(1, 2))
	    actions.perform()
	    time.sleep(.5)
	    actions6 = ActionChains(driver)
	    actions6.send_keys(Keys.TAB * 1)
	    actions6.perform()
	    time.sleep(.5)
	except NoSuchElementException:
	    pass

	try:
	    driver.find_element_by_xpath('/html/body/div[1]/div/main/div/div[2]/form/div[2]/div/div/div/div[8]/div[1]/div/div/div/div/div').click()
	    actions = ActionChains(driver)
	    actions.send_keys(Keys.ARROW_DOWN * random.randint(1, 2))
	    actions.perform()
	    time.sleep(.5)
	    actions6 = ActionChains(driver)
	    actions6.send_keys(Keys.TAB * 1)
	    actions6.perform()
	    time.sleep(.5)
	except NoSuchElementException:
	    pass

	driver.find_element_by_xpath(next_button).click()

	time.sleep(.5)
	try:
	    driver.find_element_by_xpath(pi_ssn).send_keys('12345'+str(random.randint(1,9))+str(random.randint(1,9))+str(random.randint(1,9))+str(random.randint(1,9)))
	except NoSuchElementException:
	    pass
	driver.find_element_by_xpath(next_button).click()

	#EMPLOYMENT INFORMATION
	try:
	    driver.find_element_by_xpath(ei_fy).click()
	except NoSuchElementException:
	    pass

	try:
	    driver.find_element_by_xpath(ei_et).click()
	    actions = ActionChains(driver)
	    actions.send_keys(Keys.ARROW_DOWN * random.randint(1, 2))
	    actions.perform()
	    time.sleep(.5)
	    actions6 = ActionChains(driver)
	    actions6.send_keys(Keys.TAB * 1)
	    actions6.perform()
	    time.sleep(.5)
	except NoSuchElementException:
	    pass

	try:
	    driver.find_element_by_xpath(ei_en).send_keys(random_employers[random.randint(0, 3)])
	except NoSuchElementException:
	    pass
	try:
	    driver.find_element_by_xpath(ei_ea).send_keys(random.randint(1, 90))
	    time.sleep(1.5)
	    driver.find_element_by_xpath(ei_ea).click()
	    actions5 = ActionChains(driver)
	    actions5.send_keys(Keys.ARROW_DOWN * 2)
	    actions5.perform()
	    time.sleep(.5)
	    actions6 = ActionChains(driver)
	    actions6.send_keys(Keys.TAB * 1)
	    actions6.perform()
	    time.sleep(1)
	    actions7 = ActionChains(driver)
	    actions7.send_keys("A"+str(random.randint(1, 90)))
	    actions7.perform()
	except NoSuchElementException:
	    pass

	try:
	    driver.find_element_by_xpath(ei_wpn).send_keys(phone_number)
	except NoSuchElementException:
	    pass

	try:
	    driver.find_element_by_xpath(ei_sd).send_keys(mesesnum[random.randint(0, 11)]+'/'+str(random.randint(10, 28))+'/'+str(random.randint(2000, 2020)))
	except NoSuchElementException:
	    pass

	try:
	    driver.find_element_by_xpath(ei_jt).send_keys(job_titles[random.randint(0, 4)])
	except NoSuchElementException:
	    pass

	try:
	    driver.find_element_by_xpath(ei_yip).send_keys(random.randint(1, 9))
	except NoSuchElementException:
	    pass

	try:
	    driver.find_element_by_xpath(ei_m1).send_keys("1")
	except NoSuchElementException:
	    pass

	try:
	    driver.find_element_by_xpath(ei_m2).send_keys("2")
	except NoSuchElementException:
	    pass

	try:
	    driver.find_element_by_xpath(ei_m3).send_keys("3")
	except NoSuchElementException:
	    pass

	try:
	    driver.find_element_by_xpath(ei_m4).send_keys("4")
	except NoSuchElementException:
	    pass

	try:
	    driver.find_element_by_xpath(ei_m5).send_keys("5")
	except NoSuchElementException:
	    pass

	try:
	    driver.find_element_by_xpath(ei_sy).click()
	except NoSuchElementException:
	    pass

	time.sleep(.5)

	try:
	    driver.find_element_by_xpath(ei_et2).click()
	    actions = ActionChains(driver)
	    actions.send_keys(Keys.ARROW_DOWN * random.randint(1, 2))
	    actions.perform()
	    time.sleep(.5)
	    actions6 = ActionChains(driver)
	    actions6.send_keys(Keys.TAB * 1)
	    actions6.perform()
	    time.sleep(.5)
	except NoSuchElementException:
	    pass

	try:
	    driver.find_element_by_xpath(ei_en2).send_keys(random_employers[random.randint(0, 3)])
	except NoSuchElementException:
	    pass
	time.sleep(.5)
	try:
	    driver.find_element_by_xpath(ei_ea2).send_keys(random.randint(1, 90))
	    time.sleep(1.5)
	    driver.find_element_by_xpath(ei_ea2).click()
	    actions5 = ActionChains(driver)
	    actions5.send_keys(Keys.ARROW_DOWN * 2)
	    actions5.perform()
	    time.sleep(.5)
	    actions6 = ActionChains(driver)
	    actions6.send_keys(Keys.TAB * 1)
	    actions6.perform()
	    time.sleep(1)
	    actions7 = ActionChains(driver)
	    actions7.send_keys("A"+str(random.randint(1, 90)))
	    actions7.perform()
	except NoSuchElementException:
	    pass

	try:
	    driver.find_element_by_xpath(ei_wpn2).send_keys(phone_number)
	except NoSuchElementException:
	    pass

	try:
	    driver.find_element_by_xpath(ei_sd2).send_keys(mesesnum[random.randint(0, 11)]+'/'+str(random.randint(10, 28))+'/'+str(random.randint(2000, 2020)))
	except NoSuchElementException:
	    pass

	try:
	    driver.find_element_by_xpath(ei_jt2).send_keys(job_titles[random.randint(0, 4)])
	except NoSuchElementException:
	    pass

	try:
	    driver.find_element_by_xpath(ei_yip2).send_keys(random.randint(1, 9))
	except NoSuchElementException:
	    pass

	try:
	    driver.find_element_by_xpath(ei_m6).send_keys("11")
	except NoSuchElementException:
	    pass

	try:
	    driver.find_element_by_xpath(ei_m7).send_keys("22")
	except NoSuchElementException:
	    pass

	try:
	    driver.find_element_by_xpath(ei_m8).send_keys("33")
	except NoSuchElementException:
	    pass

	try:
	    driver.find_element_by_xpath(ei_m9).send_keys("44")
	except NoSuchElementException:
	    pass

	try:
	    driver.find_element_by_xpath(ei_m10).send_keys("55")
	except NoSuchElementException:
	    pass

	try:
	    driver.find_element_by_xpath(ei_dyhaaife).click()
	except NoSuchElementException:
	    pass

	driver.find_element_by_xpath(next_button).click()

	#ADITIONAL INCOME INFORMATION
	time.sleep(.5)
	try:
	    driver.find_element_by_xpath(ai_fy).click()
	except NoSuchElementException:
	    pass

	time.sleep(.5)
	try:
	    driver.find_element_by_xpath(ai_is).click()
	    actions = ActionChains(driver)
	    actions.send_keys(Keys.ARROW_DOWN * random.randint(1, 44))
	    actions.perform()
	    time.sleep(.5)
	    actions6 = ActionChains(driver)
	    actions6.send_keys(Keys.TAB * 1)
	    actions6.perform()
	    time.sleep(.5)
	except NoSuchElementException:
	    pass

	try:
	    driver.find_element_by_xpath(ai_mi).send_keys(random.randint(1, 9))
	except NoSuchElementException:
	    pass

	try:
	    driver.find_element_by_xpath(ai_sy).click()
	except NoSuchElementException:
	    pass

	time.sleep(.5)
	try:
	    driver.find_element_by_xpath(ai_is2).click()
	    actions = ActionChains(driver)
	    actions.send_keys(Keys.ARROW_DOWN * random.randint(1, 44))
	    actions.perform()
	    time.sleep(.5)
	    actions6 = ActionChains(driver)
	    actions6.send_keys(Keys.TAB * 1)
	    actions6.perform()
	    time.sleep(.5)
	except NoSuchElementException:
	    pass

	try:
	    driver.find_element_by_xpath(ai_mi2).send_keys(random.randint(1, 9))
	except NoSuchElementException:
	    pass

	try:
	    driver.find_element_by_xpath(ai_dyhaasoita).click()
	except NoSuchElementException:
	    pass

	driver.find_element_by_xpath(next_button).click()

	pass

if loan_purpose == 'h':
	#PERSONAL INFORMATION
	wait = WebDriverWait(driver,10)
	wait.until(ec.visibility_of_element_located((By.XPATH,middle_name_field)))
	driver.find_element_by_xpath(middle_name_field).send_keys(middle_name)
	driver.find_element_by_xpath(suffix_field).click()
	actions = ActionChains(driver)
	actions.send_keys(sufijos[random.randint(0, 5)])
	actions.perform()

	actions2 = ActionChains(driver)
	actions2.send_keys(Keys.TAB * 2)
	actions2.perform()

	#driver.find_element_by_xpath(dob_field).click()
	actions3 = ActionChains(driver)
	actions3.send_keys(rand_date)
	actions3.perform()

	time.sleep(.5)
	driver.find_element_by_xpath(next_button).click()

	#PERSONAL INFORMATION
	try:
	    driver.find_element_by_xpath(pi_wiyms).click()
	except NoSuchElementException:
	    pass

	try:
	    driver.find_element_by_xpath(pi_wiycz).click()
	except NoSuchElementException:
	    pass

	try:
	    driver.find_element_by_xpath(pi_dependents).click()
	    driver.find_element_by_xpath(pi_dependents).click()
	except NoSuchElementException:
	    pass

	try:
	    driver.find_element_by_xpath(pi_lda).send_keys(dependents)
	except NoSuchElementException:
	    pass

	try:
	    driver.find_element_by_xpath(pi_hyesitum).click()
	except NoSuchElementException:
	    pass

	driver.find_element_by_xpath(next_button).click()

	#ADDRESS HISTORY
	time.sleep(1)
	try:
	    driver.find_element_by_xpath(current_address).send_keys(random.randint(1, 90))
	    time.sleep(1.5)
	    driver.find_element_by_xpath(current_address).click()
	    actions5 = ActionChains(driver)
	    actions5.send_keys(Keys.ARROW_DOWN * 2)
	    actions5.perform()
	    time.sleep(1)
	    actions6 = ActionChains(driver)
	    actions6.send_keys(Keys.TAB * 1)
	    actions6.perform()
	    time.sleep(1)
	    actions7 = ActionChains(driver)
	    actions7.send_keys("D"+str(random.randint(1, 90)))
	    actions7.perform()
	except NoSuchElementException:
	    pass

	time.sleep(.5)
	try:
	    driver.find_element_by_xpath(ityma).click()
	except NoSuchElementException:
	    pass

	try:
	    driver.find_element_by_xpath(dycoor).click()
	except NoSuchElementException:
	    pass

	try:
	    driver.find_element_by_xpath(mid_field).send_keys(mid_val)
	except NoSuchElementException:
	    pass

	time.sleep(.5)
	try:
	    driver.find_element_by_xpath(prevaddr_field).send_keys(random.randint(1, 90))
	    time.sleep(1.5)
	    driver.find_element_by_xpath(prevaddr_field).click()
	    actions5 = ActionChains(driver)
	    actions5.send_keys(Keys.ARROW_DOWN * 2)
	    actions5.perform()
	    time.sleep(.5)
	    actions6 = ActionChains(driver)
	    actions6.send_keys(Keys.TAB * 1)
	    actions6.perform()
	    time.sleep(1)
	    actions7 = ActionChains(driver)
	    actions7.send_keys("G"+str(random.randint(1, 90)))
	    actions7.perform()
	except NoSuchElementException:
	    pass

	try:
	    driver.find_element_by_xpath(dyoor).click()
	except NoSuchElementException:
	    pass

	try:
	    driver.find_element_by_xpath(mid_field2).send_keys(mid_val2)
	except NoSuchElementException:
	    pass

	# try:
	#     driver.find_element_by_xpath(ah_ma).send_keys(random.randint(1, 90))
	#     time.sleep(1.5)
	#     driver.find_element_by_xpath(ah_ma).click()
	#     actions5 = ActionChains(driver)
	#     actions5.send_keys(Keys.ARROW_DOWN * 2)
	#     actions5.perform()
	#     time.sleep(.5)
	#     actions6 = ActionChains(driver)
	#     actions6.send_keys(Keys.TAB * 1)
	#     actions6.perform()
	#     time.sleep(1)
	#     actions7 = ActionChains(driver)
	#     actions7.send_keys("N"+str(random.randint(1, 90)))
	#     actions7.perform()
	# except NoSuchElementException:
	#     pass

	driver.find_element_by_xpath(next_button).click()

	#REFINANCE INFORMATION
	try:
	    driver.find_element_by_xpath(ri_wdywtr).click()
	except NoSuchElementException:
	    pass

	try:
	    driver.find_element_by_xpath(ri_wtopieftl).click()
	except NoSuchElementException:
	    pass

	try:
	    driver.find_element_by_xpath(ri_hdyitotp).click()
	except NoSuchElementException:
	    pass

	try:
	    driver.find_element_by_xpath(ri_wywtpb).send_keys(rand_old)
	except NoSuchElementException:
	    pass
	

	driver.find_element_by_xpath(next_button).click()

	time.sleep(.5)
	try:
	    driver.find_element_by_xpath(pi_ssn).send_keys('12345'+str(random.randint(1,9))+str(random.randint(1,9))+str(random.randint(1,9))+str(random.randint(1,9)))
	except NoSuchElementException:
	    pass
	driver.find_element_by_xpath(next_button).click()

	#EMPLOYMENT INFORMATION
	try:
	    driver.find_element_by_xpath(ei_fy).click()
	except NoSuchElementException:
	    pass

	try:
	    driver.find_element_by_xpath(ei_et).click()
	    actions = ActionChains(driver)
	    actions.send_keys(Keys.ARROW_DOWN * random.randint(1, 2))
	    actions.perform()
	    time.sleep(.5)
	    actions6 = ActionChains(driver)
	    actions6.send_keys(Keys.TAB * 1)
	    actions6.perform()
	    time.sleep(.5)
	except NoSuchElementException:
	    pass

	try:
	    driver.find_element_by_xpath(ei_en).send_keys(random_employers[random.randint(0, 3)])
	except NoSuchElementException:
	    pass
	try:
	    driver.find_element_by_xpath(ei_ea).send_keys(random.randint(1, 90))
	    time.sleep(1.5)
	    driver.find_element_by_xpath(ei_ea).click()
	    actions5 = ActionChains(driver)
	    actions5.send_keys(Keys.ARROW_DOWN * 2)
	    actions5.perform()
	    time.sleep(.5)
	    actions6 = ActionChains(driver)
	    actions6.send_keys(Keys.TAB * 1)
	    actions6.perform()
	    time.sleep(1)
	    actions7 = ActionChains(driver)
	    actions7.send_keys("A"+str(random.randint(1, 90)))
	    actions7.perform()
	except NoSuchElementException:
	    pass

	try:
	    driver.find_element_by_xpath(ei_wpn).send_keys(phone_number)
	except NoSuchElementException:
	    pass

	try:
	    driver.find_element_by_xpath(ei_sd).send_keys(mesesnum[random.randint(0, 11)]+'/'+str(random.randint(10, 28))+'/'+str(random.randint(2000, 2020)))
	except NoSuchElementException:
	    pass

	try:
	    driver.find_element_by_xpath(ei_jt).send_keys(job_titles[random.randint(0, 4)])
	except NoSuchElementException:
	    pass

	try:
	    driver.find_element_by_xpath(ei_yip).send_keys(random.randint(1, 9))
	except NoSuchElementException:
	    pass

	try:
	    driver.find_element_by_xpath(ei_m1).send_keys("1")
	except NoSuchElementException:
	    pass

	try:
	    driver.find_element_by_xpath(ei_m2).send_keys("2")
	except NoSuchElementException:
	    pass

	try:
	    driver.find_element_by_xpath(ei_m3).send_keys("3")
	except NoSuchElementException:
	    pass

	try:
	    driver.find_element_by_xpath(ei_m4).send_keys("4")
	except NoSuchElementException:
	    pass

	try:
	    driver.find_element_by_xpath(ei_m5).send_keys("5")
	except NoSuchElementException:
	    pass

	try:
	    driver.find_element_by_xpath(ei_sy).click()
	except NoSuchElementException:
	    pass

	time.sleep(.5)

	try:
	    driver.find_element_by_xpath(ei_et2).click()
	    actions = ActionChains(driver)
	    actions.send_keys(Keys.ARROW_DOWN * random.randint(1, 2))
	    actions.perform()
	    time.sleep(.5)
	    actions6 = ActionChains(driver)
	    actions6.send_keys(Keys.TAB * 1)
	    actions6.perform()
	    time.sleep(.5)
	except NoSuchElementException:
	    pass

	try:
	    driver.find_element_by_xpath(ei_en2).send_keys(random_employers[random.randint(0, 3)])
	except NoSuchElementException:
	    pass
	time.sleep(.5)
	try:
	    driver.find_element_by_xpath(ei_ea2).send_keys(random.randint(1, 90))
	    time.sleep(1.5)
	    driver.find_element_by_xpath(ei_ea2).click()
	    actions5 = ActionChains(driver)
	    actions5.send_keys(Keys.ARROW_DOWN * 2)
	    actions5.perform()
	    time.sleep(.5)
	    actions6 = ActionChains(driver)
	    actions6.send_keys(Keys.TAB * 1)
	    actions6.perform()
	    time.sleep(1)
	    actions7 = ActionChains(driver)
	    actions7.send_keys("A"+str(random.randint(1, 90)))
	    actions7.perform()
	except NoSuchElementException:
	    pass

	try:
	    driver.find_element_by_xpath(ei_wpn2).send_keys(phone_number)
	except NoSuchElementException:
	    pass

	try:
	    driver.find_element_by_xpath(ei_sd2).send_keys(mesesnum[random.randint(0, 11)]+'/'+str(random.randint(10, 28))+'/'+str(random.randint(2000, 2020)))
	except NoSuchElementException:
	    pass

	try:
	    driver.find_element_by_xpath(ei_jt2).send_keys(job_titles[random.randint(0, 4)])
	except NoSuchElementException:
	    pass

	try:
	    driver.find_element_by_xpath(ei_yip2).send_keys(random.randint(1, 9))
	except NoSuchElementException:
	    pass

	try:
	    driver.find_element_by_xpath(ei_m6).send_keys("11")
	except NoSuchElementException:
	    pass

	try:
	    driver.find_element_by_xpath(ei_m7).send_keys("22")
	except NoSuchElementException:
	    pass

	try:
	    driver.find_element_by_xpath(ei_m8).send_keys("33")
	except NoSuchElementException:
	    pass

	try:
	    driver.find_element_by_xpath(ei_m9).send_keys("44")
	except NoSuchElementException:
	    pass

	try:
	    driver.find_element_by_xpath(ei_m10).send_keys("55")
	except NoSuchElementException:
	    pass

	try:
	    driver.find_element_by_xpath(ei_dyhaaife).click()
	except NoSuchElementException:
	    pass

	driver.find_element_by_xpath(next_button).click()

	#ADITIONAL INCOME INFORMATION
	time.sleep(.5)
	try:
	    driver.find_element_by_xpath(ai_fy).click()
	except NoSuchElementException:
	    pass

	time.sleep(.5)
	try:
	    driver.find_element_by_xpath(ai_is).click()
	    actions = ActionChains(driver)
	    actions.send_keys(Keys.ARROW_DOWN * random.randint(1, 44))
	    actions.perform()
	    time.sleep(.5)
	    actions6 = ActionChains(driver)
	    actions6.send_keys(Keys.TAB * 1)
	    actions6.perform()
	    time.sleep(.5)
	except NoSuchElementException:
	    pass

	try:
	    driver.find_element_by_xpath(ai_mi).send_keys(random.randint(1, 9))
	except NoSuchElementException:
	    pass

	try:
	    driver.find_element_by_xpath(ai_sy).click()
	except NoSuchElementException:
	    pass

	time.sleep(.5)
	try:
	    driver.find_element_by_xpath(ai_is2).click()
	    actions = ActionChains(driver)
	    actions.send_keys(Keys.ARROW_DOWN * random.randint(1, 44))
	    actions.perform()
	    time.sleep(.5)
	    actions6 = ActionChains(driver)
	    actions6.send_keys(Keys.TAB * 1)
	    actions6.perform()
	    time.sleep(.5)
	except NoSuchElementException:
	    pass

	try:
	    driver.find_element_by_xpath(ai_mi2).send_keys(random.randint(1, 9))
	except NoSuchElementException:
	    pass

	try:
	    driver.find_element_by_xpath(ai_dyhaasoita).click()
	except NoSuchElementException:
	    pass

	pass

time.sleep(.5)
try:
    driver.find_element_by_xpath(hdyhau).click()
    actions = ActionChains(driver)
    actions.send_keys(Keys.ARROW_DOWN * random.randint(1, 12))
    actions.perform()
    time.sleep(.5)
    actions6 = ActionChains(driver)
    actions6.send_keys(Keys.TAB * 1)
    driver.find_element_by_xpath(submit_button).click()
    actions6.perform()
    time.sleep(.5)
except NoSuchElementException:
    pass


frequency = 500  # Set Frequency To 2500 Hertz
duration = 300  # Set Duration To 1000 ms == 1 second
winsound.Beep(frequency, duration)

time.sleep(30)
driver.close()

# Cerrar:
driver.quit()