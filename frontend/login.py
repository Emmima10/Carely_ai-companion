"""
Login UI component for Streamlit
"""
import streamlit as st
from datetime import datetime, date
from typing import Optional
import json

from app.auth.auth_repository import AuthRepository, create_or_update_profile
from app.database.crud import UserCRUD


def show_login_page():
    """Display login/signup page with dashboard-matching styling"""
    st.markdown("""
        <style>
        /* Import matching fonts */
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&family=Inter:wght@400;500;600;700&display=swap');
        
        /* Match dashboard background */
        .stApp {
            background: linear-gradient(135deg, 
                #FFF5F7 0%,    /* Very light pink */
                #FFF9F5 25%,   /* Very light peach */
                #FFFEF5 50%,   /* Very light cream */
                #F5FFFA 75%,   /* Mint cream */
                #F8F5FF 100%   /* Very light lavender */
            ) !important;
            background-attachment: fixed !important;
        }
        
        /* Login container with card styling */
        .login-container {
            max-width: 550px;
            margin: 1rem auto;
            padding: 2rem;
            background: #FFFFFF;
            border-radius: 20px;
            box-shadow: 0 8px 24px rgba(0, 0, 0, 0.12);
        }
        
        /* Match dashboard input styling */
        .stTextInput > div > div > input {
            border-radius: 12px !important;
            border: 2px solid #E3F2FD !important;
            padding: 0.75rem 1rem !important;
            font-size: 1rem !important;
            font-family: 'Inter', sans-serif !important;
            transition: all 0.3s ease !important;
        }
        
        .stTextInput > div > div > input:focus {
            border-color: #667EEA !important;
            box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1) !important;
        }
        
        /* Primary button styling - purple gradient matching dashboard */
        .stButton > button[kind="primary"] {
            background: linear-gradient(135deg, #667EEA 0%, #764BA2 100%) !important;
            color: white !important;
            border: none !important;
            border-radius: 12px !important;
            padding: 0.75rem 2rem !important;
            font-size: 1.1rem !important;
            font-weight: 700 !important;
            font-family: 'Poppins', sans-serif !important;
            box-shadow: 0 4px 12px rgba(102, 126, 234, 0.3) !important;
            transition: all 0.3s ease !important;
        }
        
        .stButton > button[kind="primary"]:hover {
            background: linear-gradient(135deg, #5568D3 0%, #654A8F 100%) !important;
            box-shadow: 0 6px 16px rgba(102, 126, 234, 0.4) !important;
            transform: translateY(-2px) !important;
        }
        
        /* Tab styling - clean and minimal */
        .stTabs [data-baseweb="tab-list"] {
            gap: 0;
            background: transparent;
            border-bottom: 2px solid #E0E0E0;
        }
        
        .stTabs [data-baseweb="tab"] {
            padding: 0.75rem 1.5rem !important;
            font-family: 'Poppins', sans-serif !important;
            font-weight: 600 !important;
            font-size: 1.05rem !important;
            color: #636E72 !important;
            background: transparent !important;
            border-bottom: 3px solid transparent !important;
        }
        
        .stTabs [aria-selected="true"] {
            color: #667EEA !important;
            border-bottom: 3px solid #667EEA !important;
        }
        
        /* Checkbox styling - ensure text is visible */
        .stCheckbox {
            font-family: 'Inter', sans-serif !important;
        }
        
        .stCheckbox label {
            color: #2D3436 !important;
            font-size: 0.95rem !important;
        }
        
        .stCheckbox p {
            color: #2D3436 !important;
        }
        
        /* Date input styling */
        .stDateInput > div > div > input,
        .stDateInput input,
        input[type="date"] {
            border-radius: 12px !important;
            border: 2px solid #E3F2FD !important;
            background-color: #FFFFFF !important;
            color: #2D3436 !important;
            -webkit-text-fill-color: #2D3436 !important;
        }
        
        /* Date calendar popup */
        [data-baseweb="calendar"] {
            background-color: #FFFFFF !important;
        }
        
        [data-baseweb="calendar"] * {
            background-color: #FFFFFF !important;
            color: #2D3436 !important;
        }
        
        /* Selectbox styling */
        .stSelectbox > div > div {
            border-radius: 12px !important;
            border: 2px solid #E3F2FD !important;
            background-color: #FFFFFF !important;
            color: #2D3436 !important;
        }
        
        /* Universal input override */
        div[data-baseweb="input"],
        [data-baseweb="input"] input,
        input:not([type="checkbox"]):not([type="radio"]) {
            background-color: #FFFFFF !important;
            color: #2D3436 !important;
            -webkit-text-fill-color: #2D3436 !important;
        }
        
        /* Info box styling */
        .stAlert {
            border-radius: 12px !important;
            font-family: 'Inter', sans-serif !important;
        }
        
        /* Header text colors matching dashboard */
        h1, h2, h3 {
            font-family: 'Poppins', sans-serif !important;
        }
        </style>
    """, unsafe_allow_html=True)
    
    # Display Carely logo (same as dashboard)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image("Logo.png", use_container_width=True)
    
    # Subtitle below logo
    st.markdown("""
        <p style='text-align: center;
                  font-size: 1.2rem; 
                  color: #636E72; 
                  font-family: Inter, sans-serif; 
                  font-weight: 500;
                  margin: 0.5rem 0 2rem 0;'>
            Your caring AI companion
        </p>
    """, unsafe_allow_html=True)
    
    st.markdown("<div class='login-container'>", unsafe_allow_html=True)
    
    # Tabs for login and create account
    tab1, tab2 = st.tabs(["🔐 Log In", "✨ Create Account"])
    
    with tab1:
        show_login_form()
    
    with tab2:
        show_create_account_form()
    
    st.markdown("</div>", unsafe_allow_html=True)


