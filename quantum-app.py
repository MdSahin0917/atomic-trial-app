import streamlit as st
import subprocess
import os
import shutil
import json
import glob
import numpy as np
import matplotlib.pyplot as plt
import re
import math
import pandas as pd
from PIL import Image
from matplotlib.figure import Figure
import tempfile
import zipfile

# 🔥 ENHANCED DARK QUANTUM THEME 🔥
st.markdown("""
<style>
    /* Dark Theme - Professional Atomic Style */
    .stApp {
        background: linear-gradient(135deg, #0f0f23 0%, #1a1a2e 50%, #16213e 100%);
        color: #e0e6ed;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    /* Headers - Glowing Cyan */
    h1, h2, h3, h4, h5, h6 {
        color: #00d4ff;
        font-family: 'Segoe UI', sans-serif;
        text-shadow: 0 0 10px rgba(0, 212, 255, 0.3);
        font-weight: 600;
    }
    
    /* Sidebar - Quantum Blue */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #1a1a2e 0%, #16213e 100%);
        border-right: 1px solid #00d4ff;
    }
    
    .stSidebar .stSelectbox, .stSidebar .stButton {
        color: #e0e6ed !important;
    }
    
    /* Buttons - Glowing Effect */
    .stButton > button {
        background: linear-gradient(45deg, #00d4ff, #0099cc);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.75rem 1.5rem;
        font-weight: 600;
        font-size: 14px;
        box-shadow: 0 4px 15px rgba(0, 212, 255, 0.3);
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(0, 212, 255, 0.5);
        background: linear-gradient(45deg, #0099cc, #00d4ff);
    }
    
    /* Primary Buttons - Orange Glow */
    button[kind="primary"] {
        background: linear-gradient(45deg, #ff6b35, #f7931e) !important;
        box-shadow: 0 4px 15px rgba(255, 107, 53, 0.4) !important;
    }
    
    button[kind="primary"]:hover {
        box-shadow: 0 6px 20px rgba(255, 107, 53, 0.6) !important;
        background: linear-gradient(45deg, #f7931e, #ff6b35) !important;
    }
    
    /* Inputs - Dark Glass */
    .stTextInput > div > div > input,
    .stNumberInput > div > div > input,
    .stSelectbox > div > div > div,
    .stTextArea > div > div > textarea {
        background-color: #2a2a3e !important;
        color: #e0e6ed !important;
        border: 1px solid #00d4ff !important;
        border-radius: 6px !important;
        padding: 0.75rem !important;
        font-size: 14px;
    }
    
    /* Selectbox Options - Dark Theme */
    .stSelectbox [data-baseweb="select"] > div {
        background-color: #2a2a3e !important;
        color: #e0e6ed !important;
    }
    
    .stSelectbox [data-baseweb="popover"] {
        background-color: #2a2a3e !important;
    }
    
    .stSelectbox [data-baseweb="menu"] {
        background-color: #2a2a3e !important;
    }
    
    .stSelectbox [data-baseweb="option"] {
        background-color: #2a2a3e !important;
        color: #e0e6ed !important;
    }
    
    .stSelectbox [data-baseweb="option"]:hover {
        background-color: #00d4ff !important;
        color: #0f0f23 !important;
    }
    
    /* Metrics - Cyan Border */
    .stMetric {
        background: rgba(0, 212, 255, 0.1);
        border-radius: 8px;
        border: 1px solid #00d4ff;
        color: #e0e6ed;
        padding: 15px;
    }
    
    /* Dataframe - Dark Theme */
    .dataframe {
        background-color: #2a2a3e !important;
        color: #e0e6ed !important;
    }
    .dataframe th {
        background-color: #00d4ff !important;
        color: white !important;
        font-weight: 600;
    }
    
    .dataframe td {
        background-color: #2a2a3e !important;
        color: #e0e6ed !important;
        border-bottom: 1px solid #00d4ff33;
    }
    
    /* Expander - Glass Morphism */
    .stExpander {
        background: rgba(42, 42, 62, 0.8);
        border: 1px solid #00d4ff;
        border-radius: 8px;
        box-shadow: 0 2px 10px rgba(0, 212, 255, 0.2);
        margin-bottom: 10px;
    }
    
    .streamlit-expanderHeader {
        color: #00d4ff !important;
        font-weight: 600;
        font-size: 16px;
    }
    
    /* Alerts - Cyan Left Border */
    .stAlert {
        border-radius: 8px;
        border-left: 4px solid #00d4ff;
        background: rgba(42, 42, 62, 0.9);
        color: #e0e6ed;
        padding: 15px;
    }
    
    /* Tabs - Dark Gradient */
    .stTabs [data-baseweb="tab-list"] {
        background: linear-gradient(90deg, #1a1a2e, #16213e);
        border-radius: 8px;
        gap: 5px;
    }
    
    .stTabs [data-baseweb="tab"] {
        background-color: transparent;
        border-radius: 4px;
        color: #e0e6ed;
        padding: 10px 20px;
    }
    
    .stTabs [aria-selected="true"] {
        background-color: #00d4ff !important;
        color: #0f0f23 !important;
        font-weight: 600;
    }
    
    /* Title Glow Effect */
    .main .block-container h1 {
        background: linear-gradient(45deg, #00d4ff, #0099cc);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-weight: 700;
        margin-bottom: 1rem;
    }
    
    /* Text elements */
    p, li, .stMarkdown {
        color: #e0e6ed !important;
        font-size: 14px;
        line-height: 1.6;
    }
    
    /* Form elements */
    .stForm {
        background: rgba(42, 42, 62, 0.6);
        border-radius: 8px;
        padding: 20px;
        border: 1px solid #00d4ff33;
    }
    
    /* Footer Hidden */
    footer {visibility: hidden;}
    
    /* Custom scrollbar */
    ::-webkit-scrollbar {
        width: 8px;
    }
    
    ::-webkit-scrollbar-track {
        background: #1a1a2e;
    }
    
    ::-webkit-scrollbar-thumb {
        background: #00d4ff;
        border-radius: 4px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: #0099cc;
    }
    
    /* Improved spacing */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    
    /* Labels */
    label {
        color: #00d4ff !important;
        font-weight: 600;
        font-size: 14px;
    }
    
    /* Captions */
    .stCaption {
        color: #a0a6b5 !important;
        font-size: 12px;
    }
    
    /* Success, Error, Warning, Info */
    .stSuccess {
        background: rgba(0, 212, 255, 0.1) !important;
        border: 1px solid #00d4ff !important;
    }
    
    .stError {
        background: rgba(255, 107, 53, 0.1) !important;
        border: 1px solid #ff6b35 !important;
    }
    
    .stWarning {
        background: rgba(255, 193, 7, 0.1) !important;
        border: 1px solid #ffc107 !important;
    }
    
    .stInfo {
        background: rgba(0, 212, 255, 0.1) !important;
        border: 1px solid #00d4ff !important;
    }
</style>
""", unsafe_allow_html=True)

# Database simulation
USERS_DB = {
    "admin": {"username": "admin", "password": "admin123", "role": "admin", "name": "Administrator"},
    "Bose": {"username": "Bose", "password": "admin@123", "role": "user", "name": "Dr. Bose"},
    "student1": {"username": "student1", "password": "pass123", "role": "user", "name": "Student 1"},
}

# Helpers from original
dict_l = {0: "s", 1: "p", 2: "d", 3: "f", 4: "g", 5: "h"}

