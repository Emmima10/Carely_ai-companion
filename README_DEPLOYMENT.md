# Deploying CarelyAI to Streamlit Cloud

## Pre-Deployment Checklist

### 1. Update `.gitignore`
Ensure the following are in your `.gitignore`:
- ✅ `.env`
- ✅ `secrets.toml`
- ✅ `carely.db`
- ✅ `*.db`
- ✅ `venv/`
- ✅ `__pycache__/`

### 2. Environment Variables Setup

#### Local Development (.env file)
Your `.env` file should contain:
```env
GROQ_API_KEY=your_groq_api_key
TELEGRAM_BOT_TOKEN=your_telegram_bot_token
TELEGRAM_CHAT_ID=your_telegram_chat_id
```

**⚠️ NEVER commit this file to Git!**

#### Streamlit Cloud (secrets management)
In Streamlit Cloud dashboard:
1. Go to your app settings
2. Click on "Secrets" section
3. Add the following in TOML format:

```toml
GROQ_API_KEY = "your_groq_api_key_here"
TELEGRAM_BOT_TOKEN = "your_telegram_bot_token_here"
TELEGRAM_CHAT_ID = "your_telegram_chat_id_here"
```

### 3. Database Considerations

The app currently uses SQLite (`carely.db`). For production:

**Important Notes:**
- SQLite database will be recreated on each Streamlit Cloud restart
- User data will NOT persist between app restarts
- For production, consider migrating to PostgreSQL or another cloud database

**To keep using SQLite (good for demo/testing):**
- Database will auto-create on startup
- Sample data will be seeded automatically
- Users will need to re-register after each deployment

### 4. Required Files (Already Present)
- ✅ `requirements.txt` - All Python dependencies
- ✅ `main.py` - Entry point for Streamlit
- ✅ `.streamlit/config.toml` - Streamlit configuration

## Deployment Steps

### Step 1: Prepare Your Repository

1. **Remove sensitive files from Git tracking:**
```bash
# If .env was accidentally committed
git rm --cached .env
git rm --cached carely.db
git rm --cached .streamlit/secrets.toml
```

2. **Verify .gitignore is working:**
```bash
git status
# Should NOT show .env, *.db, secrets.toml
```

3. **Commit your changes:**
```bash
git add .
git commit -m "Prepare for Streamlit Cloud deployment"
```

### Step 2: Push to GitHub

1. **Create a new repository on GitHub** (if not already done)

2. **Push your code:**
```bash
# First time setup
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
git branch -M main
git push -u origin main

# Subsequent pushes
git push
```

### Step 3: Deploy to Streamlit Cloud

1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Sign in with GitHub
3. Click "New app"
4. Select your repository: `YOUR_USERNAME/YOUR_REPO_NAME`
5. Set main file path: `main.py`
6. Click "Advanced settings"
7. Set Python version: `3.9` or higher
8. Add secrets (see section 2 above)
9. Click "Deploy"

### Step 4: Post-Deployment Configuration

After deployment:
1. Test all features
2. Verify Groq API is working (chat functionality)
3. Test Telegram alerts (if configured)
4. Create test user accounts

## Common Issues & Solutions

### Issue: "ModuleNotFoundError"
**Solution:** Update `requirements.txt` with missing package

### Issue: Database not persisting
**Solution:** This is expected with SQLite on Streamlit Cloud. Users will be seeded on each restart.

### Issue: Environment variables not found
**Solution:** Double-check secrets are added in Streamlit Cloud dashboard (TOML format)

### Issue: App crashes on startup
**Solution:** Check logs in Streamlit Cloud dashboard for specific error

## Testing Locally Before Deployment

```bash
# Activate virtual environment
.\venv\Scripts\Activate.ps1  # Windows
source venv/bin/activate      # Mac/Linux

# Install dependencies
pip install -r requirements.txt

# Run locally
streamlit run main.py
```

## Security Reminders

- ✅ Never commit API keys or secrets to Git
- ✅ Use environment variables for all sensitive data
- ✅ Keep `.env` in `.gitignore`
- ✅ Use Streamlit Cloud secrets for production
- ✅ Regularly rotate API keys
- ✅ Review Git history to ensure no secrets were committed

## Optional: Migrate to PostgreSQL (Production)

For production with persistent data:

1. Set up a PostgreSQL database (Supabase, Railway, etc.)
2. Update `app/database/models.py`:
```python
import os
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///carely.db")
```
3. Add `DATABASE_URL` to Streamlit secrets
4. Add `psycopg2-binary` to `requirements.txt`

## Support

For issues or questions:
- Check Streamlit Community Forum
- Review Streamlit Cloud documentation
- Check app logs in Streamlit Cloud dashboard
