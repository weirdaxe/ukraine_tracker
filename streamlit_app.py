import streamlit as st
from playwright.sync_api import sync_playwright

def scrape_and_screenshot():
    screenshot_path = "chart_screenshot.png"
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, args=["--no-sandbox", "--disable-dev-shm-usage"])
        page = browser.new_page()
        url = "https://www.nzz.ch/english/ukraine-war-interactive-map-on-a-big-scale-ld.1748451"
        page.goto(url)

        # Accept cookies
        try:
            page.click('#cmpwelcomebtnyes a', timeout=5000)
        except:
            pass

        page.wait_for_selector("#chart", timeout=60000)

        chart_div = page.query_selector("#chart")
        if not chart_div:
            browser.close()
            return None, "Div with id 'chart' not found."

        chart_div.screenshot(path=screenshot_path)
        browser.close()
    return screenshot_path, None

def main():
    st.title("Ukraine War Interactive Map Scraper")

    if st.button("🔍 Scrape and Show Chart"):
        with st.spinner("Scraping and capturing chart..."):
            image_path, error = scrape_and_screenshot()
            if error:
                st.error(error)
            else:
                st.success("Screenshot captured!")
                st.image(image_path)  # Display the scraped image here
                st.download_button("Download Screenshot", open(image_path, "rb").read(), file_name="chart.png")

if __name__ == "__main__":
    main()


# import streamlit as st
# from playwright.sync_api import sync_playwright
# import os

# def scrape_and_screenshot():
#     screenshot_path = "/tmp/chart_screenshot.png"
#     with sync_playwright() as p:
#         browser = p.chromium.launch(
#             headless=True,
#             args=["--no-sandbox", "--disable-dev-shm-usage"]
#         )
#         page = browser.new_page()
#         url = "https://www.nzz.ch/english/ukraine-war-interactive-map-on-a-big-scale-ld.1748451"
#         page.goto(url)

#         # Accept cookies by clicking the button
#         try:
#             page.click('#cmpwelcomebtnyes a', timeout=5000)
#         except:
#             pass

#         # Wait up to 60 seconds for #chart to appear
#         page.wait_for_selector("#chart", timeout=60000)

#         chart_div = page.query_selector("#chart")
#         if not chart_div:
#             browser.close()
#             return None, "Div with id 'chart' not found."
        
#         chart_div.screenshot(path=screenshot_path)
#         browser.close()
#     return screenshot_path, None



# def main():
#     st.title("Ukraine War Tracker - Div Screenshot Scraper")

#     if st.button("🔍 Scrape and Download Chart Screenshot"):
#         with st.spinner("Scraping and capturing the div..."):
#             image_path, error = scrape_and_screenshot()
#             if error:
#                 st.error(error)
#             else:
#                 st.image(image_path)
#                 with open(image_path, "rb") as f:
#                     btn = st.download_button(
#                         label="Download Screenshot",
#                         data=f,
#                         file_name="chart_screenshot.png",
#                         mime="image/png"
#                     )

# if __name__ == "__main__":
#     main()


    
# import streamlit as st
# import asyncio
# from pyppeteer import launch

# async def scrape_and_screenshot():
#     browser = await launch(headless=True, args=['--no-sandbox', '--disable-dev-shm-usage'])
#     page = await browser.newPage()
#     await page.goto('https://www.nzz.ch/english/ukraine-war-interactive-map-on-a-big-scale-ld.1748451')
#     await page.waitForSelector('canvas')  # Wait for the canvas element to load
#     canvas = await page.querySelector('canvas')
#     if canvas:
#         screenshot_path = '/tmp/chart_screenshot.png'
#         await canvas.screenshot({'path': screenshot_path})
#         await browser.close()
#         return screenshot_path, None
#     else:
#         await browser.close()
#         return None, 'No canvas element found inside iframe.'

# def main():
#     st.title("Ukraine War Tracker - Screenshot Scraper")

#     if st.button("🔍 Scrape and Download Chart Screenshot"):
#         with st.spinner("Scraping and capturing chart..."):
#             loop = asyncio.new_event_loop()
#             asyncio.set_event_loop(loop)
#             image_path, error = loop.run_until_complete(scrape_and_screenshot())
#             if error:
#                 st.error(f"Error: {error}")
#             else:
#                 st.success("Screenshot saved!")
#                 st.image(image_path)
#                 st.download_button("Download Screenshot", open(image_path, "rb").read(), file_name="chart_screenshot.png")

# if __name__ == "__main__":
#     main()


# # import streamlit as st
# # from selenium import webdriver
# # from selenium.webdriver.chrome.service import Service
# # from selenium.webdriver.chrome.options import Options
# # from webdriver_manager.chrome import ChromeDriverManager

# # def scrape_and_screenshot():
# #     chrome_options = Options()
# #     chrome_options.add_argument("--headless")  # Run headless in Streamlit Cloud
# #     chrome_options.add_argument("--disable-gpu")
# #     chrome_options.add_argument("--no-sandbox")
# #     chrome_options.add_argument("--disable-dev-shm-usage")
# #     chrome_options.add_argument("--window-size=1920,1080")

