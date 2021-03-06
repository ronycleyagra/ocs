#%matplotlib inline
import os
import sys
import pandas as pd
import pymysql
import pandas.io.sql as psql
import matplotlib.pyplot as plt1
import matplotlib.pyplot as plt2

cnxn = pymysql.connect(host='*',database='*',user='*',password='*')
sql1 = "SELECT sc.path as path , re.registration_id FROM ocs.registrations re, ocs.sched_confs sc WHERE re.sched_conf_id = sc.sched_conf_id ;"
df1 = pd.read_sql(sql1, cnxn)
sql2 = "SELECT sc.path as path , pa.paper_id FROM ocs.papers pa, ocs.sched_confs sc WHERE sc.sched_conf_id = pa.sched_conf_id ;"
df2 = pd.read_sql(sql2, cnxn)
cnxn.close()

qtd1 = df1['path'].value_counts()
qtd1.plot(kind='bar', figsize=(20,5), grid=True, rot=0, color='blue', legend=False)
plt1.title('Quantidade de participantes por evento')
plt1.xlabel('Quantidade de participantes')
plt1.savefig('/home/rony/PycharmProjects/ocs/screens/registrations.jpg', dpi=None, facecolor = 'w', edgecolor = 'w', orientation = 'portrait', papertype = None, format = None, transparent = False, bbox_inches = None, pad_inches = 0.1, frameon = None)
plt1.show()

qtd2 = df2['path'].value_counts()
qtd2.plot(kind='bar', figsize=(20,5), grid=True, rot=0, color='blue', legend=False)
plt2.title('Quantidade de papers por evento')
plt2.xlabel('Quantidade de papers')
plt2.savefig('/home/rony/PycharmProjects/ocs/screens/papers.jpg', dpi=None, facecolor = 'w', edgecolor = 'w', orientation = 'portrait', papertype = None, format = None, transparent = False, bbox_inches = None, pad_inches = 0.1, frameon = None)
plt1.show()

#/home/rony/pycharm/projetoocs/task1.py
#plt.savefig('/home/rony/pycharm/aprendizadopandas/screens/tela1.jpg', dpi=None, facecolor = 'w', edgecolor = 'w', orientation = 'portrait', papertype = None, format = None, transparent = False, bbox_inches = None, pad_inches = 0.1, frameon = None)
#plt.show()