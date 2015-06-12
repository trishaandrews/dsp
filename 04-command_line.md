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
pushd - skip to directory <br>
popd - easily skip back from pushd directory <br>
mkdir - make series of directories with -p <br>
touch - makes an empty file <br>
apropos - find what man page is appropriate, displays MANY options <br>
export - export/set a new environment variable <br>
unset - remove env variable <br>
chmod - change files and directories recursively with -R <br>
	&emsp; 755 = User:rwx Group:r-x World:r-x <br>
chown - change ownership <br>
	&emsp; chown root /u <br>
	&emsp; &emsp;    Change the owner of /u to "root". <br>
xargs - execute arguments <br>
	&emsp; find /tmp -name core -type f -print0 | xargs -0 /bin/rm -f <br>
       Find files named core in or below the directory /tmp and  delete  them,
       processing  filenames  in  such a way that file or directory names con‐
       taining spaces or newlines are correctly handled. <br>
	&emsp; xargs sh -c 'emacs "$@" < /dev/tty' emacs <br>
       Launches  the  minimum  number of copies of Emacs needed, one after the
       other, to edit the files listed on xargs' standard input.  This example
       achieves the same effect as BSD's -o option, but in a more flexible and
       portable way. <br>



---


---

What does `ls` do? What do `ls -a`, `ls -l`, and `ls -lh` do? What combinations of those flags are meaningful?

ls lists files in the working directory <br>
ls -a lists files found with plain ls plus hidden files <br>
ls -l lists files along with information on their permissinos, size, and date last modified <br>
ls -lh is the same is ls -l but with the size formatted in a more readable format <br>

ls, ls -a, and ls -l are all useful for their respective purposes. ls -lh doesn't seem to serve much purpose. ls -al could be useful for seeing modifications, permissions, etc of hidden files

---


---

What does `xargs` do? Give an example of how to use it.

 xargs reads and executes input arguments <br>
 
 find /tmp -name core -type f -print0 | xargs -0 /bin/rm -f <br>
       &emsp; Find files named core in or below the directory /tmp and  delete  them,
       processing  filenames  in  such a way that file or directory names con‐
       taining spaces or newlines are correctly handled. <br>

xargs sh -c 'emacs "$@" < /dev/tty' emacs <br>
       &emsp; Launches  the  minimum  number of copies of Emacs needed, one after the
       other, to edit the files listed on xargs' standard input.  This example
       achieves the same effect as BSD's -o option, but in a more flexible and
       portable way.

---
