

[TOC]



# 链接

```
---不同同步电机结构
https://zhuanlan.zhihu.com/p/696150429
https://blog.csdn.net/qq_42057028/article/details/112213839

---同步电机
https://www.zhihu.com/question/376811991     ----转矩
https://zhuanlan.zhihu.com/p/944875986    -1磁链介绍  
https://zhuanlan.zhihu.com/p/3626119686    - 2电压、磁链推导
https://zhuanlan.zhihu.com/p/293470912    -clark,park
https://www.bilibili.com/opus/542384859742652878  -clark,park
https://zhuanlan.zhihu.com/p/616487488 // 同步电机
---异步电机

https://zhuanlan.zhihu.com/p/589098477 //异步电机
https://zhuanlan.zhihu.com/p/560914556
```



# T5: Electric Propulsion: High Performance motors, In-wheel motors, Motor Control, Steering by Wire.

# 关于基本三相模型



<img src="mini-project-pic/三相相量图.png" style="zoom:50%;" />


$$
\dot{I}_{U}+\dot{I}_W+\dot{I}_V=0 \\
即
\\
\sin (\theta)+ \sin (\theta+\frac{2\pi}{3})+ \sin (\theta-\frac{2 \pi}{3})=0
$$

$$
这个是说明，一个有相位差的实值函数的和为0。注意这里上方的图并不表示\dot{I}是个向量\\
即:虽然他们三个电流画出来是平面的，但他们没有方向\\
（但是他们的确在空间上是有与上图同样的位置关系）。
\\
$$

$$
但是注意他们产生的磁链是有方向的，如
$$

$$
\vec{\psi}_U+\vec{\psi}_W+\vec{\psi}_V  = 
\\%第二行
L(\sin (\theta)e^{i 0}+ \sin (\theta+\frac{2\pi}{3})e^{i \frac{2 \pi}{3}}+ \sin (\theta-\frac{2 \pi}{3})e^{-i \frac{2 \pi}{3}})
 \\
 利用欧拉公式\\%第三行
=L(\frac{1}{2i}[(e^{i \theta}
+e^{i (\theta+\frac{2 \pi}{3})}
+e^{i (\theta+-\frac{2 \pi}{3})}
)
-3 \cdot e^{-i \theta}]
)
\\%第四行
 =L\frac{-3}{2i}e^{-i \theta}
$$


$$
于是可见，其产生的电流是一个旋转的长度恒定的矢量
$$


## 永磁同步电机数学模型



### 基本概论

- 种类：

<img src="mini-project-pic/同步电机种类.png" style="zoom:60%;" />

