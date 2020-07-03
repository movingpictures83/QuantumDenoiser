# QuantumDenoiser
# Language: Python
# Input: CSV (file of quanta produced by CKMeans)
# Output: CSV (denoised quanta)
# Tested with: PluMA 1.1, Python 3.6
# Dependency: numpy==1.16.0

PluMA plugin that accepts as input a file of samples and quanta,
which can be produced through the plugin CKMeans:
https://github.com/movingpictures83/CKMeans

We do not list the CKMeans plugin as a dependency, since you could produce
the file through some other software.

The plugin applies a denoising algorithm to the data,
designed to eliminate spurious fluctuations in the quanta.
