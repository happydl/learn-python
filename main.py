import torch
import numpy as np
import matplotlib.pyplot as plt

def test():

    a = torch.tensor([1,2,3,4,5],dtype=torch.int32)
    b = torch.tensor([5,4,3,2,1],dtype=torch.int32)
    c = 2*a

    def test1():
        print(a[0]) # this is a tensor
        print(a[0].item()) # 1
        a[0] = 100
        d = a[1:4]

        a_col = a.view(5,1)  # transformm to coloumn matrix
        a_col = a.view(-1,1) # transform and use all elements
        # print(a_col)

        numpy_array = np.array([1,2,3,4,5])
        torch_tensor = torch.from_numpy(numpy_array)
        back_to_numpy = torch_tensor.numpy()

    def test2():

        # broadcasting
        a1 = a + 1 #[2,3,4,5,6]

        # change type
        a_float = a.type(torch.float32) 
        
        # function
        print(a_float.mean().item())
        y = torch.sin(a_float)        
        x = torch.linspace(0, 2*np.pi, 100)
        y = torch.sin(x)

        plt.plot(x.numpy(),y.numpy())
        plt.show()





    test2()



test()




