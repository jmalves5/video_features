import torch
import random
import torchvision.transforms.functional as F

class VideoTransform:
    """
    Samples one set of parameters (flip, brightness, contrast, etc.)
    and applies the same transform to each call.
    """
    def __init__(self, 
                 flip_prob=0.5,
                 brightness=0.2,
                 contrast=0.2,
                 saturation=0.2,
                 hue=0.1):
        # Sample random flip once. random returns a random number in [0,1]
        self.do_flip = (random.random() < flip_prob)
        
        # Sample random color jitter parameters once
        # We'll do it manually below
        self.brightness_factor = 1.0 + random.uniform(-brightness, brightness)
        self.contrast_factor   = 1.0 + random.uniform(-contrast, contrast)
        self.saturation_factor = 1.0 + random.uniform(-saturation, saturation)
        self.hue_factor        = random.uniform(-hue, hue)
        
    def __call__(self, img):
        # img is a PIL Image or torch.Tensor in [0,1] range
        # Apply horizontal flip if needed
        if self.do_flip:
            img = F.hflip(img)
        
        # Apply color adjustments
        # brightness
        img = F.adjust_brightness(img, self.brightness_factor)
        # contrast
        img = F.adjust_contrast(img, self.contrast_factor)
        # saturation
        img = F.adjust_saturation(img, self.saturation_factor)
        # hue
        img = F.adjust_hue(img, self.hue_factor)
        
        return img