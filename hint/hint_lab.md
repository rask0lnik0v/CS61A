注：

以下的hint都是基于**fa20版本**的

Lab 00

1.自己配置，结合MIT的missing semester使用更佳。

Lab 01

没啥难的。

Lab 02

1.前面的question，回答可以是nothing，表示什么都不显示

2.cycle：按照题目要求将内部function定义后，可以想想怎么将一个两输入的function变为分开一输入的（参考第一题）。或者说，内嵌函数中内嵌函数应该也行。

Lab 04

1.参考Hw 01的递归题，基本类似（迭代转递归，或者说是尾递归的形式），没有过难的点。

Lab 05

1.Tree的第一题参考text中is_tree函数的写法，注意是在判断语句中进行递归。

2.Tree的第二题注意是要返回一个新的树！意味着要重新写一个树。

3.riffle结合第一题couple做，注意在列表推导式中可以用下标与if else语句。

4.add_tree可以参考Lec14的QA完成。本身有难度，建议先从简单的迭代写起，然后想想怎么用递归的思想去做。

Lab 06

没啥难的。

Lab 07

没啥难的。此外，Magic: The Lambda-ing这个题neta的是Magic: The Gathering :)

Lab 08

1.cycle不用constant的解法，如果感觉自己只用了constant空间，并且过test了，原因在于只存储了一个节点（对应接特定某个点导致的循环，但是如果test是接在中间的点这样的解法就过不去，因而思考要存储多少节点进行判断）。constant解法的hint：跑400米跑道时套圈的情况。

Lab 09

略。本身有难度，有问题可以看代码。

Lab 10

1.list题需要你根据图构建相应的list，如果莫名报错可以试着删除'YOUR-CODE-HERE的注释。

2.remove思考返回一个新list，而不是在原有list上做改动。

Lab 11

1.代码量很少，难点在于理解整个interpret的过程，尤其是理解eval与apply互相调用的过程。

Lab 12

1.20fa的sqlite_shell.py是空的，找到hw中可用的直接复制进去就能正常完成lab。

Lab 13

1.同上。

Lab 14

略。本身有难度，有问题可以看代码。
