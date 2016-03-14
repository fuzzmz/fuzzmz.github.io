Date: 2012-12-09
Title: Fast filename replace
Tags: PowerShell, scripting
Category: debug
Slug: filename-replace

This is a short article for a short PowerShell command.

Have you ever had a folder filled with files wheree you wanted to replace all spaces in the file names with dashes for example? If yes, then this script will work wonders for you.

    :::ps1
    get-childitem *.mp3 | foreach { rename-item $_ $_.Name.Replace(" ", "_") }

That command replaces all spaces with underscores in all mp3 files in the folder it's run. The syntax is pretty explicit, ```get-childitem``` tells powershell to get all the contents of the folder with the extension specified (in our case it's ```*.mp3```) and makes a loop over all elements (```foreach```) where it replaces all spaces with underscores for each item found with that extension.
