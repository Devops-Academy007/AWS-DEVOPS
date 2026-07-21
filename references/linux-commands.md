# Linux Cheat Sheet for DevOps

A day-to-day command reference · 3-Month DevOps Program · Class 1 handout

## How to use this document

This is a reference, not a memorization test. Read through it once now to get familiar with the layout, then come back to it whenever you need to look something up. Nobody remembers every Linux command from memory. What separates a beginner from a professional is knowing where to look and how to combine what they know.

Commands are grouped by what you will actually do on a Linux server as a DevOps engineer. The "Most Common Commands" section below lists the fifteen you will type most often.

A note on danger: some commands, especially the ones for deletion and permissions, can seriously damage a system if run in the wrong place. Those sections have caution notes. Read them twice.

---

## The Most Common Commands

If you only remembered these fifteen, you would be productive on any Linux server. Everything else in this document builds on top of them.

| Command | What it does |
|---|---|
| `pwd` | Print the folder you are currently in |
| `ls -la` | List everything in the current folder, including hidden files, with details |
| `cd <folder>` | Change into a folder |
| `cd ..` | Go up one level in the folder tree |
| `mkdir <name>` | Make a new folder |
| `cat <file>` | Show the contents of a file |
| `tail -f <log>` | Watch a log file as it is being written |
| `grep "text" <file>` | Find lines in a file that contain a piece of text |
| `cp <src> <dst>` | Copy a file |
| `mv <src> <dst>` | Move or rename a file |
| `rm <file>` | Delete a file (there is no recycle bin) |
| `sudo <command>` | Run a command with administrator privileges |
| `df -h` | Show how full the disk is, in readable units |
| `ps aux` | List every process currently running on the system |
| `history` | Show every command you have typed in this session |

---

## 1. Where Am I? Who Am I? What is This Machine?

The first thing any engineer does when they connect to a new server is confirm who they are, where they are, and what the machine is. Confusing production with staging is one of the most common causes of serious outages, and these commands protect against it.

| Command | What it does | Example |
|---|---|---|
| `pwd` | Print the folder you are in | `pwd` |
| `whoami` | Which user am I logged in as? | `whoami` |
| `hostname` | The name of this machine | `hostname` |
| `id` | My user ID and the groups I belong to | `id` |
| `uname -a` | Details about the operating system | `uname -a` |
| `uptime` | How long has this server been running? | `uptime` |
| `date` | Current date and time | `date` |
| `who` | Who else is currently logged into this server? | `who` |

---

## 2. Looking Around — Files and Folders

Most of your day on a server is spent looking at what is there. The `ls` command is the workhorse for this. Learning to read its output is a skill in itself.

| Command | What it does | Example |
|---|---|---|
| `ls` | List files in the current folder | `ls` |
| `ls -l` | Long format: shows permissions, size, and date | `ls -l` |
| `ls -la` | Include hidden files (files starting with a dot) | `ls -la` |
| `ls -lh` | Human-readable sizes, such as KB, MB, GB | `ls -lh` |
| `ls -lt` | Sort by newest first | `ls -lt` |
| `ls /etc` | List a folder without going into it | `ls /var/log` |
| `tree` | Show a folder as a tree diagram (may need install) | `tree -L 2` |

### Reading the output of `ls -l`

A line like `-rw-r--r-- 1 niraj devops 1024 Nov 12 14:30 config.yaml` contains several pieces of information. From left to right: the file permissions, the number of hard links, the owner, the group, the size in bytes, the last modified date, and finally the filename. The permissions column is the most important, and we cover it in Section 8.

---

## 3. Moving Around the Filesystem

| Command | What it does | Example |
|---|---|---|
| `cd <folder>` | Go into a folder | `cd /var/log` |
| `cd ..` | Go up one level | `cd ..` |
| `cd ../..` | Go up two levels | `cd ../..` |
| `cd ~` | Go to your home folder | `cd ~` |
| `cd -` | Go back to the previous folder you were in | `cd -` |
| `cd /` | Go to the root of the whole system | `cd /` |
| `pushd <folder>` | Go somewhere, remember where you were | `pushd /tmp` |
| `popd` | Return to where pushd remembered | `popd` |

