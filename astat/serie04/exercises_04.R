# Aufgabe 4.1
# geysir
geysir <- read.table("serie03/geysir.dat", header = TRUE)

plot(geysir[, "Zeitspanne"], geysir[, "Eruptionsdauer"],
     pch=19,
     col="darkseagreen4")

abline(lm(geysir[, "Eruptionsdauer"] ~ geysir[, "Zeitspanne"]),
       col="orange")

cor(geysir[, "Zeitspanne"], geysir[, "Eruptionsdauer"])

# Aufgabe 4.2
# a
t.x <- (-10):10
t.x1 <- 0:10
t.y <- t.x^2
t.y1 <- t.x1^2

# b
par(mfrow=c(1,2))

plot(t.x, t.y, col = "darkseagreen4", pch = 19)
plot(t.x1, t.y1, col = "darkseagreen4", pch = 19)

# c
cor(t.x, t.y)
cor(t.x1, t.y1)

# Aufgabe 4.5
A <- 3/4
B <- 2/3

# a
library(MASS)
fractions(A * B)

# b
fractions(A + B - A*B)

# c
fractions(1 - A*B)

# d
fractions(1-(A + B - A*B))

# e
fractions(A + B - 2*A*B)
