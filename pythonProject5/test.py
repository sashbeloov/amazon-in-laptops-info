sasha.belov, [05.03.2025 13:59]
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

# Настройки Selenium
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Запуск в фоновом режиме
options.add_argument("start-maximized")
options.add_argument("disable-infobars")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Списки для хранения данных
laptop_brand = []
laptop_model = []
laptop_screensize = []
laptop_ram = []
laptop_storage = []
laptop_cpumodel = []
laptop_operating_system = []
laptop_price = []
laptop_rating = []
laptop_review_count = []
laptop_graphics_card_description = []

count = 1
next_page_url = 'https://www.amazon.in/s?k=laptop'
max_laptops = 100

while count <= max_laptops:
    laptop_links = []

    driver.get(next_page_url)
    time.sleep(3)  # Даем время загрузиться странице

    # Получаем ссылки на ноутбуки
    laptop_url = driver.find_elements(By.XPATH, "//a[@class='a-link-normal s-line-clamp-2 s-link-style a-text-normal']")
    for url in laptop_url:
        laptop_links.append(url.get_attribute('href'))

    for link in laptop_links:
        if count > max_laptops:
            break

        driver.get(link)
        time.sleep(2)

        # Извлечение данных с обработкой ошибок
        try:
            laptopbrand = driver.find_element(By.XPATH, "//tr[@class='a-spacing-small po-brand']//td[@class='a-span9']").text
        except:
            laptopbrand = 'No brand'
        laptop_brand.append(laptopbrand)

        try:
            laptopmodel = driver.find_element(By.XPATH, "//tr[@class='a-spacing-small po-model_name']//span[@class='a-size-base po-break-word']").text
        except:
            laptopmodel = 'No model'
        laptop_model.append(laptopmodel)

        try:
            screensize = driver.find_element(By.XPATH, "//tr[@class='a-spacing-small po-display.size']//span[@class='a-size-base po-break-word']").text
        except:
            screensize = 'No screen size'
        laptop_screensize.append(screensize)

        try:
            ram = driver.find_element(By.XPATH, "//tr[@class='a-spacing-small po-ram.memory']//span[@class='a-size-base po-break-word']").text
        except:
            ram = 'No RAM'
        laptop_ram.append(ram)

        try:
            storage = driver.find_element(By.XPATH, "//tr[@class='a-spacing-small po-hard_disk.size']//span[@class='a-size-base po-break-word']").text
        except:
            storage = 'No storage'
        laptop_storage.append(storage)

        try:
            cpu = driver.find_element(By.XPATH, "//tr[@class='a-spacing-small po-processor.model']//span[@class='a-size-base po-break-word']").text
        except:
            cpu = 'No CPU'
        laptop_cpumodel.append(cpu)

        try:
            operating_system = driver.find_element(By.XPATH, "//tr[@class='a-spacing-small po-operating_system']//span[@class='a-size-base po-break-word']").text
        except:
            operating_system = 'No OS'
        laptop_operating_system.append(operating_system)

        try:
            price = driver.find_element(By.XPATH, "//span[@class='a-price-whole']").text
        except:
            price = 'No price'
        laptop_price.append(price)

        try:
            rating = driver.find_element(By.XPATH, "//span[@class='a-icon-alt']").text
        except:
            rating = 'No rating'
        laptop_rating.append(rating)

        try:
            review_count = driver.find_element(By.XPATH, "//span[@id='acrCustomerReviewText']").text
        except:
            review_count = 'No reviews'
        laptop_review_count.append(review_count)

        try:
            description = driver.find_element(By.

sasha.belov, [05.03.2025 13:59]
XPATH, "//tr[@class='a-spacing-small po-graphics_description']//span[@class='a-size-base po-break-word']").text
        except:
            description = 'No description'
        laptop_graphics_card_description.append(description)

        count += 1

    # Переход на следующую страницу
    try:
        next_page = driver.find_element(By.XPATH, "//a[contains(@class, 's-pagination-next')]")
        next_page_url = next_page.get_attribute('href')
    except:
        print('Это последняя страница!')
        break

# Создание DataFrame и сохранение в CSV
df = pd.DataFrame({
    'Brand': laptop_brand,
    'Model': laptop_model,
    'Screen Size': laptop_screensize,
    'RAM': laptop_ram,
    'Storage': laptop_storage,
    'CPU': laptop_cpumodel,
    'Operating System': laptop_operating_system,
    'Price': laptop_price,
    'Rating': laptop_rating,
    'Review Count': laptop_review_count,
    'Graphics Card': laptop_graphics_card_description,
})

df.to_csv('laptops.csv', index=False)
print("Данные сохранены в laptops.csv")

# Закрываем браузер
driver.quit()

##############################
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions
import pandas as pd

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

