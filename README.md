# Pytorch with Nvidia CUDA

Initial project to start with Pytorch and Nvidia CUDA.

## 1. UV install
Windows (Powershell):
```shell
irm https://astral.sh/uv/install.ps1 | iex
```
Linux/Mac:
```shell
curl -LsSf https://astral.sh/uv/install.sh | sh
```

## 2. Repository clone
git clone https://github.com/romulorm/pytorch-gpu.git

## 3. Syncronize project
```shell
cd pytorch-gpu
uv sync
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

## 5. Execute main to test
```shell
python main.py
```

### ⚠️ If output shows Tensor matrix and device=CUDA, it's ready! 🚀