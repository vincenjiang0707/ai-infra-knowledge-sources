# [Issue #1382] AdEMA NaN when loading from state_dict

source: https://github.com/bitsandbytes-foundation/bitsandbytes/issues/1382
state: closed | updated: 2026-02-16T20:14:28Z
labels: Bug, Medium Priority, Contributions Welcome, Optimizers

## 正文

### System Info

Running a standard training loop where I save the optimizer state_dict using opt.state_dict().
Upon loading using opt.load_state_dict() to resume, the model immediately NaNs after the first backprop step.

This only occurs using the AdEMA optimizer:

`
bnb.optim.AdEMAMix8bit(model.parameters(),
                            lr=lr,
                            t_alpha=T,
                            t_beta3=T)
`

AdamW and others load state dict perfectly fine. Any ideas?


### Reproduction

`
opt = bnb.optim.AdEMAMix8bit(model.parameters())
#run training loop
torch.save(opt.state_dict(), "dt.pt")

#try resuming opt from state_dict later
opt.load_state_dict("dt.pt")
#run training loop again 
`

### Expected behavior

Optimizer should resume training without NaNning

## 评论 (1)

### darius-lam · 2024-10-08

Update: thought that the issue might have been that the value T was not loaded properly at the start of resuming training; therefore leading to exploding gradient. However even setting T = 0 does not enable resuming from AdEMA state_dict.

When not loading from AdEMA state_dict (ie resetting the optimizer), the optimization works fine (but not ideal because the whole point of AdEMA is that we can keep a moving average of gradients over many thousands of steps) 
 
