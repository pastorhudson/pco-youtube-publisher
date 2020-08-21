#!/bin/bash
#Change all the /home/user to /home/your_home_dir

# Add to crontab run every 15 min
# */15 * * * * /home/user/pco-youtube-publisher/update_publishing.sh > /home/user/pco-youtube-publisher/log.txt


timestamp() {
  date +"%T"
}
cd /home/user/pco-youtube-publisher
source /home/user/pco-youtube-publisher/venv/bin/activate
python -V >> /home/user/pco-youtube-publisher/log.txt
echo "Running script"
python3.8 /home/user/pco-youtube-publisher/pco-youtube-publisher.py >> log.txt
echo "All done" $(timestamp)
