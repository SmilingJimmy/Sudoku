# Sudoku

Using Lingo &amp; Python to solve Sudoku problem. Copyright @ *Smiling Jimmy*


## 简介

- 数独是一种运用纸、笔进行演算的逻辑游戏。玩家需要根据9×9盘面上的已知数字，推理出所有剩余空格的数字，并满足**每一行**、**每一列**、**每一个粗线宫**（3×3）内的数字均含1-9，不重复。

- 数独盘面是个九宫，每一宫又分为九个小格。在这八十一格中给出一定的已知数字和解题条件，利用逻辑和推理，在其他的空格上填入1-9的数字。使1-9每个数字在**每一行**、**每一列**和**每一宫**中都只出现**一次**。


## 解答方法

- 整数规划：[sudoku.lg4](sudoku.lg4)

  将[sudoku.xlsx](sudoku.xlsx)中**Puzzles**工作簿的任一数独问题复制到**Given**工作簿
  
  清空**Out**工作簿
  
  在**Lingo**中运行[sudoku.lg4](sudoku.lg4)，需要更改文件路径
  
  在**Out**工作簿查看结果
  
  注意：由于该整数规划约束条件较多，需要申请**License**方可运行程序

- 近似穷举：[sudoku.py](sudoku.py)

  将[sudoku.xlsx](sudoku.xlsx)中**Puzzles**工作簿的任一数独问题复制到**Given**工作簿
  
  运行[sudoku.py](sudoku.py)即得结果，需要更改文件路径
  
## 运算速度分析

- 整数规划：[sudoku.lg4](sudoku.lg4)

  速度较快，无论问题复杂程度均能在1s内（甚至0.5s内得出结果）

- 近似穷举：[sudoku.py](sudoku.py)

  运算速度随**问题难度**、**CPU运算速度**而异，快则略快于整数规划，慢则十余秒
