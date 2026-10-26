import streamlit as st
from pathlib import Path

st.title("👋 My Bio")

# ---------- TODO: Replace with your own info ----------
NAME = "Norma Gonzalez"
PROGRAM = "Major Data Science and minor in Computer science "
INTRO = (
    "Hi my name is Norma and I am studying data science, at this moment I do not know what I would to do after college. I feel like I love cleaning up data but I need to
    find more time to really focus on practicing how to do that. I am also not very well with python, I feel like R program is very intresting to me. "
    "what excites me about data visualization is the way we are able to put all the collected data in a picture. What I mean by that is when we put it either in 
    a chart or bar graph, to me that is always intresting."
)
FUN_FACTS = [
    "I love reading horror books and love halloween ",
    "I love to play video games when I have the time",
    "I would want to travel the world ",
]


PHOTO_PATH = "patrick-star-funny-.jpg"  # Put a file in repo root or set a URL


def find_photo(filename=PHOTO_PATH):
    # Try common locations for multipage apps
    try:
        script_dir = Path(__file__).resolve().parent
    except NameError:
        script_dir = Path.cwd()

    candidates = [
        script_dir / "assets" / filename,          # pages/assets/...
        script_dir.parent / "assets" / filename,   # root/assets/... (common)
        Path("assets") / filename,                 # cwd/assets/...
    ]
    for p in candidates:
        if p.exists():
            return str(p)
    return None

photo_src = find_photo(PHOTO_PATH)

# ---------- Layout ----------
col1, col2 = st.columns([1, 2], vertical_alignment="center")

with col1:
    if photo_src:
        st.image(photo_src, caption=NAME, use_container_width=True)
    else:
        st.info(
            "📷 Place `Your_Photo.jpg` inside an `assets/` folder at the app root "
            "or update the path in `find_photo()`."
        )
        
with col2:
    st.subheader(NAME)
    st.write(PROGRAM)
    st.write(INTRO)

st.markdown("### Fun facts")
for i, f in enumerate(FUN_FACTS, start=1):
    st.write(f"- {f}")

st.divider()
st.caption("Edit `pages/1_Bio.py` to customize this page.")
