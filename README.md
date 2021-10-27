# InversionInitNoise
Cached MultiVariate Gaussian, Good for Model Inversion on ImageNet, All the credit goes to [Madry's Implementations](https://github.com/MadryLab/robustness_applications/blob/master/generation.ipynb).
Simply use:
```python 
  from imagenet import ImageNetMultiVariate
  distributions = ImageNetMultiVariate()
  x = distributions[target].sample()
``` 
