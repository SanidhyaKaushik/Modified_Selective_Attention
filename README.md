# DLCV_2025_Project
This repository contains an unofficial implementation of the Selective Attention module proposed by Zhang et. al. in NeurIPS 2024 and a proposed modification of it.

Selective Attention attempts to improve upon vanilla attention by introducing token aware and position aware temperature scaling before attention score computation. The aim of the scaling is to combat attention dilution for longer context, decouple token semantics from sparsity of attention map and suppress noisy tokens.

As part of the project work for the course called Deep Learning for Computer Vision, being conducted at the Indian Institute of Science, we aim to build upon the proposed selective attention module. We aim to vectorize the temperatures so as to gain a fine grained control over the temperature scaling and have more interpretability in terms what role does each component of a query vector play in deciding the sparsity of attention maps. Although the authors mention in the original paper that vectorization of temperatures didn't result in significant gains, we aim to pursue this direction more innovatively by manually controling the scaling factors corresponding to each dimension keeping in mind the role that temperature scaling plays.

If time permits, we will explore different ways to merge token and position aware temperatures (since they are vectors now, it opens up a myriad of ideas for us to explore different combinatinon startegies) and also experiment with different score calculation metrics.

The implementation is still in progress.
