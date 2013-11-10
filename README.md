WorkSpace-Python
================
nku2db.py
----------------
    Curriculum information is on a NKU's website 
[NKU website](http://222.30.32.3/apps/xksc/index.asp)<br />

    There are totaly 140 pages
    On each page the are 20 lines information of curriculum
    We have a local MySQL database called nku.db with one table called 'class' in it
    There are 6 keys in 'class' named as follows:
> b_name (building name) <br />
> r_name (room name) <br />
> week_start (start week of a class) <br />
> week_end (end week of a class) <br />
> day_num (mon, tue, ... == 1,2,3,4,5,6,7) <br />
> day_time (1/2,3/4,5/6,7/8,9/10,11/12 == 1,2,3,4,5,6) <br />

    We would like to download the information into nku.db
