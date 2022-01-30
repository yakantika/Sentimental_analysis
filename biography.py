import nltk.sentiment
analyzer = nltk.sentiment.SentimentIntensityAnalyzer()
import streamlit as st
st.title('Sentimental analysis')
st.write("Tired! want to vent out your thoughts")
st.write("Enter your thoughts here")

def main():
    #while True:
        user_text = st.text_input("?")
        score = get_sentiment(user_text)
        reaction = get_reaction(score)
        st.write(reaction)
        st.write(score)
        st.write('')

def get_reaction(score):
    """
    Parameter score: a float between -1 and +1
    Return: An emoji as a string!
    """
    if score > 0.5:  
        return "🥰"
    if score > 0:    
        return "🙂"
    if score == 0:   
        return "😶"
    if score < -0.5: 
        return "😢"
    if score < 0:    
        return "😟"

def get_sentiment(user_text):
    """
    Parameter user_text: any text (string)
    Return: a sentiment score between -1 and +1 (float)
    """
    # 1. pass the text into the analyzer.polarity_scores function, part of the nltk package
    scores = analyzer.polarity_scores(user_text)
    # 2. extract the sentiment score. Scores is a "dictionary" (covered on May 17th)
    sentiment_score = scores['compound']

    return sentiment_score

if __name__ == '__main__':
    main()