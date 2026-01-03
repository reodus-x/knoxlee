#!/usr/bin/env python3

# Author: Arvin Gonzales
# Author ID: reodus.x
# Email: navir@reodus.dev
# Date Created: 2026/1/3
# Purpose: INSTALL yt-dlp
# Use case: For downloading online videos - like YT videos

# install 

#Download the latest yt-dlp binary
sudo curl -L https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp -o /usr/local/bin/yt-dlp

#Make it executable
sudo chmod a+rx /usr/local/bin/yt-dlp

#Verify installation
yt-dlp --version

# Enable self-updating
sudo yt-dlp -U

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

#See all available formats first
yt-dlp -F <YouTube_URL>

# Download with best audio
yt-dlp -f bestaudio --extract-audio <YouTube_URL>

# Download with max bitrate
yt-dlp -f bestaudio -x --audio-format m4a --audio-quality 0 -o '~/Music/%(title)s.%(ext)s' <YouTube_URL>

#Download a video in default quality
yt-dlp <YouTube_URL>

#137+140 → Merges video 1080p (137) + audio 128k (140)
#Automatically combine the streams
yt-dlp -f 137+140 <YouTube_URL>

#Download an entire playlist
#Creates a folder with the playlist name, saves each video with its title
yt-dlp -o '~/Videos/%(playlist)s/%(title)s.%(ext)s' <Playlist_URL>

#Download and convert to mp4
yt-dlp -f bestvideo+bestaudio --merge-output-format mp4 <YouTube_URL>

#Dowload best video and best audio
yt-dlp -f bestvideo+bestaudio --merge-output-format mp4 -o '~/Videos/%(title)s.%(ext)s' <YouTube_URL>
  

#EOF
