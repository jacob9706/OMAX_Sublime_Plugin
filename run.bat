@cd %programfiles(x86)%\

@if %ERRORLEVEL% == 0 (start /d "C:\Program Files (x86)\OMAX Corporation\OMAX_Layout_and_Make" OMAX_Script.exe /AutoRun %1)
@if %ERRORLEVEL% == 1 (start /d "C:\Program Files\OMAX Corporation\OMAX_Layout_and_Make" OMAX_Script.exe /AutoRun %1)