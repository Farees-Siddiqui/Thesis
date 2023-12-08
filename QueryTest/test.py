import numpy as np
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

t = np.load('../GeneratingEmbeddings/bert_embeddings/embeddings_1000.npz')['arr_0']

embedding_vector = np.vstack(tuple(t[i] for i in range(0, 2)))

print(embedding_vector.shape)

tsne = TSNE(n_components=3, perplexity=30, random_state=42)
embedding_3d = tsne.fit_transform(embedding_vector)

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(embedding_3d[:, 0], embedding_3d[:, 1], embedding_3d[:, 2])
ax.set_title('t-SNE Visualization of Batch 1, Chunk 1')
plt.show()