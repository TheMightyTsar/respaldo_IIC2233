import cx_Freeze as CF

CF.setup(name = 'DCCruz',
         options = {'build_exe': {'packages': ['PyQt5', 'random', 'threading', 'sys', 'os']}},
         version = '1.0',
         executables = [CF.Executable(r'C:\Users\capuc\TheMightyTsar-iic2233-2022-2\Tareas\T2\main.py')])
