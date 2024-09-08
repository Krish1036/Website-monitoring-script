import smtplib
import time

# Email configuration
email = "trialmail1036@gmail.com"
password = "rnsg oiei lpzv prpq"
recipient = "krishthakore103610@gmail.com"

# Local HTML file path to monitor
file_path = 'D:\\Main-Projects- (KS)\\Website-monitering\\text.html'  # Change this to the path of your local HTML file

# Function to fetch local file content
def fetch_file_content(file_path):
    with open(file_path, 'r') as file:
        return file.read()

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

# Monitor local file
def monitor_file():
    previous_content = fetch_file_content(file_path)

    while True:
        print("Checking for updates...")
        time.sleep(10)  # Check every 60 seconds
        current_content = fetch_file_content(file_path)

        if current_content != previous_content:
            print("File content changed!")
            send_email("File Changed", f"The file {file_path} has been updated.")
            previous_content = current_content

if __name__ == "__main__":
    monitor_file()
