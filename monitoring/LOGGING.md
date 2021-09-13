# Logging

## Report

### Grafana Gui
Logging in grafana interface:
![](https://i.imgur.com/dUAWfv7.jpg)

### Add loki data source
Adding loki as a data source in grafana:
![](https://i.imgur.com/DWB2C38.png)
As we can see, loki is successfully added:
![](https://i.imgur.com/NXzkLbF.png)

### Testing loki
I configured promtail to see container names and image names, so it will be much more convinient. As we can see, we collect logs from all other services from our docker-compose:
![](https://i.imgur.com/MWX8kMb.png)
Now we can get all logs from all services:
![](https://i.imgur.com/f6buB2O.png)


## Best practices
1. Configure promtail to have container and image names
2. Use static lables
3. Use `chunk_target_size`