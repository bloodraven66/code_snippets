'''
set seeds for reproducibility
'''
torch.backends.cudnn.benchmark = True
np.random.seed(1)
np.random.seed(1)
torch.manual_seed(1)
torch.cuda.manual_seed(1)

'''
boilerblate train loop code for single gpu
'''

def train_loop(train_loader, val_loader, model, optimizer, loss_fn, device):
    model.train()
    for i, data in enumerate(tqdm(train_loader)):
        data = data.to(device)
        out = model(data)
        loss = loss_fn(out, data)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        
'''
save torch model
'''

def saveCheckpoint(model, path):
    torch.save(model.state_dict(), path)
        
'''
load torch model
'''

def load_pretrained(path, model, device='cuda:1'):
    model.load_state_dict(torch.load(path,  map_location=device))
    return model


'''
wandb logger
'''

class WandbLogger():
    def __init__(self, config):
        self.run = wandb.init(reinit=True,
                            name=config.logging.run_name,
                            project=config.logging.project_name,
                            config=config,
                            notes=config.logging.notes,
                            tags=config.logging.tags)

    def log(self, dct):
        wandb.log(dct)

    def log_plots(self, plt_object):
        wandb.log({"ema": wandb.Image(plt_object)})

    def summary(self, dct):
        for key in dct:
            wandb.run.summary[key] = dct[key]

    def end_run(self):
        self.run.finish()
    
    def add_audio(self, audio, sr, name):
        wandb.log({name: wandb.Audio(audio, sample_rate=sr)})
