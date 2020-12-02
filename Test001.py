from ProcLib import write_log, write_errlog, read_ini
from ClassLib import const

fn_ini = 'sysmex.ini'
read_ini(fn_ini)
print(f'analyser_location={const.analyser_location}')
# print(type(const.analyser_location))  # <class 'str'>

s = const.analyser_location.encode('cp1251').decode('utf8')
print('s=', s)
filename = 'temp01.txt'
with open(filename, 'a') as f:
    f.write(f'123 test Тест прогр: {s}\n')
