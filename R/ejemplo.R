plot(iris)
library(tidytext)
?read.csv
?print
work_d <- getwd()
print(work_d)
print(typeof(work_d))
?paste
file <- paste(work_d, "/R/", "text.csv", sep = "")
print(file)
sent <- read.csv(file)

print(sent)
a <- 2
print(a)
b <- 3
c <- a + b

z <- 22
sa <- 99


for (i in 1:10) {
    print("this is awesome")
}