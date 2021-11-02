'''
Specify gpu ids to be utilised.
Helpful while training multi gpu models on specific gpus/ pytorch pin memory True on gpu id != 0
'''
os.environ["CUDA_VISIBLE_DEVICES"] = "1"
