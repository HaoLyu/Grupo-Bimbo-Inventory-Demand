import ml_metrics as metrics
pred = [1,1,0,0,0]
y_real = [1,0,1,0,0]
metrics.rmsle(pred, y_real)