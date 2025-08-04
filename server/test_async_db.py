#!/usr/bin/env python3
"""
Test script to verify async database functionality
"""

import asyncio
import os
from sqlalchemy.ext.asyncio import create_async_engine
from zeno.api.core.db import init_db
from zeno.api.core.config import Settings

async def test_async_db():
    """Test async database connection and initialization"""
    
    # Set up test environment variables
    os.environ.update({
        "ENVIRONMENT": "development",
        "HOST": "localhost",
        "PORT": "8080",
        "DATABASE_URL": "postgresql+asyncpg://postgres:password@localhost:5432/zeno_test",
        "CORS_ORIGINS": "http://localhost:3000",
        "GOOGLE_CLIENT_ID": "test_client_id",
        "GOOGLE_CLIENT_SECRET": "test_client_secret",
        "GEMINI_API_KEY": "test_api_key",
        "GEMINI_MODEL": "gemini-pro",
        "JWT_SECRET_KEY": "test_secret_key",
        "JWT_REFRESH_SECRET_KEY": "test_refresh_secret_key",
        "JWT_ALGORITHM": "HS256",
        "JWT_EXP": "30",
        "JWT_REFRESH_EXP": "1440",
        "RESET_TOK_EXP": "15",
        "SMTP_SERVER": "smtp.gmail.com",
        "SMTP_PORT": "587",
        "SMTP_USERNAME": "test@example.com",
        "SMTP_PASSWORD": "test_password",
        "EMAIL_FROM": "noreply@zeno.com",
        "FRONTEND_URL": "http://localhost:3000"
    })
    
    settings = Settings()
    
    try:
        print("🔄 Testing async database connection...")
        
        # Create async engine
        engine = create_async_engine(settings.database_url, echo=True)
        
        # Test database initialization
        await init_db(engine, settings)
        
        print("✅ Async database test completed successfully!")
        
        # Clean up
        await engine.dispose()
        
    except Exception as e:
        print(f"❌ Async database test failed: {e}")
        raise

if __name__ == "__main__":
    asyncio.run(test_async_db()) 