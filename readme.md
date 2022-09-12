test word

10个hw（有一个没有题目）

14个lab

12个disc

4个proj（除了最后一个，平均每个10题左右）

（注意：以下所有内容都基于20年秋季学期开设的CS61A）

## 课程简介

- 所属大学：UC Berkeley

- 先修要求：无

- 涉及编程语言：Python, Scheme, SQL

CS61A是UCB的编程入门课，以python作为主要的教学语言。UCB的教授以《Structure and Interpretation of Computer Programs》（大名鼎鼎的SICP）为蓝本，重新编写了以python（而不是scheme）为主要编程语言的一本教学书籍，并基于它讲授本门课程。

贯穿CS61A这一课程的核心其实就是“抽象“二字，从课本第一章（Building Abstractions with Functions）开始便强调abstraction；直至课程的末尾，虽然讲述的是解释器的原理，但本质上还是在从软件的整体角度介绍抽象概念。但在强调这一概念的同时，CS61A也很好地教授了scheme与python的基本语法（包含面向对象），基本的递归，一些基本的数据结构，并蜻蜓点水一般地提及了SQL的一些语法。

在本校中，与这门课相近定位的课程（仅对20级而论）为《计算导论与程序设计》，而后者主要以C为教学语言，且在各方面都远远逊色于本课程。因而，作为自学过该课程的人，强烈建议学有余力的同学能该门课程，它确实能帮你从OJ重复刷题的无趣中解放出来，重新以抽象的视角去分析与思考编程本身。

## 课程内容

- Lec
  
  上课的录播（类似于慕课的那种录播），一共38个Lec以及相对应的Q&A，其中一些是选学的教学内容。**建议Lec看一遍，而Q&A选择性看**，比如讲历年题就不用听了。

- Hw
  
  作业，一共10次（最后一次没有题目），一般是十道或以下的编程题+选择题。**建议完成。**

- Lab
  
  实验，一共14次，与作业类似，只是量可能更大。**建议完成。**

- Proj
  
  项目，一共4次，课程会预先提供有框架的项目文件，完成项目时仅需要根据提示完成每道问题即可，除了最后一个项目，一般是十道题左右。
  
  第一个项目是一个掷骰子的小游戏（python基本语法），第二个是英文打字游戏（递归+python自带的sequence），第三个是模仿植物大战僵尸的游戏（python面向对象），最后一个是编写一个scheme解释器（所有语法+解释器的工作原理）。**强烈建议完成。**

- Disc
  
  讨论，一共12次，每次有一张sheet，其上包含刚学的知识点与一些小练习。**可以完成。**

- Exam
  
  考试，一共3次。两次期中，一次期末。**可以完成。**



## 仓库结构

这里以目录的方式简单介绍本repo的结构。

- backup
  
  CS61A所有disc，exam，hw，lab以及proj原始文件的备份，以免不可抗力（在2022/09时网站仍能访问），今后会考虑搭建专用的网站存储backup。

- exercise
  
  我完成的所有disc，exam，hw，lab以及proj（截至目前还剩3个exam），可供参考。

- hint
  
  对于hw，lab与proj感觉在过程中遇到问题的部分都写了简短的hint，可供参考。

- mindmap
  
  根据课本内容整理的思维导图，使用的导图工具为xmind（可以官网下载免费版，~~或者吾爱破解~~）

## 学习资源

**课程资源**指的是学习课程本身就需要的资源，**相关资源**指的是我在学习时参考的资源，而**拓展**指的是学完本课后的加餐内容。

#### 课程资源

课程主页（fa20版本）：

https://inst.eecs.berkeley.edu/~cs61a/fa20/

课本：

http://composingprograms.com/

课本（中文翻译版，但是翻译的课本版本较老且内容不全）：