# Define problems with their filters and details
problems = [
    {
        "name": "Hydrogen atom in an attractive cage",
        "time": "Time Independent",
        "body": "Two Body",
        "potential": "Potential Well",
        "perturbation": "No",
        "perturbation_type": None,
        "description": "This problem simulates a hydrogen atom confined in an attractive cage, exploring the effects of spatial confinement on atomic states. The simulation calculates wavefunctions and energy eigenvalues for different confinement parameters.",
        "detailed_description": """
This computational problem models a hydrogen atom confined within an attractive potential cage. The system allows researchers to study how spatial confinement affects atomic energy levels and wavefunctions, which is crucial for understanding quantum dots, confined molecular systems, and other nanoscale quantum phenomena.

**Key Features:**
- Time-independent Schrödinger equation solution
- Variable confinement potential parameters
- Multiple orbital calculations
- Energy eigenvalue analysis

**Physical Significance:**
Understanding confined quantum systems is essential for:
- Quantum dot technology
- Nanoscale device design
- Confined molecular dynamics
- Quantum computing applications

The simulation provides both numerical results and visualizations of wavefunctions and potentials.
""",
        "equations": r"""
**Hamiltonian:** 
\[ \hat{H} = -\frac{1}{2}\frac{d^2}{dr^2} + V_{eff}(r) + V_{well}(r) \]

**Effective Potential:** 
\[ V_{eff}(r) = -\frac{1}{r} + \frac{l(l+1)}{2r^2} \]

**Well Potential:** 
\[ V_{well}(r) = \begin{cases} 
-V_0 & \text{for } R \leq r \leq R + \Delta \\
0 & \text{otherwise}
\end{cases} \]

**Boundary Conditions:**
\[ \psi(0) = 0, \quad \psi(\infty) = 0 \]
""",
        "script": "backend/h-atom-in-att-cage/run.jl",
        "tabulator_script": "backend/h-atom-in-att-cage/tabulator.py",
        "lang": "julia",
        "fields": [
            {"name": "n", "default": 2, "type": int, "description": "Principal quantum number"},
            {"name": "l", "default": 0, "type": int, "description": "Azimuthal quantum number"},
            {"name": "N", "default": 41, "type": int, "description": "Number of grid points"},
            {"name": "maxR", "default": 500, "type": int, "description": "Maximum radial distance"},
            {"name": "v0 values", "default": "-0.4,-0.2,-0.125,-0.08,-0.05", "type": str, "description": "Comma-separated potential well depths"}
        ]
    },
    {
        "name": "Free Two-Body system under penetrable spatial confinement",
        "time": "Time Independent",
        "body": "Two Body",
        "potential": "penetrable spatial confinement",
        "perturbation": "No",
        "perturbation_type": None,
        "description": "This problem models a free two-body system under penetrable spatial confinement, studying quantum mechanical behaviors in confined spaces with Gaussian barriers.",
        "detailed_description": """
This simulation models a two-body quantum system subjected to penetrable spatial confinement using Gaussian potential barriers. The system explores how quantum particles behave when confined by penetrable barriers, which is relevant for understanding quantum tunneling, confined molecular systems, and mesoscopic physics.

**Key Features:**
- Two-body quantum system simulation
- Gaussian barrier confinement
- Multiple barrier configurations
- Wavefunction penetration analysis

**Physical Applications:**
- Quantum tunneling phenomena
- Mesoscopic system modeling
- Confined molecular dynamics
- Quantum barrier transmission studies

The simulation calculates energy eigenvalues and wavefunctions for various barrier configurations and provides detailed analysis of quantum confinement effects.
""",
        "equations": r"""
**Hamiltonian for Two-Body System:**
\[ \hat{H} = -\frac{1}{2\mu}\nabla^2 + V_{conf}(\mathbf{r}) \]

**Confinement Potential (Gaussian Barriers):**
\[ V_{conf}(x) = V_0 \exp\left(-\frac{(x-x_0)^2}{2D_0^2}\right) + V_1 \exp\left(-\frac{(x-x_1)^2}{2D_1^2}\right) \]

**Reduced Mass:**
\[ \mu = \frac{m_1 m_2}{m_1 + m_2} \]

**The system solves the time-independent Schrödinger equation for the relative motion.**
""",
        "script": "backend/Code_LMM/main.py",
        "lang": "python",
        "fields": [
            {"name": "n0", "default": 1, "type": int, "description": "Initial quantum number"},
            {"name": "Z", "default": 1, "type": int, "description": "Atomic number"},
            {"name": "l", "default": 0, "type": int, "description": "Azimuthal quantum number"},
            {"name": "V0", "default": 4.0, "type": float, "description": "First barrier height"},
            {"name": "D0", "default": 2.0, "type": float, "description": "First barrier width"},
            {"name": "x0", "default": "3.0", "type": str, "description": "First barrier position(s)"},
            {"name": "V1", "default": 4.0, "type": float, "description": "Second barrier height"},
            {"name": "D1", "default": 2.0, "type": float, "description": "Second barrier width"},
            {"name": "x1", "default": "6.0,7.0", "type": str, "description": "Second barrier position(s)"},
            {"name": "pk", "default": 4, "type": int, "description": "Precision parameter"}
        ]
    }
]

# Plot config
plot_config = {
    "Hydrogen atom in an attractive cage": {
        'orbital_pattern': r'^\d+[spdfgh]?$',
        'subfolder_regex': r'\(\s*V\s*=\s*([-\d.]+)\s*,\s*R\s*=\s*([-\d.]+)\s*,\s*Delta\s*=\s*([-\d.]+)\s*\)',
        'barrier_file': "Barrier_{sub_folder}.dat",
        'wave_file': "one_particle_density_position_{sub_folder}.dat",
        'tab_file': "{orbital}_v0-{v0_clean}.dat",
    },
    "Free Two-Body system under penetrable spatial confinement": {
        'orbital_pattern': r'^l=\d+$',
        'subfolder_regex': r'\(\s*V0\s*=\s*([-\d.]+)\s*,\s*D0\s*=\s*([-\d.]+)\s*,\s*x0\s*=\s*([-\d.]+)\s*,\s*V1\s*=\s*([-\d.]+)\s*,\s*D1\s*=\s*([-\d.]+)\s*,\s*x1\s*=\s*([-\d.]+)\s*\)',
        'barrier_file': "Barrier_{sub_folder}.dat",
        'wave_file': "one_particle_density_position_{sub_folder}.dat",
        'tab_file': "{orbital}_v0{v0_clean}.dat",
    },
}

# Initialize session state
def init_session_state():
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False
    if 'current_user' not in st.session_state:
        st.session_state.current_user = None
    if 'current_page' not in st.session_state:
        st.session_state.current_page = "Login"
    if 'selected_problem' not in st.session_state:
        st.session_state.selected_problem = None
    if 'show_details' not in st.session_state:
        st.session_state.show_details = False
    if 'last_output_folder' not in st.session_state:
        st.session_state.last_output_folder = None
    if 'l' not in st.session_state:
        st.session_state.l = 0
    if 'data_gen_inputs' not in st.session_state:
        st.session_state.data_gen_inputs = {}
    if 'navigation_stack' not in st.session_state:
        st.session_state.navigation_stack = []
    if 'user_simulations' not in st.session_state:
        st.session_state.user_simulations = {}

init_session_state()

# Configure page
st.set_page_config(
    page_title="Aliah University — Atomic Physics App",
    page_icon="⚛️",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.aliah.ac.in/department/physics',
        'Report a bug': None,
        'About': "Atomic Physics Simulator v2.0 - User Data Isolation"
    }
)

# Data Management Functions
def get_user_data_directory(username):
    """Get or create user-specific data directory"""
    user_dir = f"user_data/{username}"
    os.makedirs(user_dir, exist_ok=True)
    return user_dir

def get_user_simulations(username, problem_name=None):
    """Get user's simulation data for a specific problem or all problems"""
    user_dir = get_user_data_directory(username)
    
    if problem_name:
        # Get simulations for specific problem
        problem_dir = os.path.join(user_dir, problem_name.replace(" ", "_"))
        if os.path.exists(problem_dir):
            return problem_dir
        return None
    else:
        # Get all simulations for user
        simulations = {}
        user_dir = get_user_data_directory(username)
        for problem in problems:
            problem_key = problem["name"].replace(" ", "_")
            problem_dir = os.path.join(user_dir, problem_key)
            if os.path.exists(problem_dir):
                simulations[problem["name"]] = problem_dir
        return simulations

