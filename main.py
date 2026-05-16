import torch

def main():
    

    # Check if CUDA is available
    cuda_available = torch.cuda.is_available()
    print(f"CUDA Available: {cuda_available}")

    if cuda_available:
        # Print GPU details
        print(f"GPU Name: {torch.cuda.get_device_name(0)}")
        print(f"CUDA Version: {torch.version.cuda}")
        print(f"PyTorch Version: {torch.__version__}")

        # Perform a simple tensor calculation on the GPU
        x = torch.rand(5, 3).cuda()
        print("\nExample Tensor on GPU:")
        print(30 * "-")
        print("")
        print(x)
    else:
        print("CUDA is not available. Check your Nvidia drivers.")
        print("CUDA Toolkit is not necessary for this PyTorch implementation.")



if __name__ == "__main__":
    main()
