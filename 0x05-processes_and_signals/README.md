# More system dev ops - processes and signals

## Description

This repository contains some tasks for Holberton School.

### Files description

- **0-what-is-my-pid:** a Bash script that displays its own PID.

- **1-list_your_processes:** a Bash script that displays a list of currently running processes.

- **2-show_your_bash_pid:** a Bash script that displays lines containing the bash word, thus allowing you to easily get the PID of your Bash process.

- **3-show_your_bash_pid_made_easy:** a Bash script that displays the PID, along with the process name, of processes whose name contain the word bash.

- **4-to_infinity_and_beyond:** a Bash script that displays To infinity and beyond indefinitely.

- **5-kill_me_now:** a Bash script that kills 4-to_infinity_and_beyond process.

- **6-kill_me_now_made_easy:** a Bash script that kills 4-to_infinity_and_beyond process.

- **7-highlander:** a Bash script that displays:

  - To infinity and beyond indefinitely
  - With a sleep 2 in between each iteration
  - I am invincible!!! when receiving a SIGTERM signal

- **8-beheaded_process:** a Bash script that kills the process 7-highlander.

- **100-process_and_pid_file:** a Bash script that:

  - Creates the file /var/run/holbertonscript.pid containing its PID
  - Displays To infinity and beyond indefinitely
  - Displays I hate the kill command when receiving a SIGTERM signal
  - Displays Y U no love me?! when receiving a SIGINT signal
  - Deletes the file /var/run/holbertonscript.pid and terminates itself when receiving a SIGQUIT or SIGTERM signal
