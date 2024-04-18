# Mic2Seed
An easy to use python script that collects entropy through the microphone and generates a BIP39 mnemonic seed.

### Installation
Install git, python3 and pip (if needed):
```
sudo apt install git python3 python3-pip
```
Clone the repository:
```
git clone https://github.com/ASeriousMister/Mic2Seed
```
Move to the tool's directory
```
cd /path/Mic2Seed
```
Install requirements (read above for Python virtual envitonments):
```
pip3 install -r requirements.txt
```
There may be some dependency problems, if so try installing portaudio19-dev with
```
sudo apt install portaudio19-dev
```
then install requirements again with
```
pip3 install -r requirements.txt
```
Run the tool:
```
python3 mic2seed.py
```

### Utilization
User simply has to start the tool and wait until it collects entropy.
At the end, the tool will show a 24 words BIP39 mnemonic seed, that may be used with many different software wallets.

### Optional: using Virtual Environment
Install python virtual environments
```
pip3 install virtualenv
```
Now move to DiceTracker.py's directory,
```
cd Mic2Seed
```
create a virtual environment (in the example named dtve, but you can choose your preferred name)
```
virtualenv msve
```
and activate it
```
source msve/bin/activate
```
The name of the virtual enviroment should appear, in brackets, on the left of your command line. 
Now install the dependencies
```
pip3 install -r requirements.txt
```
Finally, run the tool
```
python3 mic2seed.py
```

### Disclaimer
This ool comes with no guarantees. Do your own research about how this tool works and in general about how cryptocurrency keys work before using it.

### Credits & Donations
This tool is part of the [AnuBitux](https://anubitux.org) project. 
If you appreciate this work visit https://anubitux.org and consider making a donation
- BTC: 1AnUbiYpuFsGrc1JFxFCh5K9tXFd1BXPg
- XMR: 87PTU58siKNb3WWXcP4Hq4CmCb7kMQUsEiUWFT7SvvMMUqVw9XXFGrJZqmnGvuJLGtLoRuEqovTG4SWqkPr8YLopTSxZkkL
