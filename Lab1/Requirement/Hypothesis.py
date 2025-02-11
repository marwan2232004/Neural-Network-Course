import numpy as np

class HypothesisFunction:
    def __init__(self, l, m, k):
        # TODO [1]: Initialize the function's unknown parameters
        self.l = None
        self.m = None
        self.k = None
        
        # TODO [2]: Initialize Wh and Wo matrices from a standard normal distribution
        self.Wh = None
        self.Wo = None
        
        # TODO [3]: Initialize bo and bo column vectors as zero
        self.bo = None
        self.bh = None

    def forward(self, x):
        # Ensure input shape matches input size
        assert x.shape[0] == self.l, f"Your input must be consistent the value l={self.l}"
        
        # TODO [4]: Compute a as mentioned above
        a = None
        
        # TODO [5]: Compute output ignoring ReLU
        y = None
        
        # TODO [6]: Apply ReLU on the output with numpy boolean masking
        
        return y, a

    def double_forward(self, x1, x2):
        # Perform forward function for the two inputs
        y1, _ = self.forward(x1)
        y2, _ = self.forward(x2)
        
        # TODO [7]: Concatenate the two outputs
        z = None
        
        # TODO [8]: Normalize the concatenated result
        z_bar = None
        
        return z_bar
    
        # TODO [9]: Annotate all initialized variables and functions above
        
    def count_params(self):
        # TODO [10]: Make a lambda function num_params that takes an array z and returns np.prod(z.shape)
        num_params = None
        # TODO [11]: return the total number of parameters by summing the function over Wh, Wo, bh, bo
        total_params = None
        return total_params