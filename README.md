# HotS QM Winrate Analysis

A quick analysis of hero win rates on various maps in Heroes of the Storm, in the quickmatch game mode.

Loads hero win rate data from the six maps in rotation (as of HotS build 20.6.47133), taken from [Hotslogs](http://www.hotslogs.com). There is data from both "All" skill levels, and from the "Gold" skill level.

For both skill levels, outputs:
* density plot
* strip plot on top of a box plot

### Requirements:
* Python 2.7
* pandas
* scipy
* numpy
* matplotlib
* seaborn
