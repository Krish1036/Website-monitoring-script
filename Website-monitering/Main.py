import http.client
import smtplib
import time
from urllib.parse import urlparse

# Email configuration
email = "trialmail1036@gmail.com"
password = "rnsg oiei lpzv prpq"
recipient = "krishthakore103610@gmail.com"

# Website URL to monitor
url = 'https://www.medadmgujarat.org/ga/home.aspx'

# Function to fetch website content using http.client
def fetch_website_content(url):
    parsed_url = urlparse(url)
    connection = http.client.HTTPSConnection(parsed_url.netloc)
    connection.request("GET", parsed_url.path or "/")
    response = connection.getresponse()
    return response.read().decode()

# Function to send email notification
def send_email(subject, body):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email, password)
        message = f"Subject: {subject}\n\n{body}"
        server.sendmail(email, recipient, message)
        server.quit()
        print("Email sent successfully")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Monitor website
def monitor_website():
    previous_content = fetch_website_content(url)

    while True:
        print("Checking for updates...")  # This will print every time the website is checked
        time.sleep(60)  # Check every 60 seconds
        current_content = fetch_website_content(url)

        if current_content != previous_content:
            print("Website content changed!")
            send_email("Website Changed", f"The website {url} has been updated.")
            previous_content = current_content

if __name__ == "__main__":
    monitor_website()
