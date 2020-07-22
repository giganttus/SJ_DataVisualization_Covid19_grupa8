# SJ_DataVisualization_Covid19_grupa8

<a href="https://www.youtube.com/watch?v=b7HvB_8-97U">WATCH PREVIEW OF PROJECT</a></br>

ENG 

1) To run project, save files from repository to one folder.<br/>
2) Install python, matplotlib and pandas (from official documentation, inside created folder for current project).<br/>
3) Run script "autoran.sh".<br/>

HRV (CRO)

1) Kako bi poreknuli projekt, spremite sve datoteke iz repozitorija u jedan folder.<br/>
2) Instalirajte python, matplotlib i pandas (iz službene dokumentacije, unutar stvorenog direktorija za trenutni projekt).<br/>
3) Pokrenite skriptu "autorun.sh"<br/>

![alt text](https://i.imgur.com/ePkMs9f.png)<br/>

This project is based on real data thats is extraceted from free sources. All used data is stored in CSV format because its nicest one to manipulate with tools and standards we used. Also we manipulated some CSV files, just to remove unwanted data for project or to merge few data from seperate files, and for this kind of work we used nice software Ron's Editor that can easily manipulate data stored in CSV files. All techniques and tools are listed below. </br>

With matplotlib, pandas and great sources we made simple data analasys of "how many times are searched these words" during 90 past days (past 90 days when we started coding). We decided to track words like sanitizer, mask and symptoms of covid19 just because in these days most interest is about COVID19. When you look at preview image of project, on left window you will see number of times these words were search (y axis) and date of that word searched (x axis). It's good to say that window is simulated dynamic data with animation. We made script that read line by line of real data and graph is collecting those data while displaying it in realtime. Inside right-bottom window is  same data seperated from each other and its staticly displayed when it's compared to animted window that we described before. And finally last one (right-top) is also static data with info about "current" (at time it was coded) status of COVID19 infection, just to give a touch of same theme with finally point.</br>

Each graph has seperated program and its run by bash script called "autorun.sh". Probably you ask yourself why to run it with script. It's because I like to work on each graph in details for that specified data and most likely because of memory usage of each one file.</br> 



Real data sources:<br/>
<ul>
<li><a href="https://trends.google.com/trends/?geo=US">Google Trends</a> (CSV files)</li>
<li>Worldmeter (COVID19 RAW data)</li>
</ul>

Tools and environment:<br/>
<ul>
<li>PyCharm (Coding environment)</li>
<li>Bash (autoran.sh script)</li>
<li>Ron's Editor (CSV manipulation)</li>
<li>Python (modules: matplotlib, pandas and others)</li>
</ul></br>
<a href="https://www.youtube.com/watch?v=b7HvB_8-97U">WATCH PREVIEW OF PROJECT</a></br>
