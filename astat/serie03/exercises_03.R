# Aufgabe 3.1
# a
geysir <- read.table("serie03/geysir.dat", header = TRUE)

par(mfrow = c(2,2))
hist(geysir[, "Zeitspanne"])
hist(geysir[, "Zeitspanne"], breaks = 20)
hist(geysir[, "Zeitspanne"], breaks = seq(41, 96, by = 11))

# b
hist(geysir[, "Eruptionsdauer"])

# Aufgabe 3.2
# a
mannfrau <- read.csv("serie03/mannfrau.csv")

# b
plot(mannfrau$groesse.mann, mannfrau$groesse.frau,
     pch=16,
     col="orange",
     xlab="Groesse Mann",
     ylab="Groesse Frau")

abline(lm(mannfrau$groesse.frau ~ mannfrau$groesse.mann), lwd = 3, col="deepskyblue")

# c
lm(mannfrau$groesse.frau ~ mannfrau$groesse.mann)

# Aufgabe 3.3
# a
income <- read.table("serie03/income.dat", header = TRUE)

# b
plot(income$Educ, income$Income2005,
     pch=16,
     col="orange",
     xlab="Years of education",
     ylab="Income")

abline(lm(income$Income2005 ~ income$Educ), lwd=3, col="deepskyblue")

lm(income$Income2005 ~ income$Educ)

# Aufgabe 3.4
# a
head(anscombe)

# b
data(anscombe)
reg <- lm(anscombe$y1 ~ anscombe$x1)
reg2 <- lm(anscombe$y2 ~ anscombe$x2)
reg3 <- lm(anscombe$y3 ~ anscombe$x3)
reg4 <- lm(anscombe$y4 ~ anscombe$x4)
par(mfrow=c(2,2))
plot(anscombe$x1, anscombe$y1, ylab = "Y1", xlab = "X1")
abline(reg)
plot(anscombe$x2, anscombe$y2, ylab = "Y2", xlab = "X2")
abline(reg2)
plot(anscombe$x3, anscombe$y3, ylab = "Y3", xlab = "X3")
abline(reg3)
plot(anscombe$x4, anscombe$y4, ylab= "Y4", xlab= "X4" )
abline(reg4)
