import smtplib
import schedule
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Email account credentials
EMAIL_ADDRESS = 'email@example.com'
EMAIL_PASSWORD = 'app password'

# Recipient's email address
TO_ADDRESS = 'email@example.com'

# Create email content
def create_email():
    subject = "Daily Performance Report"

    # Generate report data
    total_users = 1234
    new_signups = 56
    active_users = 789
    transactions = 105
    revenue = 20345.67

    body = f"""
    Hello,

    Here is your daily performance report:

    - **Total Users:** {total_users}
    - **New Signups Today:** {new_signups}
    - **Active Users:** {active_users}
    - **Transactions Processed:** {transactions}
    - **Revenue Generated:** ${revenue:,.2f}

    **Highlights:**
    - User engagement increased by 15% compared to yesterday.
    - Revenue from premium subscriptions grew by 10%.
    - New features launched have positive feedback from users.

    **Upcoming Tasks:**
    - Launch the new referral program on Monday.
    - Conduct a review meeting with the marketing team on Wednesday.
    - Prepare the quarterly performance review by the end of the month.

    Please review the attached document for a more detailed analysis.

    Best regards,
    lovis.
    """
    return subject, body

# Send email function
def send_email(subject, body):
    # Create the email
    msg = MIMEMultipart()
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = TO_ADDRESS
    msg['Subject'] = subject

    # Attach the message body
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Connect to the server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()

        # Log in to the server
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

        # Send the email
        server.send_message(msg)
        print("Message sent successfully!")

    except Exception as e:
        print(f"Failed to send email. Error: {e}")

    finally:
        # Quit the server
        server.quit()

# Task to be scheduled
def daily_report():
    subject, body = create_email()
    send_email(subject, body)

# Schedule the task to run daily at a specific time
schedule.every().day.at("18:00").do(daily_report)

# Run the scheduled tasks
while True:
    schedule.run_pending()
    time.sleep(60)  # wait 1 minute