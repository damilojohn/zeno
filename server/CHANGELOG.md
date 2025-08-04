# Changelog

## [Unreleased] - 2024-01-XX

### Added
- **Async SQLAlchemy Support**: Converted all database operations to use async SQLAlchemy
  - Updated database configuration to use `create_async_engine` and `async_sessionmaker`
  - Modified all database queries to use async operations with `session.execute()` and `select()`
  - Updated dependency injection to use `AsyncSession` instead of `Session`
  - Added `asyncpg` dependency for async PostgreSQL support

- **HTML Email Functionality**: Implemented professional HTML email sending for password reset
  - Added `aiosmtplib` and `jinja2` dependencies for async email and templating
  - Created beautiful HTML email template with responsive design
  - Added email configuration settings (SMTP server, credentials, etc.)
  - Implemented `send_password_reset_email()` function with proper error handling
  - Added test email endpoint for debugging email configuration

- **Token Cleanup**: Enhanced password reset security
  - Modified `create_new_password()` to delete all reset tokens for a user after successful password reset
  - This prevents token reuse and improves security

### Changed
- **Database Operations**: All database operations are now async
  - `get_current_user()`: Now uses async queries
  - `add_new_user()`: Async user creation with proper error handling
  - `authenticate_user()`: Async authentication with improved error messages
  - `reset_password()`: Async password reset with email sending
  - `create_new_password()`: Async password update with token cleanup

- **Email System**: Replaced fake email logging with real HTML email sending
  - `send_reset_mail()`: Now sends actual HTML emails instead of just logging
  - Added fallback to logging if email sending fails
  - Professional email template with Zeno branding

### Technical Details
- **Database**: Uses `postgresql+asyncpg://` connection string for async PostgreSQL
- **Email**: Supports Gmail SMTP with TLS encryption
- **Templates**: Jinja2 templating for dynamic email content
- **Error Handling**: Graceful fallbacks for email failures

### Environment Variables Added
```env
# Email Configuration
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
SMTP_USERNAME=your_email@gmail.com
SMTP_PASSWORD=your_app_password
EMAIL_FROM=noreply@zeno.com
FRONTEND_URL=http://localhost:3000
```

### Dependencies Added
- `aiosmtplib>=3.0.0` - Async SMTP client
- `jinja2>=3.1.0` - Template engine
- `asyncpg>=0.29.0` - Async PostgreSQL driver

### Breaking Changes
- All database operations now require `await` keyword
- Session type changed from `Session` to `AsyncSession`
- Database URL should use `postgresql+asyncpg://` instead of `postgresql://`

### Migration Guide
1. Update your database URL to use `postgresql+asyncpg://`
2. Install new dependencies: `pip install aiosmtplib jinja2 asyncpg`
3. Set up email configuration in environment variables
4. Update any custom database operations to use async syntax 