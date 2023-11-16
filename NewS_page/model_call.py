from .model_set import Summarize



def summary(content_text : str):
    summarize = Summarize('kykim/bertshared-kor-base','kykim/bertshared-kor-base')


    if content_text and len(content_text) > 500:
        content_text = content_text[:500]
    else:
        content_text = content_text[:len(content_text)]



    return summarize(content_text)