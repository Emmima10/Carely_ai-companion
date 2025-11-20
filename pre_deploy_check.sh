#!/bin/bash

# Pre-Deployment Checklist Script for CarelyAI
# Run this before pushing to Git

echo "🔍 CarelyAI Pre-Deployment Checklist"
echo "======================================"
echo ""

# Check 1: .env file exists but not tracked
echo "✓ Checking .env file..."
if [ -f ".env" ]; then
    if git ls-files --error-unmatch .env 2>/dev/null; then
        echo "  ⚠️  WARNING: .env file is tracked by Git!"
        echo "  Run: git rm --cached .env"
    else
        echo "  ✅ .env file exists and is not tracked"
    fi
else
    echo "  ⚠️  .env file not found (required for local dev)"
fi
echo ""

# Check 2: Database file not tracked
echo "✓ Checking database files..."
if git ls-files --error-unmatch *.db 2>/dev/null; then
    echo "  ⚠️  WARNING: Database file is tracked by Git!"
    echo "  Run: git rm --cached *.db"
else
    echo "  ✅ Database files are not tracked"
fi
echo ""

# Check 3: secrets.toml not tracked
echo "✓ Checking Streamlit secrets..."
if git ls-files --error-unmatch .streamlit/secrets.toml 2>/dev/null; then
    echo "  ⚠️  WARNING: secrets.toml is tracked by Git!"
    echo "  Run: git rm --cached .streamlit/secrets.toml"
else
    echo "  ✅ secrets.toml is not tracked"
fi
echo ""

# Check 4: Required files exist
echo "✓ Checking required files..."
FILES=("requirements.txt" "main.py" ".gitignore" ".streamlit/config.toml")
for file in "${FILES[@]}"; do
    if [ -f "$file" ]; then
        echo "  ✅ $file exists"
    else
        echo "  ❌ $file is missing!"
    fi
done
echo ""

# Check 5: Check for hardcoded secrets
echo "✓ Checking for hardcoded secrets..."
if grep -r "sk-" --include="*.py" --exclude-dir=venv --exclude-dir=.git . 2>/dev/null; then
    echo "  ⚠️  WARNING: Possible API keys found in code!"
else
    echo "  ✅ No obvious hardcoded secrets found"
fi
echo ""

echo "======================================"
echo "📋 Manual Checks Required:"
echo ""
echo "1. [ ] Verify all API keys are in .env (not in code)"
echo "2. [ ] Test app locally: streamlit run main.py"
echo "3. [ ] Commit changes: git add . && git commit -m 'message'"
echo "4. [ ] Push to GitHub: git push"
echo "5. [ ] Add secrets in Streamlit Cloud dashboard"
echo "6. [ ] Deploy on share.streamlit.io"
echo ""
echo "See README_DEPLOYMENT.md for detailed instructions"
echo "======================================"
