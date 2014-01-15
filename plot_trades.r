require(timeDate)
data <- read.csv(file="/home/eric/workspace/auto_trader_play/trades.csv",head=TRUE,sep=",")
summary(data)

data$time <- as.timeDate(data$time)

plot(data$time, data$price, col="black")

points(data[data$buyorsell=="s",]$time,data[data$buyorsell=="s",]$price,col="red",bg="red", pch=24)
points(data[data$buyorsell=="b",]$time,data[data$buyorsell=="b",]$price,col="blue",bg="blue", pch=24)
lines(data$time, data$price, col="black")

