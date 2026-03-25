def get_custom_css():
    return """
    <style>
    /* Dark Theme Animated App Background */
    .stApp, [data-testid="stAppViewContainer"] {
        background-color: #090b10 !important;
        background-image: url("https://media.giphy.com/media/xTiTnxpQ3ghPiB2Hp6/giphy.gif") !important;
        background-size: cover !important;
        background-position: center !important;
        background-repeat: no-repeat !important;
        background-attachment: fixed !important;
        color: #ffffff;
    }
    
    /* Glowing Title */
    .glowing-title {
        font-family: 'Courier New', Courier, monospace;
        font-size: 5rem;
        font-weight: 900;
        text-align: center;
        margin-top: 5vh;
        color: #ffffff;
        text-shadow: 0 0 10px #00ffff, 0 0 20px #00ffff, 0 0 40px #00ffff;
        animation: glow 1.5s ease-in-out infinite alternate;
        letter-spacing: 4px;
    }

    /* Typewriter effect for subtitle */
    .typewriter-text {
        overflow: hidden; 
        border-right: .15em solid #00ffff; 
        white-space: nowrap; 
        margin: 0 auto; 
        letter-spacing: .15em; 
        animation: typing 3.5s steps(40, end), blink-caret .75s step-end infinite;
        text-align: center;
        width: max-content;
        color: #aaaaaa;
        margin-bottom: 20px;
    }

    /* The typing effect */
    @keyframes typing {
      from { width: 0 }
      to { width: 100% }
    }

    /* The typewriter cursor effect */
    @keyframes blink-caret {
      from, to { border-color: transparent }
      50% { border-color: #00ffff; }
    }

    @keyframes glow {
        from { text-shadow: 0 0 10px #00ffff, 0 0 20px #00ffff, 0 0 30px #00ffff; }
        to   { text-shadow: 0 0 20px #ff00ff, 0 0 30px #ff00ff, 0 0 40px #ff00ff; }
    }

    /* Streamlit Primary Button Styling */
    div.stButton > button {
        background: linear-gradient(135deg, #ff00cc 0%, #3333ff 100%);
        color: white;
        border: none;
        padding: 0.75rem 2.5rem;
        font-size: 1.25rem;
        font-weight: bold;
        border-radius: 50px;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        margin-top: 1rem;
        width: 100%;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
    }
    div.stButton > button:hover {
        transform: scale(1.05);
        box-shadow: 0 10px 25px rgba(255, 0, 204, 0.6);
        color: white;
    }
    
    div.stButton > button p {
        font-size: 1.2rem;
    }

    /* Target specific components to give them a glassmorphism feel */
    [data-testid="stTabs"] {
        background: rgba(255, 255, 255, 0.05);
        border-radius: 16px;
        box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.18);
        padding: 2rem;
        margin-top: 1rem;
    }

    /* Tab Label Styling */
    button[data-baseweb="tab"] {
        color: #ffffff;
        font-size: 1.1rem;
    }
    button[data-baseweb="tab"][aria-selected="true"] {
        color: #00ffff !important;
        border-bottom: 2px solid #00ffff !important;
    }

    /* Make all widget labels and text visible */
    label, p, span {
        color: #ffffff !important;
    }

    [data-testid="stRadio"] label, [data-testid="stRadio"] p, [data-testid="stRadio"] span {
        color: #e0e0e0 !important;
    }

    @keyframes neon-pulse {
        0% { box-shadow: 0 0 5px #00ffff, inset 0 0 5px #00ffff; border-color: #00ffff; }
        50% { box-shadow: 0 0 20px #ff00cc, inset 0 0 10px #ff00cc; border-color: #ff00cc; }
        100% { box-shadow: 0 0 5px #00ffff, inset 0 0 5px #00ffff; border-color: #00ffff; }
    }

    /* Style the file uploader and audio inputs to sit well on dark backgrounds */
    [data-testid="stFileUploader"] {
        background-color: transparent !important;
    }
    
    [data-testid="stFileUploaderDropzone"], 
    [data-testid="stAudioInput"],
    [data-testid="stCameraInput"] {
        background-color: #1a1e29 !important;
        border: 2px dashed #00ffff !important;
        border-radius: 15px !important;
        animation: neon-pulse 2.5s infinite alternate !important;
    }
    
    [data-testid="stFileUploaderDropzone"] *,
    [data-testid="stAudioInput"] *,
    [data-testid="stCameraInput"] * {
        color: #ffffff !important;
    }
    
    /* Ensure no white div wrappers inside audio remain */
    [data-testid="stAudioInput"] div,
    [data-testid="stCameraInput"] div {
        background-color: transparent !important;
    }
    
    /* Style the internal buttons inside these components */
    [data-testid="stFileUploaderDropzone"] button,
    [data-testid="stAudioInput"] button,
    [data-testid="stCameraInput"] button {
        background-color: #2a2e39 !important;
        color: #ffffff !important;
        border: 1px solid #00ffff !important;
    }

    /* Style the Text Area widget to have a beautiful glassmorphism effect (letting the main animated background shine through) */
    .stTextArea div[data-baseweb="textarea"],
    .stTextArea div[data-baseweb="base-input"] {
        background-color: rgba(10, 15, 30, 0.6) !important;
        background-image: none !important; /* Removes broken GIPHY */
        backdrop-filter: blur(10px) !important;
        border: 1px solid #00ffff !important;
        border-radius: 10px !important;
    }

    .stTextArea textarea {
        background-color: transparent !important;
        color: #ffffff !important;
        text-shadow: 1px 1px 3px #000000 !important;
        font-size: 1.05rem !important;
        letter-spacing: 0.5px !important;
    }
    
    .stTextArea textarea::placeholder {
        color: #dddddd !important;
        text-shadow: 1px 1px 2px #000000 !important;
    }

    /* Hide sidebar and header */
    [data-testid="collapsedControl"] { display: none; }
    section[data-testid="stSidebar"] { display: none; }
    header[data-testid="stHeader"] { display: none; }
    </style>
    """
