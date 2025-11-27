# A-simple-language-model-based-on-the-first-order-Markov-process
markov.pdf：文件说明  
beatles.txt：使用The Beatles的《Help!》歌词作为训练文本  
feed.txt：使用AI生成的句子作为训练文本  
markov_text.py：可编译python源码  
# 关于如何使用
将源码markov_text.py与训练文本放在同一目录下，更改变量text_path为训练文本相对目录。  
text_path 默认为"beatles.txt",满足题文要求。  
另有feed.txt为大量分类训练文本。共用14组，每组50个简单句和50个复合句。主题分别是：  
animals; trees and flowers; 
