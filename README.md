# fundsAllocation

# Objective

The ideia of this project is to maximize dividend (Real Estate specific), considering available resources, wallets and important indexes. Mathematically, the ideia is:

maximize: 

<!-- $$
\sum_{i,j}d_{ij}x_{ij}
$$ --> 

<div align="center"><img style="background: white;" src="..\..\svg\uJJqjE7wIa.svg"></div>

<!--<p align="center">

  <img width="100" height="50" src="https://latex.codecogs.com/gif.image?\dpi{300}&space;\sum_{i,j}d_{ij}x_{ij}">
</p> -->

subject to:

<!-- $$
\sum_{i,j}x_{ij} \le b
$$ --> 

<div align="center"><img style="background: white;" src="..\..\svg\OecpIzFuc8.svg"></div>

<!-- $$
\sum_{i}x_{ij} \ge 1
$$ --> 

<div align="center"><img style="background: white;" src="..\..\svg\VZ11QqaKNR.svg"></div>

<!-- $$
\sum_{i,j}(p_{ij} - \bar{p}) \le 0
$$ --> 

<div align="center"><img style="background: white;" src="..\..\svg\n6MIObCn9r.svg"></div>
<!-- <p align="center">
  <img width="100" height="50" src="https://latex.codecogs.com/gif.image?\dpi{300}&space;\sum_{i,j}&space;x_{ij}&space;\le&space;b" title="\sum_{i,j} x_{ij} \le b">
</p> -->
<!-- <p align="center">
  <img width="100" height="50" src="https://latex.codecogs.com/gif.image?\dpi{300}&space;\sum_{i}&space;x_{ij}&space;\ge&space;1">
</p>
<p align="center">
  <img width="150" height="50" src="https://latex.codecogs.com/gif.image?\dpi{300}&space;\sum_{ij}&space;(p_{ij}-\bar{p})x_{ij}&space;\le&space;0">
</p> -->

Where:

* x<sub>ij</sub> - Amount of shares from i-th wallet, j-th enterprise;
* d<sub>ij</sub> - Dividend yield from i-th wallet, j-th enterprise's share;
* b - Financial boundary - The total amount of available resources to invest;
* p<sub>ij</sub> - Relation between net worth and amount of total share amount;
* $\bar{p}$ - Maximum mean relation between net worth and amount of total share amount expected to achieve;