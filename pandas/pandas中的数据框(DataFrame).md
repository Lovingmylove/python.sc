#pandas中的数据框(DataFrame)
**pandas是python环境下最有名的数据统计包，而DataFrame翻译为数据框，是一种数据组织方式，在pandas中常用DataFrame组织数据。**   
![](/Users/Lovingmylove521/Desktop/python.sc/pandas/pandas_logo.png)
##DataFrame的创建和查看
###DataFrame的创建
<pre>
import numpy as np
import pandas as pd

#创建时间索引
dates = pd.date_range('20160530', periods=6)
#创建一个6x4的数据：randn函数用于创建随机数，参数表示行数和列数，dates是上一步创建的索引列
df = pd.DataFrame(np.random.randn(6,4),index=dates,columns=list('ABCD'))
</pre>
####输出结果
![](/Users/Lovingmylove521/Desktop/python.sc/pandas/output_1.png)
###DataFrame数据查看
####查看前n行数据
<pre>
>>df.head(2)
</pre>
####输出结果
![](/Users/Lovingmylove521/Desktop/python.sc/pandas/output_2.png)
####查看后n行数据
<pre>
>>df.tail(2)
</pre>
####输出结果
![](/Users/Lovingmylove521/Desktop/python.sc/pandas/output_3.png)
####查看描述性统计
<pre>
>>df.describe()
</pre>
####输出结果
![](/Users/Lovingmylove521/Desktop/python.sc/pandas/output_4.png)
####使用T来转置数据
<pre>
>>df.T
</pre>
####输出结果
![](/Users/Lovingmylove521/Desktop/python.sc/pandas/output_5.png)
####对数据进行排序
<pre>
df.sort(columns='C')
</pre>
####输出结果
![](/Users/Lovingmylove521/Desktop/python.sc/pandas/output_6.png)
###DataFrame数据选择
####选择一列数据进行操作
<pre>
>>df['A']
</pre>
####输出结果
<pre>
2016-05-30   -1.648243
2016-05-31   -0.396251
2016-06-01    0.900163
2016-06-02    0.492773
2016-06-03   -0.125150
2016-06-04   -0.489626
Freq: D, Name: A, dtype: float64
</pre>
####数据的切片操作
<pre>
>>df[1:3]
</pre>
####输出结果
![](/Users/Lovingmylove521/Desktop/python.sc/pandas/output_7.png)
####使用行标签来指定输出的行
<pre>
>>df['20160530':'20160602']
</pre>
####输出结果
![](/Users/Lovingmylove521/Desktop/python.sc/pandas/output_8.png)   
**DataFrame的loc方法是帮助选择数据**
####索引位置为0的一行数据
<pre>
>>df.loc[dates[0]]
</pre>
####输出结果
<pre>
A   -1.648243
B   -1.041104
C   -1.956653
D   -0.182282
Name: 2016-05-30 00:00:00, dtype: float64
</pre>
####选择多列数据
<pre>
>>df.loc[:,['A','B']]
</pre>
####输出结果
![](/Users/Lovingmylove521/Desktop/python.sc/pandas/output_9.png)
####选择局部数据，行和列的交叉区域
<pre>
>>df.loc['20160530':'20160601',['A','B']]
</pre>
####输出结果
![](/Users/Lovingmylove521/Desktop/python.sc/pandas/output_10.png)
####选择某一个数据
<pre>
>>df.loc[dates[0],'A']
</pre>
**另外，at是专门用于获取某个值的命令**
<pre>
>>df.at[dates[0],'A']
</pre>
####输出结果
<pre>
-1.648242737270514
</pre>
####DataFrame切片操作
**DataFrame数据框允许我们使用iloc方法来像操作数组一样对DataFrame进行切片操作，其操作与前面提到的df.loc和df.at命令类似，加上i之后就可以像操作数组一样操作DataFrame了**
<pre>
>>df.iloc[1:3,2:4]
</pre>
####输出结果
![](/Users/Lovingmylove521/Desktop/python.sc/pandas/output_11.png)
<pre>
>>df.iat[1,1]
</pre>
####输出结果
<pre>
0.84289892419232126
</pre>
##测试环境
**Canopy** version:1.6.2 for **Mac** OSX 10.11.3
>                                        Stay hungry, Stay foolish. ---Steve Jobs