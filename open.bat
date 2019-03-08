@echo off
ren UDT
start "" "C:\Users\muna8996\ESS_PRD - Pilot V2\EssAgentDesktop.exe"
timeout 2
%~dp0\UDTAutoEnv\python.exe %~dp0enterExten.py %*