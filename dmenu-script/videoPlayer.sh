cd $HOME/Videos
mpv "$(ls *mp4 | dmenu -l 30)"