> Note: `cd -` is the undo for navigation. If you jumped somewhere and want to come straight back, `cd -` bounces you back instantly. Small trick, saved many minutes.

---

## 4. Creating Things

| Command | What it does | Example |
|---|---|---|
| `mkdir <name>` | Make a folder | `mkdir logs` |
| `mkdir -p <a/b/c>` | Make nested folders in a single command | `mkdir -p app/logs/archive` |
| `touch <file>` | Make an empty file | `touch config.yaml` |
| `touch file1 file2 file3` | Make several files at once | `touch a.txt b.txt c.txt` |
| `echo "text" > <file>` | Write text into a file, overwriting anything there | `echo "hi" > note.txt` |
| `echo "text" >> <file>` | Append text to the end of a file | `echo "more" >> note.txt` |
| `nano <file>` | Open a simple editor: Ctrl+O to save, Ctrl+X to exit | `nano config.yaml` |
| `vim <file>` | A more powerful editor with a steeper learning curve | `vim script.sh` |

> Note: single arrow `>` overwrites, double arrow `>>` appends. This is one of the most common mistakes in shell scripts. One arrow is a scalpel that replaces everything, two arrows are glue that adds to the end.

---

## 5. Reading Files, Especially Logs

This is one of the most heavily used categories in DevOps. Logs are how you understand what your applications and servers are doing, and how you debug problems when they fail.

| Command | What it does | Example |
|---|---|---|
| `cat <file>` | Show the entire file at once | `cat error.log` |
| `less <file>` | Scroll through a file page by page (press q to quit) | `less huge.log` |
| `head <file>` | Show the first ten lines | `head config.yaml` |
| `head -n 50 <file>` | Show the first fifty lines | `head -n 50 access.log` |
| `tail <file>` | Show the last ten lines | `tail error.log` |
| `tail -n 100 <file>` | Show the last hundred lines | `tail -n 100 app.log` |
| `tail -f <file>` | Follow a file live as it grows | `tail -f /var/log/app.log` |
| `wc -l <file>` | Count lines in a file | `wc -l access.log` |

> Note: `tail -f` is possibly the single most-used command in a working DevOps engineer's day. When something is going wrong right now in production, this is the command that lets you watch the app in real time. Press Ctrl+C to stop watching.

---

## 6. Copy, Move, Delete

| Command | What it does | Example |
|---|---|---|
| `cp <src> <dst>` | Copy a file | `cp config.yaml config.backup` |
| `cp -r <src> <dst>` | Copy a folder and its contents | `cp -r app/ backup/` |
| `mv <src> <dst>` | Move or rename | `mv old.txt new.txt` |
| `rm <file>` | Delete a file | `rm junk.txt` |
| `rm -r <folder>` | Delete a folder and everything inside it | `rm -r old-project/` |
| `rm -rf <folder>` | Delete without asking, without complaining | `rm -rf temp/` |
| `rmdir <folder>` | Delete only if the folder is empty | `rmdir empty-folder/` |

> Caution: Linux does not have a recycle bin. When you delete a file, it is gone immediately. Never run `rm -rf /` anywhere, never run `rm -rf *` unless you have just confirmed where you are with `pwd`. There are well-known stories of engineers deleting entire production servers with a single stray command. Respect this section.

---

## 7. Searching Inside Files and Across Folders

Two commands do the heavy lifting here: `find`, for locating files by name or other properties, and `grep`, for searching inside files. Both are absolutely essential.

### find — locate files

| Command | What it does |
|---|---|
| `find . -name "config.yaml"` | Find files named config.yaml starting from the current folder |
| `find /var/log -name "*.log"` | Find all files ending with .log under /var/log |
| `find . -type f -mtime -1` | Find files modified in the last twenty-four hours |
| `find . -size +100M` | Find files bigger than 100 MB |

### grep — search inside files

| Command | What it does |
|---|---|
| `grep "error" app.log` | Show every line in app.log containing the word error |
| `grep -i "error" app.log` | Case-insensitive search |
| `grep -r "TODO" .` | Search across all files under the current folder |
| `grep -n "fail" app.log` | Show line numbers alongside matches |
| `grep -v "info" app.log` | Show lines that do not contain the given text |
| `grep -c "error" app.log` | Count how many matching lines there are |

