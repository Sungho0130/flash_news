from .model_set import Summarize



def summary(content_text : str):
    # sum = []
    # summarize = Summarize('C:/Users/Admin/OneDrive/바탕 화면/python_Ai/파이널 프로젝트/web_test/main_page/fine')
    summarize = Summarize('hyunwoongko/kobart','hyunwoongko/kobart')

    # for i in content_text:

    if content_text and len(content_text) > 500:
        content_text = content_text[:500]
    else:
        content_text = content_text[:len(content_text)]



    return summarize(content_text)