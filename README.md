# 🔥 Pytorch-GPU project setup 🔥 

Initial project to start with Pytorch and GPU.

## 1. Clone this repo
```shell
git clone https://github.com/romulorm/pytorch-gpu
```
### 1.1 Open folder project in VSCode

## 2. UV install
### 2.1 Open terminal in VSCode and install UV
Windows (Powershell):
```shell
irm https://astral.sh/uv/install.ps1 | iex
```
Linux/Mac:
```shell
curl -LsSf https://astral.sh/uv/install.sh | sh
```

## 3. Create virtual environment
```shell
cd pytorch-gpu
uv venv .venv --python 3.13 --seed
```

## 4. Activate virtual environment
Windows:
```shell
.\.venv\Scripts\activate 
```
Linux/Mac:
```shell
source .venv/bin/activate
```

## 5. Install Pytorch packages
### For old graphics cards before RTX 20XX series, like Quadro P4000 and GTX 10XX:
```shell
uv add numpy torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu126
```
 ## For newer Nvidia graphics cards since RTX 20XX series:
```shell
uv add numpy torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu130
```
## For AMD graphics cards :
```shell
uv add numpy torch torchvision torchaudio --index-url https://download.pytorch.org/whl/rocm7.2
```
 
## 6. Execute main to test
```shell
python main.py
```

### If output shows Tensor matrix and device=CUDA, it's ready! 🚀