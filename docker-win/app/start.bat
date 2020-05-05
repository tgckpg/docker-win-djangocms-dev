@echo off

IF EXIST %SystemRoot%\System32\magic1.dll ( GOTO RUN_SERVER ) ELSE ( GOTO SETUP_WIN_MAGIC )

:SETUP_WIN_MAGIC
echo Setting up WinMagic...
cd C:\Python\Lib\site-packages\winmagic\nscaife\
copy *.dll %SystemRoot%\System32\

:RUN_SERVER
cd %ProjRoot%

:BEG_WEB_SRV
GOTO TEST_DB_CONN

:TEST_DB_WAIT
:: ping hack, wait for 3 seconds
ping 127.0.0.1 -n 4 > nul
echo Waiting for db to start...

:TEST_DB_CONN
psql -h db -d postgres -c "SELECT true;" > nul 2>&1
IF ERRORLEVEL 1 ( GOTO TEST_DB_WAIT )

python ./manage.py runserver 0.0.0.0:8000
GOTO BEG_WEB_SRV
