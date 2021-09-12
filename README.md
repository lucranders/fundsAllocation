# fundsAllocation

# Objective

The ideia of this project is to maximize dividend (Real Estate specific), considering available resources, wallets and important indexes. Mathematically, the ideia is:

maximize: 


<p align="center">

  <img width="100" height="50" src="https://latex.codecogs.com/gif.image?\dpi{300}&space;\sum_{i,j}d_{ij}x_{ij}">
</p>

subject to:


<p align="center">
  <img width="100" height="50" src="https://latex.codecogs.com/gif.image?\dpi{300}&space;\sum_{i,j}&space;x_{ij}&space;\le&space;b" title="\sum_{i,j} x_{ij} \le b">
</p>
<p align="center">
  <img width="100" height="50" src="https://latex.codecogs.com/gif.image?\dpi{300}&space;\sum_{i}&space;x_{ij}&space;\ge&space;1">
</p>
<p align="center">
  <img width="170" height="50" src="https://latex.codecogs.com/gif.image?\dpi{300}&space;\sum_{i,j}&space;(p_{ij}-p)x_{ij}&space;\le&space;0">
</p>

Where:

* x<sub>ij</sub> - Amount of shares from i-th wallet, j-th enterprise;
* d<sub>ij</sub> - Dividend yield from i-th wallet, j-th enterprise's share;
* b - Financial boundary - The total amount of available resources to invest;
* p<sub>ij</sub> - Relation between net worth and amount of total share amount;
* p - Maximum mean relation between net worth and amount of total share amount expected to achieve;

# How to use

In the same folder this project was cloned, two files must be created:

* ListFiis.txt - Must contain the chosen Real Estate shares of desire and from which wallet it comes from (without header). File example:

<p align="center">
HGCR11,2<br/>
VISC11,1<br/>
LUGG11,1<br/>
RECT11,3<br/>
CPTS11,2<br/>
JSRE11,3<br/>
HGRU11,1<br/>
HSLG11,4<br/>
RBRP11,3<br/>
VILG11,4<br/>

</p>

* tolValues.txt - Must contain the Maximum mean relation between net worth and amount of total share amount expected to achieve and the expected value to invest (p and b). File example:

<p align="center">
0.9,1000
</p>

When both files exist and are correctly filled, it is only needed to execute the main.py program. It is easier for Windows users, because it only requires to double click exec.bat file. The output will be as shown below:


<p align="center">
  <img width="400" height="300" src="output.PNG">
</p>