def show_login_form():
    """Display login form"""
    st.markdown("""
        <div style='margin-bottom: 1.5rem;'>
            <h2 style='color: #2D3436; font-size: 1.6rem; font-weight: 700; margin-bottom: 0.3rem;'>
                Welcome back! 👋
            </h2>
            <p style='color: #636E72; font-size: 1rem; margin: 0;'>
                Log in to continue to your dashboard
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    with st.form("login_form"):
        email = st.text_input("Email", placeholder="your.email@example.com")
        passcode = st.text_input("Passcode", type="password", placeholder="Enter your passcode")
        
        submit = st.form_submit_button("Log In", use_container_width=True, type="primary")
        
        if submit:
            if not email or not passcode:
                st.error("Please enter both email and passcode")
                return
            
            # Validate credentials
            account = AuthRepository.get_account_by_email(email.lower().strip())
            
            if not account:
                st.error("Invalid email or passcode")
                return
            
            if not AuthRepository.verify_passcode(passcode, account.passcode_hash):
                st.error("Invalid email or passcode")
                return
            
            # Successful login
            session_token = AuthRepository.create_session_token(account.id)
            AuthRepository.update_last_login(account.id)
            
            # Store in session state
            st.session_state.session_token = session_token
            st.session_state.account_id = account.id
            st.session_state.logged_in = True
            
            # Get user profile
            if account.user_id:
                user = UserCRUD.get_user(account.user_id)
                if user:
                    st.session_state.user_id = user.id
                    st.session_state.user_name = user.name
                    
                    # Load timezone from preferences
                    if user.preferences:
                        try:
                            prefs = json.loads(user.preferences) if isinstance(user.preferences, str) else user.preferences
                            st.session_state.timezone = prefs.get('timezone', 'America/Chicago')
                        except:
                            st.session_state.timezone = 'America/Chicago'
                    else:
                        st.session_state.timezone = 'America/Chicago'
            
            # Check if onboarding is complete
            if not account.onboarding_completed:
                st.session_state.show_onboarding = True
            
            st.success(f"Welcome back! Redirecting...")
            st.rerun()


def show_create_account_form():
    """Display account creation form"""
    st.markdown("""
        <div style='margin-bottom: 1.5rem;'>
            <h2 style='color: #2D3436; font-size: 1.6rem; font-weight: 700; margin-bottom: 0.3rem;'>
                Create your account ✨
            </h2>
            <p style='color: #636E72; font-size: 1rem; margin: 0;'>
                Join Carely to start your personalized care journey
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    with st.form("create_account_form"):
        email = st.text_input("Email *", placeholder="your.email@example.com")
        
        col1, col2 = st.columns(2)
        with col1:
            display_name = st.text_input("Display Name", placeholder="Optional (uses email prefix)")
        with col2:
            timezone = st.selectbox("Timezone *", 
                                   ["America/Chicago", "America/New_York", "America/Los_Angeles", 
                                    "America/Denver", "America/Phoenix"],
                                   index=0)
        
        # Date of birth
        dob = st.date_input("Date of Birth *", 
                           min_value=date(1920, 1, 1),
                           max_value=date.today(),
                           value=date(1950, 1, 1))
        
        # Calculate age
        today = date.today()
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
        st.info(f"Age: {age} years")
        
        passcode = st.text_input("Passcode *", type="password", 
                                placeholder="Create a secure passcode")
        passcode_confirm = st.text_input("Confirm Passcode *", type="password",
                                        placeholder="Re-enter your passcode")
        
        st.markdown("---")
        
        # Consent checkboxes
        consent_terms = st.checkbox(
            "I agree to the Terms of Service and understand that Carely is not a substitute for medical advice *",
            value=False
        )
        
        consent_metrics = st.checkbox(
            "I consent to anonymous usage metrics to help improve the service (optional)",
            value=True
        )
        
        st.markdown("*Required fields")
        
        submit = st.form_submit_button("Create Account", use_container_width=True, type="primary")
        
        if submit:
            # Validation
            if not email or not passcode:
                st.error("Please fill in all required fields")
                return
            
            if not consent_terms:
                st.error("You must agree to the Terms of Service to continue")
                return
            
            if passcode != passcode_confirm:
                st.error("Passcodes do not match")
                return
            
            if len(passcode) < 6:
                st.error("Passcode must be at least 6 characters")
                return
            
            # Create account
            email_clean = email.lower().strip()
            
            # Check if account exists
            existing = AuthRepository.get_account_by_email(email_clean)
            if existing:
                st.error("An account with this email already exists")
                return
            
            # Create account
            account = AuthRepository.create_account(email_clean, passcode, "demo")
            
            if not account:
                st.error("Failed to create account. Please try again.")
                return
            
            # Create user profile
            profile_data = {
                'name': display_name or email_clean.split('@')[0],
                'email': email_clean,
                'preferences': {
                    'timezone': timezone,
                    'date_of_birth': dob.isoformat(),
                    'age': age,
                    'consent_terms': consent_terms,
                    'consent_metrics': consent_metrics
                }
            }
            
            user = create_or_update_profile(account.id, profile_data)
            
            # Create session
            session_token = AuthRepository.create_session_token(account.id)
            
            # Store in session state
            st.session_state.session_token = session_token
            st.session_state.account_id = account.id
            st.session_state.user_id = user.id
            st.session_state.user_name = user.name
            st.session_state.timezone = timezone
            st.session_state.logged_in = True
            st.session_state.show_onboarding = True
            
            st.success("Account created successfully! Redirecting to onboarding...")
            st.rerun()


def check_authentication():
    """
    Check if user is authenticated
    Returns True if authenticated, False otherwise
    """
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False
    
    if 'session_token' not in st.session_state:
        return False
    
    # Validate session token
    account_id = AuthRepository.validate_session_token(st.session_state.session_token)
    
    if not account_id:
        # Invalid token, clear session
        clear_session()
        return False
    
    # Ensure account_id is set
    if 'account_id' not in st.session_state:
        st.session_state.account_id = account_id
    
    return True


def clear_session():
    """Clear session state and log out"""
    if 'session_token' in st.session_state:
        AuthRepository.invalidate_session_token(st.session_state.session_token)
    
    # Clear all auth-related session state
    keys_to_clear = ['session_token', 'account_id', 'user_id', 'user_name', 
                     'logged_in', 'show_onboarding', 'timezone']
    
    for key in keys_to_clear:
        if key in st.session_state:
            del st.session_state[key]


def show_logout_button():
    """Display logout button in sidebar with matching purple gradient styling"""
    # Add CSS for logout button to match Chat section buttons
    st.sidebar.markdown("""
        <style>
        /* Style logout button with purple gradient matching Quick Actions */
        div[data-testid="stSidebar"] button[kind="secondary"] {
            background: linear-gradient(135deg, #667EEA 0%, #764BA2 100%) !important;
            color: white !important;
            border: none !important;
            font-weight: 700 !important;
            font-size: 1.1rem !important;
            transition: all 0.3s ease !important;
            box-shadow: 0 2px 4px rgba(102, 126, 234, 0.2) !important;
        }
        
        div[data-testid="stSidebar"] button[kind="secondary"]:hover {
            background: linear-gradient(135deg, #5568D3 0%, #654A8F 100%) !important;
            box-shadow: 0 4px 8px rgba(102, 126, 234, 0.3) !important;
            transform: translateY(-2px) !important;
        }
        
        div[data-testid="stSidebar"] button[kind="secondary"]:active {
            transform: translateY(0px) !important;
        }
        </style>
    """, unsafe_allow_html=True)
    
    if st.sidebar.button("🚪 Log Out", use_container_width=True):
        clear_session()
        st.rerun()
