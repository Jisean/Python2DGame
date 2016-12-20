; Script generated by the Inno Setup Script Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

[Setup]
; NOTE: The value of AppId uniquely identifies this application.
; Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppId={{507FC28D-D5C9-47F1-A8DB-101C718600F4}
AppName=Jazz
AppVersion=1.0
;AppVerName=Jazz 1.0
AppPublisher=Nia
DefaultDirName=C:\Jazz
DisableProgramGroupPage=yes
OutputDir=C:\Users\hsp05\Desktop
OutputBaseFilename=JazzSetup
Compression=lzma
SolidCompression=yes

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
Source: "C:\Users\hsp05\Desktop\2d����\Python2dgame\Client\dist\mygame.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\hsp05\Desktop\2d����\Python2dgame\Client\dist\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs
; NOTE: Don't use "Flags: ignoreversion" on any shared system files

[Icons]
Name: "{commonprograms}\Jazz"; Filename: "{app}\mygame.exe"
Name: "{commondesktop}\Jazz"; Filename: "{app}\mygame.exe"; Tasks: desktopicon

[Run]
Filename: "{app}\mygame.exe"; Description: "{cm:LaunchProgram,Jazz}"; Flags: nowait postinstall skipifsilent

