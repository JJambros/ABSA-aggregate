The dataset is included in this package at data/acos/rest16
All requirements can be downloaded with this, including the pretrained T5 model used:

pip install torch==1.12.1+cu116 torchvision==0.13.1+cu116 torchaudio==0.12.1 --extra-index-url https://download.pytorch.org/whl/cu116
pip install -r requirements.txt

Its possible you may need to make a seperate environment to get it to run:
conda create -n mvp python=3.8
conda activate mvp


To train:
bash scripts/run_main.sh