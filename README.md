# XQpy 象棋巫师(非官方)python实现

XQpy，简单而强的纯python中国象棋引擎

## 介绍
XQpy ，实现了一个很强的中国象棋ai，所有逻辑均使用python实现。
总代码量只有1000多行，适合爱好者进行搜索算法学习和魔改，以及整合进其他系统。

XQpy 是象棋巫师[XQlightweight](https://github.com/xqbase/xqwlight) 的非官方python版本，是著名象棋引擎[象眼eleeye](https://github.com/xqbase/eleeye)的轻量版本。

## 使用

下载XQpy后，直接运行```python3 play_against_ai.py```执行和ai的对弈步骤,下面是一个和ai对弈的sample输出：

```text
你想要： 
	1. 执红先行
	2. 执黑后行
	 请选择:
2

  9 俥傌象士将士象傌俥
  8 ．．．．．．．．．
  7 ．砲．．．．．砲．
  6 卒．卒．卒．卒．卒
  5 ．．．．．．．．．
  4 ．．．．．．．．．
  3 兵．兵．兵．兵．兵
  2 ．炮．．相．．炮．
  1 ．．．．．．．．．
  0 车马．仕帅仕相马车
    ａｂｃｄｅｆｇｈｉ


电脑的上一步： c0e2
请输入你的行棋步子，比如 c6c5 
悔棋请输入 shameonme :
```

电脑默认会进行大约5秒的思考。由于python性能问题，如果追求ai强度，推荐使用pypy3替代python执行本程序，并且给予更多的运算时间，计算速度会提升半个数量级。

## 特性

1. 具有[elephantfish](https://github.com/bupticybee/elephantfish) 所有特性，相比elephantfish强很多，但相应的代码量也更多
2. 实现开局库
3. 搜索部分使用纯python实现，很容易翻译成其他语言或对外提供接口

## 如何学习这个项目

1. 如果没有象棋引擎基础，推荐先学习这里的文章 https://github.com/bupticybee/elephantfish/tree/master/articles
2. 在掌握MTD二分搜索算法，空着裁剪，力价值表等概念后，先阅读```positioin.py```，然后阅读```search.py```即可完成对本项目的学习

# License

[GNU GPL v3](https://www.gnu.org/licenses/gpl-3.0.en.html)
