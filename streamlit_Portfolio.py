from pathlib import Path
from urllib.parse import quote

import streamlit as st

# =====================================================================
# CONFIG  -  edit this section with your own details
# =====================================================================
NAME = "Ahmed Ehab"
TITLE = "Data Scientist & Engineer"
TAGLINE = (
    "I turn raw data into clear, interactive dashboards and models "
    "that help people make better decisions."
)
EMAIL = "ahmedehab2336@gmail.com"
LOCATION = "Alexandria, Egypt"  # set to "" to hide
PHOTO_PATH = "data/profile.jpg"  # optional
CV_PATH = "data/Ahmed_Ehab_CV.pdf"  # put your CV here

SOCIAL_LINKS = {
    "LinkedIn": "https://www.linkedin.com/in/ahmedehab233",
    "GitHub": "https://github.com/Ahmed-Ehab233",
    "Upwork": "",
}

ABOUT = [
    f"Hi, I'm {NAME}, a data scientist and engineer who enjoys building dashboards and "
    "machine learning models that turn messy data into decisions.",
    "I work mainly with Python and SQL, and I like projects where analysis, "
    "modelling and a clean user experience come together.",
    "Replace this paragraph with a short note about your background, "
    "what you study or do, and what you are looking for.",
]

STATS = [  # (label, value)
    ("Featured projects", "1+"),
    ("Main BI tool", "Python & SQL"),
    ("ML & analysis", "Python"),
]

SKILLS = {
    "Programming & Querying": {
        "status": "",
        "items": ["Python", "SQL", "Pandas", "NumPy"],
    },
    "Data Analysis & BI": {
        "status": "",
        "items": ["Power BI", "DAX", "Power Query", "Excel", "Matplotlib", "Seaborn"],
    },
    "Machine Learning": {
        "status": "",
        "items": [
            "Scikit-learn", "Feature Engineering", "Data Preprocessing",
            "Model Evaluation", "ML Algorithms",
        ],
    },
    "Data Engineering & Tools": {
        "status": "Currently developing",
        "items": ["ETL / Data Pipelines", "Distributed Computing", "Docker", "Git"],
    },
}

PROJECTS = [
    {
        "title": "FIFA Players — Machine Learning",
        "subtitle": "University team project · Leading role",
        "description": (
            "An end-to-end machine learning project using FIFA player data to predict "
            "player market value and classify performance tiers. The project combines "
            "preprocessing, feature engineering, model comparison, and ensemble learning "
            "in an interactive prediction application."
        ),
        "highlights": [
            "Predicting player performance tiers and market value",
            "Building and comparing classification and regression models",
            "Using stacking ensembles and hyperparameter tuning",
        ],
        "tech": [
            "Python", "Pandas", "NumPy", "Matplotlib", "Seaborn", "Plotly",
            "Scikit-learn", "Streamlit", "Feature Engineering", "GridSearch",
            "Ensemble Learning",
        ],
        # Add your links here. Empty values are hidden automatically.
        "links": {
            "Live App": "",  # e.g. "https://your-app.streamlit.app"
            "GitHub": "https://github.com/Ahmed-Ehab233/Football-Player-Prediction-app",    # e.g. "https://github.com/you/fifa-ml"
            "Report / Slides": "",
        },
    },
    # To add your second project, copy the block above, paste it here and edit it.
]

EXPERIENCE = [
    {
        "role": "Data Engineering Track",
        "org": "Digital Egypt Pioneers Initiative (DEPI)",
        "period": "Jul 2026 – Present",
        "points": [
            "Selected for DEPI's intensive, hands-on training track in data engineering.",
            "Building end-to-end data pipelines and working with big data technologies.",
            "Deploying data solutions on cloud platforms, with a focus on Azure.",
            "Covering SQL and database management, advanced Python, deployment, "
            "prompt engineering and AI for data engineers.",
            "Finishing with a capstone project that brings the full pipeline together.",
        ],
    }
]

SERVICES_INTRO = "Applying data skills to practical problems while continuing to grow."

SERVICES = [
    {
        "title": "Excel Data Cleaning & Analysis",
        "description": "Cleaning, organizing and structuring datasets in Excel so they are ready for analysis and reporting.",
        "tech": ["Microsoft Excel"],
    },
    {
        "title": "Power BI Dashboards",
        "description": "Designing interactive dashboards that present data clearly and support better business decisions.",
        "tech": ["Power BI", "Power Query", "DAX"],
    },
    {
        "title": "Python Data Analysis",
        "description": "Exploring, cleaning and visualizing data with Python libraries to find clear, useful insights.",
        "tech": ["Python", "Pandas", "NumPy", "Matplotlib", "Seaborn"],
    },
    {
        "title": "SQL & Database Analysis",
        "description": "Writing SQL queries to retrieve, analyze and summarize data from relational databases.",
        "tech": ["SQL", "MySQL"],
    },
    {
        "title": "Basic Machine Learning Solutions",
        "description": "Building introductory regression and classification models and evaluating their results.",
        "tech": ["Python", "Scikit-learn"],
    },
]
# =====================================================================


