#!/bin/bash


set -e  # stop on first error

SESSION="discord_watcher"
LOG="$HOME/git/template_discord_watcher/run.log"

exec > >(tee -a "$LOG") 2>&1

tmux new -d -s $SESSION | true

tmux send-keys C-u
tmux send-keys -t $SESSION "cd ~"  C-m
tmux send-keys -t $SESSION "source venv_discord/bin/activate"  C-m
tmux send-keys -t $SESSION "cd ~/git/template_discord_watcher" C-m
tmux send-keys -t $SESSION "python3 main.py" C-m