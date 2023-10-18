import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

def get_obfuscated_emails(url):
    # Initialize the Edge WebDriver with WebDriver Manager
    driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

    # Navigate to the web page containing obfuscated email addresses
    driver.get(url)

    # Function to de-obfuscate email addresses (modify this based on your obfuscation method)
    def deobfuscate_email(email):
        # Implement your email de-obfuscation logic here
        return email

    # Find and extract obfuscated email addresses
    email_elements = driver.find_elements(By.XPATH, '//a[contains(@href, "mailto:")]')
    email_list = []

    for email_element in email_elements:
        obfuscated_email = email_element.get_attribute("href").replace("mailto:", "")
        deobfuscated_email = deobfuscate_email(obfuscated_email)
        email_list.append([deobfuscated_email])  # Wrap the email in a list

    # Close the WebDriver
    driver.quit()

    return email_list

def main():
    # Prompt for the URL if not provided
    url = input("Enter the URL of the web page containing obfuscated email addresses: ")

    # Get the list of email addresses
    email_list = get_obfuscated_emails(url)

    # Save the extracted email addresses to a CSV file
    csv_file = "extracted_emails.csv"

    with open(csv_file, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Email"])
        writer.writerows(email_list)

    print(f"Extracted {len(email_list)} email addresses and saved to {csv_file}")

if __name__ == "__main__":
    main()
