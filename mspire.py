import re
import json
import traceback
import wiki_scraping
from openai import OpenAI

def make_inspire(title_in=None, target_lang='zh'):
    success = True
    exception = None
    try:
        title, summary = wiki_scraping.get_page(title_in, target_lang)
        if not summary or summary.isspace():
            raise Exception('MSpire got no return')
        prompt = f"利用提供的以下信息, 主动和我简单地聊聊{re.sub('_', '', title)}: {summary} 你只应使用自然语言, 以聊天语气对话, 并在每句开始时以方括号中的文字表示情绪."
        if target_lang == 'en':
            prompt += '\n你应当使用英文回答.\nAnswer in English.'
        else:
            prompt += '\n你应当使用中文回答.'
        message = json.dumps({"role": "user", "content": prompt}, ensure_ascii=False)
    except Exception as excepted:
        #traceback.print_exc()
        success = False
        exception = excepted
    #print(summary)
    return success, exception, prompt


if __name__ == '__main__':
   print(make_inspire(target_lang='en')[2])