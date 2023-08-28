from rich.traceback import install
install(show_locals=True)
from selenium import webdriver

# Video ID of the YouTube video
video_id = 'r5NQecwZs1A&ab'

video_url = f'https://www.youtube.com/watch?v={video_id}'
# Set up the WebDriver
driver = webdriver.Chrome()  # You'll need to have ChromeDriver installed

# Open the video URL
driver.get(video_url)

# Find the element that contains the view count
view_count_element = driver.find_element_by_xpath('//*[@class="view-count"]')

if view_count_element:
    view_count = view_count_element.text
    print(f"View Count: {view_count}")
else:
    print("View count element not found on the page.")

# Close the browser window
driver.quit()