laptop_brand = []
laptop_model = []
laptop_screensize = []
laptop_ram = []
laptop_storage = []
laptop_cpumodel = []
laptop_os = []
laptop_price = []
laptop_rating = []
laptop_review_count = []
laptop_gcd = []

next_page_url = "https://www.amazon.in/s?k=laptop&crid=3P9YDE8F7NM97&sprefix=laptop%2Caps%2C545&ref=nb_sb_noss_2"

count = 1
max_count = 1

while count <= max_count:
    laptop_links = []
    for i in range(3):
        driver.get(next_page_url)
    try:
        next_page = WebDriverWait(driver, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, "//a[@class='s-pagination-item s-pagination-next s-pagination-button s-pagination-button-accessibility s-pagination-separator']")))
        next_page_url = next_page.get_attribute("href")
    except:
        print("end page")
        break

    laptop_url = driver.find_elements(By.XPATH, "//a[@class='a-link-normal s-line-clamp-2 s-link-style a-text-normal']")
    for url in laptop_url:
        l_link = url.get_attribute("href")
        laptop_links.append(l_link)

    for link in laptop_links:
        driver.get(link)

        try:
            brand = WebDriverWait(driver, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, "//tr[@class='a-spacing-small po-brand']//td[@class='a-span9']"))).text
        except:
            brand = "No brand"
        print(count)
        print(f"brand: {brand}")
        laptop_brand.append(brand)

        try:
            model = WebDriverWait(driver, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, "//tr[@class='a-spacing-small po-model_name']//span[@class='a-size-base po-break-word']"))).text
        except:
            model = "No model"
        print(f"model: {model}")
        laptop_model.append(model)

        try:
            screensize = WebDriverWait(driver, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, "//tr[@class='a-spacing-small po-display.size']//span[@class='a-size-base po-break-word']"))).text
        except:
            screensize = "No screensize"
        print(f"screensize: {screensize}")
        laptop_screensize.append(screensize)

        try:
            ram = WebDriverWait(driver, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, "//th[@class='a-color-secondary a-size-base prodDetSectionEntry' and contains(text(), 'Maximum Memory Supported')]//following-sibling::td"))).text
        except:
            ram = "No ram"
        print(f"ram: {ram}")
        laptop_ram.append(ram)

        try:
            storage = WebDriverWait(driver, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, "//tr[@class='a-spacing-small po-hard_disk.size']//span[@class='a-size-base po-break-word']"))).text
        except:
            storage = "No storage"
        print(f"storage: {storage}")
        laptop_storage.append(storage)

        try:
            cpu = WebDriverWait(driver, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, "//th[@class='a-color-secondary a-size-base prodDetSectionEntry' and contains(text(), 'Processor Type')]//following-sibling::td"))).text
        except:
            cpu = "No cpu"
        print(f"cpu: {cpu}")
        laptop_cpumodel.append(cpu)


        try:
            os = WebDriverWait(driver, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, "//th[@class='a-color-secondary a-size-base prodDetSectionEntry' and contains(text(), 'Operating System')]//following-sibling::td"))).text
        except:
            os = "No os"
        print(f"os: {os}")
        laptop_os.append(os)

        try:
            price = WebDriverWait(driver, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, "//span[@class='a-price aok-align-center reinventPricePriceToPayMargin priceToPay']//span//span[@class='a-price-whole']"))).text
        except:
            price = "No price"
        print(f"price: {price}")
        laptop_price.append(price)

        try:
            rating = WebDriverWait(driver, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, "//span[@class='reviewCountTextLinkedHistogram noUnderline']"))).text
        except:
            rating = "No rating"
        print(f"rating: {rating}")
        laptop_rating.append(rating)

        try:
            review_count = WebDriverWait(driver, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, "//span[@id='acrCustomerReviewText']"))).text
        except:
            review_count = "No review_count"
        print(f"review_count: {review_count}")
        laptop_review_count.append(review_count)

        try:
            description = WebDriverWait(driver, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, "//th[@class='a-color-secondary a-size-base prodDetSectionEntry' and contains(text(), 'Graphics Card Description')]//following-sibling::td"))).text
        except:
            description = "No description"
        print(f"description: {description}")
        print("\n")
        laptop_gcd.append(description)

        count += 1

df = pd.DataFrame({
    "laptop_brand":laptop_brand,
    "laptop_model":laptop_model,
    "laptop_screensize":laptop_screensize,
    "laptop_ram":laptop_ram,
    "laptop_storage":laptop_storage,
    "laptop_cpumodel":laptop_cpumodel,
    "laptop_os":laptop_os,
    "laptop_price":laptop_price,
    "laptop_rating":laptop_rating,
    "laptop_review_count":laptop_review_count,
    "laptop_gcd":laptop_gcd,
})
df.to_csv("laptops100.csv")
