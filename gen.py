import streamlit as st
import random
import nltk

nltk.download("wordnet")
from nltk.corpus import wordnet as wn


def get_fav_item(fav):
    """
    Get synonym of the favourite thing
    """
    # initialise empty list
    item_list = []
    # loop thorugh all the synonym
    for item in wn.synsets(fav):
        # extract word
        item_list.append(str(item).replace("Synset('", "").split(".")[0])
    # remove duplicate
    item_list = list(set(item_list))
    # return random synonym
    return item_list[random.randint(0, (len(item_list) - 1))]


# initialise dictionaries
pronoun_dict = {"her": "Lady ", "him": "Sir ", "other": ""}
title_dict = {"her": ", Mistress of ", "him": ", Lord of ", "other": ""}


# show headers
st.subheader("KSL proudly presents:")
st.header("Castle Cumalot Royalty Title Generator")

# get pronoun
pronoun = st.radio(label="choose pronoun", options=["her", "him"])
# get name
name = st.text_input(label="your name")

# get favourite thing 1
fav1 = st.text_input(label="Something you enjoy")
if fav1:
    fav1 = get_fav_item(fav1)

else:
    fav1 = ""

# get favourite thing 2
fav2 = st.text_input(label="Another thing you enjoy")
if fav2:

    fav2 = get_fav_item(fav2)
else:
    fav2 = ""

# get favourite thing 3
fav3 = st.text_input(label="And another one!")
if fav3:

    fav3 = get_fav_item(fav3)
else:
    fav3 = ""

title = pronoun_dict[pronoun] + name
if len(fav1) > 0:
    title = title + title_dict[pronoun] + fav1
    if (len(fav2) + len(fav3)) == 0:
        title = title + "!"

if (len(fav2) > 0) & (len(fav3) == 0):
    title = title + " and " + fav2 + "!"
else:
    title = title + ", " + fav2 + " and " + fav3 + "!"
generate = st.button("bestow thy title")

if generate:
    st.subheader("All hail")
    st.header(title)
    gif_number = random.randint(0, 4)
    if gif_number == 0:
        st.markdown(
            f'<iframe src="https://giphy.com/embed/wsncUQAWt1Z74JDipx" width="480" height="360" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>',
            unsafe_allow_html=True,
        )
    if gif_number == 1:
        st.markdown(
            f'<iframe src="https://giphy.com/embed/2gS1FmUodZ3Cio2fsR" width="480" height="480" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>',
            unsafe_allow_html=True,
        )
    if gif_number == 2:
        st.markdown(
            f'<iframe src="https://giphy.com/embed/hULEICa1CJFtIGrePQ" width="480" height="480" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>',
            unsafe_allow_html=True,
        )
    if gif_number == 3:
        st.markdown(
            f'<iframe src="https://giphy.com/embed/diss1MXzXlA8o" width="480" height="270" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>',
            unsafe_allow_html=True,
        )
