import streamlit as st
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import base64
import os

def scrape_and_screenshot():
    # Setup Chrome options for headless scraping
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920,1080")

    # Use local chromedriver (must be in the repo)
    driver_path = "./chromedriver"
    service = Service(driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        url = "https://www.nzz.ch/english/ukraine-war-interactive-map-of-the-current-front-line-ld.1688087"
        driver.get(url)

        time.sleep(5)  # Allow iframe to load

        iframes = driver.find_elements(By.TAG_NAME, "iframe")
        chart_found = False

        for iframe in iframes:
            try:
                driver.switch_to.frame(iframe)
                time.sleep(2)

                # Look for chart content
                if "highcharts" in driver.page_source or "chart" in driver.page_source:
                    chart_found = True
                    break

                driver.switch_to.default_content()
            except Exception:
                continue

        if not chart_found:
            driver.quit()
            return None, "Chart iframe not found."

        # Save screenshot
        screenshot_path = "chart_screenshot.png"
        driver.save_screenshot(screenshot_path)
        driver.quit()

        return screenshot_path, None

    except Exception as e:
        driver.quit()
        return None, f"Error: {str(e)}"

# --- Streamlit App UI ---

st.set_page_config(page_title="NZZ Chart Scraper", layout="centered")
st.title("📈 Scrape Chart Screenshot from NZZ Article")
st.caption("This tool scrapes the chart from the NZZ Ukraine front line article and gives you a downloadable image.")

if st.button("🔍 Scrape and Download Chart Screenshot"):
    with st.spinner("Scraping and capturing chart..."):
        image_path, error = scrape_and_screenshot()

    if error:
        st.error(error)
    else:
        # Read image bytes
        with open(image_path, "rb") as f:
            image_bytes = f.read()

        # Display image
        st.image(image_bytes, caption="Chart Screenshot", use_column_width=True)

        # Create download button
        b64 = base64.b64encode(image_bytes).decode()
        st.markdown(
            f'<a href="data:image/png;base64,{b64}" download="chart_screenshot.png">📥 Click here to download the image</a>',
            unsafe_allow_html=True
        )
