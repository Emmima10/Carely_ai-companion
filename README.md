# 🩺 CarelyAI - AI Companion for Elderly Care

An intelligent, empathetic AI companion designed to support elderly individuals with daily wellness checks, medication reminders, emotional support, and emergency detection.

## ✨ Features

- **💬 Conversational AI**: Natural language chat powered by Groq LLaMA
- **💊 Medication Management**: Track medications, set reminders, and log doses
- **📅 Schedule Management**: Personal events, appointments, and reminders
- **🧠 Multi-Layer Memory System**: 
  - Short-term memory for recent conversations
  - Long-term memory with vector embeddings
  - Episodic memory for important life events
  - Structured memory for medications and schedules
- **🚨 Emergency Detection**: Intelligent detection of health emergencies with caregiver alerts
- **📊 Health Analytics**: Mood tracking, medication adherence, conversation insights
- **🎵 Entertainment**: Music recommendations, jokes, puzzles, memory games
- **👨‍⚕️ Caregiver Dashboard**: Monitor patient wellness and receive alerts
- **🔒 Secure Authentication**: Role-based access control for patients and caregivers

## 🚀 Quick Start

### Prerequisites
- Python 3.9 or higher
- Groq API key (get one at [console.groq.com](https://console.groq.com))
- (Optional) Telegram Bot for emergency alerts

### Local Installation

1. **Clone the repository**
```bash
git clone https://github.com/YOUR_USERNAME/CarelyAI.git
cd CarelyAI
```

2. **Create virtual environment**
```bash
python -m venv venv

# Windows
.\venv\Scripts\Activate.ps1

# Mac/Linux
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Set up environment variables**

Create a `.env` file in the root directory:
```env
GROQ_API_KEY=your_groq_api_key_here
TELEGRAM_BOT_TOKEN=your_telegram_bot_token_here  # Optional
TELEGRAM_CHAT_ID=your_telegram_chat_id_here      # Optional
```

5. **Run the application**
```bash
streamlit run main.py
```

The app will open in your browser at `http://localhost:8501`

### Demo Accounts

The app includes pre-seeded demo accounts:

**Patient Account:**
- Email: `dorothy@example.com`
- Passcode: `1234`

**Caregiver Account:**
- Email: `alice@caregiver.com`
- Passcode: `5678`

## 🌐 Streamlit Cloud Deployment

See [README_DEPLOYMENT.md](README_DEPLOYMENT.md) for complete deployment instructions.

**Quick Deploy:**
1. Push code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your repository
4. Add secrets in Streamlit dashboard
5. Deploy!

## 📁 Project Structure

```
CarelyAI/
├── app/
│   ├── agents/          # AI companion agent logic
│   ├── api/             # FastAPI endpoints (optional)
│   ├── auth/            # Authentication system
│   ├── database/        # Database models and CRUD
│   ├── memory/          # Multi-layer memory system
│   ├── scheduling/      # Reminder scheduler
│   └── styles/          # UI themes and styling
├── frontend/
│   ├── dashboard.py     # Main patient dashboard
│   ├── login.py         # Authentication UI
│   └── onboarding.py    # New user onboarding
├── utils/
│   ├── pii_redaction.py        # Privacy protection
│   ├── sentiment_analysis.py   # Mood detection
│   ├── telegram_notification.py # Emergency alerts
│   └── timezone_utils.py       # Time management
├── data/
│   └── sample_data.py   # Demo data seeder
├── .streamlit/
│   └── config.toml      # Streamlit configuration
├── main.py              # Application entry point
└── requirements.txt     # Python dependencies
```

## 🛠️ Technology Stack

- **Frontend**: Streamlit
- **AI Model**: Groq LLaMA 3.3 70B
- **Database**: SQLite (SQLModel ORM)
- **Vector Store**: ChromaDB
- **Scheduling**: APScheduler
- **Notifications**: Telegram Bot API
- **Audio**: gTTS, Streamlit Mic Recorder

## 🔐 Security & Privacy

- **PII Detection**: Automatic detection and redaction of sensitive information
- **Secure Authentication**: Bcrypt password hashing
- **Data Privacy**: Personal health information is protected
- **Environment Variables**: Sensitive credentials stored securely

## 📊 Key Components

### AI Companion Agent
- Natural language understanding
- Context-aware responses with memory
- Emergency detection and caregiver alerts
- Medication logging and reminders

### Memory System
- **Short-term**: Recent conversation context (last 5 exchanges)
- **Long-term**: Vector similarity search for relevant past conversations
- **Episodic**: Important life events and milestones
- **Structured**: Medications, schedules, preferences

### Emergency Detection
- Keyword-based symptom detection
- Severity classification (Critical, Concerning, Manageable)
- Automatic caregiver notifications via Telegram
- Safety check workflow

### Health Analytics
- Mood trend analysis with sentiment scoring
- Medication adherence tracking
- Conversation pattern insights
- Personalized health recommendations

## 🧪 Development

### Running Tests
```bash
python -m pytest
```

### Code Quality
```bash
# Format code
black .

# Lint
flake8 .
```

## 🤝 Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📝 License

This project is for educational and demonstration purposes.

## 🙏 Acknowledgments

- Built with [Streamlit](https://streamlit.io)
- AI powered by [Groq](https://groq.com)
- Vector embeddings by [ChromaDB](https://www.trychroma.com)

## 📧 Contact

For questions or support, please open an issue on GitHub.

---

**Made with ❤️ for better elderly care**
