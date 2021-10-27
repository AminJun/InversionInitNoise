# InversionInitNoise
Cached MultiVariate Gaussian, Good for Model Inversion on ImageNet, All the credit goes to [https://github.com/MadryLab/robustness_applications/blob/master/generation.ipynb]( Madry's Implementations ).
Simply use:
```python 
  from imagenet import ImageNetMultiVariate
  distributions = ImageNetMultiVariate()
  x = distributions[target].sample()
``` 