def save_simulation_data(username, problem_name, output_folder):
    """Save simulation data to user's directory"""
    user_dir = get_user_data_directory(username)
    problem_key = problem_name.replace(" ", "_")
    target_dir = os.path.join(user_dir, problem_key)
    
    # Copy simulation results to user directory
    if os.path.exists(output_folder):
        # Remove existing data for this problem
        if os.path.exists(target_dir):
            shutil.rmtree(target_dir)
        
        # Copy new data
        shutil.copytree(output_folder, target_dir)
        
        # Update user simulations in session state
        if username not in st.session_state.user_simulations:
            st.session_state.user_simulations[username] = {}
        st.session_state.user_simulations[username][problem_name] = target_dir
        
        return target_dir
    return None

def setup_backend_dependencies(temp_dir):
    """Copy backend dependencies to temporary directory"""
    try:
        # Check if backend directory exists
        if not os.path.exists("backend"):
            st.error("❌ Backend directory not found. Please ensure the 'backend' folder exists in the app directory.")
            return False
        
        # Debug information
        st.info(f"📁 Setting up backend in: {temp_dir}")
        st.info(f"📁 Source backend path: {os.path.abspath('backend')}")
        
        # Copy the entire backend structure to temporary directory
        backend_src = "backend"
        backend_dest = os.path.join(temp_dir, "backend")
        
        # Remove existing backend in temp dir if exists
        if os.path.exists(backend_dest):
            shutil.rmtree(backend_dest)
        
        # Copy backend to temp directory
        shutil.copytree(backend_src, backend_dest)
        
        # Verify the copy was successful
        if os.path.exists(backend_dest):
            # List contents for debugging
            backend_contents = []
            for root, dirs, files in os.walk(backend_dest):
                for file in files:
                    rel_path = os.path.relpath(os.path.join(root, file), backend_dest)
                    backend_contents.append(rel_path)
            
            st.info(f"✅ Backend setup successful. Copied {len(backend_contents)} files/directories")
            return True
        else:
            st.error("❌ Backend copy failed - destination directory not created")
            return False
            
    except Exception as e:
        st.error(f"❌ Error setting up backend dependencies: {str(e)}")
        # List backend directory contents for debugging
        if os.path.exists("backend"):
            backend_items = os.listdir("backend")
            st.info(f"📁 Backend directory contents: {backend_items}")
        return False

# Navigation helper functions
def navigate_to(page_name):
    """Navigate to a specific page and manage navigation stack"""
    if st.session_state.current_page != page_name:
        st.session_state.navigation_stack.append(st.session_state.current_page)
        st.session_state.current_page = page_name
    st.rerun()

def navigate_back():
    """Navigate back to previous page"""
    if st.session_state.navigation_stack:
        previous_page = st.session_state.navigation_stack.pop()
        st.session_state.current_page = previous_page
        st.rerun()

# ========== LOGIN PAGE ==========
def login_page():
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        # Display logo instead of atom icon
        logo_path = "assets/logo.webp"
        if os.path.exists(logo_path):
            st.image(logo_path, width=100)
        else:
            st.markdown("<h1 style='text-align: center;'>⚛️</h1>", unsafe_allow_html=True)
        
        st.markdown("<h1 style='text-align: center;'>Aliah University</h1>", unsafe_allow_html=True)
        st.markdown("<h2 style='text-align: center; color: #00d4ff;'>Atomic Physics Simulation Platform</h2>", unsafe_allow_html=True)
        
        # Login card
        with st.container():
            st.markdown("<div style='background: rgba(42, 42, 62, 0.8); padding: 30px; border-radius: 12px; border: 1px solid #00d4ff; box-shadow: 0 8px 25px rgba(0, 212, 255, 0.2);'>", unsafe_allow_html=True)
            st.markdown("<h3 style='text-align: center; margin-bottom: 30px;'>🔐 Secure Login</h3>", unsafe_allow_html=True)
            
            with st.form("login_form", clear_on_submit=False):
                username = st.text_input(
                    "👤 **Username**", 
                    placeholder="Enter your username",
                    key="login_username"
                )
                password = st.text_input(
                    "🔑 **Password**", 
                    type="password", 
                    placeholder="Enter your password",
                    key="login_password"
                )
                submit = st.form_submit_button(
                    "**Login to Platform**", 
                    type="primary", 
                    use_container_width=True
                )
            
            st.markdown("</div>", unsafe_allow_html=True)
        
        if submit:
            if username in USERS_DB and USERS_DB[username]["password"] == password:
                st.session_state.logged_in = True
                st.session_state.current_user = username
                st.session_state.current_page = "Home"
                st.session_state.navigation_stack = []
                st.success(f"✅ Welcome back, {USERS_DB[username]['name']}!")
                st.balloons()
            else:
                st.error("❌ Invalid username or password. Please try again.")
        
        # Demo credentials
        with st.expander("ℹ️ Demo Credentials"):
            st.markdown("""
            **Admin Account:**
            - Username: `admin`
            - Password: `admin123`
            
            **User Accounts:**
            - Username: `Bose` | Password: `admin@123`
            - Username: `student1` | Password: `pass123`
            """)

# ========== ADMIN PANEL ==========
def admin_panel():
    st.title("⚙️ Admin Control Panel")
    st.markdown(f"### Welcome, **{USERS_DB[st.session_state.current_user]['name']}** (Administrator)")
    
    tab1, tab2, tab3 = st.tabs(["👥 User Management", "🔬 Problem Management", "📊 System Analytics"])
    
    with tab1:
        st.subheader("User Management Dashboard")
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown("#### 📋 Registered Users")
            user_data = []
            for username, user_info in USERS_DB.items():
                user_data.append({
                    "Username": username,
                    "Full Name": user_info["name"],
                    "Role": user_info["role"].capitalize(),
                    "Status": "Active"
                })
            user_df = pd.DataFrame(user_data)
            st.dataframe(user_df, use_container_width=True, height=300)
        
        with col2:
            st.markdown("#### ➕ Add New User")
            with st.form("add_user_form"):
                new_name = st.text_input("Full Name", placeholder="Enter full name")
                new_username = st.text_input("Username", placeholder="Enter unique username")
                new_password = st.text_input("Password", type="password", placeholder="Set secure password")
                new_role = st.selectbox("Role", ["user", "admin"])
                
                add_user = st.form_submit_button("Add User", type="primary", use_container_width=True)
                if add_user:
                    if not new_name or not new_username or not new_password:
                        st.error("❌ All fields are required.")
                    elif new_username in USERS_DB:
                        st.error("❌ Username already exists.")
                    else:
                        USERS_DB[new_username] = {
                            "username": new_username, 
                            "password": new_password, 
                            "role": new_role, 
                            "name": new_name
                        }
                        st.success(f"✅ User '{new_name}' added successfully!")
                        st.rerun()
    
    with tab2:
        st.subheader("Problem Configuration")
        for i, problem in enumerate(problems):
            with st.expander(f"**{i+1}. {problem['name']}**", expanded=False):
                st.write(f"**Description:** {problem['description']}")
                col1, col2, col3 = st.columns([2, 1, 1])
                with col1:
                    st.write(f"**Script:** `{problem['script']}`")
                    st.write(f"**Language:** {problem['lang'].capitalize()}")
                with col2:
                    if st.button(f"✏️ Edit", key=f"edit_prob_{i}", use_container_width=True):
                        st.info("🛠️ Edit functionality coming in next update.")
                with col3:
                    if st.button(f"🗑️ Delete", key=f"del_prob_{i}", use_container_width=True):
                        st.warning(f"Deletion of '{problem['name']}' would be performed here.")
    
    with tab3:
        st.subheader("System Analytics & Monitoring")
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            # Count user data directories
            user_count = len([d for d in os.listdir("user_data") if os.path.isdir(os.path.join("user_data", d))]) if os.path.exists("user_data") else 0
            st.metric("Active Users", user_count, delta="+2 this month")
        with col2:
            st.metric("Available Problems", len(problems))
        with col3:
            # Count total simulations across all users
            total_simulations = 0
            if os.path.exists("user_data"):
                for user_dir in os.listdir("user_data"):
                    user_path = os.path.join("user_data", user_dir)
                    if os.path.isdir(user_path):
                        for problem_dir in os.listdir(user_path):
                            problem_path = os.path.join(user_path, problem_dir)
                            if os.path.isdir(problem_path):
                                total_simulations += 1
            st.metric("Total Simulations", total_simulations, delta="+15 today")
        with col4:
            st.metric("System Status", "Online", delta="Active")
        
        # Analytics chart
        fig = plt.figure(figsize=(10, 4))
        ax = fig.add_subplot(111)
        categories = ["Users", "Problems", "Simulations", "Active Sessions"]
        values = [user_count, len(problems), total_simulations, 3]
        bars = ax.bar(categories, values, color=['#00d4ff', '#ff6b35', '#28a745', '#ffc107'])
        ax.set_ylabel("Count", fontsize=12)
        ax.set_title("System Overview", fontsize=14, fontweight='bold', color='#00d4ff')
        
        # Add value labels on bars
        for bar, value in zip(bars, values):
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height + 0.1,
                    f'{value}', ha='center', va='bottom', fontweight='bold')
        
        plt.xticks(rotation=15)
        plt.tight_layout()
        st.pyplot(fig)