You can combine grep with the earlier `tail -f` to watch a log for a specific pattern in real time. For example, `tail -f app.log | grep "error"` will only print new lines that contain the word error, ignoring everything else. This single line has helped solve countless production incidents.

---

## 8. Permissions and Ownership

Every file and folder in Linux has three things associated with it: an owner (a user), a group, and a set of permissions. Permissions cover three actions: read, write, and execute, and they are set separately for the owner, the group, and everyone else.

| Command | What it does | Example |
|---|---|---|
| `chmod <mode> <file>` | Change permissions on a file or folder | `chmod +x script.sh` |
| `chmod 755 <file>` | Numeric permissions (see the reference below) | `chmod 755 script.sh` |
| `chown <user> <file>` | Change the owner of a file (usually needs sudo) | `sudo chown niraj config.yaml` |
| `chown <user>:<group> <file>` | Change both owner and group | `sudo chown niraj:devops app/` |
| `chgrp <group> <file>` | Change only the group | `sudo chgrp devops config.yaml` |

### Common numeric permission patterns

| Command | What it does |
|---|---|
| `chmod +x file.sh` | Make a script executable |
| `chmod 644 file` | Owner can read and write, everyone else can only read — typical for config files |
| `chmod 755 script.sh` | Owner has full access, everyone else can read and run — typical for scripts |
| `chmod 600 secret.key` | Only the owner can read or write — use this for keys and passwords |

---

## 9. Sudo and Users

| Command | What it does | Example |
|---|---|---|
| `sudo <command>` | Run a single command as the administrator | `sudo apt update` |
| `sudo -i` | Become the administrator for the whole session | `sudo -i` |
| `sudo !!` | Rerun your previous command with sudo | `sudo !!` |
| `su - <user>` | Switch to another user account | `su - deploy` |
| `passwd` | Change your own password | `passwd` |
| `exit` | Leave the current shell or SSH session | `exit` |

> Note: `sudo !!` is a gift. You typed a command, got permission denied, now type `sudo !!` and it reruns the previous command with sudo. It looks like a small trick but you will use it every day.

---

## 10. Processes — Everything That is Running

Every program running on a Linux machine is called a process. Each process has a unique number called a PID, or process ID. Managing processes — starting them, checking them, stopping them — is a daily activity.

| Command | What it does | Example |
|---|---|---|
| `ps aux` | List every process on the system | `ps aux` |
| `ps aux \| grep nginx` | Find a specific process by name | `ps aux \| grep python` |
| `top` | Live view of running processes (press q to quit) | `top` |
| `htop` | A prettier version of top; may need install | `htop` |
| `kill <PID>` | Ask a process to stop cleanly | `kill 12345` |
| `kill -9 <PID>` | Force a process to stop immediately | `kill -9 12345` |
| `killall <name>` | Kill all processes with a given name | `killall python` |
| `jobs` | List background jobs in the current shell | `jobs` |
| `<command> &` | Run a command in the background | `python script.py &` |
| `nohup <cmd> &` | Run in the background, keep running after logout | `nohup ./server.sh &` |

---

## 11. System Health — Disk, Memory, CPU

Checking these commands is a reflex for every operations engineer. When a server misbehaves, the first thing you do is ask: is it out of disk, out of memory, or out of CPU?

| Command | What it does | Example |
|---|---|---|
| `df -h` | How full is each disk? | `df -h` |
| `du -sh <folder>` | Size of a specific folder | `du -sh /var/log` |
| `du -sh *` | Size of everything in the current folder | `du -sh *` |
| `free -h` | RAM usage in human-readable form | `free -h` |
| `top` | Live CPU, memory and process view | `top` |
| `uptime` | Load average — how busy the system has been | `uptime` |
| `lscpu` | CPU details | `lscpu` |
| `lsblk` | List storage devices attached to the system | `lsblk` |

> Note: when a server acts up, the standard first ritual is: `uptime`, then `df -h`, then `free -h`, then `top`. Four commands, and most problems become visible.

---

## 12. Networking Essentials

