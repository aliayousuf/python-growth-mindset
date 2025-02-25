import streamlit as st
import random
import datetime



st.set_page_config(
    page_title="Mindset Mastery Hub",
    page_icon="🚀",
    layout="wide"
)

# Apply custom background style

st.markdown(
    """
    <style>
        /* Full page gradient background */
        .stApp {
            background: linear-gradient(to right, #E0C3FC, #8EC5FC);
            color: #4A0072;
        }

        /* Sidebar styling */
        .css-1d391kg {
            background: linear-gradient(to bottom, #D8BFD8, #E0C3FC);
            color: #4A0072;
        }

        /* Style headers */
        h1, h2, h3, h4, h5, h6 {
            color: #4A0072 !important;
            text-shadow: 1px 1px 4px rgba(0,0,0,0.2);
        }

        /* Fix interactive elements losing cursor */
        .stTextInput > div, 
        .stTextArea > div, 
        .stSelectbox > div {
            background: white !important;
            color: #4A0072 !important;
            border-radius: 8px !important;
            padding: 10px !important;
            box-shadow: 0px 4px 6px rgba(0,0,0,0.1) !important;
        }

        /* Buttons */
        .stButton>button {
            background: linear-gradient(to right, #D8BFD8, #E0C3FC);
            color: #4A0072;
            border-radius: 12px;
            transition: 0.3s;
            font-weight: bold;
        }

        .stButton>button:hover {
            background: linear-gradient(to right, #C3A1D8, #D8BFD8);
            transform: scale(1.05);
            box-shadow: 0px 4px 10px rgba(0,0,0,0.2);
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Initialize session state variables only if they don't exist
if "journal_entries" not in st.session_state:
    st.session_state.journal_entries = []
if "progress" not in st.session_state:
    st.session_state.progress = 0
if "quiz_score" not in st.session_state:
    st.session_state.quiz_score = 0
if "quiz_attempted" not in st.session_state:
    st.session_state.quiz_attempted = 0
if "quiz_answers" not in st.session_state:
    st.session_state.quiz_answers = {}
if "selected_challenge" not in st.session_state:
    st.session_state.selected_challenge = None
if "quiz_submitted" not in st.session_state:
    st.session_state.quiz_submitted = False
if "mood" not in st.session_state:
    st.session_state.mood = "😊 Happy"
if "goal" not in st.session_state:
    st.session_state.goal = ""

# Sidebar Navigation
st.sidebar.title("🚀 Mindset Mastery Hub")
page = st.sidebar.radio("Explore", ["Dashboard", "Daily Challenge", "Quiz Arena", "Inspiring Tales", "Reflection Journal", "Track Progress"])

# Dashboard
if page == "Dashboard":
    st.title("🚀 Welcome to Mindset Mastery Hub!")
    st.markdown("""
        ### Unlock Your Full Potential:
        - 🌟 **Daily mindset challenges** to fuel your growth.
        - 🧩 **Interactive quizzes** to test your knowledge.
        - 📖 **Stories of resilience** to keep you motivated.
        - ✍ **Personal journal** to reflect on progress.
        - 🎯 **Track your progress** to stay on course.
    """)
    st.write("🌈 Start your transformation today!")

# Daily Challenge
elif page == "Daily Challenge":
    st.title("🎯 Today's Challenge")
    
    challenges = [
        "Write down a fear and take one small step to overcome it.",
        "Tackle a problem using a completely new approach.",
        "Explain something complex in simple terms to a friend.",
        "Reframe a negative thought into a positive lesson.",
        "Do something outside your comfort zone and reflect on it."
    ]
    
    # Retain selected challenge
    st.session_state.selected_challenge = st.selectbox(
        "Choose your challenge for today:", 
        challenges, 
        index=challenges.index(st.session_state.selected_challenge) if st.session_state.selected_challenge else 0
    )

    st.subheader(st.session_state.selected_challenge)
    st.success("Remember: Growth starts at the edge of your comfort zone!")

# Quiz Arena
elif page == "Quiz Arena":
    st.title("🧠 Mindset Quiz Challenge")

    questions = {
        "What is the core principle of a growth mindset?": ["Avoiding failure", "Embracing challenges", "Sticking to what you know"],
        "Which mindset helps you learn from mistakes?": ["Fixed mindset", "Growth mindset", "No mindset"],
        "How should you respond to constructive criticism?": ["Ignore it", "Take it personally", "Use it for improvement"],
        "What should you do when a task feels too difficult?": ["Give up", "Look for strategies to improve", "Complain about it"]
    }

    correct_answers = {
        "What is the core principle of a growth mindset?": "Embracing challenges",
        "Which mindset helps you learn from mistakes?": "Growth mindset",
        "How should you respond to constructive criticism?": "Use it for improvement",
        "What should you do when a task feels too difficult?": "Look for strategies to improve"
    }

    for question, options in questions.items():
        if question not in st.session_state.quiz_answers:
            st.session_state.quiz_answers[question] = None  

        st.session_state.quiz_answers[question] = st.radio(
            question, options, 
            index=options.index(st.session_state.quiz_answers[question]) if st.session_state.quiz_answers[question] else None
        )

    if st.button("Submit Answers"):
        if None in st.session_state.quiz_answers.values():
            st.warning("⚠️ Please answer all questions before submitting!")
        else:
            st.session_state.quiz_score = sum(
                1 for q, a in st.session_state.quiz_answers.items() if a == correct_answers[q]
            )
            st.session_state.quiz_attempted += 1
            st.session_state.quiz_submitted = True  

    if st.session_state.quiz_submitted:
        st.write(f"### 🏆 Your Score: {st.session_state.quiz_score}/{len(questions)}")
        if st.session_state.quiz_score == 4:
            st.success("🎉 Perfect score! Keep up the amazing mindset!")
            st.balloons()
        elif st.session_state.quiz_score == 3:
            st.info("🌟 Great job! You're almost there!")
        elif st.session_state.quiz_score == 2:
            st.warning("👍 Good effort! Keep practicing!")
        else:
            st.error("💡 Keep learning! Mindset shifts take time!")

        st.write("### ✅ Correct Answers:")
        for question, answer in correct_answers.items():
            st.write(f"**{question}**")
            st.write(f"✔ Correct Answer: **{answer}**")

# Inspiring Tales
elif page == "Inspiring Tales":
    st.title("📖 Stories of Grit and Growth")
    stories = [
        "🌟 Walt Disney was once told he lacked imagination and had no good ideas. Today, his creative empire inspires millions worldwide.",
        "📚 J.K. Rowling faced multiple rejections before 'Harry Potter' became a global phenomenon. Her perseverance paid off!",
        "💡 Thomas Edison failed over 1,000 times before inventing the light bulb. His lesson? Failure is just another step toward success!",
        "🚀 Elon Musk encountered countless setbacks with Tesla and SpaceX, but his vision and resilience changed the future of technology.",
        "🎾 Serena Williams overcame injuries and setbacks to become one of the greatest athletes of all time. Hard work beats talent!"
    ]
    selected_stories = random.sample(stories, 3)
    for story in selected_stories:
        st.write(story)
        st.write("---")
    st.write("🌟 Every setback is a setup for a comeback! Keep pushing forward!")

# Reflection Journal
elif page == "Reflection Journal":
    st.title("📝 Personal Reflection")
    
    st.session_state.mood = st.selectbox("💭 How do you feel today?", ["😊 Happy", "😌 Calm", "🤔 Reflective", "😞 Struggling", "💪 Motivated"], index=["😊 Happy", "😌 Calm", "🤔 Reflective", "😞 Struggling", "💪 Motivated"].index(st.session_state.mood))
    st.session_state.goal = st.text_input("🎯 What's one goal for tomorrow?", st.session_state.goal)
    entry = st.text_area("✨ What did you learn today? Any breakthroughs or insights?")
    
    if st.button("Save Entry"):
        formatted_entry = f"{datetime.date.today()} | Mood: {st.session_state.mood} | Goal: {st.session_state.goal}\nReflection: {entry}"
        st.session_state.journal_entries.append(formatted_entry)
        st.success("📝 Reflection saved!")

    st.write("### 📜 Previous Entries")
    for saved_entry in st.session_state.journal_entries:
        st.write(saved_entry)
        st.write("---")


# Track Progress
elif page == "Track Progress":
    st.title("📊 Your Growth Tracker")

    st.session_state.progress = st.slider("How much have you improved this week?", 0, 100, st.session_state.progress)
    st.write(f"### 📈 Progress: {st.session_state.progress}%")
