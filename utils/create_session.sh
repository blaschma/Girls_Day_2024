

host_name=$(hostname -f)
#create local dir
rm -rf ~/$host_name
mkdir ~/$host_name
cd ~/$host_name
git clone https://github.com/blaschma/Girls_Day_2024
cd Girls_Day_2024
nohup jupyter notebook --no-browser --NotebookApp.token='' --NotebookApp.password='' &
profile="gast_$host_name"
firefox-esr -CreateProfile $profile
firefox-esr --kiosk "http://localhost:8888/" -P $profile