# ========== HOME PAGE ==========
def home_page():
    st.title("⚛️ Aliah University — Atomic Physics Simulator")
    st.markdown("## Welcome to the Quantum Exploration Platform")
    
    # Get user statistics
    username = st.session_state.current_user
    user_simulations = get_user_simulations(username)
    user_sim_count = len(user_simulations)
    
    # Hero section
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        <div style='background: rgba(0, 212, 255, 0.1); padding: 25px; border-radius: 12px; border: 1px solid #00d4ff; margin-bottom: 25px;'>
            <h3 style='color: #00d4ff; margin-top: 0;'>🚀 Discover the Quantum World</h3>
            <p>Our advanced simulation platform enables cutting-edge research in atomic and quantum physics through computational modeling and visualization.</p>
            <p><strong>Your Data:</strong> All your simulations are stored securely and privately. Only you can access your generated data.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div style='background: rgba(255, 107, 53, 0.1); padding: 25px; border-radius: 12px; border: 1px solid #ff6b35;'>
            <h4 style='color: #ff6b35; margin-top: 0;'>📊 Your Stats</h4>
            <p><strong>Problems:</strong> {len(problems)}</p>
            <p><strong>Your Simulations:</strong> {user_sim_count}</p>
            <p><strong>Status:</strong> Active</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Features section
    st.markdown("## 🔬 Platform Capabilities")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div style='background: rgba(42, 42, 62, 0.8); padding: 20px; border-radius: 8px; border: 1px solid #00d4ff; height: 100%;'>
            <h4 style='color: #00d4ff;'>💡 Advanced Simulations</h4>
            <ul>
            <li>Model complex atomic systems including one-body, two-body, and many-body interactions</li>
            <li>Investigate various potential configurations and perturbation effects</li>
            <li>Analyze quantum mechanical behaviors with high precision</li>
            <li>Visualize theoretical and computational results interactively</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style='background: rgba(42, 42, 62, 0.8); padding: 20px; border-radius: 8px; border: 1px solid #00d4ff; height: 100%;'>
            <h4 style='color: #00d4ff;'>🔒 Data Security</h4>
            <ul>
            <li>User-specific data isolation</li>
            <li>Private simulation storage</li>
            <li>Secure access control</li>
            <li>Personalized workspace</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # User's recent simulations
    if user_sim_count > 0:
        st.markdown("## 📁 Your Recent Simulations")
        
        for problem_name, problem_dir in user_simulations.items():
            with st.expander(f"**{problem_name}** - Last updated: {os.path.getmtime(problem_dir):.0f}", expanded=False):
                col1, col2 = st.columns([3, 1])
                with col1:
                    st.write(f"**Data location:** `{problem_dir}`")
                    # Count files in directory
                    file_count = len([f for f in os.listdir(problem_dir) if os.path.isfile(os.path.join(problem_dir, f))])
                    st.write(f"**Files generated:** {file_count}")
                
                with col2:
                    if st.button("View Results", key=f"view_{problem_name}"):
                        st.session_state.selected_problem = problem_name
                        st.session_state.show_details = True
                        navigate_to("Problem Selection")
    
    # Getting started section
    st.markdown("## 🚀 Getting Started")
    
    guide_col1, guide_col2, guide_col3 = st.columns(3)
    
    with guide_col1:
        st.markdown("""
        <div style='text-align: center; padding: 15px;'>
            <div style='font-size: 24px; margin-bottom: 10px;'>1</div>
            <h4 style='color: #00d4ff;'>Select Problem</h4>
            <p>Choose from available quantum physics problems in the Problems section</p>
        </div>
        """, unsafe_allow_html=True)
    
    with guide_col2:
        st.markdown("""
        <div style='text-align: center; padding: 15px;'>
            <div style='font-size: 24px; margin-bottom: 10px;'>2</div>
            <h4 style='color: #00d4ff;'>Configure Parameters</h4>
            <p>Set simulation parameters and run computational models</p>
        </div>
        """, unsafe_allow_html=True)
    
    with guide_col3:
        st.markdown("""
        <div style='text-align: center; padding: 15px;'>
            <div style='font-size: 24px; margin-bottom: 10px;'>3</div>
            <h4 style='color: #00d4ff;'>Analyze Results</h4>
            <p>Visualize and interpret simulation results within the problem page</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Quick action buttons
    st.markdown("---")
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("🔬 Browse Problems", type="primary", use_container_width=True):
            navigate_to("Problem Selection")
    with col2:
        if st.button("👥 About Us", use_container_width=True):
            navigate_to("About Us")
    with col3:
        if st.button("📧 Contact", use_container_width=True):
            navigate_to("Contact Us")

# ========== PROBLEM SELECTION PAGE ==========
def problem_selection_page():
    st.title("🔬 Problem Selection Center")
    
    if st.session_state.show_details and st.session_state.selected_problem:
        problem_name = st.session_state.selected_problem
        problem = next((p for p in problems if p["name"] == problem_name), None)
        
        if problem:
            # Problem details view
            st.header(f"{problem['name']}")
            
            # Check if user has existing data for this problem
            username = st.session_state.current_user
            user_problem_data = get_user_simulations(username, problem_name)
            has_existing_data = user_problem_data is not None
            
            col1, col2 = st.columns([3, 1])
            
            with col1:
                # Problem description
                st.subheader("📖 Problem Description")
                st.write(problem["detailed_description"] or problem["description"])
                
                # Key equations
                st.subheader("🧮 Mathematical Formulation")
                st.markdown(problem["equations"])
                
                # Technical details
                st.subheader("⚙️ Technical Specifications")
                col_spec1, col_spec2 = st.columns(2)
                with col_spec1:
                    st.write(f"**Time Dependency:** {problem['time']}")
                    st.write(f"**System Type:** {problem['body']}")
                with col_spec2:
                    st.write(f"**Potential Type:** {problem['potential']}")
                    st.write(f"**Implementation:** {problem['lang'].capitalize()}")
                
                # User's existing data for this problem
                if has_existing_data:
                    st.subheader("📁 Your Existing Data")
                    st.success(f"✅ You have existing simulation data for this problem.")
                    
                    # Show data statistics
                    if os.path.exists(user_problem_data):
                        file_count = len([f for f in os.listdir(user_problem_data) if os.path.isfile(os.path.join(user_problem_data, f))])
                        folder_count = len([d for d in os.listdir(user_problem_data) if os.path.isdir(os.path.join(user_problem_data, d))])
                        st.write(f"**Files:** {file_count} | **Folders:** {folder_count}")
                        
                        # Quick visualization button
                        if st.button("📊 Quick Visualize Existing Data", key="quick_viz", use_container_width=True):
                            st.session_state.last_output_folder = user_problem_data
                            # Show visualization directly in this page
                            show_problem_visualization(problem_name, user_problem_data)
            
            with col2:
                st.subheader("🚀 Actions")
                
                # Action buttons in a card
                st.markdown("""
                <div style='background: rgba(42, 42, 62, 0.8); padding: 20px; border-radius: 8px; border: 1px solid #00d4ff;'>
                """, unsafe_allow_html=True)
                
                if st.button("⚙️ Configure & Run", type="primary", use_container_width=True, key="proceed_data_gen"):
                    navigate_to("Data Generation")
                
                if has_existing_data:
                    if st.button("📊 Visualize Data", use_container_width=True, key="viz_existing"):
                        st.session_state.last_output_folder = user_problem_data
                        show_problem_visualization(problem_name, user_problem_data)
                
                st.markdown("</div>", unsafe_allow_html=True)
                
                # Quick info
                st.markdown("""
                <div style='background: rgba(255, 107, 53, 0.1); padding: 15px; border-radius: 8px; border: 1px solid #ff6b35; margin-top: 20px;'>
                    <h4 style='color: #ff6b35; margin-top: 0;'>💡 Tip</h4>
                    <p style='font-size: 14px;'>Configure simulation parameters in the next step before running computations.</p>
                </div>
                """, unsafe_allow_html=True)
            
            # Back button
            if st.button("🔙 Back to Problem List", use_container_width=True):
                st.session_state.show_details = False
                st.rerun()
                
        else:
            st.error("Problem not found.")
            st.session_state.show_details = False
            st.rerun()
            
    else:
        # Problem list view with filters
        st.markdown("### 🔍 Find the Right Problem")
        
        # Filters
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            time_filter = st.selectbox(
                "⏱️ Time Dependency", 
                ["All", "Time Dependent", "Time Independent"],
                key="time_filter"
            )
        with col2:
            body_filter = st.selectbox(
                "🔢 System Type", 
                ["All", "One Body", "Two Body", "Three Body", "Many Body"],
                key="body_filter"
            )
        with col3:
            potential_filter = st.selectbox(
                "📊 Potential Type", 
                ["All", "Potential Well", "Potential Barrier", "penetrable spatial confinement", "None"],
                key="potential_filter"
            )
        with col4:
            perturbation_filter = st.selectbox(
                "🌀 Perturbation", 
                ["All", "Yes", "No"],
                key="perturbation_filter"
            )
        
        # Apply filters
        filtered_problems = [p for p in problems if 
            (time_filter == "All" or p["time"] == time_filter) and
            (body_filter == "All" or p["body"] == body_filter) and
            (potential_filter == "All" or p["potential"] == potential_filter) and
            (perturbation_filter == "All" or p["perturbation"] == perturbation_filter)]
        
        # Display problems
        if not filtered_problems:
            st.warning("No problems match the selected filters. Try adjusting the criteria.")
            
            # Reset filters button
            if st.button("🔄 Reset All Filters", use_container_width=True):
                st.rerun()
        else:
            st.subheader(f"📋 {len(filtered_problems)} Available Problem(s)")
            
            for i, problem in enumerate(filtered_problems, 1):
                with st.expander(f"**{i}. {problem['name']}**", expanded=False):
                    col_prob1, col_prob2, col_prob3 = st.columns([3, 1, 1])
                    
                    with col_prob1:
                        st.write(problem["description"])
                        
                        # Problem metadata
                        col_meta1, col_meta2, col_meta3 = st.columns(3)
                        with col_meta1:
                            st.caption(f"⏱️ {problem['time']}")
                        with col_meta2:
                            st.caption(f"🔢 {problem['body']}")
                        with col_meta3:
                            st.caption(f"📊 {problem['potential']}")
                        
                        # Show user data status
                        username = st.session_state.current_user
                        user_data = get_user_simulations(username, problem["name"])
                        if user_data:
                            st.success("✅ You have data for this problem")
                    
                    with col_prob2:
                        if st.button("View Details", key=f"view_{i}", use_container_width=True):
                            st.session_state.selected_problem = problem["name"]
                            st.session_state.show_details = True
                            st.rerun()
                    
                    with col_prob3:
                        # Quick run button
                        if st.button("⚡ Quick Run", key=f"quick_{i}", use_container_width=True):
                            st.session_state.selected_problem = problem["name"]
                            st.session_state.show_details = True
                            navigate_to("Data Generation")

def show_problem_visualization(problem_name, data_folder):
    """Show visualization for a specific problem with user's data"""
    st.markdown("---")
    st.subheader("📊 Your Simulation Results")
    
    config = plot_config.get(problem_name, {})
    
    if not config:
        st.info("Visualization configuration not available for this problem.")
        return
    
    # Find available orbitals in user's data
    orbitals = sorted([d for d in os.listdir(data_folder) if os.path.isdir(os.path.join(data_folder, d)) and re.match(config.get('orbital_pattern', r'.*'), d)])
    
    if not orbitals:
        st.info("No orbital data found in your simulation results.")
        return
    
    # Orbital selection
    col1, col2 = st.columns([1, 2])
    with col1:
        orbital = st.selectbox("Select Orbital", orbitals, key="viz_orbital_select")
    
    if not orbital:
        st.warning("Please select an orbital to visualize.")
        return
        
    folder = os.path.join(data_folder, orbital)
    
    # Find subfolders with configurations
    subfolders = sorted([d for d in os.listdir(folder) if os.path.isdir(os.path.join(folder, d)) and d.startswith('(') and d.endswith(')')])
    
    if not subfolders:
        st.info(f"No configuration data found in {orbital}.")
        return
    
    # Configuration selection with search
    st.subheader("Configuration Selection")
    search_term = st.text_input("🔍 Search Configurations", placeholder="Enter search term...", key="viz_config_search")
    
    filtered_subfolders = [cfg for cfg in subfolders if search_term.lower() in cfg.lower()] if search_term else subfolders
    
    if not filtered_subfolders:
        st.warning("No configurations match your search.")
        return
        
    # Display configurations in a user-friendly way
    sub_folder = st.selectbox(
        "Select Configuration", 
        filtered_subfolders,
        format_func=lambda x: f"{x[:50]}..." if len(x) > 50 else x,
        key="viz_config_select"
    )
    
    if not sub_folder:
        return
        
    sub_path = os.path.join(folder, sub_folder)
    
    # Visualization section
    st.subheader("Potential and Wavefunction Visualization")
    
    # File paths
    barrier_file = os.path.join(sub_path, config['barrier_file'].format(sub_folder=sub_folder))
    wave_file = os.path.join(sub_path, config['wave_file'].format(sub_folder=sub_folder))
    
    # Create visualization
    fig, ax = plt.subplots(figsize=(10, 6))
    r, potential, barrier_data, wave_data = None, None, None, None
    
    # Load data
    if os.path.exists(barrier_file):
        try:
            data = np.loadtxt(barrier_file)
            r = data[:, 0]
            barrier_data = data[:, 1]
        except Exception as e:
            st.error(f"Error loading barrier data: {e}")
    
    if os.path.exists(wave_file):
        try:
            data = np.loadtxt(wave_file)
            if data.shape[1] >= 2:
                wave_data = data[:, 1]
        except Exception as e:
            st.error(f"Error loading wavefunction data: {e}")
    
    # Plot data
    if r is not None:
        l = st.session_state.l
        potential = np.where(r != 0, -1/r + l*(l+1)/(2*r**2), 0)
        ax.plot(r, potential, 'g-', label='Effective Potential', linewidth=2)
    
    if barrier_data is not None:
        ax.plot(r, barrier_data, 'r-', label='Barrier Potential', linewidth=2)
    
    if wave_data is not None:
        # Normalize wavefunction for visualization
        wave_norm = wave_data / np.max(np.abs(wave_data)) * 0.5 if np.max(np.abs(wave_data)) > 0 else wave_data
        ax.plot(r, wave_norm, 'b--', label='Wavefunction (normalized)', linewidth=2)
    
    ax.set_xlabel('Radial Distance (a.u.)', fontsize=12)
    ax.set_ylabel('Potential Energy (a.u.)', fontsize=12)
    ax.legend(frameon=True, edgecolor='black', loc='best')
    ax.grid(True, alpha=0.3)
    ax.set_title(f"Quantum System Visualization\n{orbital} - {sub_folder}", fontsize=14)
    
    st.pyplot(fig)
    
    # Data download section
    st.subheader("📥 Download Your Data")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if os.path.exists(barrier_file):
            with open(barrier_file, 'rb') as f:
                st.download_button(
                    label="📄 Download Barrier Data",
                    data=f,
                    file_name=f"barrier_data_{orbital}_{sub_folder}.dat",
                    mime="text/plain",
                    use_container_width=True
                )
    
    with col2:
        if os.path.exists(wave_file):
            with open(wave_file, 'rb') as f:
                st.download_button(
                    label="📄 Download Wavefunction Data",
                    data=f,
                    file_name=f"wavefunction_data_{orbital}_{sub_folder}.dat",
                    mime="text/plain",
                    use_container_width=True
                )
    
    with col3:
        # Create zip of entire configuration
        if st.button("📦 Download All Configuration Data", use_container_width=True):
            with tempfile.NamedTemporaryFile(delete=False, suffix='.zip') as tmp_file:
                with zipfile.ZipFile(tmp_file, 'w') as zipf:
                    for root, dirs, files in os.walk(sub_path):
                        for file in files:
                            file_path = os.path.join(root, file)
                            arcname = os.path.relpath(file_path, sub_path)
                            zipf.write(file_path, arcname)
                
                with open(tmp_file.name, 'rb') as f:
                    st.download_button(
                        label="⬇️ Download ZIP",
                        data=f,
                        file_name=f"{problem_name}_{orbital}_{sub_folder}.zip",
                        mime="application/zip",
                        use_container_width=True
                    )
            
            os.unlink(tmp_file.name)

# ========== DATA GENERATION PAGE ==========
def data_generation_page():
    st.title("⚙️ Simulation Data Generation")
    
    problem_name = st.session_state.selected_problem
    problem = next((p for p in problems if p["name"] == problem_name), None)
    
    if problem is None:
        st.error("❌ No problem selected. Please select a problem first.")
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("🔬 Select Problem", type="primary", use_container_width=True):
                navigate_to("Problem Selection")
        with col2:
            if st.button("🏠 Return Home", use_container_width=True):
                navigate_to("Home")
        return
    
    # Problem header
    st.header(problem_name)
    st.info("Configure the simulation parameters below and run the computation. Your data will be stored privately.")
    
    # Initialize inputs if not exist
    if problem_name not in st.session_state.data_gen_inputs:
        st.session_state.data_gen_inputs[problem_name] = {}
    
    entries = st.session_state.data_gen_inputs[problem_name]
    
    # Parameter configuration
    st.subheader("🔧 Parameter Configuration")
    
    # Create form for parameters
    with st.form("simulation_parameters", clear_on_submit=False):
        st.markdown("### Simulation Parameters")
        
        # Dynamically create input fields based on problem definition
        for field_info in problem["fields"]:
            field_name = field_info["name"]
            default_value = field_info["default"]
            field_type = field_info["type"]
            description = field_info.get("description", "")
            
            col1, col2 = st.columns([2, 3])
            with col1:
                label = field_name.replace('_', ' ').title() + ":"
                
                if field_type == str:
                    entries[field_name] = st.text_input(
                        label, 
                        value=entries.get(field_name, str(default_value)),
                        key=f"input_{field_name}_{problem_name}",
                        help=description
                    )
                elif field_type == int:
                    entries[field_name] = st.number_input(
                        label, 
                        value=entries.get(field_name, default_value),
                        step=1,
                        key=f"input_{field_name}_{problem_name}",
                        help=description
                    )
                elif field_type == float:
                    entries[field_name] = st.number_input(
                        label, 
                        value=entries.get(field_name, default_value),
                        key=f"input_{field_name}_{problem_name}",
                        help=description
                    )
            
            with col2:
                st.markdown(f"<div style='margin-top: 28px; color: #a0a6b5; font-size: 12px;'>{description}</div>", unsafe_allow_html=True)
        
        # Form submit button
        submitted = st.form_submit_button("🚀 Run Simulation", type="primary", use_container_width=True)
    
    # Action buttons outside form
    st.markdown("---")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        # Check if user has existing data for visualization
        username = st.session_state.current_user
        user_problem_data = get_user_simulations(username, problem_name)
        if user_problem_data and st.button("📊 View Existing Results", type="primary", use_container_width=True, key="view_existing_results"):
            st.session_state.last_output_folder = user_problem_data
            st.session_state.show_details = True
            navigate_to("Problem Selection")
    
    with col2:
        if st.button("🔙 Back to Problem", use_container_width=True):
            st.session_state.show_details = True
            navigate_to("Problem Selection")
    
    with col3:
        if st.button("🏠 Return Home", use_container_width=True):
            navigate_to("Home")
    
    # Handle form submission
    if submitted:
        with st.spinner("🔄 Executing simulation... This may take a few moments."):
            try:
                username = st.session_state.current_user
                # Create a simpler temp directory name
                temp_output_dir = f"temp_{username}_{problem_name.replace(' ', '_')}"
                # Clean up any existing temp directory
                if os.path.exists(temp_output_dir):
                    shutil.rmtree(temp_output_dir)
                os.makedirs(temp_output_dir, exist_ok=True)
                
                # Copy backend dependencies to temporary directory
                if not setup_backend_dependencies(temp_output_dir):
                    st.error("❌ Failed to set up backend dependencies.")
                    return
                
                # Store original directory
                original_dir = os.getcwd()
                
                # Change to temporary directory for simulation
                os.chdir(temp_output_dir)
                
                # Verify the backend files exist before running
                julia_script_path = os.path.join("backend", "h-atom-in-att-cage", "run.jl")
                python_script_path = os.path.join("backend", "Code_LMM", "main.py")
                
                if problem["name"] == "Hydrogen atom in an attractive cage":
                    # Extract parameters
                    n = entries["n"]
                    l = entries["l"]
                    st.session_state.l = l
                    N = entries["N"]
                    maxR = entries["maxR"]
                    v0_values = [float(v.strip()) for v in entries["v0 values"].split(",") if v.strip()]
                    
                    # Create output directory
                    src_folder = f"{n}{dict_l.get(l, '')}"
                    os.makedirs(src_folder, exist_ok=True)
                    
                    # Run simulations
                    progress_bar = st.progress(0)
                    status_text = st.empty()
                    
                    for i, v0 in enumerate(v0_values):
                        status_text.text(f"Running simulation {i+1}/{len(v0_values)} with V0 = {v0}")
                        
                        # Run Julia script with correct path
                        if not os.path.exists(julia_script_path):
                            st.error(f"❌ Julia script not found at: {julia_script_path}")
                            break
                            
                        result = subprocess.run(
                            ["julia", julia_script_path, str(v0), str(n), str(l), str(N), str(maxR)], 
                            capture_output=True, text=True, check=True
                        )
                        
                        # Run Python tabulator
                        tabulator_script_path = os.path.join("backend", "h-atom-in-att-cage", "tabulator.py")
                        if not os.path.exists(tabulator_script_path):
                            st.error(f"❌ Tabulator script not found at: {tabulator_script_path}")
                            break
                            
                        subprocess.run(
                            ["python3", tabulator_script_path, str(v0), str(n), str(l), str(N), str(maxR)], 
                            capture_output=True, text=True, check=True
                        )
                        
                        progress_bar.progress((i + 1) / len(v0_values))
                    
                    output_folder = os.path.abspath(src_folder)

                elif problem["name"] == "Free Two-Body system under penetrable spatial confinement":
                    # Extract parameters
                    n0 = entries["n0"]
                    Z = entries["Z"]
                    l = entries["l"]
                    st.session_state.l = l
                    V0 = entries["V0"]
                    D0 = entries["D0"]
                    x0_values = [float(x.strip()) for x in entries["x0"].split(",") if x.strip()]
                    V1 = entries["V1"]
                    D1 = entries["D1"]
                    x1_values = [float(x.strip()) for x in entries["x1"].split(",") if x.strip()]
                    pk = entries["pk"]
                    
                    # Run simulations
                    total_simulations = len(x0_values) * len(x1_values)
                    progress_bar = st.progress(0)
                    status_text = st.empty()
                    
                    count = 0
                    for x0 in x0_values:
                        for x1 in x1_values:
                            status_text.text(f"Running simulation {count+1}/{total_simulations} with x0={x0}, x1={x1}")
                            
                            if not os.path.exists(python_script_path):
                                st.error(f"❌ Python script not found at: {python_script_path}")
                                break
                                
                            subprocess.run(
                                ["python3", python_script_path, str(n0), str(Z), str(l), str(V0), str(D0), str(x0), 
                                 str(V1), str(D1), str(x1), str(pk)], 
                                capture_output=True, text=True, check=True
                            )
                            
                            count += 1
                            progress_bar.progress(count / total_simulations)
                    
                    output_folder = os.getcwd()
                
                # Return to original directory
                os.chdir(original_dir)
                
                # Save data to user directory
                user_data_folder = save_simulation_data(username, problem_name, os.path.join(temp_output_dir, output_folder))
                
                # Clean up temporary directory
                shutil.rmtree(temp_output_dir)
                
                if user_data_folder:
                    st.session_state.last_output_folder = user_data_folder
                    st.success("✅ Simulation completed successfully! Data saved to your private storage.")
                    st.balloons()
                    
                    # Show output location and offer visualization
                    st.info(f"📁 Your data is securely stored at: `{user_data_folder}`")
                    
                    # Auto-navigate to visualization
                    st.markdown("---")
                    st.subheader("🎉 Ready to View Your Results!")
                    if st.button("📊 View Visualization Now", type="primary", use_container_width=True):
                        st.session_state.show_details = True
                        navigate_to("Problem Selection")

            except subprocess.CalledProcessError as e:
                # Return to original directory on error
                if 'original_dir' in locals():
                    os.chdir(original_dir)
                st.error(f"❌ Simulation Error: {e.stderr}")
                st.info("Please check your parameters and ensure all required software is installed.")
            except Exception as e:
                # Return to original directory on error
                if 'original_dir' in locals():
                    os.chdir(original_dir)
                st.error(f"❌ Unexpected Error: {str(e)}")
                st.info("Please check your parameters and try again.")

# ========== ABOUT US PAGE ==========
def about_us_page():
    st.title("👥 About Us")
    st.markdown("### Pioneering Quantum Simulation at Aliah University")
    
    # University info
    col1, col2 = st.columns([1, 2])
    with col1:
        # Display logo
        logo_path = "assets/logo.webp"
        if os.path.exists(logo_path):
            st.image(logo_path, width=200)
        else:
            st.markdown("""
            <div style='background: rgba(0, 212, 255, 0.1); padding: 30px; border-radius: 12px; border: 1px solid #00d4ff; text-align: center;'>
                <div style='font-size: 48px; margin-bottom: 20px;'>⚛️</div>
                <h3 style='color: #00d4ff;'>Aliah University</h3>
                <p>Department of Physics</p>
            </div>
            """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style='background: rgba(42, 42, 62, 0.8); padding: 25px; border-radius: 8px; border: 1px solid #00d4ff;'>
            <h4 style='color: #00d4ff;'>Institutional Excellence</h4>
            <p>Established in 2008, Aliah University is a premier institution for higher education in Kolkata, India. 
            The Department of Physics is dedicated to advancing knowledge in fundamental and applied physics through 
            innovative research and quality education.</p>
            
            <p>Our mission is to foster scientific curiosity and develop computational tools that bridge the gap between 
            theoretical concepts and practical applications in quantum physics.</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Team section
    st.markdown("## 🧑‍💻 Our Development Team")
    
    team_col1, team_col2 = st.columns(2)
    
    with team_col1:
        st.markdown("""
        <div style='background: rgba(42, 42, 62, 0.8); padding: 25px; border-radius: 8px; border: 1px solid #00d4ff; height: 100%;'>
            <h4 style='color: #00d4ff;'>Md Sahin Ahamed</h4>
            <p><strong>Lead Developer & Researcher</strong></p>
            <ul>
            <li>Expertise: Quantum Computing, Software Architecture</li>
            <li>M.Sc. Physics, Aliah University</li>
            <li>Specialization: Computational Physics</li>
            <li>Research Interests: Quantum Simulations, Algorithm Development</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with team_col2:
        st.markdown("""
        <div style='background: rgba(42, 42, 62, 0.8); padding: 25px; border-radius: 8px; border: 1px solid #00d4ff; height: 100%;'>
            <h4 style='color: #00d4ff;'>Koustav Das Chakladar</h4>
            <p><strong>Co-Developer & UI/UX Specialist</strong></p>
            <ul>
            <li>Expertise: Computational Physics, Interface Design</li>
            <li>M.Sc. Physics, Aliah University</li>
            <li>Specialization: Quantum Mechanics</li>
            <li>Research Interests: Nanoscale Systems, Visualization</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # Mission and technology
    st.markdown("## 🎯 Mission & Vision")
    
    col_mission1, col_mission2 = st.columns(2)
    
    with col_mission1:
        st.markdown("""
        <div style='background: rgba(42, 42, 62, 0.8); padding: 25px; border-radius: 8px; border: 1px solid #00d4ff; height: 100%;'>
            <h4 style='color: #00d4ff;'>Our Mission</h4>
            <p>To bridge the gap between theoretical quantum mechanics and practical simulation through:</p>
            <ul>
            <li>Advanced computational tools for researchers</li>
            <li>Interactive educational platforms for students</li>
            <li>Innovation in atomic and molecular physics</li>
            <li>Contributions to the global scientific community</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col_mission2:
        st.markdown("""
        <div style='background: rgba(42, 42, 62, 0.8); padding: 25px; border-radius: 8px; border: 1px solid #00d4ff; height: 100%;'>
            <h4 style='color: #00d4ff;'>Technology Stack</h4>
            <ul>
            <li><strong>Frontend:</strong> Streamlit Framework</li>
            <li><strong>Backend:</strong> Python, Julia, NumPy</li>
            <li><strong>Visualization:</strong> Matplotlib, Plotly</li>
            <li><strong>Deployment:</strong> Cloud-based with secure authentication</li>
            <li><strong>Simulation:</strong> Custom quantum algorithms</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # Back to home
    st.markdown("---")
    if st.button("🏠 Return to Home", use_container_width=True):
        navigate_to("Home")

# ========== CONTACT US PAGE ==========
def contact_us_page():
    st.title("📧 Contact Our Team")
    st.markdown("### Get in Touch with Aliah University Physics Department")
    
    # Contact information and form
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div style='background: rgba(42, 42, 62, 0.8); padding: 25px; border-radius: 8px; border: 1px solid #00d4ff; height: 100%;'>
            <h4 style='color: #00d4ff;'>Contact Information</h4>
            
            <p><strong>🏢 Address:</strong><br>
            Aliah University<br>
            Department of Physics<br>
            IIA/27, New Town, Kolkata-700160<br>
            West Bengal, India</p>
            
            <p><strong>📞 Phone:</strong><br>
            +91-33-23416444 (General)<br>
            +91-XXXXXXXXXX (Department)</p>
            
            <p><strong>📧 Email:</strong><br>
            physics@aliah.ac.in<br>
            support@atomicsim.aliah.ac.in</p>
            
            <p><strong>🕒 Working Hours:</strong><br>
            Monday - Friday: 9:30 AM - 5:30 PM IST</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Map placeholder
        st.markdown("""
        <div style='background: rgba(0, 212, 255, 0.1); padding: 30px; border-radius: 8px; border: 1px solid #00d4ff; text-align: center; margin-top: 20px;'>
            <p><strong>📍 Campus Location</strong></p>
            <p>New Town, Kolkata</p>
            <div style='font-size: 48px; margin: 20px 0;'>🗺️</div>
            <p>Interactive map would be displayed here</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("### Send Us a Message")
        with st.form("contact_form", clear_on_submit=True):
            name = st.text_input("Your Full Name *", placeholder="Enter your full name")
            email = st.text_input("Your Email Address *", placeholder="your.email@example.com")
            subject = st.selectbox("Subject *", [
                "General Inquiry", 
                "Technical Support", 
                "Collaboration Proposal", 
                "Research Inquiry",
                "Feedback",
                "Other"
            ])
            message = st.text_area("Message *", placeholder="Please provide details about your inquiry...", height=150)
            
            submitted = st.form_submit_button("Send Message", type="primary", use_container_width=True)
            
            if submitted:
                if name and email and subject and message:
                    st.success("✅ Your message has been sent successfully!")
                    st.info(f"**Summary:** From {name} ({email}) - Subject: {subject}")
                    st.balloons()
                else:
                    st.error("❌ Please fill all required fields (marked with *).")
    
    # FAQ section
    st.markdown("## ❓ Frequently Asked Questions")
    
    with st.expander("How do I reset my password?"):
        st.write("Currently, password resets require administrator assistance. Please contact the physics department admin via email for password reset requests.")
    
    with st.expander("Can I add custom problems to the platform?"):
        st.write("Admin users can manage problems through the admin panel. For regular users, custom problem addition is currently limited. Contact the development team for custom simulation requirements.")
    
    with st.expander("What should I do if a simulation fails?"):
        st.write("""
        If you encounter simulation errors:
        1. Check your parameter values are within reasonable ranges
        2. Ensure all required software (Python, Julia) is properly installed
        3. Verify input formats match the expected patterns
        4. Contact technical support with the error message and your parameter settings
        """)
    
    with st.expander("Is my data secure on this platform?"):
        st.write("Yes, all user data and simulation results are stored securely in user-specific directories. The platform uses authentication and does not share user data with other users.")
    
    with st.expander("Can I export my simulation results?"):
        st.write("Yes, simulation results can be exported in various formats from the problem visualization page. Tabulated data is available for download alongside visualization options.")
    
    # Back to home
    st.markdown("---")
    if st.button("🏠 Return to Home", use_container_width=True):
        navigate_to("Home")

# ========== MAIN APP PAGES ==========
def main_app():
    # Sidebar Navigation
    with st.sidebar:
        st.title("⚛️ Navigation")
        
        # Display logo in sidebar
        logo_path = "assets/logo.webp"
        if os.path.exists(logo_path):
            st.image(logo_path, width=80)
        else:
            st.markdown("<div style='text-align: center; font-size: 48px;'>⚛️</div>", unsafe_allow_html=True)
        
        # User info card
        user_info = USERS_DB[st.session_state.current_user]
        st.markdown(f"""
        <div style='background: rgba(0, 212, 255, 0.1); padding: 15px; border-radius: 8px; border: 1px solid #00d4ff; margin-bottom: 20px;'>
            <div style='font-size: 14px; color: #00d4ff;'>Logged in as:</div>
            <div style='font-size: 16px; font-weight: 600;'>{user_info['name']}</div>
            <div style='font-size: 12px; color: #a0a6b5;'>Role: {user_info['role'].capitalize()}</div>
        </div>
        """, unsafe_allow_html=True)
        
        # Navigation menu
        st.markdown("### 📍 Main Menu")
        
        # Define navigation options based on user role
        nav_options = [
            {"icon": "🏠", "label": "Home", "page": "Home"},
            {"icon": "🔬", "label": "Problems", "page": "Problem Selection"},
        ]
        
        if user_info["role"] == "admin":
            nav_options.append({"icon": "⚙️", "label": "Admin Panel", "page": "Admin"})
        
        nav_options.extend([
            {"icon": "👥", "label": "About Us", "page": "About Us"},
            {"icon": "📧", "label": "Contact", "page": "Contact Us"},
        ])
        
        # Create navigation buttons
        for option in nav_options:
            if st.button(
                f"{option['icon']} {option['label']}", 
                key=f"nav_{option['page']}",
                use_container_width=True,
                type="primary" if st.session_state.current_page == option['page'] else "secondary"
            ):
                navigate_to(option['page'])
        
        st.markdown("---")
        
        # Quick actions
        st.markdown("### ⚡ Quick Actions")
        if st.session_state.selected_problem:
            st.info(f"**Current Problem:**\n{st.session_state.selected_problem}")
            
            if st.button("📝 Run Simulation", key="sidebar_data_gen", use_container_width=True):
                navigate_to("Data Generation")
        
        # Logout button
        st.markdown("---")
        if st.button("🚪 Logout", key="sidebar_logout", use_container_width=True):
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.rerun()
    
    # Main content area based on current page
    current_page = st.session_state.current_page
    
    # Header with breadcrumbs
    col1, col2, col3 = st.columns([3, 2, 1])
    with col1:
        if current_page != "Home":
            st.markdown(f"### {current_page}")
        
        # Breadcrumbs
        if st.session_state.navigation_stack:
            breadcrumbs = " > ".join([st.session_state.navigation_stack[-1]] + [current_page])
            st.caption(f"Navigation: {breadcrumbs}")
    
    with col3:
        if st.session_state.navigation_stack and current_page != "Home":
            if st.button("🔙 Back", key="header_back", use_container_width=True):
                navigate_back()
    
    # Page content routing
    if current_page == "Home":
        home_page()
    elif current_page == "Problem Selection":
        problem_selection_page()
    elif current_page == "Data Generation":
        data_generation_page()
    elif current_page == "Admin":
        admin_panel()
    elif current_page == "About Us":
        about_us_page()
    elif current_page == "Contact Us":
        contact_us_page()

# ========== MAIN EXECUTION ==========
if not st.session_state.logged_in:
    login_page()
else:
    main_app()

# ENHANCED FOOTER
st.markdown("---")
st.markdown(
    '<div style="text-align: center; color: #00d4ff; font-size: 14px; text-shadow: 0 0 10px rgba(0, 212, 255, 0.5); padding: 20px;">'
    '⚛️ Atomic Physics Simulator v2.0 | User Data Isolation System<br>'
    'Developed by Md Sahin Ahamed & Koustav Das Chakladar | Aliah University © 2025'
    '</div>',
    unsafe_allow_html=True
)