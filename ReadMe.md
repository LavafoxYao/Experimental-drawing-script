## 绘图脚本的使用方法

### 环境

查看自己`python`现在在用的解释器是否安装了`matplotlib`包，我会提供一个自动安装`matplotlib`的脚本，使用这个脚本安装的前提条件是你安装的`pycharm`都是默认安装，最主要的一点是不要改当前使用`python`解释器的路径。**（如果你已经很熟悉怎么去切换python的解释器以及安装python包的过程,上述直接无视）**

自动化安装的脚本`auto_matplotlib.bat`，直接双击执行即可。再按`windows+R`输入`CMD`，在CMD中输入`pip list`，查看`matplotlib`包是否安装成功。若安装成功,如红色框图所示.

![](https://wooyooyoo-photo.oss-cn-hangzhou.aliyuncs.com/blog/2020/09/Snipaste_2020-09-08_09-22-46.png)

### 使用方法

![](https://wooyooyoo-photo.oss-cn-hangzhou.aliyuncs.com/blog/2020/09/Snipaste_2020-09-08_08-33-24.png)

`path` 是你生成 `reports` 的路径(**`path`是每次读取`reports`的路径**)
`COLNAME` 是画图的纵坐标的名称
`ROWNAME` 是画图的横坐标的名称

![](https://wooyooyoo-photo.oss-cn-hangzhou.aliyuncs.com/blog/2020/09/Snipaste_2020-09-08_09-12-32.png)

`norm` 是你指定的比较指标，是在上面的 `dict `中直接复制替换即可.
综上所述🏉如果已经指定好了` path` 路径，每次实验只需修改` COLNAME` 、 `ROWNAME` 、 `norm` 。

**`path`是每次读取`reports`的路径**

### 使用的注意事项

1. 由于我只选取了8组颜色与线段的类型，一次实验对比最多最多只能有8种。
2. 要保证 reports 中的报告是能够正常换行的。一个指标是一行，而不是不能换行的。
3. 在自定义给算法命名的时候**切忌不要使用数字**，比如生成报告的名称不要取 `mytest1 `类似于这样
   的名称,而尽量使用 `mytestA `，**否则在读取报告的时候会出现被程序误解的困难**。
4. 生成的`reports`不要使用中文!!

### 第二版
解决第一版存在的两个问题:

1. 无法读取报告名字中的浮点数
2. 无法在报告文件夹中包含其他类型的文件
3. 增加实验组的对比上限，从原来最多做6组对比上升到8组

### 第三版
解决第二版存在的一个问题：

1. 图例在图中不固定会穿插到绘图的空白处，现已固定在绘图的右上角处，一般来说如果数据正常绘制的线段不会与图例重叠。

**如果你有什么好的设计想法以及需要完善功能也可以与我一起讨论，并对上述代码进行改进。**
