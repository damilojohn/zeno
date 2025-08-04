#!/bin/bash

echo "🚀 Setting up Zeno Server with Async SQLAlchemy and Email Support"

# Check if we're in the server directory
if [ ! -f "pyproject.toml" ]; then
    echo "❌ Error: Please run this script from the server directory"
    exit 1
fi

echo "📦 Installing new dependencies..."
pip install aiosmtplib jinja2 asyncpg

echo "✅ Dependencies installed successfully!"

echo ""
echo "🔧 Configuration Required:"
echo ""
echo "1. Update your DATABASE_URL to use asyncpg:"
echo "   Change from: postgresql://user:pass@host:port/db"
echo "   Change to:   postgresql+asyncpg://user:pass@host:port/db"
echo ""
echo "2. Add email configuration to your .env file:"
echo "   SMTP_SERVER=smtp.gmail.com"
echo "   SMTP_PORT=587"
echo "   SMTP_USERNAME=your_email@gmail.com"
echo "   SMTP_PASSWORD=your_app_password"
echo "   EMAIL_FROM=noreply@zeno.com"
echo "   FRONTEND_URL=http://localhost:3000"
echo ""
echo "3. For Gmail, you'll need to:"
echo "   - Enable 2-factor authentication"
echo "   - Generate an App Password"
echo "   - Use the App Password as SMTP_PASSWORD"
echo ""
echo "4. Test the setup:"
echo "   python test_async_db.py"
echo ""
echo "🎉 Setup complete! Check CHANGELOG.md for detailed information." 