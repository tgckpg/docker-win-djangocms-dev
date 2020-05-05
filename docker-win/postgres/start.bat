@echo off

IF EXIST "%PGDATA%\pg_hba.conf" GOTO SERVICE_START ELSE GOTO INIT_DB

:INIT_DB
initdb --encoding="UTF8"
echo listen_addresses = '*' >> "%PGDATA%\postgresql.conf"
echo host  all  all  0.0.0.0/0  trust >> "%PGDATA%\pg_hba.conf"
echo host  all  all  ::0/0      trust >> "%PGDATA%\pg_hba.conf"

:SERVICE_START
pg_ctl -D "%PGDATA%" start -l pg.log

:MONITOR_LOOP
waitfor SIGNOP /t 3 2>NUL
pg_ctl -D "%PGDATA%" status >NUL
IF %ERRORLEVEL% EQU 0 ( GOTO MONITOR_LOOP ) ELSE ( exit %ERRORLEVEL% )
