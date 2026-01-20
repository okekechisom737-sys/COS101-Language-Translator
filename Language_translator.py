import streamlit as st

# ================= IGBO (20 words) =================
igbo = {
    "hello": "ndewo",
    "good morning": "ututu oma",
    "good evening": "mgbede oma",
    "thank you": "daalu",
    "please": "biko",
    "water": "mmiri",
    "food": "nri",
    "house": "ulo",
    "man": "nwoke",
    "woman": "nwanyi",
    "child": "nwa",
    "school": "ulo akwukwo",
    "book": "akwukwo",
    "market": "ahia",
    "money": "ego",
    "friend": "enyi",
    "love": "ihunanya",
    "road": "uzo",
    "sun": "anya anyanwu",
    "rain": "mmiri ozuzo"
}

# ================= HAUSA (20 words) =================
hausa = {
    "hello": "sannu",
    "good morning": "ina kwana",
    "good evening": "ina wuni",
    "thank you": "na gode",
    "please": "don Allah",
    "water": "ruwa",
    "food": "abinci",
    "house": "gida",
    "man": "namiji",
    "woman": "mace",
    "child": "yaro",
    "school": "makaranta",
    "book": "littafi",
    "market": "kasuwa",
    "money": "kudi",
    "friend": "aboki",
    "love": "so",
    "road": "hanya",
    "sun": "rana",
    "rain": "ruwan sama"
}

# ================= TIV (20 words) =================
tiv = {
    "hello": "m sugh",
    "good morning": "m sugh u dedoo",
    "good evening": "m sugh u nger",
    "thank you": "doo",
    "please": "kpaa",
    "water": "inya",
    "food": "mger",
    "house": "ya",
    "man": "or",
    "woman": "kwase",
    "child": "wan",
    "school": "shule",
    "book": "ikav",
    "market": "mbakange",
    "money": "kudi",
    "friend": "wam",
    "love": "doo u ikyo",
    "road": "kwagh",
    "sun": "tser",
    "rain": "orvese"
}

# ================= YORUBA (20 words) =================
yoruba = {
    "hello": "bawo",
    "good morning": "ekaaro",
    "good evening": "ekale",
    "thank you": "ese",
    "please": "jowo",
    "water": "omi",
    "food": "ounje",
    "house": "ile",
    "man": "okunrin",
    "woman": "obinrin",
    "child": "omo",
    "school": "ile iwe",
    "book": "iwe",
    "market": "oja",
    "money": "owo",
    "friend": "ore",
    "love": "ife",
    "road": "ona",
    "sun": "oorun",
    "rain": "ojo"
}

languages = {
    "Igbo": igbo,
    "Hausa": hausa,
    "Tiv": tiv,
    "Yoruba": yoruba
}

# ================= STREAMLIT UI =================
st.set_page_config(page_title="African Language Translator", page_icon="🌍")

st.title("🌍 African Language Translator")
st.write("Translate English words into **Igbo, Hausa, Tiv, and Yoruba**")

language = st.selectbox("Select Language", list(languages.keys()))
word = st.text_input("Enter an English word")

if st.button("Translate"):
    word = word.lower().strip()
    if word == "":
        st.warning("Please enter a word")
    else:
        result = languages[language].get(word, "Word not found")
        st.success(f"Translation in {language}: **{result}**")