# #     # Get ChromeDriver automatically, no manual download or chmod needed
# #     driver_path = ChromeDriverManager().install()
# #     service = Service(driver_path)

# #     driver = webdriver.Chrome(service=service, options=chrome_options)

# #     try:
# #         url = "https://www.nzz.ch/english/ukraine-war-interactive-map-on-a-big-scale-ld.1748451"
# #         driver.get(url)
# #         driver.implicitly_wait(10)  # Wait for page load

# #         # Screenshot the full page
# #         screenshot_path = "/tmp/chart_screenshot.png"
# #         driver.save_screenshot(screenshot_path)

# #         return screenshot_path, None
# #     except Exception as e:
# #         return None, str(e)
# #     finally:
# #         driver.quit()


# # if __name__ == "__main__":
# #     st.title("Ukraine War Tracker - Screenshot Scraper")

# #     if st.button("🔍 Scrape and Download Chart Screenshot"):
# #         with st.spinner("Scraping and capturing chart..."):
# #             image_path, error = scrape_and_screenshot()
# #             if error:
# #                 st.error(f"Error: {error}")
# #             else:
# #                 st.success("Screenshot saved!")
# #                 st.image(image_path)
# #                 st.download_button("Download Screenshot", open(image_path, "rb").read(), file_name="chart_screenshot.png")


# # # import streamlit as st
# # # from playwright.sync_api import sync_playwright
# # # import subprocess
# # # import os

# # # def install_playwright_browsers():
# # #     cache_path = os.path.expanduser("~/.cache/ms-playwright")
# # #     if not os.path.exists(cache_path):
# # #         st.info("Installing Playwright browsers. This may take a moment...")
# # #         try:
# # #             # Run playwright install WITHOUT --with-deps to avoid sudo
# # #             subprocess.run(["playwright", "install"], check=True)
# # #         except Exception as e:
# # #             st.error(f"Error installing Playwright browsers: {e}")

# # # install_playwright_browsers()

# # # def scrape_and_screenshot():
# # #     screenshot_path = "chart_screenshot.png"
# # #     try:
# # #         with sync_playwright() as p:
# # #             browser = p.chromium.launch(headless=True, args=["--no-sandbox"])
# # #             page = browser.new_page()
# # #             url = "https://www.nzz.ch/english/ukraine-war-interactive-map-of-the-current-front-line-ld.1688087"
# # #             page.goto(url)
# # #             page.wait_for_timeout(10000)  # Wait 10 seconds for iframe/chart to load

# # #             iframe_element = page.query_selector("iframe")
# # #             if not iframe_element:
# # #                 browser.close()
# # #                 return None, "No iframe found on the page."

# # #             frame = iframe_element.content_frame()
# # #             if not frame:
# # #                 browser.close()
# # #                 return None, "Could not access iframe content."

# # #             frame.wait_for_selector("canvas", timeout=10000)
# # #             canvas = frame.query_selector("canvas")
# # #             if not canvas:
# # #                 browser.close()
# # #                 return None, "No canvas element found inside iframe."

# # #             canvas.screenshot(path=screenshot_path)
# # #             browser.close()
# # #             return screenshot_path, None
# # #     except Exception as e:
# # #         return None, str(e)

# # # def main():
# # #     st.title("Ukraine War Front Line Map Scraper")
# # #     st.markdown("Scrape the iframe chart and download it as an image.")

# # #     if st.button("🔍 Scrape and Download Chart Screenshot"):
# # #         with st.spinner("Scraping and capturing chart... Please wait up to 10 seconds."):
# # #             image_path, error = scrape_and_screenshot()

# # #         if error:
# # #             st.error(f"Error: {error}")
# # #         else:
# # #             st.success("Screenshot captured successfully!")
# # #             st.image(image_path)
# # #             with open(image_path, "rb") as f:
# # #                 st.download_button(
# # #                     label="Download Chart Image",
# # #                     data=f,
# # #                     file_name="ukraine_war_frontline.png",
# # #                     mime="image/png"
# # #                 )

# # # if __name__ == "__main__":
# # #     main()



# # # # import streamlit as st
# # # # # from selenium import webdriver
# # # # # from selenium.webdriver.chrome.service import Service
# # # # # from selenium.webdriver.chrome.options import Options

# # # # from selenium import webdriver
# # # # from selenium.webdriver.chrome.service import Service
# # # # from selenium.webdriver.chrome.options import Options
# # # # from webdriver_manager.chrome import ChromeDriverManager

# # # # import os
# # # # import stat
# # # # import time

# # # # def make_executable(path):
# # # #     st_mode = os.stat(path).st_mode
# # # #     os.chmod(path, st_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)
    
# # # # def scrape_and_screenshot():
# # # #     chrome_options = Options()
# # # #     chrome_options.add_argument("--headless=new")
# # # #     chrome_options.add_argument("--disable-gpu")
# # # #     chrome_options.add_argument("--no-sandbox")
# # # #     chrome_options.add_argument("--window-size=1920,1080")

# # # #     service = Service(ChromeDriverManager().install())

