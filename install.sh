echo "Installing virtual environment and requirements."
if [[ "$OSTYPE" == "linux-gnu" ]]; then
    sudo apt-get install python3-venv
elif [[ "$OSTYPE" == "darwin"* ]]; then
    echo "Python3-venv should be on your machine, if there is an issue, please install it."
else
    echo "Please use MACOS or Linux, you may refer to README.md"
fi
python3 -m venv venv
. venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

echo "Now installing the example database."
python3 install.py
echo "You may now use the script: launch.sh to launch the app."
