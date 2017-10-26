#%matplotlib inline
import os
import sys
import pandas as pd
import pymysql
import pandas.io.sql as psql
import matplotlib.pyplot as plt1
import matplotlib.pyplot as plt2
from bokeh.charts import Bar, output_file, show

cnxn = pymysql.connect(host='localhost',database='ocs',user='root',password='')
sql1 = "SELECT sc.path as path , count(re.registration_id) as qtd FROM ocs.registrations re, ocs.sched_confs sc WHERE re.sched_conf_id = sc.sched_conf_id group by path ;"
df1 = pd.read_sql(sql1, cnxn)
sql2 = "SELECT sc.path as path , pa.paper_id FROM ocs.papers pa, ocs.sched_confs sc WHERE sc.sched_conf_id = pa.sched_conf_id ;"
df2 = pd.read_sql(sql2, cnxn)
cnxn.close()
#print(df1)
p=Bar(df1, values='qtd', label=['path','qtd'])
output_file("graphs/barras1.html")
show(p)

