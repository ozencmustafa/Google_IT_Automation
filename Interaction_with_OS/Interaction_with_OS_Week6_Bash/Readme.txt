Script 1: findJane.sh
This script should catch all "jane" lines in the list.txt file and store them in another text file called oldFiles.txt.

Script 2: changeJane.py
Rename files using Python script. changeJane.py, that takes oldFiles.txt as a command line 
argument and then renames files with the new username "jdoe". 
Since oldFiles.txt is passed as a command line argument, it's stored in the variable sys.argv[1]

we run the script as below:
./changeJane.py oldFiles.txt


###################### Some unix command exercise #########################
Below information is nothing to do with the scripts above but just to remember some nice filtering methods.
As an example below is list.txt file contents:

001 jane /data/jane_profile_07272018.doc
002 kwood /data/kwood_profile_04022017.doc
003 pchow /data/pchow_profile_05152019.doc
004 janez /data/janez_profile_11042019.doc
005 jane /data/jane_pic_07282018.jpg
006 kwood /data/kwood_pic_04032017.jpg
007 pchow /data/pchow_pic_05162019.jpg
008 jane /data/jane_contact_07292018.csv
009 kwood /data/kwood_contact_04042017.csv
010 pchow /data/pchow_contact_05172019.csv


Example 1: 
<user># grep " jane " ../data/list.txt | cut -d ' ' -f 1
	001
	005
	008
Description:	
we use the cut command with grep command. For cut command, we'll use the whitespace 
character (‘ ‘) as a delimiter (denoted by -d) since the text strings are separated by spaces 
within the list.txt file. We'll also fetch results by specifying the fields using -f option.

Example 2:
<user># cat list.txt | tr ' ' '\n' | sort | uniq -c | sort -nr | head
	  3 pchow
      3 kwood
      3 jane
      1 janez
      1 /data/pchow_profile_05152019.doc
      1 /data/pchow_pic_05162019.jpg
      1 /data/pchow_contact_05172019.csv
      1 /data/kwood_profile_04022017.doc
      1 /data/kwood_pic_04032017.jpg
      1 /data/kwood_contact_04042017.csv

Description:
[tr ' ' '\n'] : translate space into new line. Basicly we put each word into new lines.
[sort] this command sorts the words alphabetically.
[uniq -c] displays each match once and -c flag prefixes each unique line with a number of occurance.
[sort -nr] sorts the result numerically in the reverse order from most to least.
[head] shows the first 10 lines.