| Command | What it does | Example |
|---|---|---|
| `ping <host>` | Is the host reachable? Press Ctrl+C to stop. | `ping google.com` |
| `curl <url>` | Fetch a URL from the command line | `curl https://api.github.com` |
| `curl -I <url>` | Just the response headers (useful for checking status codes) | `curl -I https://mysite.com` |
| `wget <url>` | Download a file from a URL | `wget https://example.com/file.tar.gz` |
| `ss -tuln` | Show which ports on this machine are listening | `ss -tuln` |
| `ip a` | Show the network addresses of this machine | `ip a` |
| `dig <domain>` | Look up DNS records for a domain | `dig google.com` |
| `nslookup <domain>` | Simpler DNS lookup | `nslookup google.com` |
| `traceroute <host>` | Show every network hop to a destination | `traceroute google.com` |

### SSH — remote access to servers

| Command | What it does |
|---|---|
| `ssh user@host` | Connect to a remote server |
| `ssh -i key.pem user@host` | Connect using a private key file |
| `scp file user@host:/path/` | Copy a file to a remote server |
| `scp user@host:/path/file .` | Copy a file from a remote server |
| `rsync -avz src/ user@host:dst/` | Smart file sync — only transfers what has changed |

---

## 13. Package Management (Ubuntu and Debian)

These are the commands to install and remove software on Ubuntu. WSL uses Ubuntu by default, and much of AWS runs on Ubuntu or Amazon Linux (which uses similar commands with `yum` or `dnf` instead of `apt`).

| Command | What it does | Example |
|---|---|---|
| `sudo apt update` | Refresh the list of available packages | `sudo apt update` |
| `sudo apt upgrade` | Install available updates | `sudo apt upgrade` |
| `sudo apt install <pkg>` | Install a package | `sudo apt install curl` |
| `sudo apt remove <pkg>` | Uninstall a package | `sudo apt remove curl` |
| `apt search <term>` | Search for available packages | `apt search python3` |
| `apt list --installed` | List everything that is already installed | `apt list --installed` |
| `which <cmd>` | Show where a command lives on disk | `which python3` |

---

## 14. Compression and Archives

Very common when moving files between servers or storing backups. The `tar` command is worth remembering well.

| Command | What it does | Example |
|---|---|---|
| `tar -czf <name>.tar.gz <folder>` | Create a compressed archive of a folder | `tar -czf backup.tar.gz app/` |
| `tar -xzf <name>.tar.gz` | Extract a compressed archive | `tar -xzf backup.tar.gz` |
| `tar -tzf <name>.tar.gz` | Look inside an archive without extracting | `tar -tzf backup.tar.gz` |
| `gzip <file>` | Compress a single file | `gzip large.log` |
| `gunzip <file.gz>` | Decompress a gzip file | `gunzip large.log.gz` |
| `zip -r out.zip <folder>` | Create a zip file from a folder | `zip -r site.zip site/` |
| `unzip <file.zip>` | Extract a zip file | `unzip site.zip` |

> Note: a memory trick for tar — think `czf` as Create and `xzf` as eXtract. Almost nobody remembers the flags without a mental shortcut.

---

## 15. Pipes and Redirection

This is where Linux stops being a set of separate commands and starts feeling like a language. You take small commands, chain them together, and build powerful behaviour by combining simple pieces.

| Symbol | What it does |
|---|---|
| `\|` | Send the output of one command into the input of another |
| `>` | Send output to a file, overwriting anything there |
| `>>` | Send output to a file, appending to the end |
| `<` | Read input from a file |
| `2>` | Redirect error messages to a file |
| `&>` | Redirect both output and error messages to the same place |
| `command1 && command2` | Run the second command only if the first succeeded |
| `command1 \|\| command2` | Run the second command only if the first failed |
| `;` | Run several commands one after another |

A real example: `ps aux | grep nginx | grep -v grep | awk '{print $2}'` finds every nginx process and prints only its PID. Once you can read a chained pipeline like this, you are on your way to using Linux fluently.

---

## 16. Text Processing

These commands become more relevant when we get into shell scripting in Week 2. For now, know they exist.

