"""
Multi-step onboarding wizard for new users
"""
import streamlit as st
from datetime import datetime, date, time
import json
import os

from app.database.crud import UserCRUD, MedicationCRUD, PersonalEventCRUD, CaregiverPatientCRUD
from app.auth.auth_repository import AuthRepository, create_or_update_profile
from utils.timezone_utils import now_central, to_central


def show_onboarding_wizard():
    """Display multi-step onboarding wizard"""
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
        
        .onboarding-container {
            max-width: 800px;
            margin: 0 auto;
            padding: 2rem;
        }
        
        .step-indicator {
            display: flex;
            justify-content: space-between;
            margin-bottom: 2rem;
        }
        
        .step {
            flex: 1;
            text-align: center;
            padding: 1rem;
            border-radius: 12px;
            background: #FFFFFF;
            margin: 0 0.5rem;
            border: 2px solid #E3F2FD;
            font-family: 'Poppins', sans-serif;
            transition: all 0.3s ease;
        }
        
        .step.active {
            background: linear-gradient(135deg, #667EEA 0%, #764BA2 100%);
            color: white;
            font-weight: bold;
            box-shadow: 0 4px 12px rgba(102, 126, 234, 0.3);
            border-color: transparent;
        }
        
        .step.completed {
            background: linear-gradient(135deg, #27AE60 0%, #2ECC71 100%);
            color: white;
            border-color: transparent;
            box-shadow: 0 2px 8px rgba(39, 174, 96, 0.3);
        }
        
        /* Match dashboard input styling */
        .stTextInput > div > div > input {
            border-radius: 12px !important;
            border: 2px solid #E3F2FD !important;
            background-color: #FFFFFF !important;
            color: #2D3436 !important;
            padding: 0.75rem 1rem !important;
            font-size: 1rem !important;
            font-family: 'Inter', sans-serif !important;
        }
        
        .stTextInput > div > div > input:focus {
            border-color: #667EEA !important;
            box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1) !important;
        }
        
        /* Input labels */
        .stTextInput label, .stSelectbox label, .stTimeInput label, .stDateInput label {
            color: #2D3436 !important;
            font-weight: 600 !important;
            font-size: 0.95rem !important;
        }
        
        /* Primary button styling */
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
        
        /* Secondary button styling */
        .stButton > button[kind="secondary"] {
            border-radius: 12px !important;
            border: 2px solid #667EEA !important;
            background-color: #FFFFFF !important;
            color: #667EEA !important;
            font-weight: 600 !important;
            font-family: 'Poppins', sans-serif !important;
        }
        
        /* Selectbox styling */
        .stSelectbox > div > div {
            border-radius: 12px !important;
            border: 2px solid #E3F2FD !important;
            background-color: #FFFFFF !important;
        }
        
        .stSelectbox > div > div > div {
            color: #2D3436 !important;
            background-color: #FFFFFF !important;
        }
        
        /* ===== COMPREHENSIVE DROPDOWN STYLING ===== */
        /* Target all possible dropdown/popover containers */
        [data-baseweb="popover"],
        [data-baseweb="menu"],
        [data-baseweb="select"] [role="listbox"],
        div[role="listbox"],
        ul[role="listbox"] {
            background-color: #FFFFFF !important;
            border: 1px solid #E3F2FD !important;
            border-radius: 8px !important;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1) !important;
        }
        
        /* All dropdown options */
        [role="option"],
        li[role="option"],
        div[role="option"] {
            background-color: #FFFFFF !important;
            color: #2D3436 !important;
            padding: 0.5rem 1rem !important;
            font-size: 0.95rem !important;
        }
        
        /* Hover state for options */
        [role="option"]:hover,
        li[role="option"]:hover,
        div[role="option"]:hover {
            background-color: #F0F4FF !important;
            color: #2D3436 !important;
        }
        
        /* Selected option */
        [role="option"][aria-selected="true"],
        li[role="option"][aria-selected="true"],
        div[role="option"][aria-selected="true"] {
            background-color: #E3F2FD !important;
            color: #2D3436 !important;
            font-weight: 600 !important;
        }
        
        /* Selectbox specific */
        .stSelectbox [data-baseweb="popover"] {
            background-color: #FFFFFF !important;
        }
        
        .stSelectbox [data-baseweb="select"] {
            background-color: #FFFFFF !important;
        }
        
        .stSelectbox div[data-baseweb="select"] span,
        .stSelectbox div[data-baseweb="select"] div {
            color: #2D3436 !important;
        }
        
        /* Dropdown panel content */
        [data-baseweb="popover"] > div,
        [data-baseweb="menu"] > div,
        [data-baseweb="menu"] ul {
            background-color: #FFFFFF !important;
        }
        
        /* Time input styling */
        .stTimeInput > div > div > input {
            border-radius: 12px !important;
            border: 2px solid #E3F2FD !important;
            background-color: #FFFFFF !important;
            color: #2D3436 !important;
        }
        
        /* Time picker dropdown */
        .stTimeInput [data-baseweb="popover"] {
            background-color: #FFFFFF !important;
        }
        
        .stTimeInput [role="listbox"] {
            background-color: #FFFFFF !important;
            border: 1px solid #E3F2FD !important;
        }
        
        .stTimeInput [role="option"] {
            background-color: #FFFFFF !important;
            color: #2D3436 !important;
        }
        
        .stTimeInput [role="option"]:hover {
            background-color: #F0F4FF !important;
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
        .stDateInput [data-baseweb="popover"],
        .stDateInput [data-baseweb="calendar"],
        [data-baseweb="calendar"] {
            background-color: #FFFFFF !important;
            border: 2px solid #E3F2FD !important;
        }
        
        [data-baseweb="calendar"] * {
            background-color: #FFFFFF !important;
            color: #2D3436 !important;
        }
        
        [data-baseweb="calendar"] td:hover {
            background-color: #E3F2FD !important;
        }
        
        [data-baseweb="calendar"] td[aria-selected="true"] {
            background-color: #667EEA !important;
            color: white !important;
        }
        
        /* Checkbox styling */
        .stCheckbox label {
            color: #2D3436 !important;
        }
        
        /* All paragraph and text elements */
        p, div, span {
            color: #2D3436 !important;
        }
        
        /* Universal input override */
        div[data-baseweb="input"],
        div[data-baseweb="base-input"],
        [data-baseweb="input"] input {
            background-color: #FFFFFF !important;
            color: #2D3436 !important;
            -webkit-text-fill-color: #2D3436 !important;
        }
        
        input:not([type="checkbox"]):not([type="radio"]) {
            background-color: #FFFFFF !important;
            color: #2D3436 !important;
            -webkit-text-fill-color: #2D3436 !important;
        }
        
        h1, h2, h3 {
            font-family: 'Poppins', sans-serif !important;
        }
        </style>
    """, unsafe_allow_html=True)
    
    # Initialize onboarding step
    if 'onboarding_step' not in st.session_state:
        st.session_state.onboarding_step = 1
    
    st.markdown("<div class='onboarding-container'>", unsafe_allow_html=True)
    
    # Header with gradient matching dashboard
    st.markdown("""
        <div style='background: linear-gradient(135deg, #667EEA 0%, #764BA2 100%);
                    text-align: center; 
                    margin: -1rem -1rem 1.5rem -1rem; 
                    padding: 1.5rem 1rem 1.5rem 1rem;
                    border-radius: 0 0 24px 24px;
                    box-shadow: 0 8px 24px rgba(102, 126, 234, 0.15);'>
        </div>
    """, unsafe_allow_html=True)
    
    # Display Carely logo (same as dashboard)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image("Logo.png", use_container_width=True)
    
    # Welcome message below logo
    st.markdown("""
        <h2 style='text-align: center;
                   color: #2D3436; 
                   font-size: 2rem; 
                   font-weight: 700; 
                   font-family: Poppins, sans-serif; 
                   margin: 1rem 0 0.5rem 0;'>
            Welcome to Carely! 🎉
        </h2>
        <p style='text-align: center;
                  font-size: 1.2rem; 
                  color: #636E72; 
                  font-family: Inter, sans-serif; 
                  font-weight: 500;
                  margin: 0 0 1.5rem 0;'>
            Let's set up your personalized care experience
        </p>
    """, unsafe_allow_html=True)
    
    # Step indicator
    show_step_indicator(st.session_state.onboarding_step)
    
    # Display appropriate step
    if st.session_state.onboarding_step == 1:
        show_step_1_profile()
    elif st.session_state.onboarding_step == 2:
        show_step_2_caregiver()
    elif st.session_state.onboarding_step == 3:
        show_step_3_medications_events()
    
    st.markdown("</div>", unsafe_allow_html=True)


def show_step_indicator(current_step: int):
    """Display step progress indicator"""
    steps = [
        ("1", "Profile"),
        ("2", "Caregiver"),
        ("3", "Health Info")
    ]
    
    cols = st.columns(len(steps))
    
    for idx, (col, (num, label)) in enumerate(zip(cols, steps), 1):
        with col:
            if idx < current_step:
                st.markdown(f"<div class='step completed'>✓ {label}</div>", unsafe_allow_html=True)
            elif idx == current_step:
                st.markdown(f"<div class='step active'>{num}. {label}</div>", unsafe_allow_html=True)
            else:
                st.markdown(f"<div class='step'>{num}. {label}</div>", unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)


def show_step_1_profile():
    """Step 1: Basic Profile & Consent"""
    st.markdown("### Step 1: Your Profile")
    st.markdown("Tell us a bit about yourself")
    
    # Get current account
    account = AuthRepository.get_account_by_id(st.session_state.account_id)
    
    # Get existing user if available
    user = None
    if account and account.user_id:
        user = UserCRUD.get_user(account.user_id)
    
    # Pre-fill with existing data
    default_name = user.name if user else account.email.split('@')[0]
    default_timezone = st.session_state.get('timezone', 'America/Chicago')
    
    # Get DOB from preferences if available
    default_dob = date(1950, 1, 1)
    if user and user.preferences:
        try:
            prefs = json.loads(user.preferences) if isinstance(user.preferences, str) else user.preferences
            dob_str = prefs.get('date_of_birth')
            if dob_str:
                default_dob = date.fromisoformat(dob_str)
        except:
            pass
    
    with st.form("profile_form"):
        display_name = st.text_input("Display Name *", value=default_name)
        
        timezone = st.selectbox("Timezone *", 
                               ["America/Chicago", "America/New_York", "America/Los_Angeles", 
                                "America/Denver", "America/Phoenix"],
                               index=0 if default_timezone == "America/Chicago" else 
                                     ["America/Chicago", "America/New_York", "America/Los_Angeles", 
                                      "America/Denver", "America/Phoenix"].index(default_timezone)
                                     if default_timezone in ["America/Chicago", "America/New_York", 
                                                            "America/Los_Angeles", "America/Denver", 
                                                            "America/Phoenix"] else 0)
        
        dob = st.date_input("Date of Birth *", 
                           value=default_dob,
                           min_value=date(1920, 1, 1),
                           max_value=date.today())
        
        # Calculate and display age
        today = date.today()
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
        st.info(f"Age: {age} years")
        
        st.markdown("---")
        
        consent_terms = st.checkbox(
            "I understand that Carely is not a substitute for professional medical advice *",
            value=True
        )
        
        col1, col2 = st.columns([1, 1])
        with col1:
            if st.form_submit_button("← Back to Login"):
                st.session_state.show_onboarding = False
                st.rerun()
        
        with col2:
            submit = st.form_submit_button("Next →", type="primary", use_container_width=True)
        
        if submit:
            if not display_name or not consent_terms:
                st.error("Please fill in all required fields and accept the terms")
                return
            
            # Save profile
            profile_data = {
                'name': display_name,
                'email': account.email,
                'preferences': {
                    'timezone': timezone,
                    'date_of_birth': dob.isoformat(),
                    'age': age,
                    'consent_terms': consent_terms
                }
            }
            
            user = create_or_update_profile(st.session_state.account_id, profile_data)
            
            # Update session state
            st.session_state.user_id = user.id
            st.session_state.user_name = user.name
            st.session_state.timezone = timezone
            
            # Move to next step
            st.session_state.onboarding_step = 2
            st.rerun()


def show_step_2_caregiver():
    """Step 2: Caregiver Contact (Optional)"""
    st.markdown("### Step 2: Caregiver Contact")
    st.markdown("Add a caregiver who can receive alerts and updates (optional)")
    
    # Get defaults from environment
    default_telegram_token = os.getenv("TELEGRAM_BOT_TOKEN", "")
    default_telegram_chat_id = os.getenv("TELEGRAM_CHAT_ID", "")
    
    with st.form("caregiver_form"):
        st.markdown("**Caregiver Information**")
        
        caregiver_name = st.text_input("Caregiver Name", placeholder="e.g., John Smith")
        
        contact_channel = st.selectbox("Contact Channel", 
                                      ["Telegram", "Email", "SMS"],
                                      index=0)
        
        if contact_channel == "Telegram":
            col1, col2 = st.columns(2)
            with col1:
                telegram_token = st.text_input("Telegram Bot Token", 
                                              value=default_telegram_token,
                                              placeholder="From @BotFather")
            with col2:
                telegram_chat_id = st.text_input("Telegram Chat ID",
                                                value=default_telegram_chat_id,
                                                placeholder="Your chat ID")
        else:
            caregiver_contact = st.text_input("Contact Information", 
                                            placeholder="Email or phone number")
        
        st.markdown("---")
        
        col1, col2, col3 = st.columns([1, 1, 1])
        
        with col1:
            if st.form_submit_button("← Previous"):
                st.session_state.onboarding_step = 1
                st.rerun()
        
        with col2:
            skip = st.form_submit_button("Skip", use_container_width=True)
        
        with col3:
            submit = st.form_submit_button("Next →", type="primary", use_container_width=True)
        
        if skip:
            st.session_state.onboarding_step = 3
            st.rerun()
        
        if submit:
            # Save caregiver if provided
            if caregiver_name:
                # Create caregiver user
                caregiver_email = f"caregiver_{st.session_state.user_id}@carely.local"
                
                caregiver_user = UserCRUD.create_user(
                    name=caregiver_name,
                    email=caregiver_email,
                    user_type="caregiver",
                    preferences={
                        'contact_channel': contact_channel,
                        'telegram_token': telegram_token if contact_channel == "Telegram" else None,
                        'telegram_chat_id': telegram_chat_id if contact_channel == "Telegram" else None
                    }
                )
                
                # Link caregiver to patient
                if caregiver_user:
                    CaregiverPatientCRUD.assign_patient(
                        caregiver_id=caregiver_user.id,
                        patient_id=st.session_state.user_id,
                        relationship="family",
                        notification_preferences={'alerts': True, 'weekly_reports': True}
                    )
                    
                    st.success(f"Caregiver {caregiver_name} added successfully!")
            
            st.session_state.onboarding_step = 3
            st.rerun()


def show_step_3_medications_events():
    """Step 3: Medications & Personal Events (Optional)"""
    st.markdown("### Step 3: Health Information")
    st.markdown("Add your medications and important events (optional)")
    
    # Tabs for medications and events
    tab1, tab2 = st.tabs(["💊 Medications", "📅 Personal Events"])
    
    with tab1:
        show_medication_form()
    
    with tab2:
        show_events_form()
    
    st.markdown("---")
    
    col1, col2, col3 = st.columns([1, 1, 1])
    
    with col1:
        if st.button("← Previous", use_container_width=True):
            st.session_state.onboarding_step = 2
            st.rerun()
    
    with col2:
        if st.button("Skip", use_container_width=True):
            complete_onboarding()
    
    with col3:
        if st.button("Finish ✓", type="primary", use_container_width=True):
            complete_onboarding()


def show_medication_form():
    """Display medication entry form"""
    st.markdown("**Add Medications**")
    
    with st.form("medication_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            med_name = st.text_input("Medication Name *", placeholder="e.g., Lisinopril")
            dose = st.text_input("Dose", placeholder="e.g., 10mg")
            frequency = st.selectbox("Frequency", ["daily", "twice_daily", "weekly", "as_needed"])
        
        with col2:
            reminder_time = st.time_input("Reminder Time *", value=time(9, 0))
            timezone = st.selectbox("Timezone", 
                                   [st.session_state.get('timezone', 'America/Chicago')],
                                   index=0)
            active = st.checkbox("Active", value=True)
        
        instructions = st.text_area("Instructions", placeholder="Optional instructions for taking this medication")
        
        submit = st.form_submit_button("Add Medication", use_container_width=True)
        
        if submit:
            if not med_name or not reminder_time:
                st.error("Please provide medication name and reminder time")
                return
            
            # Verify user_id exists in session
            if 'user_id' not in st.session_state or not st.session_state.user_id:
                st.error("Session error: User ID not found. Please complete Step 1 first.")
                return
            
            # Convert time to schedule times list
            schedule_times = [reminder_time.strftime("%H:%M")]
            if frequency == "twice_daily":
                # Add second time 12 hours later
                second_hour = (reminder_time.hour + 12) % 24
                schedule_times.append(f"{second_hour:02d}:{reminder_time.minute:02d}")
            
            try:
                # Create medication (schedule_times should be a list, not JSON string)
                MedicationCRUD.create_medication(
                    user_id=st.session_state.user_id,
                    name=med_name,
                    dosage=dose,
                    frequency=frequency,
                    schedule_times=schedule_times,
                    instructions=instructions
                )
                
                st.success(f"Medication '{med_name}' added successfully!")
                st.rerun()
            except Exception as e:
                st.error(f"Failed to save medication: {str(e)}")
    
    # Display existing medications
    medications = MedicationCRUD.get_user_medications(st.session_state.user_id)
    if medications:
        st.markdown("**Your Medications:**")
        for med in medications:
            with st.expander(f"💊 {med.name} - {med.dosage}"):
                st.write(f"**Frequency:** {med.frequency}")
                st.write(f"**Schedule:** {med.schedule_times}")
                if med.instructions:
                    st.write(f"**Instructions:** {med.instructions}")
                st.write(f"**Status:** {'Active' if med.active else 'Inactive'}")


def show_events_form():
    """Display personal events entry form"""
    st.markdown("**Add Personal Events**")
    
    with st.form("event_form"):
        title = st.text_input("Event Title *", placeholder="e.g., Doctor's Appointment")
        
        col1, col2 = st.columns(2)
        with col1:
            event_date = st.date_input("Date *", min_value=date.today())
            event_time = st.time_input("Time *", value=time(10, 0))
        
        with col2:
            importance = st.selectbox("Importance", ["low", "medium", "high"], index=1)
            event_type = st.selectbox("Type", 
                                     ["appointment", "medication", "family_event", 
                                      "birthday", "hobby", "health"],
                                     index=0)
        
        notes = st.text_area("Notes", placeholder="Optional notes about this event")
        
        recurrence = st.selectbox("Recurrence", 
                                 ["None", "Daily", "Weekly", "Monthly"],
                                 index=0)
        
        submit = st.form_submit_button("Add Event", use_container_width=True)
        
        if submit:
            if not title:
                st.error("Please provide an event title")
                return
            
            # Verify user_id exists in session
            if 'user_id' not in st.session_state or not st.session_state.user_id:
                st.error("Session error: User ID not found. Please complete Step 1 first.")
                return
            
            # Combine date and time
            event_datetime = datetime.combine(event_date, event_time)
            
            try:
                # Create event
                PersonalEventCRUD.create_event(
                    user_id=st.session_state.user_id,
                    event_type=event_type,
                    title=title,
                    description=notes,
                    event_date=event_datetime,
                    recurring=(recurrence != "None"),
                    importance=importance
                )
                
                st.success(f"Event '{title}' added successfully!")
                st.rerun()
            except Exception as e:
                st.error(f"Failed to save event: {str(e)}")
    
    # Display existing events
    events = PersonalEventCRUD.get_upcoming_events(st.session_state.user_id, days=30)
    if events:
        st.markdown("**Your Upcoming Events:**")
        for event in events[:5]:  # Show first 5
            event_time_str = event.event_date.strftime("%b %d, %Y at %I:%M %p") if event.event_date else "No date"
            with st.expander(f"📅 {event.title} - {event_time_str}"):
                st.write(f"**Type:** {event.event_type}")
                st.write(f"**Importance:** {event.importance}")
                if event.description:
                    st.write(f"**Notes:** {event.description}")


def complete_onboarding():
    """Complete onboarding and redirect to main app"""
    # Mark onboarding as complete
    AuthRepository.mark_onboarding_complete(st.session_state.account_id)
    
    # Clear onboarding flags
    st.session_state.show_onboarding = False
    if 'onboarding_step' in st.session_state:
        del st.session_state.onboarding_step
    
    st.success("🎉 Onboarding complete! Welcome to Carely!")
    st.rerun()
