@if not "%programfiles(x86)%" == "" (start /d "%programfiles(x86)%\OMAX Corporation\OMAX_Layout_and_Make" Layout.exe %1)
@if "%programfiles(x86)%" == "" (start /d "%programfiles%\OMAX Corporation\OMAX_Layout_and_Make" Layout.exe %1)