| Command | What it does | Example |
|---|---|---|
| `sort` | Sort lines alphabetically | `sort names.txt` |
| `uniq` | Remove duplicate lines (needs sorted input) | `sort names.txt \| uniq` |
| `cut -d "," -f 1` | Take a specific column from delimited input | `cut -d "," -f 1 data.csv` |
| `wc -l` | Count lines | `wc -l access.log` |
| `sed 's/old/new/g'` | Find and replace in a stream of text | `sed 's/error/ERROR/g' log.txt` |
| `awk '{print $1}'` | Take the first column of each line | `ps aux \| awk '{print $2}'` |

---

## 17. Environment Variables

Values that Linux remembers for you and shares with the programs you run. Programs read them for configuration — a common pattern in modern DevOps.

| Command | What it does | Example |
|---|---|---|
| `echo $HOME` | Print the value of a variable | `echo $HOME` |
| `echo $PATH` | Where the shell searches for commands | `echo $PATH` |
| `env` | List every environment variable | `env` |
| `export VAR=value` | Set a variable for the current session | `export API_KEY=abc123` |
| `unset VAR` | Remove a variable | `unset API_KEY` |

### Useful built-in variables

| Variable | What it holds |
|---|---|
| `$HOME` | Your home folder |
| `$USER` | Your username |
| `$PATH` | The list of folders where the shell looks for commands |
| `$SHELL` | Which shell you are currently running, usually /bin/bash |

---

## 18. Keyboard Shortcuts

These are worth more than any single command. Tab completion alone will roughly double your speed on the terminal.

| Keys | What it does |
|---|---|
| `Tab` | Auto-complete a file, folder, or command name. Press twice to see options. |
| `Up / Down arrow` | Cycle through previous commands |
| `Ctrl + R` | Search through command history. Start typing, then press Ctrl+R again for older matches. |
| `Ctrl + C` | Cancel the currently running command |
| `Ctrl + D` | Log out or end input |
| `Ctrl + L` | Clear the screen (same as running clear) |
| `Ctrl + A` | Jump to the beginning of the line |
| `Ctrl + E` | Jump to the end of the line |
| `Ctrl + U` | Erase the entire line |
| `Ctrl + K` | Erase from the cursor to the end of the line |
| `Ctrl + W` | Delete one word backwards |
| `!!` | The previous command. Combine with sudo as `sudo !!` to rerun as admin. |
| `!$` | The last argument from the previous command |

---

## 19. Getting Help Without Leaving the Terminal

| Command | What it does |
|---|---|
| `<command> --help` | Quick reference for how to use a command |
| `man <command>` | The full manual. Press q to quit. |
| `history` | Every command you have typed in this session |
| `history \| grep <word>` | Search back through your history |
| `which <cmd>` | Show where a command lives on disk |
| `type <cmd>` | Is it a program, an alias, or a shell builtin? |
| `clear` | Clear the screen |

---

## 20. Ten Commands You Will Type Without Thinking

The commands that a working platform engineer runs almost automatically, several times a day. Your own list will look very similar within a few months.

| Command | Why |
|---|---|
| `ls -la` | What is in this folder? |
| `cd -` | Bounce back to where I was |
| `tail -f /var/log/app.log` | Watch the application in real time |
| `grep -i "error" *.log` | What went wrong? |
| `ps aux \| grep <name>` | Is that process running? |
| `df -h` | Are we running out of disk? |
| `sudo systemctl status <service>` | Is the service healthy? |
| `ssh <server>` | Hop over to another machine |
| `history \| grep <word>` | What did I do last time to solve this? |
| `!!` | I meant to sudo that, didn't I? |

---

## Where to Practice Safely

- Your own terminal — WSL on Windows, Terminal on Mac, or GitHub Codespaces in a browser. You cannot damage your machine by typing commands in your home folder.
- explainshell.com — paste any command into the box and it explains every piece of it. Extremely helpful when you find a scary-looking one-liner in a tutorial.
- overthewire.org/wargames/bandit — free Linux puzzles that teach commands through play. Highly recommended for evenings in the first two weeks of the course.

---

This document will grow with you over the next twelve weeks. Refer back to it whenever you need to, use the commands inside labs and homework, and they will start to feel natural on their own.