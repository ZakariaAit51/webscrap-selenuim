from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Set up Chrome options for headless mode
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run Chrome in headless mode
chrome_options.add_argument("--disable-gpu")  # Disable GPU acceleration
chrome_options.add_argument("--no-sandbox")  # Bypass OS security model
chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems

# Create a new instance of the Chrome driver with the specified options
driver = webdriver.Chrome(options=chrome_options)

# Open a website (Python official blog)
url = "https://www.linkedin.com/home"
driver.get(url)

# Scrape the titles of articles
articles = driver.title

# Print the titles of the blog posts
print(articles)

# Close the driver
driver.quit()
