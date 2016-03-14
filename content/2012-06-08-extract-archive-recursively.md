Date: 2012-06-08
Title: Enhanc... erm, extract!
Tags: 7-zip, recursive, archives, bat
Category: debug
Slug: extract-archive-recursively

We've all been there, haven't we? We just downloaded the latest seaso... erm, Linux distro and it came with lots of folders which in turn contain lots of archives, one folder per episode. One way to do things is to just extract each episode... erm, distro, by hand, watch it, move to the next and so on.

Another way would be to write a Windows batch script to make [7-zip](www.7-zip.org/) go through all the archives and extract their contents, which means you run it once and end up with all the files out.

	:::bat
	FOR /D /r %%F in ("*") DO (
		pushd %CD%
		cd %%F
			FOR %%X in (*.rar *.zip) DO (
				"C:\Program Files\7-zip\7z.exe" x %%X
			)
		popd
	)

Note that if you're running a 64bit OS but don't have the 64bit version of 7-zip installed you need to change "C:\Program Files\7-zip\7z.exe" x %%X into "C:\Program Files (x86)\7-zip\7z.exe" x %%X

Launch the bat, and all rar's/zips will be extracted into the folder they are contained in.

Now let's be helpful and dissect the script, shall we?

	:::bat
	FOR /D /r %%F in ("*") DO (

This is a simple for loop to go through all folders in the current directory, and put the path into a variable %%F.

	:::bat
	pushd %CD%

Put the current directory into memory.

	:::bat
	cd %%F

Set the folder from variable %%F as the current directory.

	:::bat
	FOR %%X in (*.rar *.zip) DO (

For all the archives (rar and zip) in the current folder, do:

	:::bat
	"C:\Program Files\7-zip\7z.exe" x %%X

Run 7-zip on the files with the extract parameter (basically call the command line version of 7-zip telling it to extract the current archive)

	:::bat
	popd

Return to the previous directory stored in memory.

That's it! Pretty simple and efficient, isn't it?
