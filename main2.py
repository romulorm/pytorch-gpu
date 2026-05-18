import torch

def main():  

    # 1. Define o dispositivo dinamicamente (Padrão PyTorch)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Dispositivo selecionado: {device.type.upper()}")

    # 2. Exibe informações de hardware baseadas no dispositivo disponível
    if device.type == "cuda":
        print(f"CUDA Available: True")
        print(f"GPU Name: {torch.cuda.get_device_name(0)}")
        print(f"CUDA Version: {torch.version.cuda}")
    else:
        print(f"CUDA Available: False (Rodando em modo CPU)")
        print("Dica: Se deveria ter GPU, cheque os drivers com 'nvidia-smi'.")

    print(f"PyTorch Version: {torch.__version__}\n")

    # 3. Executa o cálculo de forma agnóstica ao hardware
    # Usando o .to(device), o tensor vai para a GPU se ela existir, ou fica na CPU se não existir
    x = torch.rand(5, 3).to(device)

    print(f"Example Tensor on {device.type.upper()}:")
    print(30 * "-")
    print(x)



if __name__ == "__main__":
    main()



