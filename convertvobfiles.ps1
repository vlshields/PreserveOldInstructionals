# Set the path to the folder where you want to store the extracted VOB files
$extractedFolderPath = "C:\Users\Vince\desktop\WormGuard"

# Set the path to the MakeMKV executable
$makemkvPath = "C:\Program Files (x86)\MakeMKV\makemkv.exe"

# Set the drive letter of your DVD drive
$dvdDriveLetter = "D:"

# Use MakeMKV to extract VOB files from the DVD
& $makemkvPath --minlength=600 mkv disc:$dvdDriveLetter all $extractedFolderPath

# Get all .mkv files in the extracted folder
$mkvFiles = Get-ChildItem -Path $extractedFolderPath -Filter *.mkv

