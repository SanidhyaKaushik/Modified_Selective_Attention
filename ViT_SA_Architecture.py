from ViT_SA.py import ViTWithSelectiveAttention
from Training_SA.py import train_vit_cifar10
model = ViTWithSelectiveAttention(
        img_size=32,
        patch_size=8,
        in_channels=3,
        num_classes=10,
        embed_dim=192,
        depth=9,
        k_dim=64,
        v_dim=192,
        mlp_ratio=4,
        dropout=0.1,
        pool='cls'
    )


total_params = sum(p.numel() for p in model.parameters())
print(f"Total parameters: {total_params:,}")


history = train_vit_cifar10(
        model=model,
        device=device,
        epochs=100,
        batch_size=128,
        lr=0.001,
        weight_decay=0.05
    )
