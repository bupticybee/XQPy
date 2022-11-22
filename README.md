# XQpy 象棋巫师(非官方)python实现

## 介绍
XQpy 实现了[XQlightweight](https://github.com/xqbase/xqwlight) 象棋巫师的算法和接口，将所有逻辑移植到python，并且提供了命令行接口用户人机对弈.

不同于之前的象棋ai项目[elephantfish](https://github.com/bupticybee/elephantfish)，XQpy实现的算法具有一定强度，经过评估肯定已经超越 average human水平。

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