[第一章 使用函数构建抽象 - 1.1 引言 - 《SICP Python 描述 中文版（UCB CS61a 教材：SICP Python）》 - 书栈网 · BookStack](https://www.bookstack.cn/read/sicp-py-zh/1.1.md)

B站搬运的全套课程视频（感谢这位up主）：

https://www.bilibili.com/video/BV1s3411G7yM

课程提供的网页终端（用来运行python，scheme与sql语句）：

https://code.cs61a.org/

Python Tutor（可以用来运行python代码并识别其中的frame，课上会用）：

[Online Python Tutor - Composing Programs - Python 3](https://pythontutor.com/composingprograms.html#mode=edit)

CS61A的课程archive（收录了历年CS61A课程的资源，可以选择自己喜欢的版本去学习）：

https://inst.eecs.berkeley.edu/~cs61a/archives.html

#### 相关资源

csdiy（梦开始的地方，强烈建议通读一遍这位学长写的前言与规划部分。并在这里向其致以微不足道的谢意。）：

[UCB CS61A: Structure and Interpretation of Computer Programs - CS自学指南](https://csdiy.wiki/%E7%BC%96%E7%A8%8B%E5%85%A5%E9%97%A8/CS61A/)

Scheme语言简明教程（如果你在学习scheme中头痛可以看看，也可以作为手册进行简单的查阅）：

https://wizardforcel.gitbooks.io/teach-yourself-scheme/content/

#### 拓展

How to Design Programs（John教授在课上推荐的，关于编程的思维的一本书，笔者还未看过，这里仅作记录）：

https://htdp.org/

SICP（学完这门课真正让我有了去通读一遍它的想法）：

[Structure and Interpretation of Computer Programs - 2nd Edition (MIT) (豆瓣)](https://book.douban.com/subject/1451622/)

## Q&A

这里仅仅收录一些可能的常见的问题，欢迎在issue中或以邮件方式直接向我（rask0lnik0v@tutanota.com）提问。如有空闲我会逐一回答并更新在这里。**但是建议提问前先搜索一下“提问的智慧”**（[How To Ask Questions The Smart Way](http://www.catb.org/~esr/faqs/smart-questions.html)），**这样可能可以省下我们彼此不少的时间。**

Q1：我不会英语，能学这门课吗？

A1：这确实是最大的问题，没有之一。对于学CS61A的同学而言，不会英语其实是可以规避的，通过B站视频的字幕翻译以及很多脚本的翻译能解决Lec的翻译问题，而课程的作业则可以通过浏览器的翻译功能解决，并且最重要的是由于这门课程的热门导致网上的中文资源还是相当丰富的，只需要你善用搜索引擎，相信学完本课不是问题。

但是，这并不代表英文在之后的CS学习尤其是自学中不重要。首先，就就以课本为例，很多经典CS课本的中文翻译可以说是不堪卒读，此时便需要你有阅读原版的能力。其次，CS61A的中文资源较多是因为其课程的热门，但在之后学习更深一层的课程中便不会有如此的便利了。最后，我假设看到这里的读者至少可能今后会从事计算机相关的工作，那么至少你的英文水平得足够到看懂英文手册的程度。幸运地是，学这些课程的英文要求也差不多，所以现在就强迫自己适应这样的英文环境是有百利而无一害的。

总而言之，我的建议是，如果你有一定的英文基础（高中及以上的英文学习经历），你可以结合字典的查阅直接以英文形式完成本课。而对于毫无英文学习经历的读者而言，还是结合相关中文资源学完本课，并视自身情况决定是否恶补一下英语。

Q2：学习这个课程需要梯子吗？

A1：截至笔者写作此文时（2022/09），所有CS61A的课程资源都不需要梯子，或者可以通过其它方式规避（youtube的课程视频被搬运到b站上了）。至于github如何上，既然你已经看到了这行文字，相信这对你也不是个问题。

Q3：学习与做作业过程中遇到难点卡住了怎么办？

A3：我认为这个视你计划花在课程上的时间而定：如果你想要快点刷完本课，可以先试着做一点，做不了就暂时跳过，回头看题目发现还不会就上网找思路并解决，最后对其复盘；如果你有充分的时间，我认为不断试错卡个几天也不是坏事，毕竟这就是学习的过程，而且只有你自己独立完成的东西才能真正烙印在脑中。
