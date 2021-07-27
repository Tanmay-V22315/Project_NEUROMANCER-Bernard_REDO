echo "------------------------------------------------------------"
echo " ________________"
echo "/_  __/_  __/ __/"
echo " / /   / / _\ \  "
echo "/_/   /_/ /___/  "
echo "------------------------------------------------------------"

echo "Updating apt's package list..."
sudo apt update
echo "Done!"
echo "Installing python dependencies..."
pip3 install nltk sounddevice hjson
echo "Done!"
echo "Installing NLTK's 'punkt' module...."
python3 -m nltk.downloader punkt
echo "Done!"
echo "Installing Coqui-TTS..."

getclonedir() {
    cd ~
    echo "Where would you like the TTS repository to be cloned?"
    echo "Current Directory: " && pwd
    echo ">>Type the directory below:"
    read cloning_dir
    cd $cloning_dir


    if [ -d $cloning_dir ]
     then {
        echo "Changing directory..."
        cd $cloning_dir
        }
    else {
        echo "Directory not found, try again "
        echo
        getclonedir
    }
    fi
}


getclonedir 


git clone https://github.com/coqui-ai/TTS.git
cd TTS
make install
echo "Coqui TTS was installed"
echo "installation of dependencies for Text-To-Speech was finished. To test if it is working, execute modeltest.py after the other parts are installed. (src/Voice/utils/modeltest.py)"