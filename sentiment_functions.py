from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

#finding the sentiment scores for a paragraph
def sentiment_scores(paragraph):
    intensity = SentimentIntensityAnalyzer()
    sentiment_dict = intensity.polarity_scores(paragraph)
    percentage_pos = sentiment_dict['pos']*100
    return percentage_pos


def writing_to_file(title, body_text, file):
    if len(body_text) > 1:
        body = body_text[0].text
        for i in range(0, len(body_text)):
            text = body_text[i].text
            body += "//" + text
    else:
        body = body_text[0].text
    title_article = '"%s"'% title.text
    text_article = '"%s"'% body
    positivity_score = sentiment_scores(text_article)
    statement = title_article + ", " + text_article  + ", " + str(round(positivity_score,2))+"%" + "\n"
    file.write(statement)
    return(positivity_score)
