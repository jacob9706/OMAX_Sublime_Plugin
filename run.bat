@cd %programfiles(x86)%\

@if %ERRORLEVEL% == 0 (echo x64&&"C:\Program Files (x86)\OMAX Corporation\OMAX_Layout_and_Make\Layout.exe" %1)

@if %ERRORLEVEL% == 1 (echo x86&&"C:\Program Files\OMAX Corporation\OMAX_Layout_and_Make\Layout.exe %1")
