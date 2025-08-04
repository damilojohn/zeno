import aiosmtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from jinja2 import Template
from zeno.api.core.config import Settings
from zeno.api.core.utils import LOG

settings = Settings()

# HTML template for password reset email
PASSWORD_RESET_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Password Reset - Zeno</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 600px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f4f4f4;
        }
        .container {
            background-color: #ffffff;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }
        .header {
            text-align: center;
            margin-bottom: 30px;
        }
        .logo {
            font-size: 2em;
            font-weight: bold;
            color: #2c3e50;
            margin-bottom: 10px;
        }
        .title {
            color: #e74c3c;
            font-size: 1.5em;
            margin-bottom: 20px;
        }
        .content {
            margin-bottom: 30px;
        }
        .button {
            display: inline-block;
            background-color: #3498db;
            color: white;
            padding: 12px 30px;
            text-decoration: none;
            border-radius: 5px;
            font-weight: bold;
            margin: 20px 0;
        }
        .button:hover {
            background-color: #2980b9;
        }
        .footer {
            text-align: center;
            margin-top: 30px;
            padding-top: 20px;
            border-top: 1px solid #eee;
            color: #666;
            font-size: 0.9em;
        }
        .warning {
            background-color: #fff3cd;
            border: 1px solid #ffeaa7;
            color: #856404;
            padding: 15px;
            border-radius: 5px;
            margin: 20px 0;
        }
        .token {
            background-color: #f8f9fa;
            border: 1px solid #dee2e6;
            padding: 15px;
            border-radius: 5px;
            font-family: 'Courier New', monospace;
            font-size: 1.1em;
            text-align: center;
            margin: 20px 0;
            word-break: break-all;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <div class="logo">📚 Zeno</div>
            <div class="title">Password Reset Request</div>
        </div>
        
        <div class="content">
            <p>Hello,</p>
            
            <p>We received a request to reset your password for your Zeno account. If you didn't make this request, you can safely ignore this email.</p>
            
            <p>To reset your password, please use the following token:</p>
            
            <div class="token">
                <strong>{{ reset_token }}</strong>
            </div>
            
            <p>Or click the button below to go to the password reset page:</p>
            
            <div style="text-align: center;">
                <a href="{{ reset_url }}" class="button">Reset Password</a>
            </div>
            
            <div class="warning">
                <strong>⚠️ Important:</strong>
                <ul>
                    <li>This token will expire in {{ expiry_minutes }} minutes</li>
                    <li>Never share this token with anyone</li>
                    <li>If you didn't request this reset, please ignore this email</li>
                </ul>
            </div>
        </div>
        
        <div class="footer">
            <p>This is an automated message from Zeno. Please do not reply to this email.</p>
            <p>If you have any questions, please contact our support team.</p>
        </div>
    </div>
</body>
</html>
"""


async def send_password_reset_email(email: str, reset_token: str, username: str) -> bool:
    """
    Send HTML password reset email to user
    
    Args:
        email: User's email address
        reset_token: The reset token to include in the email
        username: User's username for personalization
        
    Returns:
        bool: True if email sent successfully, False otherwise
    """
    try:
        # Create message
        message = MIMEMultipart("alternative")
        message["Subject"] = "Password Reset Request - Zeno"
        message["From"] = settings.email_from
        message["To"] = email
        
        # Create reset URL
        reset_url = f"{settings.frontend_url}/reset-password?token={reset_token}"
        
        # Render HTML template
        template = Template(PASSWORD_RESET_TEMPLATE)
        html_content = template.render(
            reset_token=reset_token,
            reset_url=reset_url,
            username=username,
            expiry_minutes=settings.reset_tok_exp
        )
        
        # Create HTML part
        html_part = MIMEText(html_content, "html")
        message.attach(html_part)
        
        # Send email
        await aiosmtplib.send(
            message,
            hostname=settings.smtp_server,
            port=settings.smtp_port,
            username=settings.smtp_username,
            password=settings.smtp_password,
            use_tls=True
        )
        
        LOG.info(f"Password reset email sent successfully to {email}")
        return True
        
    except Exception as e:
        LOG.error(f"Failed to send password reset email to {email}: {e}")
        return False


async def send_test_email(email: str) -> bool:
    """
    Send a test email to verify email configuration
    
    Args:
        email: Email address to send test to
        
    Returns:
        bool: True if email sent successfully, False otherwise
    """
    try:
        message = MIMEMultipart("alternative")
        message["Subject"] = "Test Email - Zeno"
        message["From"] = settings.email_from
        message["To"] = email
        
        html_content = """
        <html>
        <body>
            <h1>Test Email</h1>
            <p>This is a test email to verify the email configuration is working correctly.</p>
        </body>
        </html>
        """
        
        html_part = MIMEText(html_content, "html")
        message.attach(html_part)
        
        await aiosmtplib.send(
            message,
            hostname=settings.smtp_server,
            port=settings.smtp_port,
            username=settings.smtp_username,
            password=settings.smtp_password,
            use_tls=True
        )
        
        LOG.info(f"Test email sent successfully to {email}")
        return True
        
    except Exception as e:
        LOG.error(f"Failed to send test email to {email}: {e}")
        return False 