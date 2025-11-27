# A-simple-language-model-based-on-the-first-order-Markov-process

markov.pdf：文件说明  
beatles.txt：使用The Beatles的《Help!》歌词作为训练文本，230词  
feed.txt：使用AI生成的句子作为训练文本，  
markov_text.py：可编译python源码  

# 关于如何使用

将源码markov_text.py与训练文本放在同一目录下，更改变量text_path为训练文本相对目录。  
text_path 默认为"beatles.txt",满足题文要求。  
另有feed.txt为大量分类训练文本。共用14组，每组50个简单句和50个复合句。主题分别是：  
Animals; Trees and flowers; City and countryside; Buildings and public facilities; Food and drinks;
Dining and cooking; House; Clothes and accessories; Transportation; Life and careers;
Daily necessities; Natural science; Sports; Musical instruments

生成函数generate有4个参数，分别是生成句数，词数下限，词数上限，迭代次数。  
生成句子时不一定满足下限，这是避免死循环的让步。超过上限的句子会被截断。  
每个句子终止操作触发次数上限为迭代次数。超过此次数时强制结束句子。提高迭代次数会减少句长低于下限的可能，
但会显著增加时间复杂度。  

加入了计时器以便分析时间复杂度。  
加入了内存分析器以查看内存占用  

#  运行示例

采取参数：文本'X Y Z. X Z Y? Y X Z! Z Z Z. Y Z Y.'  
num_sentences=4,word_min=3, word_max=20, iterations=1  

<img width="501" height="181" alt="image-20251127112203074" src="https://github.com/user-attachments/assets/3114027e-dba7-4da6-b88d-64da69321188" />

采取参数：训练模型beatles.txt  
num_sentences=4,word_min=5, word_max=20, iterations=5  

<img width="810" height="180" alt="image-20251127112450443" src="https://github.com/user-attachments/assets/540fa7a1-f8aa-4157-b81d-1554d01ee4a9" />

采取参数：训练模型feed.txt  
num_sentences=3,word_min=50, word_max=800, iterations=1000  

<img width="1569" height="254" alt="image-20251127235652652" src="https://github.com/user-attachments/assets/27416079-1b5d-4c85-b533-df8edaed159b" />

