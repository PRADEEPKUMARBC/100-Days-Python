from selenium import webdriver

#keep chrome browser open after program finishes

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.chrome(options=chrome_options)
driver.get("https://www.amazon.in/boAt-Airdopes-Alpha-Wireless-Earbuds/dp/B0C3ZYFZ77/?_encoding=UTF8&pd_rd_w=bm63m&content-id=amzn1.sym.14ff1b43-540a-4bfd-a18c-350bea29dfa2&pf_rd_p=14ff1b43-540a-4bfd-a18c-350bea29dfa2&pf_rd_r=QVD08X5WXR64GAM03HNK&pd_rd_wg=W3mK6&pd_rd_r=149cef25-2bc4-4f6f-b414-5828fe4509bb&ref_=pd_hp_d_atf_Headphones&th=1")

price_dollar = driver.find_element(By.CLASSNAME, value="a-price-whole")
price_cents = driver.find_element(By.CLASSNAME, value="a-price-fraction")
print(f"The Price is {price_dollar}.{price_cents}")

driver.quit()