> 分为：凸装（极）/表贴式， 内嵌/嵌入/内置式， 内埋式
>
> 所谓内置式和表贴式其实就是结构不同，内置式就是把电机内部转子内嵌在永磁体，永磁体外表面与定子铁心内圆之间有铁磁物质制成的[极靴](https://zhida.zhihu.com/search?content_id=242830206&content_type=Article&match_order=1&q=极靴&zhida_source=entity)，可以保护永磁体。这种永磁电机的重要特点是直、交轴的主电感不相等。因此，这两种电机的性能有所不同，内嵌式结构扭矩更大，退磁风险更低。
>

### 凸极式定义

> 凸极”指的是转子磁极形状上**突出于圆周表面**的极部件，即在转子铁芯外围安装的、向外凸出的磁极极靴（pole shoe）。（下图就是）



### d-直轴，q-交轴

<img src="mini-project-pic/dq轴1.png" style="zoom:60%;" />

> ## 直轴 (d 轴)
>
> - 方向定义 d 轴是穿过转子永磁体南—北极心（磁极中心）的轴线。
> - 空间位置 它对应电机内部磁路中永磁体磁通的主要方向，也是气隙磁阻最小的方向。
> - 坐标变换中的含义 在 d–q 坐标系里，d 轴是将定子绕组电流分解后产生直轴磁场的分量方向，主要用于控制励磁分量（Φ_d）。
>
> ## 交轴 (q 轴)
>
> - 方向定义 q 轴与 d 轴在电角度上正交，垂直于 d 轴；即在转子旋转方向上，q 轴领先 d 轴 90°（电角度）。
> - 空间位置 q 轴穿过两极之间的磁极齿顶点区域，对应气隙磁阻较大的路径。
> - 坐标变换中的含义 在 d–q 坐标系里，q 轴是将定子绕组电流分解后产生交轴磁场的分量方向，主要用于控制扭矩分量（I_q）。

<img src="mini-project-pic/表贴式和内置式同步电机直轴和交轴电感.png" style="zoom:70%;" />


- 电感类型

$$
\begin{align}
&L_A \quad自感 \\
&L_{AB}\quad互感\\
&L_{s\sigma} \quad漏感\\
&L_{m1} \quad 励磁电感\\
&L_m \quad 等效励磁电感\\
&L_s\quad同步电感\\
&L_d\quad直轴同步电感\\
&L_q\quad交轴同步电感\\
\end{align}
$$

- 磁路

<img src="mini-project-pic/同步电机磁路.png" style="zoom:60%;" />

- 重要电感参数公式

$$
\begin{align}
\psi_A & =L_A i_a = (L_{m1}+L_{s\sigma})i_a \qquad  通常漏感L_{s\sigma}可以忽略 \\
L_{BA}& =L_{CA}=L_{AB}=L_{AC}=L_{BC}=L_{CB}=-\frac{1}{2}L_{m1}  \qquad 正负表示方向 \\
L_A &=L_B=L_C=L_{m1}+L_{s\sigma}   \qquad    即自感均相同
\end{align}
$$







- 磁链与电流关系

$$ 
\psi_{fX} \quad 这一类是永磁体转子通过A,B,C产生的磁链
$$

- 表贴式永磁同步电机（SPMSM）磁链

$$
\begin{align}
\begin{bmatrix}
\psi_A \\
\psi_B \\
\psi_C  
\end{bmatrix}
&= % 磁链矩阵
\begin{bmatrix}
L_{AA} & L_{AB} & L_{AC} \\
L_{BA} & L_{BB} & L_{BC} \\
L_{CA} & L_{CB} & L_{CC}
\end{bmatrix}
\begin{bmatrix}
i_a \\
i_b \\
i_c
\end{bmatrix}
+
\begin{bmatrix}
\psi_{fA} \\
\psi_{fB} \\
\psi_{fC}
\end{bmatrix}
\\
&=
\begin{bmatrix}
L_{m1} + L_{\sigma} & -\frac{1}{2}L_{m1} & -\frac{1}{2}L_{m1} \\
-\frac{1}{2}L_{m1} & L_{m1} + L_{\sigma} & -\frac{1}{2}L_{m1} \\
-\frac{1}{2}L_{m1} & -\frac{1}{2}L_{m1} & L_{m1} + L_{\sigma}
\end{bmatrix}
\begin{bmatrix}
i_a \\
i_b \\
i_c
\end{bmatrix}
+
\begin{bmatrix}
\psi_{fA} \\
\psi_{fB} \\
\psi_{fC}
\end{bmatrix}
\end{align}
$$

- 每一相的磁链


$$
\begin{align}
\psi_A &=L_Ai_a+L_{AB}i_b +L_{AC}i_c+\psi_{fA}\\
 &= (L_{m1}+L_{s\sigma})i_a-\frac{1}{2}L_{m1}(i_b+i_c)+\psi_{fA}
\\ &\left\{
    \begin{array}{ll}
        \mathbf{由于i_a+i_b+i_c=0  \rightarrow \quad i_b+i_c=-i_a }
    \end{array}
    \right\}
    \\
 &= (L_{m1}+L_{s\sigma}+\frac{1}{2}L_{m1})_a +\psi_{fA} 
 \\ &\mathbf{
    \left\{
    \begin{array}{ll}
        L_{m}=\frac{3}{2}L_{m1}\\
        L_{s} =\frac{3}{2}L_{m1}+L_{s\sigma}=L_m+L_{s\sigma}
    \end{array}
    \right\}
    =L_si_a+\psi_{fA}
 }
 \end{align}
$$





- 总结

```
1：L_A自感 ：表示绕组通入电流后产生磁链的能力，由两部分组成，励磁电感L_{m1} 和漏感L_s\sigma ，励磁电感与通过主磁路形成闭合回路的那部分磁链（主磁链）对应，漏磁电感与通过气隙形成闭合回路的那部分磁链（漏磁链）对应；

2.互感L_{AB} ：表示某一相绕组通入电流后，在其他绕组中产生磁链的能力，其大小为励磁电感的1/2，且为负数，负表示产生的磁链为反方向；

3.等效励磁电感L_m ：由于三相电流之和为零，任意两相绕组中的电流产生的磁通链过第三相绕组所产生的磁链总和可以用第三相绕组中的电流等效表示出来，因此第三相绕组中的主磁链可以用等效励磁电感来计算，等效是指两部分的和：绕组自身的励磁电感加相间互感。

4.同步电感 L_s ：同步电感是漏感和等效励磁电感之和，有了同步电感的定义之后，某相绕组的磁链仅用该相的电流就能表示出来，不再需要其他相的电流了

5.L_d, L_q :直轴同步电感，交轴同步电感
表贴式永磁同步电机（SPMSM）的气隙磁场是均匀的，所以绕组的自感和绕组间的互感是恒定的，其大小不会随转子位置变化
内埋式永磁同步电机（IPMSM）的气隙磁场不是均匀的：正对永磁体的方向（d轴）和其反方向，气隙最大，磁阻最大，而超前永磁体90°电角度（q轴）的方向和其反方向，气隙最小，磁阻最小。（注意看前面的示例图有标明方向）(其变化速度是机械角速度的两倍，由于对称性)

```



---



### 电压方程 

$$ 
R_s \quad 为定子绕组电阻 \\
\psi_x \quad 表示abc 三相磁链 \\
i_x \quad 表示三相相电流
$$


$$
\begin{bmatrix} u_a \\ u_b \\ u_c  \end{bmatrix} = 
\begin{bmatrix} R_s & 0 &0 \\ 0 & R_s & 0\\ 0 & 0 & R_s  \end{bmatrix}
\begin{bmatrix} i_a \\ i_b \\ i_c  \end{bmatrix}
+ 
\frac{d }{d_t}\begin{bmatrix} \psi_a \\ \psi_b \\ \psi_c  \end{bmatrix}
$$


### 磁链方程


$$
\begin{align}
&L_{aa}  \quad这类是自感\\
&M_{ab} \quad 这类互感 \\
&L_{s0} \quad为气隙产生电感分量 \\
&L_{s2} \quad为转子位置依赖磁链产生电感分量\\
&\psi_f \quad 为永磁体磁链 \\
&\theta\quad 为转子N极与a相夹角 \\
&M_{s0} \quad 互感之间直流分量 
\end{align}
$$

$$
\begin{bmatrix} \psi_a \\ \psi_b \\ \psi_c  \end{bmatrix} = 
\begin{bmatrix} L_{aa} & M_{ab} &M_{ac} \\ M_{ba} & L_{bb} & M_{bc}\\ M_{ca} & M_{cb} & L_{cc}  \end{bmatrix}
\begin{bmatrix} i_a \\ i_b \\ i_c  \end{bmatrix}
+ 
\psi_f\begin{bmatrix} cos(\theta)\\ cos(\theta-\frac{2}{3}\pi) \\ cos(\theta+\frac{2}{3}\pi) \end{bmatrix}
$$

$$
\begin{align}
 L_{aa}& = L_{s0} + L_{s2} \cos(2\theta)  \\ \\
L_{bb} &= L_{s0} + L_{s2} \cos\left(2(\theta - \frac{2}{3}\pi)\right)\\
&= L_{s0} + L_{s2} \cos\left(2\theta + \frac{2}{3}\pi\right)\\
\\ 
L_{cc} &= L_{s0} + L_{s2} \cos\left(2(\theta + \frac{2}{3}\pi)\right) \\
 &= L_{s0} + L_{s2} \cos\left(2\theta - \frac{2}{3}\pi\right)\\
\\
M_{ab} &= M_{ba} =  M_{s0}+ L_{s2} \cos\left(2(\theta + \frac{2}{3}\pi)\right) \\
&=  M_{s0} + L_{s2} \cos\left(2\theta - \frac{2}{3}\pi\right)\\
\\
M_{bc} &= M_{cb} =  M_{s0}+ L_{s2} \cos(2\theta) \\
&=  M_{s0} + L_{s2} \cos\left(2\theta - \frac{2}{3}\pi\right)\\
\\
M_{ca} &= M_{ac} =  M_{s0} + L_{s2} \cos\left(2(\theta - \frac{2}{3}\pi)\right) \\
&=  M_{s0} + L_{s2} \cos\left(2\theta - \frac{2}{3}\pi\right)\\
\end{align}
$$

$$
这里的L_1即为励磁分量，由于磁路对称，在忽略漏感时互感之间直流分量 M_{s0}为励磁分量的-\frac{1}{2} \\
即：M_{s0}=-\frac{1}{2}L_{s0} \\
L_2为正弦幅值分量
$$



> **3. 为什么是2θ而不是θ？**
>
> 关键在于**磁导的对称性**：
>
> - 转子每转过180°电角度（π弧度），磁导分布重复一次
> - 这是因为N极和S极具有相同的磁阻特性
> - 因此磁导函数的周期是π，而不是2π
>
> 
>
> 

### 电磁转矩

> - 机械角速度 ωₘ 描述转子相对于机壳的物理转动速率，一圈机械转动对应 360° 机械角。
> - 电角速度 ωₑ 描述定子磁场完成一个电周期（360° 电角）时的速率。由于每对极（Pole Pair）对应一次电周期，电角速度要比机械角速度多 p 倍。
>
> 举例：
>
> - 若电机有 4 极（p=2），转子转一圈（360° 机械角），等同于磁场走过 2 个电周期（720° 电角），即 ωₑ=2×ωₘ。

> 电磁功率不含电阻部分，所以只是磁链，没有电阻值

$$
\begin{align}
&P_n \quad 为极对数 \\
&\theta_m \quad 机械角 \\
&\omega_m \quad 机械角速度\\
&i_{3s}\quad为三项电流统称\\
&\psi_{3s}\quad为三项磁链统称（磁链*电流=能量）\\
&\omega_e \quad 为电角速度\\
\end{align}
$$


$$
\begin{align}
&T_e = \frac{1}{2} \frac{\partial (i_{3s}^T\cdot\psi_{3s}) }{\theta_m}
\\
&T_e = \frac{P_e}{\omega_m}= \frac{P_e}{\omega_e / P_n}=\frac{P_e}{2\pi n/60}
\end{align}
$$


> 注意这里两个转矩并不是化简得来的，下面的是由功率=转矩*角速度得来





### 机械运动方程


$$
\begin{align}
&J \quad 转动惯量\\
&B \quad 阻尼系数 \\
&T_L \quad 负载转矩\\

\end{align}
$$

$$
J \frac{\omega_m}{dt}=T_e - T_L-B\omega_m
$$


---



### clarke 变换（初步变换为\alpha  - \beta 坐标系   ）

> 为了化简复杂的三项耦合，如下的clarke为了使电压相等，若令功率相等，则添加k=sqrt(3/2)

<img src="mini-project-pic/clarke变换示意1.png" style="zoom:40%;" />

$$
clarke记为:T_{3s/2s} \\
反clarke记为:T_{2s/3s}
$$

$$
T_{3s/2s}=\frac{2}{3}
\begin{bmatrix}
1 & -\frac{1}{2} & -\frac{1}{2} \\
0 & \frac{\sqrt{3}}{2} & -\frac{\sqrt{3}}{2}\\
\frac{1}{2} & \frac{1}{2} &\frac{1}{2}
\end{bmatrix}
\\
T_{3s/2s}=
\begin{bmatrix}
1 & 0 & 1\\
-\frac{1}{2} & \frac{\sqrt{3}}{2} & 1\\
-\frac{1}{2} & -\frac{\sqrt{3}}{2} & 1
\end{bmatrix}
$$



> 取 \alpha 轴与a相重合,下方是通用变换公式，f_x 可谓任意元素（电压磁链）

$$ %通用clarke变换公式
\begin{align}
\begin{bmatrix}
f_\alpha \\
f_\beta  \\
f_0
\end{bmatrix} % f行结束
=T_{3s/2s}f(abc)
&=
\frac{2}{3}
\begin{bmatrix}
1 & cos(\frac{2}{3}\pi) & cos(-\frac{2}{3}\pi )\\
0 & sin(\frac{2}{3}\pi)& sin(-\frac{2}{3}\pi)\\
\frac{1}{2} & \frac{1}{2} &\frac{1}{2}
\end{bmatrix}
\begin{bmatrix}
f_a\\
f_b\\
f_c
\end{bmatrix}
\\
&=
\frac{2}{3}
\begin{bmatrix}
1 & -\frac{1}{2} & -\frac{1}{2} \\
0 & \frac{\sqrt{3}}{2} & -\frac{\sqrt{3}}{2}\\
\frac{1}{2} & \frac{1}{2} &\frac{1}{2}
\end{bmatrix}
\begin{bmatrix}
f_a\\
f_b\\
f_c
\end{bmatrix}
\end{align}
$$



> 其中1/2 行 是由于为了使其成为满秩，2/3是单纯转换系数， 
>
> f_0是零分量，即第三行满足 f_a+f_b+f_c=f_0=0

#### clarke 变换下新的磁链方程，电压方程，转矩方程

- *磁链方程*

$$
\begin{align}
&\psi_f \quad 为永磁体磁链 \\
&\omega_e \quad为电角速度 \\
&e_\alpha ,e_\beta \quad 为切割转子磁感线产生的电动势
\end{align}
$$


$$
\begin{bmatrix} \psi_a \\ \psi_b \\ \psi_c  \end{bmatrix} = 
\begin{bmatrix} L_{aa} & M_{ab} &M_{ac} \\ M_{ba} & L_{bb} & M_{bc}\\ M_{ca} & M_{cb} & L_{cc}  \end{bmatrix}
\begin{bmatrix} i_a \\ i_b \\ i_c  \end{bmatrix}
+ 
\psi_f\begin{bmatrix} cos(\theta)\\ cos(\theta-\frac{2}{3}\pi) \\ cos(\theta+\frac{2}{3}\pi) \end{bmatrix}
$$



$$
T_{2s/3s}
\begin{bmatrix} \psi_\alpha \\ \psi_\beta \\ \psi_0 \end{bmatrix}= 
\begin{bmatrix} 
L_{aa} & M_{ab} &M_{ac} \\ M_{ba} & L_{bb} & M_{bc}\\ M_{ca} & M_{cb} & L_{cc}  
\end{bmatrix}
T_{2s/3s}
\begin{bmatrix} 
i_\alpha \\ i_\beta \\i_0  
\end{bmatrix}
+ 
\psi_f
\begin{bmatrix} cos(\theta)\\ cos(\theta-\frac{2}{3}\pi) \\ cos(\theta+\frac{2}{3}\pi) \end{bmatrix}
\\
\begin{bmatrix} \psi_\alpha \\ \psi_\beta \\ \psi_0 \end{bmatrix} 
=T_{3s/2s}
\begin{bmatrix} L_{aa} & M_{ab} &M_{ac} \\ M_{ba} & L_{bb} & M_{bc}\\ M_{ca} & M_{cb} & L_{cc}  \end{bmatrix}
T_{2s/3s}
\begin{bmatrix} i_\alpha \\ i_\beta \\i_0  \end{bmatrix}
+
\psi_f T_{3s/2s}
\begin{bmatrix} cos(\theta)\\ cos(\theta-\frac{2}{3}\pi) \\ cos(\theta+\frac{2}{3}\pi) \end{bmatrix}
\\ 
$$


$$
\begin{bmatrix} \psi_\alpha \\ \psi_\beta \\ \psi_0 
\end{bmatrix} 
=\begin{bmatrix}
L_{s0}-M_{s0}+(3L_{s2}cos(2\theta))/2 & (3L_{s2}sin(2\theta))/2 & 0 \\
(3L_{s2}sin(2\theta))/2 & L_{s0}-M_{s0}-(3L_{s2}cos(2\theta))/2 & 0 \\
0 & 0 & L_{s0}+2M_{s0}
\end{bmatrix}
\begin{bmatrix} i_\alpha \\ i_\beta \\ i_0  \end{bmatrix}
+
\psi_f 
\begin{bmatrix} 
    cos(\theta)\\ sin(\theta) \\ 0
\end{bmatrix}
$$



> 因为\alpha \beta两个轴相互垂直，因此不存在他们之间的互感电动势





- *电压方程*

$$
\begin{bmatrix} u_a \\ u_b \\ u_c  \end{bmatrix} = 
\begin{bmatrix} R_s & 0 &0 \\ 0 & R_s & 0\\ 0 & 0 & R_s  \end{bmatrix}
\begin{bmatrix} i_a \\ i_b \\ i_c  \end{bmatrix}
+ 
\frac{d }{d_t}\begin{bmatrix} \psi_a \\ \psi_b \\ \psi_c  \end{bmatrix}
$$

$$
\begin{bmatrix} u_\alpha \\ u_\beta \\ u_0  \end{bmatrix} = 
T_{3s/2s}
\begin{bmatrix} R_s & 0 &0 \\ 0 & R_s & 0\\ 0 & 0 & R_s  \end{bmatrix}
T_{2s/3s}
\begin{bmatrix} i_\alpha \\ i_\beta \\ i_0  \end{bmatrix}
+ 
\frac{d }{d_t}
T_{3s/2s}
\begin{bmatrix} \psi_a \\ \psi_b \\ \psi_c  \end{bmatrix}
$$

$$
根据数乘单位阵性质T(R_s\cdot E)T^{-1}=R_s \cdot E
$$

$$
\begin{bmatrix} u_\alpha \\ u_\beta \\ u_0  \end{bmatrix} = 
\begin{bmatrix} R_s & 0 &0 \\ 0 & R_s & 0\\ 0 & 0 & R_s  \end{bmatrix}
\begin{bmatrix} i_\alpha \\ i_\beta \\ i_0  \end{bmatrix}
+ 
\frac{d }{dt}
\begin{bmatrix} \psi_\alpha \\ \psi_\beta \\ \psi_0  \end{bmatrix}
$$

$$
带入\alpha-\beta坐标系下磁链方程
$$

$$
\begin{align}
\begin{bmatrix} u_\alpha \\ u_\beta \\ u_0  \end{bmatrix} 
= \begin{bmatrix} R_s & 0 &0 \\ 0 & R_s & 0\\ 0 & 0 & R_s  \end{bmatrix}
\begin{bmatrix} i_\alpha \\ i_\beta \\ i_0  \end{bmatrix}
+% 这里到了磁链部分
\frac{d }{dt}
\left\{
\begin{bmatrix}  %电流与磁链矩阵
L_{s0}-M_{s0}+(3L_{s2}cos(2\theta))/2 & (3L_{s2}sin(2\theta))/2 & 0 \\
(3L_{s2}sin(2\theta))/2 & L_{s0}-M_{s0}-(3L_{s2}cos(2\theta))/2 & 0 \\
0 & 0 & L_{s0}+2M_{s0}
\end{bmatrix}
\begin{bmatrix} i_\alpha \\ i_\beta \\i_0  \end{bmatrix}
+
\psi_f 
\begin{bmatrix} 
cos(\theta)\\ sin(\theta) \\0
\end{bmatrix}
\right\}
\end{align}
$$

$$
注意 \\
\theta =\omega \cdot t \\
转速恒定情况下
d \theta = \omega \cdot dt
$$

$$
\begin{bmatrix} u_\alpha \\ u_\beta \\ u_0  \end{bmatrix} 
=\begin{bmatrix}  %电流无微分矩阵
R_s-3\omega L_{s2}sin(2\theta)  & 3L_{s2}\omega cos(2\theta) &  0 \\
3L_{s2}\omega cos(2\theta)  & R_s+ 3L_{s2}\omega sin(2\theta)  &  0 \\
0 & 0 & R_s
\end{bmatrix}
 \begin{bmatrix} i_\alpha \\ i_\beta \\i_0  \end{bmatrix}
+
\begin{bmatrix}  %微分电流与磁链矩阵
L_{s0}-M_{s0}+(3L_{s2}cos(2\theta))/2 & (3L_{s2}sin(2\theta))/2 & 0 \\
(3L_{s2}sin(2\theta))/2 & L_{s0}-M_{s0}-(3L_{s2}cos(2\theta))/2 & 0 \\
0 & 0 & L_{s0}+2M_{s0}
\end{bmatrix}
\frac{d}{dt}
\begin{bmatrix} i_\alpha \\ i_\beta \\i_0  \end{bmatrix}
+
\psi_f \omega
\begin{bmatrix} 
-sin(\theta)\\ cos(\theta) \\0
\end{bmatrix}
\\
$$











- *转矩方程*（不想写了，写到parker内就行了）

$$
\begin{align}
P_{\alpha\beta} &=\frac{3}{2}(u_\alpha i_\alpha+u_\beta i_\beta+u_0 i_0)\\
P_{ab} &=(u_a i_a+u_b i_b+u_c i_c) \\
\\
& u_a+u_b+u_c=0 \\
& i_a+i_b +i_c=0
\end{align}
\\
$$

> 电磁转矩 Te 的定义是转子在机械运动中“每转一弧度”所做的力矩，其物理量纲是牛·米（N·m）。
>
> 机械角速度 ωm 表示转子每秒钟转过的真实机械角位移（rad/s），反映了机械系统的运动速率。
>
> 注意量纲即可获得如下表达式



> 电磁功率不含电阻部分

$$
T_e=\frac{P_e}{\omega_m}=\frac{3}{2}P_n(\psi_\alpha i_\beta - \psi_\beta i_\alpha)
$$



### parker变换(d-p旋转)

> parker变换使用的\theta是电角度，而不是机械角

#### parker 变换阵

$$
推导考虑分块矩阵构造方式，不影响其中的2*2矩阵 \\
易知
\begin{bmatrix}
A,0 \\
0,1
\end{bmatrix}的逆为
\begin{bmatrix}
A^{-1},0 \\
0,1
\end{bmatrix}
\\
A则可以保证为2*2parker矩阵\\
A=
\begin{bmatrix}
\cos \theta,\sin \theta \\
-\sin \theta,\cos \theta
\end{bmatrix}
$$



- 3*3

$$
正parker: T_{2s/2r}=
\begin{bmatrix}
\cos θ & \sin θ & 0\\
-\sin θ & \cos θ & 0\\
0 & 0 & 1
\end{bmatrix}
\\
反parker: T_{2r/2s}=
\begin{bmatrix}
\cos θ & -\sin θ & 0\\
\sin θ & \cos θ & 0\\
0 & 0 & 1
\end{bmatrix}
$$


$$
正park: T_{2s/2r}=
\begin{bmatrix}
cos\theta & sin\theta \\
-sin\theta & cos\theta \\
\end{bmatrix}
\\
反park: T_{2r/2s}=
\begin{bmatrix}
cos\theta & -sin\theta \\
sin\theta & cos\theta \\
\end{bmatrix}
$$

- 基本正park变换公式

$$
\begin{bmatrix}
    f_d \\
    f_q
\end{bmatrix}
= \begin{bmatrix}
    cos\theta & sin\theta \\
    -sin\theta & cos\theta 
\end{bmatrix}
\begin{bmatrix}
    f_\alpha \\
    f_\beta
\end{bmatrix}
$$

#### parker变换下电流表达式、磁链，电压，转矩方程



- 电流表达式

$$
\begin{bmatrix}
    i_d \\
    i_q  \\
    i_0
\end{bmatrix}
=\begin{bmatrix}
\frac{2}{3}\cos \theta & -\frac{2}{3}\cos(\theta+\frac{\pi}{3})  & -\frac{2}{3}\cos(\theta-\frac{\pi}{3})  \\%变换矩阵第一行
-\frac{2}{3}\sin \theta & \frac{2}{3}\sin(\theta+\frac{\pi}{3})  & -\frac{2}{3}\cos(\theta+\frac{\pi}{6}) \\
1/3  &1/3 & 1/3
\end{bmatrix}
\\
\begin{bmatrix}
i_a \\
i_b \\
i_c
\end{bmatrix}
$$

$$
利用:\sin(\theta+\pi/2)=\cos(\theta);\\
可以得知:
\left\{
\begin{array}{ll}
\frac{\partial i_d}{\partial \theta}=i_q  \\
\frac{\partial i_q}{\partial \theta}=-i_d 

\end{array}
\right\}
$$



- 磁链方程

$$
\begin{align}
\begin{bmatrix} \psi_d \\ \psi_q\\ \psi_0 \end{bmatrix} 
&=T_{2s/2r}
\begin{bmatrix}
    L_{s0}-M_{s0}+(3L_{s2}cos(2\theta))/2 & (3L_{s2}sin(2\theta))/2 & 0 \\
    (3L_{s2}sin(2\theta))/2 & L_{s0}-M_{s0}-(3L_{s2}cos(2\theta))/2 & 0 \\
    0 & 0 & L_{s0}+2M_{s0}
\end{bmatrix}
T_{2r/2s}
\begin{bmatrix} i_d \\ i_q \\i_0  \end{bmatrix}
+
\psi_f 
T_{2s/2r}
\begin{bmatrix} 
    cos(\theta)\\ sin(\theta) \\0
\end{bmatrix}
\\ %第二行
&=\begin{bmatrix}
    L_{s0}-M_{s0}+(3L_{s2})/2 & 0 & 0 \\
    0 & L_{s0}-M_{s0}-(3L_{s2})/2 & 0 \\
    0 & 0 & L_{s0}+2M_{s0} 
\end{bmatrix}
\begin{bmatrix} i_d \\ i_q \\i_0  \end{bmatrix}
+
%转子永磁体部分
\psi_f
\begin{bmatrix} 1 \\ 0 \\0  \end{bmatrix}
\\ %第三行简化
&=\begin{bmatrix}
    L_d & 0 & 0 \\
    0 &L_q & 0 \\
    0 & 0 & L_0
\end{bmatrix}
\begin{bmatrix} i_d \\ i_q \\i_0  \end{bmatrix}
+
%转子永磁体部分
\psi_f
\begin{bmatrix} 1 \\ 0 \\0  \end{bmatrix}
\end{align}
$$



- 电压方程

$$
\begin{bmatrix} u_\alpha \\ u_\beta \\ u_0  \end{bmatrix} = 
\begin{bmatrix} R_s & 0 &0 \\ 0 & R_s & 0\\ 0 & 0 & R_s  \end{bmatrix}
\begin{bmatrix} i_\alpha \\ i_\beta \\ i_0  \end{bmatrix}
+ 
\frac{d }{d_t}
\begin{bmatrix} \psi_\alpha \\ \psi_\beta \\ \psi_0  \end{bmatrix}
$$

$$
同乘T_{2s/2r} ,同时用逆变换处理\vec{\psi}
$$


$$
\begin{align}
    \begin{bmatrix} u_d \\ u_q \\ u_0  \end{bmatrix} 
&=  \begin{bmatrix} R_s & 0 &0 \\ 0 & R_s & 0\\ 0 & 0 & R_s  \end{bmatrix}
    \begin{bmatrix} i_d \\ i_q \\ i_0  
\end{bmatrix}
+T_{2s/2r}%对角阵不变，主要是磁链变化
\frac{d}{dt}\left\{
    T_{2r/2s}
    \begin{bmatrix} \psi_\alpha \\ \psi_\beta \\ \psi_{0}  \end{bmatrix}
\right\}   \\ %第二行
&=\begin{bmatrix} R_s & 0 &0 \\ 0 & R_s & 0\\ 0 & 0 & R_s  \end{bmatrix}
\begin{bmatrix} i_d \\ i_q \\ i_0  \end{bmatrix}
+%化简的磁链
\begin{bmatrix}
    \frac{d \psi_d}{dt}-\omega \psi_q \\
    \frac{d \psi_q}{dt}+\omega \psi_d \\ 0
\end{bmatrix}
\end{align}
$$

$$
再带入磁链方程，用i_d,i_q表示电压
$$

$$
\begin{bmatrix} u_d \\ u_q \\ u_0  \end{bmatrix} 
= \begin{bmatrix} R_s & -\omega L_q &0 \\ \omega L_d & R_s & 0\\ 0 & 0 & R_s  \end{bmatrix}
\begin{bmatrix} i_d \\ i_q \\ i_0  \end{bmatrix}%对齐等号 
+ 
\begin{bmatrix} 
    L_d & 0 & 0 \\
    0 & L_q & 0 \\
    0 & 0 & 0 \\
\end{bmatrix}
\frac{d }{d_t}%对角阵不变，主要是磁链变化%微分矩阵
\begin{bmatrix} i_d \\ i_q \\ i_0  \end{bmatrix}
+
\begin{bmatrix} 0 \\ \omega \psi_f \\0  \end{bmatrix}
$$



- 转矩方程

> 首先我们先确定转换后系数

$$
\begin{align}
W
&=\frac{1}{2}
\begin{bmatrix}
    i_a & i_b & i_c
\end{bmatrix}
\begin{bmatrix}% 磁链
    \psi_a \\
    \psi_b \\
    \psi_c
\end{bmatrix}
\\%第二行 %dq转换后
&=\frac{1}{2}
\begin{bmatrix}
    i_d & i_q
\end{bmatrix}
T^{T}_{dq-abc}
T_{dq-abc}
\begin{bmatrix}
    \psi_d \\
    \psi_q
\end{bmatrix}
\\ % 第三行,分别化为dq-\alpha,\beta -abc
&=\frac{1}{2}
\begin{bmatrix}
    i_d & i_q
\end{bmatrix}
T^{T}_{2r/2s}
T^{T}_{2s/3s}
T_{2s/3s}
T_{2r/2s}
\begin{bmatrix}
\psi_d \\
\psi_q
\end{bmatrix}
\end{align}
$$

$$
由于这里我们不考了第三分量i_0,故采用非可逆矩阵的变换形式 \\
T_{3s/2s}=
\begin{bmatrix}
    1 & -\frac{1}{2} & -\frac{1}{2} \\
    0 & \frac{\sqrt{3}}{2} & -\frac{\sqrt{3}}{2}
\end{bmatrix}
\\
T_{3s/2s}=
\begin{bmatrix}
    1 & 0 \\
    -\frac{1}{2} & \frac{\sqrt{3}}{2} \\
    -\frac{1}{2} &  -\frac{\sqrt{3}}{2}
\end{bmatrix}
\\
\\
易知
T^{T}_{2s/3s}
T_{2s/3s}   =
\begin{bmatrix}
    1 & 0 \\
    0 & 1 
\end{bmatrix}
\\ 同时T_{3s/2s}^{T}T_{3s/2s} = \frac{3}{2}
\begin{bmatrix}
    1 & 0 \\
    0 & 1 
\end{bmatrix}
$$
$$
W=\frac{3}{4}
\begin{bmatrix}
    i_d & i_q
\end{bmatrix}
\begin{bmatrix}
    \psi_d \\
    \psi_q
\end{bmatrix}
$$

$$
将上述磁链方程\psi_d ,\psi_q 与i_d ,i_q的表达式代入,这里简化乘二维的向量
$$

$$
\\ %第三行简化
\begin{bmatrix}
    \psi_d \\
    \psi_q
\end{bmatrix}
=\begin{bmatrix}
    L_d & 0  \\
    0 & L_q  \\
\end{bmatrix}
\begin{bmatrix} i_d \\ i_q \end{bmatrix}
+ 
\psi_f  %转子永磁体部分
\begin{bmatrix} 1 \\ 0  \end{bmatrix}
$$


$$
W_s = \frac{3}{4}(L_di_d^2 +L_qi_q^2+i_d\psi_f)
$$

$$
这里不打算考虑转子的等效磁场，即直接认为\psi_f =L_mi_f 为定值（同时由于d轴与其同相）， \\
则可认为i_f恒定，不参与力矩计算。\\
\theta是电角速度，\theta_m是机械角速度\\
\theta=\theta_m /p_n
$$

$$
\begin{align}
T
&=\frac{\partial W}{\partial \theta_m}
=\frac{\partial W_s}{\partial \theta/p_n}\\
&=p_n 
(\frac{\partial W_s}{\partial i_d}\cdot \frac{\partial i_d}{\partial \theta}
+
\frac{\partial W_s}{\partial i_q}\cdot \frac{\partial i_q}{\partial \theta})
\end{align}
$$


$$
利用上述i_d与i_q对电位角的偏导关系
\left\{
\begin{array}{ll}
\frac{\partial i_d}{\partial \theta}=i_q  \\
\frac{\partial i_q}{\partial \theta}=-i_d 
\end{array}
\right\}
$$

$$
T=\frac{3}{2}p_n[\psi_fi_q+(L_d-L_q)i_di_q]
$$



---



## 三项异步电机异步

### 电压、磁链、转矩方程


$$
\begin{align}
i_{sx}& \quad为定子侧三相电流 \\
i_{rx}& \quad 为折算到定子侧的转子三相电流  \\
\psi_{sx}& \quad为定子侧三相磁链 \\
\psi_{rx}& \quad 为折算到定子侧的转子三相磁链 \\
L_{1m} & \quad 为主磁通对应的定子电感 \\
\theta & \quad 为A轴与转子A之间的空间夹角\\
\end{align}
$$


- 电压

$$
\begin{bmatrix}
    u_{sa} \\
    u_{sb} \\
    u_{sc} \\
    0 \\
    0 \\
    0
\end{bmatrix}
=\begin{bmatrix}
    R_s & 0 & 0 & 0 & 0 & 0 \\
    0 & R_s & 0 & 0 & 0 & 0 \\
    0 & 0 & R_s & 0 & 0 & 0 \\
    0 & 0 & 0 & R_r & 0 & 0 \\
    0 & 0 & 0 & 0 & R_r & 0 \\
    0 & 0 & 0 & 0 & 0 & R_r
\end{bmatrix}
\begin{bmatrix}
    i_{sa} \\
    i_{sb} \\
    i_{sc} \\
    i_{ra} \\
    i_{rb} \\
    i_{rc}
\end{bmatrix}
+
\frac{d}{dt}
\begin{bmatrix}
    \psi_{sa} \\
    \psi_{sb} \\
    \psi_{sc} \\
    \psi_{ra} \\
    \psi_{rb} \\
    \psi_{rc}
\end{bmatrix}
$$

- 磁链

$$
\begin{bmatrix}
    \psi_{sa} \\
    \psi_{sb} \\
    \psi_{sc} \\
    \psi_{ra} \\
    \psi_{rb} \\
    \psi_{rc}
\end{bmatrix}
=\begin{bmatrix}
    L_{sl} + L_{lm} & -\frac{1}{2}L_{lm} & -\frac{1}{2}L_{lm} & L_{lm}\cos\theta & L_{lm}\cos(\theta+\frac{2\pi}{3}) & L_{lm}\cos(\theta-\frac{2\pi}{3}) \\
    -\frac{1}{2}L_{lm} & L_{sl} + L_{lm} & -\frac{1}{2}L_{lm} & L_{lm}\cos(\theta-\frac{2\pi}{3}) & L_{lm}\cos\theta & L_{lm}\cos(\theta+\frac{2\pi}{3}) \\
    -\frac{1}{2}L_{lm} & -\frac{1}{2}L_{lm} & L_{sl} + L_{lm} & L_{lm}\cos(\theta+\frac{2\pi}{3}) & L_{lm}\cos(\theta-\frac{2\pi}{3}) & L_{lm}\cos\theta \\
    L_{lm}\cos\theta & L_{lm}\cos(\theta-\frac{2\pi}{3}) & L_{lm}\cos(\theta+\frac{2\pi}{3}) & L_{rl} + L_{lm} & -\frac{1}{2}L_{lm} & -\frac{1}{2}L_{lm} \\
    L_{lm}\cos(\theta+\frac{2\pi}{3}) & L_{lm}\cos\theta & L_{lm}\cos(\theta-\frac{2\pi}{3}) & -\frac{1}{2}L_{lm} & L_{rl} + L_{lm} & -\frac{1}{2}L_{lm} \\
    L_{lm}\cos(\theta-\frac{2\pi}{3}) & L_{lm}\cos(\theta+\frac{2\pi}{3}) & L_{lm}\cos\theta & -\frac{1}{2}L_{lm} & -\frac{1}{2}L_{lm} & L_{rl} + L_{lm}
\end{bmatrix}
\begin{bmatrix}
    i_{sa} \\
    i_{sb} \\
    i_{sc} \\
    i_{ra} \\
    i_{rb} \\
    i_{rc}
\end{bmatrix}
$$

- 转矩

> 这里电流假定不变，即与机械角无关


$$
\begin{align}
T_e &=\frac{d}{d \theta}
\begin{bmatrix}
    i_{sa} & i_{sb}& i_{sc}  
\end{bmatrix}
\begin{bmatrix}
    \psi_{sa} \\
    \psi_{sb} \\
    \psi_{sc}  
\end{bmatrix}
\\% 第二行 \\
&=\frac{d}{d \theta}
(
\begin{bmatrix}
    i_{sa} & i_{sb}& i_{sc}  
\end{bmatrix}
\begin{bmatrix}
    \psi_{sa} \\
    \psi_{sb} \\
    \psi_{sc}  
\end{bmatrix})\\ %第三行
&=\frac{d}{d \theta}
(\begin{bmatrix}
    i_{sa} & i_{sb}& i_{sc}  
\end{bmatrix}
\frac{\partial L}{\partial \theta_m}
\begin{bmatrix}
    i_{sa} \\
    i_{sb} \\
    i_{sc}  
\end{bmatrix})\\ %第四行
\end{align}
$$


$$
\begin{align}
T_e = n_pL_{sm}
[(i_{sa}i_{ra}+i_{sb}i_{rb}+i_{sc}i_{rc})\sin \theta
+(i_{sa}i_{ra}+i_{sb}i_{rc}+i_{sc}i_{ra})\sin (\theta+\frac{2\pi}{3})
+(i_{sa}i_{rc}+i_{sb}i_{ra}+i_{sc}i_{rb})\sin (\theta-\frac{2\pi}{3})]
\end{align}
$$


## Constant voltage operation

```
指在电机或电磁回路中保持端电压（或励磁电压）恒定的运行方式。
书中前面章节对磁路、磁通密度 B、励磁安匝 NI、气隙和饱和等概念已有铺垫
因此恒压运行的直接后果要从这些物理量的相互关系来理解（例如磁路的磁动势 NI 推动磁通 Φ，气隙决定主要磁阻，磁密 B = Φ/A）
```





### 关键技术

#### buck-boost





#### DC/AC(单向逆变)









