# Preventing sudo timeout https://serverfault.com/a/833888
trap "exit" INT TERM; trap "kill 0" EXIT; sudo -v || exit $?; sleep 1; while true; do sleep 60; sudo -nv; done 2>/dev/null &

echo "Updating and Upgrading"
sudo apt update && sudo apt upgrade -y

echo "Installing Multimedia Libraries"
sudo apt install ubuntu-restricted-extras -y

echo "Installing Gnome Tweak Tool"
sudo apt install gnome-tweaks -y

echo "Installing Communitheme"
sudo snap install communitheme

echo "Installing Sublime Text"
sudo snap install sublime-text --classic

echo "Installing Spotify"
sudo snap install spotify

echo "Installing Pycharm Community"
sudo snap install pycharm-community --classic

echo "Installing Android Studio"
sudo snap install android-studio --classic

echo "Installing IntelliJ IDEA Community"
sudo snap install intellij-idea-community --classic

echo "Installing Visual Studio Code"
sudo snap install code --classic

echo "Installing Postman"
sudo snap install Postman

echo "Installing pip and pip3"
sudo apt install python-pip -y
sudo apt install python3-pip -y

echo "Installing standard Python libraries"
pip3 install --user numpy
pip3 install --user pandas
pip3 install --user scipy
pip3 install --user matplotlib

echo "Install PX4 pip dependencies"
pip3 install --user empy
pip3 install --user pyros-genmsg
pip3 install --user packaging
pip3 install --user jinja2
pip3 install --user toml

echo "Cleaning"
sudo apt autoclean
sudo apt clean
sudo apt autoremove
