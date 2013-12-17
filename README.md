reduce
======

Reducing Majorise Series

Preface.
This code contains some mathematical terms. In this text, "majorise" verb needs two series of positive integers namely A(a1,a2,...,an) and B(b1,b2,...,bn) and the verb means the sum of the terms in A and B equals, also to any point, sum of terms of A is greater or equal to sum of terms of B.

This algorithm takes two majorise series namely "A majorise B", and with several operations turns A into B. This reducing makes our work easy about mathematics, especieally Analysis and Inequalities. 

The main purpose of this code is prove well known inequalities in mathematics with vairous ways, namely getting our proof done WITHOUT dealing variables and hard thinking of mathematics.

The simple application of this algorithm is verify the fact Square Root - Arithmetic Root Mean located at http://mathworld.wolfram.com/SquareRootInequality.html

If interested with connection this code into Analysis Mathematics, feel free to mail me.

After mention about math, lets take a look about what our code does,

Let A=(7,7,2) and B(6,6,4). We want to turn A into B in such way,

-Every single turn, select two terms from A, namely m and n, and change them to m-1,n+1 such that A still remains downwards sorted and majorise to B.

If we run our code with A and B, outputs will be [7, 7, 2] [7, 6, 3] [6, 6, 4] so A is turned into B.

Behind the code there is a combinatoric proof of after several turns, it always be possible to reduce A into B. 

You can contact me at  mehmetfazil at outlook dot com.
