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
  <img width="150" height="50" src="https://latex.codecogs.com/gif.image?\dpi{300}&space;\sum_{ij}&space;(p_{ij}-p)x_{ij}&space;\le&space;0">
</p>

Where:

* x<sub>ij</sub> - Amount of shares from i-th wallet, j-th enterprise;
* d<sub>ij</sub> - Dividend yield from i-th wallet, j-th enterprise's share;
* b - Financial boundary - The total amount of available resources to invest;
* p<sub>ij</sub> - Relation between net worth and amount of total share amount;
* p - Maximum mean relation between net worth and amount of total share amount expected to achieve;