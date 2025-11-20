"""
Global theme and styling for Carely application
Provides consistent light theme across all pages (login, onboarding, dashboard)
"""

import streamlit as st


def apply_global_theme():
    """
    Apply global light theme styling to all Streamlit widgets
    Ensures consistency across login, onboarding, and dashboard pages
    """
    st.markdown("""
        <style>
        /* ========== GLOBAL CARELY THEME ========== */
        /* Import modern fonts */
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&family=Inter:wght@400;500;600;700&display=swap');
        
        /* Force light color scheme */
        :root {
            color-scheme: light !important;
        }
        
        /* ========== GLOBAL TEXT COLORS ========== */
        /* Ensure all text is visible on light backgrounds */
        .stApp, .stApp * {
            color: #2D3436 !important;
        }
        
        /* Override for specific elements that should stay light */
        .stButton > button[kind="primary"],
        .stButton > button[kind="primary"] * {
            color: white !important;
        }
        
        /* ========== INPUT FIELDS ========== */
        /* Text inputs, number inputs, text areas */
        .stTextInput > div > div > input,
        .stTextArea > div > div > textarea,
        .stNumberInput > div > div > input {
            background-color: #FFFFFF !important;
            color: #2D3436 !important;
            border: 2px solid #E3F2FD !important;
            border-radius: 12px !important;
            padding: 0.75rem 1rem !important;
            font-size: 1rem !important;
            font-family: 'Inter', sans-serif !important;
        }
        
        .stTextInput > div > div > input:focus,
        .stTextArea > div > div > textarea:focus,
        .stNumberInput > div > div > input:focus {
            border-color: #667EEA !important;
            box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1) !important;
            outline: none !important;
        }
        
        /* Input placeholders */
        .stTextInput input::placeholder,
        .stTextArea textarea::placeholder,
        .stNumberInput input::placeholder {
            color: #95A5A6 !important;
            opacity: 1 !important;
        }
        
        /* ========== LABELS ========== */
        /* All input labels */
        .stTextInput label,
        .stTextArea label,
        .stNumberInput label,
        .stSelectbox label,
        .stMultiselect label,
        .stDateInput label,
        .stTimeInput label,
        .stCheckbox label,
        .stRadio label {
            color: #2D3436 !important;
            font-weight: 600 !important;
            font-size: 0.95rem !important;
            font-family: 'Inter', sans-serif !important;
        }
        
        /* ========== SELECTBOX / DROPDOWN ========== */
        /* Selectbox container */
        .stSelectbox > div > div {
            background-color: #FFFFFF !important;
            border: 2px solid #E3F2FD !important;
            border-radius: 12px !important;
            color: #2D3436 !important;
        }
        
        .stSelectbox > div > div:hover {
            border-color: #667EEA !important;
        }
        
        /* Selected value text */
        .stSelectbox > div > div > div {
            color: #2D3436 !important;
        }
        
        /* ===== AGGRESSIVE DROPDOWN PANEL STYLING ===== */
        /* Target ALL possible dropdown containers */
        [data-baseweb="popover"],
        [data-baseweb="menu"],
        div[data-baseweb="popover"],
        div[data-baseweb="menu"] {
            background-color: #FFFFFF !important;
            border: 2px solid #E3F2FD !important;
            border-radius: 12px !important;
            box-shadow: 0 4px 16px rgba(0, 0, 0, 0.1) !important;
        }
        
        /* Dropdown inner content */
        [data-baseweb="popover"] > div,
        [data-baseweb="menu"] > div,
        [data-baseweb="popover"] ul,
        [data-baseweb="menu"] ul {
            background-color: #FFFFFF !important;
        }
        
        /* All listbox containers */
        div[role="listbox"],
        ul[role="listbox"],
        .stSelectbox div[role="listbox"],
        .stSelectbox ul[role="listbox"] {
            background-color: #FFFFFF !important;
            border: 2px solid #E3F2FD !important;
            border-radius: 12px !important;
            box-shadow: 0 4px 16px rgba(0, 0, 0, 0.1) !important;
        }
        
        /* ALL dropdown options - comprehensive targeting */
        [role="option"],
        div[role="option"],
        li[role="option"],
        .stSelectbox [role="option"],
        .stSelectbox div[role="option"],
        .stSelectbox li[role="option"],
        [data-baseweb="list-item"],
        div[data-baseweb="list-item"] {
            background-color: #FFFFFF !important;
            color: #2D3436 !important;
            padding: 0.75rem 1rem !important;
            font-family: 'Inter', sans-serif !important;
            font-size: 0.95rem !important;
        }
        
        /* Hovered option - ALL variants */
        [role="option"]:hover,
        div[role="option"]:hover,
        li[role="option"]:hover,
        .stSelectbox [role="option"]:hover,
        .stSelectbox div[role="option"]:hover,
        .stSelectbox li[role="option"]:hover,
        [data-baseweb="list-item"]:hover {
            background-color: #F0F4FF !important;
            color: #2D3436 !important;
        }
        
        /* Selected option - ALL variants */
        [role="option"][aria-selected="true"],
        div[role="option"][aria-selected="true"],
        li[role="option"][aria-selected="true"],
        .stSelectbox [role="option"][aria-selected="true"],
        .stSelectbox div[role="option"][aria-selected="true"],
        .stSelectbox li[role="option"][aria-selected="true"],
        [data-baseweb="list-item"][aria-selected="true"] {
            background-color: #E3F2FD !important;
            color: #667EEA !important;
            font-weight: 600 !important;
        }
        
        /* Selectbox text elements */
        .stSelectbox div[data-baseweb="select"] span,
        .stSelectbox div[data-baseweb="select"] div,
        .stSelectbox div[data-baseweb="select"] * {
            color: #2D3436 !important;
        }
        
        /* ========== MULTISELECT ========== */
        .stMultiselect > div > div {
            background-color: #FFFFFF !important;
            border: 2px solid #E3F2FD !important;
            border-radius: 12px !important;
        }
        
        .stMultiselect div[role="listbox"] {
            background-color: #FFFFFF !important;
            border: 2px solid #E3F2FD !important;
            border-radius: 12px !important;
            box-shadow: 0 4px 16px rgba(0, 0, 0, 0.1) !important;
        }
        
        .stMultiselect div[role="option"] {
            background-color: #FFFFFF !important;
            color: #2D3436 !important;
        }
        
        .stMultiselect div[role="option"]:hover {
            background-color: #F8F9FA !important;
            color: #667EEA !important;
        }
        
        /* ========== DATE INPUT ========== */
        /* Force white background and black text for date inputs */
        .stDateInput > div > div > input,
        .stDateInput input,
        div[data-baseweb="input"] input {
            background-color: #FFFFFF !important;
            color: #2D3436 !important;
            border: 2px solid #E3F2FD !important;
            border-radius: 12px !important;
            padding: 0.75rem 1rem !important;
            -webkit-text-fill-color: #2D3436 !important;
        }
        
        .stDateInput > div > div > input:focus {
            border-color: #667EEA !important;
            box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1) !important;
        }
        
        /* Calendar popup - comprehensive targeting */
        .stDateInput [data-baseweb="popover"],
        .stDateInput [data-baseweb="calendar"],
        div[data-baseweb="popover"],
        div[data-baseweb="calendar"] {
            background-color: #FFFFFF !important;
            border: 2px solid #E3F2FD !important;
            border-radius: 12px !important;
            box-shadow: 0 4px 16px rgba(0, 0, 0, 0.1) !important;
        }
        
        /* Calendar inner content */
        [data-baseweb="calendar"] > div,
        [data-baseweb="calendar"] * {
            background-color: #FFFFFF !important;
        }
        
        /* Calendar header and controls */
        .stDateInput [data-baseweb="calendar"] button,
        .stDateInput [data-baseweb="calendar"] div,
        [data-baseweb="calendar"] button,
        [data-baseweb="calendar"] div {
            color: #2D3436 !important;
            background-color: #FFFFFF !important;
        }
        
        /* Calendar days */
        .stDateInput [data-baseweb="calendar"] td,
        [data-baseweb="calendar"] td,
        [data-baseweb="calendar"] span {
            color: #2D3436 !important;
            background-color: #FFFFFF !important;
        }
        
        /* Selected date */
        .stDateInput [data-baseweb="calendar"] td[aria-selected="true"],
        [data-baseweb="calendar"] td[aria-selected="true"] {
            background-color: #667EEA !important;
            color: white !important;
        }
        
        /* Hovered date */
        .stDateInput [data-baseweb="calendar"] td:hover,
        [data-baseweb="calendar"] td:hover {
            background-color: #E3F2FD !important;
            color: #2D3436 !important;
        }
        
        /* ========== TIME INPUT ========== */
        /* Force white background and black text for time inputs */
        .stTimeInput > div > div > input,
        .stTimeInput input,
        input[type="time"] {
            background-color: #FFFFFF !important;
            color: #2D3436 !important;
            border: 2px solid #E3F2FD !important;
            border-radius: 12px !important;
            padding: 0.75rem 1rem !important;
            -webkit-text-fill-color: #2D3436 !important;
        }
        
        .stTimeInput > div > div > input:focus {
            border-color: #667EEA !important;
            box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1) !important;
        }
        
        /* Time picker popup - comprehensive targeting */
        .stTimeInput [data-baseweb="popover"],
        .stTimeInput [data-baseweb="timepicker"],
        [data-baseweb="timepicker"] {
            background-color: #FFFFFF !important;
            border: 2px solid #E3F2FD !important;
            border-radius: 12px !important;
            box-shadow: 0 4px 16px rgba(0, 0, 0, 0.1) !important;
        }
        
        /* Time picker options and content */
        .stTimeInput [data-baseweb="timepicker"] *,
        [data-baseweb="timepicker"] *,
        [data-baseweb="timepicker"] div,
        [data-baseweb="timepicker"] ul,
        [data-baseweb="timepicker"] li {
            color: #2D3436 !important;
            background-color: #FFFFFF !important;
        }
        
        .stTimeInput [data-baseweb="timepicker"] li:hover,
        [data-baseweb="timepicker"] li:hover {
            background-color: #E3F2FD !important;
            color: #2D3436 !important;
        }
        
        /* ========== CHECKBOXES ========== */
        .stCheckbox {
            color: #2D3436 !important;
        }
        
        .stCheckbox label {
            color: #2D3436 !important;
            font-family: 'Inter', sans-serif !important;
        }
        
        .stCheckbox p {
            color: #2D3436 !important;
        }
        
        /* Checkbox input */
        .stCheckbox input[type="checkbox"] {
            accent-color: #667EEA !important;
        }
        
        /* ========== RADIO BUTTONS ========== */
        .stRadio label {
            color: #2D3436 !important;
        }
        
        .stRadio div[role="radiogroup"] label {
            color: #2D3436 !important;
        }
        
        .stRadio input[type="radio"] {
            accent-color: #667EEA !important;
        }
        
        /* ========== BUTTONS ========== */
        /* Primary buttons */
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
        
        .stButton > button[kind="primary"]:disabled {
            background: linear-gradient(135deg, #C4C4C4 0%, #ABABAB 100%) !important;
            opacity: 0.6 !important;
            cursor: not-allowed !important;
            box-shadow: none !important;
        }
        
        /* Secondary buttons */
        .stButton > button[kind="secondary"] {
            background-color: #FFFFFF !important;
            color: #667EEA !important;
            border: 2px solid #667EEA !important;
            border-radius: 12px !important;
            padding: 0.75rem 2rem !important;
            font-weight: 600 !important;
            font-family: 'Poppins', sans-serif !important;
            transition: all 0.3s ease !important;
        }
        
        .stButton > button[kind="secondary"]:hover {
            background-color: #F8F9FA !important;
            border-color: #5568D3 !important;
            color: #5568D3 !important;
        }
        
        .stButton > button[kind="secondary"]:disabled {
            background-color: #F8F9FA !important;
            border-color: #C4C4C4 !important;
            color: #95A5A6 !important;
            opacity: 0.6 !important;
            cursor: not-allowed !important;
        }
        
        /* Tertiary/default buttons */
        .stButton > button {
            background-color: #FFFFFF !important;
            color: #2D3436 !important;
            border: 2px solid #E0E0E0 !important;
            border-radius: 12px !important;
            font-family: 'Inter', sans-serif !important;
        }
        
        .stButton > button:hover {
            background-color: #F8F9FA !important;
            border-color: #667EEA !important;
        }
        
        /* ========== TABS ========== */
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
        
        /* ========== SLIDERS ========== */
        .stSlider > div > div > div {
            color: #2D3436 !important;
        }
        
        .stSlider [role="slider"] {
            background-color: #667EEA !important;
        }
        
        /* ========== FILE UPLOADER ========== */
        .stFileUploader > div {
            background-color: #FFFFFF !important;
            border: 2px dashed #E3F2FD !important;
            border-radius: 12px !important;
        }
        
        .stFileUploader label {
            color: #2D3436 !important;
        }
        
        /* ========== EXPANDER ========== */
        .streamlit-expanderHeader {
            background-color: #F8F9FA !important;
            color: #2D3436 !important;
            border-radius: 12px !important;
        }
        
        .streamlit-expanderContent {
            background-color: #FFFFFF !important;
            color: #2D3436 !important;
        }
        
        /* ========== ALERTS / MESSAGES ========== */
        .stAlert {
            border-radius: 12px !important;
            font-family: 'Inter', sans-serif !important;
        }
        
        /* Success */
        .stAlert[data-baseweb="notification"][kind="success"] {
            background-color: #D4EDDA !important;
            color: #155724 !important;
            border: 1px solid #C3E6CB !important;
        }
        
        /* Info */
        .stAlert[data-baseweb="notification"][kind="info"] {
            background-color: #D1ECF1 !important;
            color: #0C5460 !important;
            border: 1px solid #BEE5EB !important;
        }
        
        /* Warning */
        .stAlert[data-baseweb="notification"][kind="warning"] {
            background-color: #FFF3CD !important;
            color: #856404 !important;
            border: 1px solid #FFEAA7 !important;
        }
        
        /* Error */
        .stAlert[data-baseweb="notification"][kind="error"] {
            background-color: #F8D7DA !important;
            color: #721C24 !important;
            border: 1px solid #F5C6CB !important;
        }
        
        /* ========== DATAFRAME / TABLES ========== */
        .stDataFrame, .stTable {
            background-color: #FFFFFF !important;
            color: #2D3436 !important;
        }
        
        /* ========== PROGRESS BAR ========== */
        .stProgress > div > div {
            background-color: #E3F2FD !important;
        }
        
        .stProgress > div > div > div {
            background-color: #667EEA !important;
        }
        
        /* ========== SPINNER ========== */
        .stSpinner > div {
            border-color: #667EEA !important;
        }
        
        /* ========== TOOLTIPS ========== */
        div[data-baseweb="tooltip"] {
            background-color: #2D3436 !important;
            color: #FFFFFF !important;
            border-radius: 8px !important;
        }
        
        /* ========== MARKDOWN / TEXT ========== */
        .stMarkdown, .stMarkdown * {
            color: #2D3436 !important;
        }
        
        /* Keep headings styled properly */
        h1, h2, h3, h4, h5, h6 {
            font-family: 'Poppins', sans-serif !important;
        }
        
        /* ========== METRICS ========== */
        .stMetric {
            background-color: #FFFFFF !important;
            padding: 1rem !important;
            border-radius: 12px !important;
        }
        
        .stMetric label {
            color: #636E72 !important;
        }
        
        .stMetric div[data-testid="stMetricValue"] {
            color: #2D3436 !important;
        }
        
        /* ========== FORM STYLING ========== */
        .stForm {
            background-color: transparent !important;
        }
        
        /* ========== SIDEBAR OVERRIDES ========== */
        [data-testid="stSidebar"] {
            background-color: #FFFFFF !important;
        }
        
        [data-testid="stSidebar"] * {
            color: #2D3436 !important;
        }
        
        /* ========== UNIVERSAL INPUT OVERRIDES ========== */
        /* Target ALL baseweb inputs to ensure white background */
        div[data-baseweb="input"],
        div[data-baseweb="base-input"],
        input[data-baseweb="input"],
        [data-baseweb="input"] input {
            background-color: #FFFFFF !important;
            color: #2D3436 !important;
            -webkit-text-fill-color: #2D3436 !important;
        }
        
        /* Force all input elements */
        input:not([type="checkbox"]):not([type="radio"]) {
            background-color: #FFFFFF !important;
            color: #2D3436 !important;
            -webkit-text-fill-color: #2D3436 !important;
        }
        
        /* All popover panels should be white */
        [data-baseweb="popover"] {
            background-color: #FFFFFF !important;
        }
        
        [data-baseweb="popover"] * {
            background-color: #FFFFFF !important;
        }
        </style>
    """, unsafe_allow_html=True)
