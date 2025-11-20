# Pre-Deployment Checklist for CarelyAI (PowerShell)
# Run this before pushing to Git

Write-Host "🔍 CarelyAI Pre-Deployment Checklist" -ForegroundColor Cyan
Write-Host "======================================" -ForegroundColor Cyan
Write-Host ""

# Check 1: .env file exists but not tracked
Write-Host "✓ Checking .env file..." -ForegroundColor Yellow
if (Test-Path ".env") {
    $envTracked = git ls-files --error-unmatch .env 2>$null
    if ($LASTEXITCODE -eq 0) {
        Write-Host "  ⚠️  WARNING: .env file is tracked by Git!" -ForegroundColor Red
        Write-Host "  Run: git rm --cached .env" -ForegroundColor Red
    } else {
        Write-Host "  ✅ .env file exists and is not tracked" -ForegroundColor Green
    }
} else {
    Write-Host "  ⚠️  .env file not found (required for local dev)" -ForegroundColor Yellow
}
Write-Host ""

# Check 2: Database file not tracked
Write-Host "✓ Checking database files..." -ForegroundColor Yellow
$dbTracked = git ls-files --error-unmatch *.db 2>$null
if ($LASTEXITCODE -eq 0) {
    Write-Host "  ⚠️  WARNING: Database file is tracked by Git!" -ForegroundColor Red
    Write-Host "  Run: git rm --cached *.db" -ForegroundColor Red
} else {
    Write-Host "  ✅ Database files are not tracked" -ForegroundColor Green
}
Write-Host ""

# Check 3: secrets.toml not tracked
Write-Host "✓ Checking Streamlit secrets..." -ForegroundColor Yellow
$secretsTracked = git ls-files --error-unmatch .streamlit/secrets.toml 2>$null
if ($LASTEXITCODE -eq 0) {
    Write-Host "  ⚠️  WARNING: secrets.toml is tracked by Git!" -ForegroundColor Red
    Write-Host "  Run: git rm --cached .streamlit/secrets.toml" -ForegroundColor Red
} else {
    Write-Host "  ✅ secrets.toml is not tracked" -ForegroundColor Green
}
Write-Host ""

# Check 4: Required files exist
Write-Host "✓ Checking required files..." -ForegroundColor Yellow
$requiredFiles = @("requirements.txt", "main.py", ".gitignore", ".streamlit\config.toml")
foreach ($file in $requiredFiles) {
    if (Test-Path $file) {
        Write-Host "  ✅ $file exists" -ForegroundColor Green
    } else {
        Write-Host "  ❌ $file is missing!" -ForegroundColor Red
    }
}
Write-Host ""

# Check 5: Check for hardcoded secrets (basic check)
Write-Host "✓ Checking for hardcoded secrets..." -ForegroundColor Yellow
$secretsFound = Select-String -Path "*.py" -Pattern "sk-" -Exclude "venv" -Recurse 2>$null
if ($secretsFound) {
    Write-Host "  ⚠️  WARNING: Possible API keys found in code!" -ForegroundColor Red
} else {
    Write-Host "  ✅ No obvious hardcoded secrets found" -ForegroundColor Green
}
Write-Host ""

Write-Host "======================================" -ForegroundColor Cyan
Write-Host "📋 Manual Checks Required:" -ForegroundColor Cyan
Write-Host ""
Write-Host "1. [ ] Verify all API keys are in .env (not in code)"
Write-Host "2. [ ] Test app locally: streamlit run main.py"
Write-Host "3. [ ] Commit changes: git add . && git commit -m 'message'"
Write-Host "4. [ ] Push to GitHub: git push"
Write-Host "5. [ ] Add secrets in Streamlit Cloud dashboard"
Write-Host "6. [ ] Deploy on share.streamlit.io"
Write-Host ""
Write-Host "See README_DEPLOYMENT.md for detailed instructions"
Write-Host "======================================" -ForegroundColor Cyan
