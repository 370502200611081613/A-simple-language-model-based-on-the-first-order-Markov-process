"""
基于Markov过程的文本生成:
**此处我更改了markov_dict的格式，使其除了有单词种类还包含了数量**
markov_dict:  { 'word': [{ 'word':'word1', num : 1 }.....], ..... }
"""

import os
import random
import time
import sys

#text_path = 'feed.txt'
text_path = 'beatles.txt'
markov_dicts = {'':[]}   # Start of Sentence
sentence_sep = '.?!'    # 句子结束标志

def is_end(word):
    """ 判断word是否是句子结束标志"""
    return word[-1] in sentence_sep

def get_index(word, word_list):
    """ 获取word在word_list中的索引"""
    for i, item in enumerate(word_list):
        if item['word'] == word:
            return i
    return -1

def insert_word(word,lastword):
    index = get_index(word, markov_dicts[lastword])
    if index == -1:
        markov_dicts[lastword].append({'word': word, 'num': 1})
    else:
        markov_dicts[lastword][index]['num'] += 1

def parse(text):
    """ 分析text，产生相应的dict"""
    flag = True # 是否是句子开始
    for i in range(len(text)):
        if text[i] not in markov_dicts:
            markov_dicts[text[i]] = []
        if flag:
            insert_word(text[i], '')
            flag = False
        else:
            if is_end(text[i]):
                flag = True
            insert_word(text[i], text[i-1])
            
        word = text[i]

def choose_word(list_):
    """ 根据传入的list，随机选择一个单词，考虑权重"""
    total = sum([item['num'] for item in list_])
    rand_val = random.randint(1, total)
    cumulative = 0
    for item in list_:
        cumulative += item['num']
        if rand_val <= cumulative:
            return item['word']
    return list_[-1]['word']

def generate(num_sentences=1,word_min=5, word_max=50, iterations=100):
    """ 根据前面调用parse得到的dict，随机生成多个句子"""
    ans = []
    for _ in range(num_sentences):
        sentence = ''
        next_word=''
        last_word = ''
        for _ in range(word_max):
            num = 0
            cnt = 0
            while num < word_min:
                cnt += 1
                if cnt > iterations:  # 防止死循环
                    break
                next_word = choose_word(markov_dicts[last_word])
                if not is_end(next_word):
                    break
            
            sentence += next_word + ' '
            last_word = next_word
            num += 1
            if is_end(next_word):
                break
        ans.append(sentence.strip())
    return ans
        

def input_text(_path_):
    text = []
    with open(_path_, 'r', encoding='utf-8') as f:
        for line in f:
            text.extend(line.strip().split())
    return text

def markov_main():
    start_time = time.time()
    text = input_text(text_path)
    #text= 'X Y Z. X Z Y? Y X Z! Z Z Z. Y Z Y.'.strip().split()
    end_time = time.time()
    print('读取文本用时: %.1f 毫秒' % (1000*(end_time - start_time)))
    start_time = time.time()
    parse(text)
    end_time = time.time()
    print('分析文本用时: %.1f 毫秒，读取词数：%d' % (1000*(end_time - start_time), len(text)))
    print('字典体积：%.1f kb' % (sys.getsizeof(markov_dicts)/1024))
    n = 4
    start_time = time.time()
    list_ = generate(n,3,40,2)
    end_time = time.time()
    for i in range(len(list_)):
        print(i+1,': ', list_[i])
    print('生成%d条文本用时: %.1f 毫秒，平均用时%.2f毫秒' % (n,1000*(end_time - start_time), 1000*(end_time - start_time)/n))

if __name__ == '__main__':
    markov_main()

