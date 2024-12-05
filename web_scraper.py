from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import csv


#  Configure Chrome options for web scraping (GPU disabled, window size set)
options = webdriver.ChromeOptions()
options.add_argument('--disable-gpu')
options.add_argument('--window-size=1920x1080')

#  This function contains the logic for web scraping product data from the Noon website
def scrape_noon_products():

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    # Keep track of the total number of fetched products to control execution flow
    total_products = 0
    rank = 0

# Open or create a CSV file to store the scraped data
    with open('noon_products.csv', 'w', newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file)

        # Write the header row in the CSV file
        csv_writer.writerow([
            "SKU", "Title", "Average Rating", 
            "Rating Count", "Sponsored", "Price", "Old Price", 
            "Discount", "Express", "Rank", "Link"
        ])

        try:
             # Loop through 90 pages to scrape product data
            for page in range(1, 90):
                driver.get(f"https://www.noon.com/uae-en/sports-and-outdoors/exercise-and-fitness/yoga-16328/?isCarouselView=false&limit=50&page={page}&sort%5Bby%5D=popularity&sort%5Bdir%5D=desc")
                
                #  Wait for up to 10 seconds for products to load on the page
                products = WebDriverWait(driver, 10).until(
                    EC.presence_of_all_elements_located((By.CLASS_NAME, 'sc-57fe1f38-0'))
                )
                total_products += len(products)
                
        # Stop scraping if the total number of products fetched exceeds 400
                if total_products > 400:
                    break
                # Loop through each product element to extract details
                for product in products:
                    try:
                        # Extract product data; return "N/A" if any data is missing to handle errors
                        sku = product.find_element(By.XPATH, "//div[contains(@class, 'sc-57fe1f38-0') and contains(@class, 'eSrvHE')]/a").get_attribute("id") if len(product.find_elements(By.XPATH, "//div[contains(@class, 'sc-57fe1f38-0') and contains(@class, 'eSrvHE')]/a")) > 0 else "N/A"
                        title = product.find_element(By.CSS_SELECTOR, '[data-qa="product-name"]').text if len(product.find_elements(By.CSS_SELECTOR, '[data-qa="product-name"]')) > 0 else "N/A"

                        average_rating = product.find_element(By.CLASS_NAME, 'sc-9cb63f72-2').text if len(product.find_elements(By.CLASS_NAME, 'sc-9cb63f72-2')) > 0 else "N/A"
                        rating_count = product.find_element(By.CLASS_NAME, 'sc-9cb63f72-5').text if len(product.find_elements(By.CLASS_NAME, 'sc-9cb63f72-5')) > 0 else "N/A"
                        sponsored = "Y" if len(product.find_elements(By.CLASS_NAME, 'sc-d96389d1-24.kXouJu')) > 0 else "N"

                        try:
                            currency = product.find_element(By.CLASS_NAME, 'currency').text
                            price = product.find_element(By.CLASS_NAME, 'amount').text
                            current_price = f"{currency} {price}"
                        except:
                            current_price = "N/A"
                        
                        old_price = product.find_element(By.CLASS_NAME, 'oldPrice').text if len(product.find_elements(By.CLASS_NAME, 'oldPrice')) > 0 else "N/A"
                        discount = product.find_element(By.CLASS_NAME, 'discount').text if len(product.find_elements(By.CLASS_NAME, 'discount')) > 0 else "N/A"
                        express = "Y" if len(product.find_elements(By.CSS_SELECTOR, '[data-qa="product-noon-express"]')) > 0 else "N"
                        rank += 1
                        link = product.find_element(By.CSS_SELECTOR, '.sc-57fe1f38-0.eSrvHE a').get_attribute('href') if len(product.find_elements(By.CSS_SELECTOR, '.sc-57fe1f38-0.eSrvHE a')) > 0 else "N/A"

                        # Write the product data to the CSV file
                        csv_writer.writerow([
                            sku, title, average_rating, 
                            rating_count, sponsored, current_price, old_price, 
                            discount, express, rank, link
                        ])
                    # Handle errors during product data extraction
                    except Exception as e:
                        print(f"Error processing product: {e}")
                        continue
        # Handle errors during page loading or scraping
        except Exception as e:
            print(f"An error occurred: {e}")
        # Close the browser after scraping is complete
        finally:
            driver.quit()

    print("Scraping completed. Check noon_products.csv for results.")
if __name__ == "__main__":
    scrape_noon_products()