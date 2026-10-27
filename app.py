import os
from datetime import datetime

import numpy as np
import pandas as pd
import streamlit as st

NAME = "Andre Martin B. Camasura"
SECTION = "CS365 - F2"
PROGRAM = "BS Computer Science"            
YEAR = "3rd Year"                          
TAGLINE = "Aspiring Software engineer who loves turning messy data into useful tools."  
EMAIL = "andrecamasura144@gmail.com"                  
PHOTO_PATH = "profile.png" 

SHORT_BIO = (
    "Hello, I'm Andre Martin B. Camasura, a 3rd-year BS Computer Science student at Cebu Institute of Technology University. I have a strong passion for software engineering and data analysis, and I'm always eager to learn new technologies and improve my skills. This portfolio showcases my journey, skills, projects,"
)

BACKGROUND = (
    "I was born at a very young age and I was raised in Cebu City, here in Tisa. Growing up, I wasn't very tech savy, the only exposre I had to tech or computer science was those Disney shows where they say 'they're past the fire wall', or 'broken the mainframe'. "
    "I became interested in the field when I had a Java programming class in grade 10, I really liked it, I thought 'maybe i don't need to take engineering and be away from the difficult math' (man, little did I know). Now, I am in my 3rd year, and I still have a long way to go, but I am excited."
)
EDUCATION = [  
    ("2022 - Present", "Cebu Institute of Technology University", "BS Computer Science"),
    ("2022 - 2024", "Asian College of Technology", "STEM Strand"),
    ("2021 - 2022", "University of San Jose Recoletos - Basak", "only grade 10"),
    ("2012 - 2021", "B.R.I.G.H.T Academy", "Elementary until grade 9"),
]
INTERESTS = ["Music", "Avatar the Last Airbender franchise!!!", "Hongkong films", "Data Science", "Football", "Running"] 
MILESTONES = [  
    (2015, "Wrote my first HTML page"),
    (2022, "Built my first full project, java calculator app"),
    (2023, "Built my first robot using Arduino"),
    (2024, "Began my CS journey at CIT-U"),
]

SKILLS = pd.DataFrame(  
    {
        "Skill": ["Python", "SQL", "Streamlit", "Java", "C/C++", "C#", "Kotlin",
                  "Node.js", "Django", "Tailwind CSS", "Teamwork", "Leadership", "Git/GitHub"],
        "Level": [60, 70, 40, 75, 75, 75, 65, 60, 50, 40, 100, 90, 80],
        "Category": ["Technical", "Technical", "Technical", "Technical", "Technical", "Technical",
                     "Technical", "Technical", "Technical", "Technical", "Soft", "Soft", "Technical"],
    }
)

PROJECTS = [  
    {
        "title": "CivicGuard",
        "category": "Software Application",
        "role": "Backend developer",
        "tools": ["Java", "MariaDB", "Leaflet.js", "Git"],
        "outcome": "Presented to my OOP 2 class and awarded best UI/UX and best capstone idea by my professor.",
        "link": "https://github.com/kworuu/CivicGuard",
    },
    {
        "title": "Piyesa: Picture to ready-to-checkout cart",
        "category": "Web Application",
        "role": "Backend developer, AI integration, and team lead",
        "tools": ["Node.js", "Google Gemini API", "HTML/CSS/JS"],
        "outcome": "Reached 88% accuracy on a test set and was able to create a checkout cart.",
        "link": "https://github.com/kworuu/piyesa",
    },
    {
        "title": "ToolShedd: Community tool sharing platform",
        "category": "Android Application",
        "role": "Solo developer",
        "tools": ["Kotlin", "Firebase", "Google maps API"],
        "outcome": "Professor rated it highly",
        "link": "https://github.com/kworuu/ToolShedd",
    },
]

FUN_FACTS = [ 
    "I can do a backflip from a 14 feet ledge.",
    "I am my best at debugging code when I am tired and sleepy.",
    "I can only code while listening to techno and acid music.",
]