# # # #     try:
# # # #         driver = webdriver.Chrome(service=service, options=chrome_options)
# # # #         url = "https://www.nzz.ch/english/ukraine-war-interactive-map-of-the-current-front-line-ld.1688087"
# # # #         driver.get(url)
# # # #         time.sleep(10)  # wait for iframe and graph to load fully

# # # #         # Switch to iframe (adjust selector as needed)
# # # #         iframe = driver.find_element("css selector", "iframe")
# # # #         driver.switch_to.frame(iframe)

# # # #         # Locate the graph element inside iframe (adjust selector to target graph)
# # # #         graph = driver.find_element("css selector", "canvas")  # example: assuming graph is a canvas element
# # # #         screenshot_path = "chart_screenshot.png"
# # # #         graph.screenshot(screenshot_path)

# # # #         driver.quit()
# # # #         return screenshot_path, None

# # # #     except Exception as e:
# # # #         return None, str(e)

# # # # st.title("Ukraine War Front Line Map Scraper")

# # # # if st.button("🔍 Scrape and Download Chart Screenshot"):
# # # #     with st.spinner("Scraping and capturing chart..."):
# # # #         image_path, error = scrape_and_screenshot()
# # # #         if error:
# # # #             st.error(f"Error: {error}")
# # # #         else:
# # # #             with open(image_path, "rb") as f:
# # # #                 st.download_button(
# # # #                     label="Download Chart Screenshot",
# # # #                     data=f,
# # # #                     file_name="ukraine_frontline_chart.png",
# # # #                     mime="image/png"
# # # #                 )


# # # # # import streamlit as st
# # # # # from selenium import webdriver
# # # # # from selenium.webdriver.chrome.service import Service
# # # # # from selenium.webdriver.common.by import By
# # # # # from selenium.webdriver.chrome.options import Options
# # # # # import time
# # # # # import base64
# # # # # import os

# # # # # def scrape_and_screenshot():
# # # # #     # Setup Chrome options for headless scraping
# # # # #     chrome_options = Options()
# # # # #     chrome_options.add_argument("--headless")
# # # # #     chrome_options.add_argument("--disable-gpu")
# # # # #     chrome_options.add_argument("--no-sandbox")
# # # # #     chrome_options.add_argument("--disable-dev-shm-usage")
# # # # #     chrome_options.add_argument("--window-size=1920,1080")

# # # # #     # Use local chromedriver (must be in the repo)
# # # # #     driver_path = "./chromedriver"
# # # # #     service = Service(driver_path)
# # # # #     driver = webdriver.Chrome(service=service, options=chrome_options)

# # # # #     try:
# # # # #         url = "https://www.nzz.ch/english/ukraine-war-interactive-map-of-the-current-front-line-ld.1688087"
# # # # #         driver.get(url)

# # # # #         time.sleep(5)  # Allow iframe to load

# # # # #         iframes = driver.find_elements(By.TAG_NAME, "iframe")
# # # # #         chart_found = False

# # # # #         for iframe in iframes:
# # # # #             try:
# # # # #                 driver.switch_to.frame(iframe)
# # # # #                 time.sleep(2)

# # # # #                 # Look for chart content
# # # # #                 if "highcharts" in driver.page_source or "chart" in driver.page_source:
# # # # #                     chart_found = True
# # # # #                     break

# # # # #                 driver.switch_to.default_content()
# # # # #             except Exception:
# # # # #                 continue

# # # # #         if not chart_found:
# # # # #             driver.quit()
# # # # #             return None, "Chart iframe not found."

# # # # #         # Save screenshot
# # # # #         screenshot_path = "chart_screenshot.png"
# # # # #         driver.save_screenshot(screenshot_path)
# # # # #         driver.quit()

# # # # #         return screenshot_path, None

# # # # #     except Exception as e:
# # # # #         driver.quit()
# # # # #         return None, f"Error: {str(e)}"

# # # # # # --- Streamlit App UI ---

# # # # # st.set_page_config(page_title="NZZ Chart Scraper", layout="centered")
# # # # # st.title("📈 Scrape Chart Screenshot from NZZ Article")
# # # # # st.caption("This tool scrapes the chart from the NZZ Ukraine front line article and gives you a downloadable image.")

# # # # # if st.button("🔍 Scrape and Download Chart Screenshot"):
# # # # #     with st.spinner("Scraping and capturing chart..."):
# # # # #         image_path, error = scrape_and_screenshot()

# # # # #     if error:
# # # # #         st.error(error)
# # # # #     else:
# # # # #         # Read image bytes
# # # # #         with open(image_path, "rb") as f:
# # # # #             image_bytes = f.read()

# # # # #         # Display image
# # # # #         st.image(image_bytes, caption="Chart Screenshot", use_column_width=True)

# # # # #         # Create download button
# # # # #         b64 = base64.b64encode(image_bytes).decode()
# # # # #         st.markdown(
# # # # #             f'<a href="data:image/png;base64,{b64}" download="chart_screenshot.png">📥 Click here to download the image</a>',
# # # # #             unsafe_allow_html=True
# # # # #         )
