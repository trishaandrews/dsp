# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](http://cli.learncodethehardway.org/book/). This is a great,
quick tutorial. Each "chapter" focuses on a command. Type the commands
you see in the _Do This_ section, and read the _You Learned This_
section. Move on to the next chapter. You should be able to go through
these in a couple of hours.


---

Make a cheat sheet for yourself: a list of commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

cmd line reference <br>
pushd - skip to directory

popd - easily skip back from pushd directory

mkdir - make series of directories with -p

touch - makes an empty file

apropos - find what man page is appropriate, displays MANY options

export - export/set a new environment variable

unset - remove env variable

chmod - change files and directories recursively with -R
	755 = User:rwx Group:r-x World:r-x
chown - change ownership
	chown root /u
	    Change the owner of /u to "root".

xargs - execute arguments
	find /tmp -name core -type f -print0 | xargs -0 /bin/rm -f
	Find files named core in or below the directory /tmp and  delete  them,
       processing  filenames  in  such a way that file or directory names con‐
       taining spaces or newlines are correctly handled.
       
xargs sh -c 'emacs "$@" < /dev/tty' emacs
	
       Launches  the  minimum  number of copies of Emacs needed, one after the
       other, to edit the files listed on xargs' standard input.  This example
       achieves the same effect as BSD's -o option, but in a more flexible and
       portable way.



---


---

What does `ls` do? What do `ls -a`, `ls -l`, and `ls -lh` do? What combinations of those flags are meaningful?

ls lists files in the working directory
ls -a lists files found with plain ls plus hidden files
ls -l lists files along with information on their permissinos, size, and date last modified
ls -lh is the same is ls -l but with the size formatted in a more readable format

ls, ls -a, and ls -l are all useful for their respective purposes. ls -lh doesn't seem to serve much purpose. ls -al could be useful for seeing modifications, permissions, etc of hidden files

---


---

What does `xargs` do? Give an example of how to use it.

 xargs reads and executes input arguments
	find /tmp -name core -type f -print0 | xargs -0 /bin/rm -f
	
       Find files named core in or below the directory /tmp and  delete  them,
       processing  filenames  in  such a way that file or directory names con‐
       taining spaces or newlines are correctly handled.

xargs sh -c 'emacs "$@" < /dev/tty' emacs
	
       Launches  the  minimum  number of copies of Emacs needed, one after the
       other, to edit the files listed on xargs' standard input.  This example
       achieves the same effect as BSD's -o option, but in a more flexible and
       portable way.

---