# ---------------------------------------------------------------------------
# PAGE SETUP
# ---------------------------------------------------------------------------
st.set_page_config(
    page_title=f"{NAME} | Portfolio",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.session_state.setdefault("likes", 0)
st.session_state.setdefault("messages", [])
st.session_state.setdefault("fact_idx", 0)


def placeholder_photo(size=300):
    """Generate a gradient stand-in image so the page works without a photo."""
    x = np.linspace(0, 1, size)
    xx, yy = np.meshgrid(x, x)
    img = np.stack([79 + 100 * xx, 70 + 120 * yy, 229 - 80 * xx], axis=-1)
    return img.astype(np.uint8)


def show_photo():
    if os.path.exists(PHOTO_PATH):
        st.image(PHOTO_PATH, caption=NAME, width="stretch")
    else:
        st.image(placeholder_photo(), caption="Stand-in photo (add profile.jpg)",
                 width="stretch")


# ---------------------------------------------------------------------------
# SIDEBAR
# ---------------------------------------------------------------------------
with st.sidebar:
    show_photo()
    st.markdown(f"### {NAME}")
    st.caption(f"{PROGRAM} | {YEAR}")
    st.caption(f"{SECTION}")
    st.divider()

    st.subheader("Page options")
    show_skill_table = st.checkbox("Show skills table", value=True)
    chart_type = st.radio("Skills chart style", ["Bar", "Line"], horizontal=True)
    min_level = st.slider("Minimum skill level", 0, 100, 50, step=5)

    st.divider()
    if st.button("Like this portfolio"):
        st.session_state.likes += 1
        st.toast("Thanks for the like!")
    st.write(f"Likes this session: **{st.session_state.likes}**")

# ---------------------------------------------------------------------------
# HEADER
# ---------------------------------------------------------------------------
st.title(f"Hi, I'm {NAME}")
st.subheader(TAGLINE)
st.caption(f"{SECTION}  |  {PROGRAM}, {YEAR}")

m1, m2, m3, m4 = st.columns(4)
m1.metric("Projects", len(PROJECTS))
m2.metric("Skills tracked", len(SKILLS))
m3.metric("Top skill", SKILLS.loc[SKILLS["Level"].idxmax(), "Skill"],
          f"{SKILLS['Level'].max()}%")
m4.metric("Average skill level", f"{SKILLS['Level'].mean():.0f}%")

st.divider()

# ---------------------------------------------------------------------------
# MAIN TABS
# ---------------------------------------------------------------------------
tab_about, tab_auto, tab_skills, tab_projects, tab_contact = st.tabs(
    ["About", "Autobiography", "Skills", "Projects", "Contact"]
)

# ---- ABOUT ----------------------------------------------------------------
with tab_about:
    left, right = st.columns([1, 2], gap="large")
    with left:
        show_photo()
    with right:
        st.header("About me")
        st.write(SHORT_BIO)
        st.markdown(
            f"""
- **Name:** {NAME}
- **Program:** {PROGRAM}
- **Year:** {YEAR}
- **Section:** {SECTION}
- **Email:** {EMAIL}
"""
        )
        st.markdown("**Interests:** " + " | ".join(f"`{i}`" for i in INTERESTS))

        st.subheader("Fun fact")
        st.info(FUN_FACTS[st.session_state.fact_idx])
        if st.button("Another fun fact"):
            st.session_state.fact_idx = (st.session_state.fact_idx + 1) % len(FUN_FACTS)
            st.rerun()

# ---- AUTOBIOGRAPHY --------------------------------------------------------
with tab_auto:
    st.header("My story")
    c1, c2 = st.columns(2, gap="large")

    with c1:
        st.subheader("Background")
        st.write(BACKGROUND)

        st.subheader("Education")
        edu_df = pd.DataFrame(EDUCATION, columns=["Years", "School", "Level / Program"])
        st.table(edu_df)

    with c2:
        st.subheader("Milestones")
        for year, text in MILESTONES:
            st.markdown(f"**{year}** — {text}")

        st.subheader("Milestone explorer")
        picked = st.selectbox("Pick a year", [y for y, _ in MILESTONES])
        st.success(dict(MILESTONES)[picked])

        st.subheader("Interests")
        chosen = st.multiselect("What would you like to chat about?",
                                INTERESTS, default=INTERESTS[:2])
        if chosen:
            st.write("Great, let's talk about: " + ", ".join(chosen) + ".")

    with st.expander("Read my autobiography as plain text"):
        story = (
            f"{NAME}\n{PROGRAM}, {YEAR} ({SECTION})\n\n"
            f"About: {SHORT_BIO}\n\nBackground: {BACKGROUND}\n\nMilestones:\n"
            + "\n".join(f"- {y}: {t}" for y, t in MILESTONES)
        )
        st.text(story)
        st.download_button("Download autobiography (.txt)", story,
                           file_name="autobiography.txt")

# ---- SKILLS ---------------------------------------------------------------
with tab_skills:
    st.header("Skills")
    cats = st.multiselect("Categories", sorted(SKILLS["Category"].unique()),
                          default=sorted(SKILLS["Category"].unique()))
    view = SKILLS[(SKILLS["Level"] >= min_level) & (SKILLS["Category"].isin(cats))]

    if view.empty:
        st.warning("No skills match the current filters. Lower the minimum level in the sidebar.")
    else:
        c1, c2 = st.columns([2, 1], gap="large")
        with c1:
            chart_df = view.set_index("Skill")[["Level"]]
            if chart_type == "Bar":
                st.bar_chart(chart_df)
            else:
                st.line_chart(chart_df)
        with c2:
            if show_skill_table:
                st.dataframe(view, hide_index=True, width="stretch")
            st.download_button("Download skills (.csv)",
                               view.to_csv(index=False), file_name="skills.csv",
                               mime="text/csv")

        st.subheader("Progress bars")
        for _, row in view.iterrows():
            st.write(row["Skill"])
            st.progress(int(row["Level"]))

# ---- PROJECTS -------------------------------------------------------------
with tab_projects:
    st.header("Projects")
    categories = ["All"] + sorted({p["category"] for p in PROJECTS})
    f1, f2 = st.columns(2)
    category = f1.selectbox("Filter by type", categories)
    all_tools = sorted({t for p in PROJECTS for t in p["tools"]})
    tool_filter = f2.multiselect("Filter by tool", all_tools)

    shown = [
        p for p in PROJECTS
        if (category == "All" or p["category"] == category)
        and (not tool_filter or set(tool_filter) & set(p["tools"]))
    ]
    st.caption(f"Showing {len(shown)} of {len(PROJECTS)} projects")

    cols = st.columns(3) if shown else []
    for col, p in zip(cols, shown):
        with col.container(border=True):
            st.subheader(p["title"])
            st.markdown(f"**Role:** {p['role']}")
            st.markdown("**Tools:** " + ", ".join(f"`{t}`" for t in p["tools"]))
            st.markdown(f"**Outcome:** {p['outcome']}")
            st.link_button("View project", p["link"])
    if not shown:
        st.info("No projects match those filters.")

# ---- CONTACT --------------------------------------------------------------
with tab_contact:
    st.header("Contact / feedback")
    left, right = st.columns([2, 1], gap="large")

    with left:
        with st.form("contact_form", clear_on_submit=True):
            who = st.text_input("Your name")
            email = st.text_input("Your email")
            reason = st.selectbox("Reason", ["Feedback", "Collaboration", "Question", "Just saying hi"])
            rating = st.slider("How would you rate this site?", 1, 5, 4)
            message = st.text_area("Message", height=120)
            subscribe = st.checkbox("Send me a copy of my message")
            submitted = st.form_submit_button("Send")

        if submitted:
            if not who.strip() or not message.strip():
                st.error("Please enter at least your name and a message.")
            else:
                st.session_state.messages.append(
                    {"time": datetime.now().strftime("%H:%M:%S"), "name": who,
                     "reason": reason, "rating": rating}
                )
                st.success(f"Thanks, {who}! Your {reason.lower()} was received. "
                           f"I'll reply to {email or 'you'} soon.")
                if subscribe:
                    st.info("A copy would be sent to your email (demo only).")

    with right:
        st.subheader("This session")
        if st.session_state.messages:
            st.dataframe(pd.DataFrame(st.session_state.messages), hide_index=True)
            if st.button("Clear messages"):
                st.session_state.messages = []
                st.rerun()
        else:
            st.caption("No messages sent yet.")

# ---------------------------------------------------------------------------
# FOOTER
# ---------------------------------------------------------------------------
st.divider()
st.caption(f"© {datetime.now().year} {NAME} | {SECTION} | Built with Streamlit")