def link_row(links):
    """Show link buttons side by side, skipping empty links."""
    active = {label: url for label, url in links.items() if url}
    if not active:
        st.caption("Links coming soon")
        return
    cols = st.columns(3)  # fixed width, so a single button stays small
    for col, (label, url) in zip(cols, active.items()):
        col.link_button(label, url, use_container_width=True)


def badges(items):
    """Show technology tags on a single line using Streamlit badges."""
    st.markdown(" ".join(f":blue-badge[{i}]" for i in items))


st.set_page_config(page_title=f"{NAME} | Portfolio", page_icon="📊", layout="wide")

# ------------------------------------------------------------------ hero
left, right = st.columns([3, 1], vertical_alignment="center")
with left:
    st.caption("Hello, I'm")
    st.title(f":blue[{NAME}]")
    st.subheader(f":blue[{TITLE}]")
    st.write(TAGLINE)
    if LOCATION:
        st.caption(f"📍 {LOCATION}")

    cv_file = Path(CV_PATH)
    btn_cv, btn_hi, _ = st.columns([1, 1, 2])
    with btn_cv:
        if cv_file.exists():
            st.download_button(
                "⬇ Download CV", cv_file.read_bytes(), file_name=cv_file.name,
                mime="application/pdf", type="primary", use_container_width=True,
            )
        else:
            st.caption(f"Add your CV at `{CV_PATH}`")

with right:
    if Path(PHOTO_PATH).exists():
        st.image(PHOTO_PATH)

st.divider()

# ----------------------------------------------------------------- about

st.header("About Me", divider="blue")
for para in ABOUT:
    st.write(para)
for col, (label, value) in zip(st.columns(len(STATS)), STATS):
    with col:
        with st.container(border=True):
            st.metric(label, value)

st.divider()

# ---------------------------------------------------------------- skills
st.header("Skills", divider="blue")
groups = list(SKILLS.items())
for i in range(0, len(groups), 2):
    cols = st.columns(2)
    for col, (group, info) in zip(cols, groups[i:i + 2]):
        with col:
            with st.container(border=True):
                st.subheader(group)
                if info["status"]:
                    st.caption(f"🌱 {info['status']}")
                badges(info["items"])

st.divider()

# -------------------------------------------------------------- projects
st.header("Projects", divider="blue")
for p in PROJECTS:
    with st.container(border=True):
        st.subheader(p["title"])
        st.caption(p["subtitle"])
        st.write(p["description"])

        left, right = st.columns(2)
        with left:
            st.markdown("**Key highlights**")
            for h in p["highlights"]:
                st.markdown(f"- {h}")
        with right:
            st.markdown("**Technologies**")
            badges(p["tech"])

        link_row(p["links"])
st.divider()

# ------------------------------------------------------------ experience
st.header("Experience", divider="blue")
for x in EXPERIENCE:
    with st.container(border=True):
        st.markdown(f"**{x['role']}**")
        st.caption(f"{x['org']} · {x['period']}")
        for point in x["points"]:
            st.markdown(f"- {point}")

st.divider()

st.header("Services", divider="blue")
st.write(SERVICES_INTRO)
for col_left, col_right in zip(SERVICES[0::2], SERVICES[1::2] + [None]):
    cols = st.columns(2)
    for col, s in zip(cols, (col_left, col_right)):
        if s is None:
            continue
        with col:
            with st.container(border=True):
                st.subheader(s["title"])
                st.write(s["description"])
                badges(s["tech"])
                subject = quote(f"Project inquiry: {s['title']}")
                st.link_button("Discuss Project", f"mailto:{EMAIL}?subject={subject}")
st.divider()


# --------------------------------------------------------------- contact
st.header("Contact", divider="blue")
form_col, info_col = st.columns([3, 2])
with form_col:
    with st.form("contact_form"):
        name = st.text_input("Your name")
        email = st.text_input("Your email")
        message = st.text_area("Message", height=140)
        sent = st.form_submit_button("Prepare message")
    if sent:
        if not (name and message):
            st.warning("Please enter your name and a message.")
        else:
            body = f"{message}\n\n— {name} ({email})"
            mailto = f"mailto:{EMAIL}?subject={quote('Portfolio message from ' + name)}&body={quote(body)}"
            st.success("Your message is ready. Click below to send it from your email app.")
            st.link_button("Open email app ✉", mailto)
with info_col:
    with st.container(border=True):
        st.subheader("Let's work together")
        st.write("Have a dashboard, analysis or ML idea? Send me a message or reach out directly.")
        st.write(f"✉ {EMAIL}")
        for label, url in SOCIAL_LINKS.items():
            if url:
                st.link_button(label, url, use_container_width=True)

st.caption(f"© 2026 {NAME} · Built with Streamlit")
