require(timeDate)
data <- read.csv(file="/home/eric/workspace/auto_trader_play/spread.csv",head=TRUE,sep=",")
summary(data)

data$time <- as.timeDate(data$time)

plot(data$time, data$ask, col="red")
lines(data$time, data$ask, col="red")
lines(data$time, data$bid, col="blue")
