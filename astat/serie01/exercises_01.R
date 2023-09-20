# Aufgabe 1.2
# a
x <- c(4, 2, 1, 3, 3, 5, 7)

# b
x[3]

# c
x[c(1, 4)]

# d
length(x)

# e
x + 2

# f
sum(x + 2)

# g
x <= 3

# h
x[x <= 3]

# i
sort(x)

# j
order(x)

# k
x[4] <- 8


# Aufgabe 1.3
# a
fahrenheit <- c(51.9, 51.8, 51.9, 53)

# b
celsius <- 5 / 9 * (fahrenheit - 32)

# c
fahrenheit - c(48, 48.2, 48, 48.7)


# Aufgabe 1.4
# a
weight <- c(60, 72, 57, 90, 95, 72)
height <- c(1.75, 1.80, 1.65, 1.90, 1.74, 1.91)

# b
bmi <- weight / (height * height)


# Aufgabe 1.5
# a)
# seq to
seq(10)

# seq from to
seq(3, 10)

# seq from to by
seq(3, 10, 0.5)

# seq form to with length
seq(3, 10, length.out = 5)

# b)
x <- c(4, 10, 3, NA, NA, 1, 8)

# ii
mean(x, na.rm = TRUE)

# c
z <- c(4, 2, 8, 9, 7, 5, 2, 1)
plot(z)

# i
plot(z,
     type = "l",
     col = "blue",
     lty = 2,
     main = "Haupttitel",
     xlab = "Ein paar Zahlen",
     ylab = "Andere Zahlen"
)

# ii
abline(v = 3,
       col = "green"
)
abline(h = 4,
       col = "red",
       lty = 3
)
abline(1, 2,
       col = "brown",
       lty = 5
)


# Aufgabe 1.6
# a
data <- read.csv("weather.csv")
data

# b
data[2, 3]

# c
data[4,]

# d
data[, c("Luzern", "Zurich")]

# e
data1 <- data[, c("Luzern", "Zurich")]
write.csv(data1, "weather2.csv")

# f
colnames(data)[3]

# g
colnames(data)[2] <- "Genf"


# Aufgabe 1.7
# a
d.fuel <- read.table(file = "./d.fuel.dat" ,header = T, sep = ",")

# b
d.fuel[5,]

# c
d.fuel[1:5,]

# d
d.fuel[c(1:3, 57:60), ]

# e
mean(d.fuel[,"mpg"])

# f
mean(d.fuel[7:22, "mpg"])

# g
t.kml <- d.fuel[, "mpg"] * 1.6093 / 3.789
t.kg <- d.fuel[, "weight"] * 0.45359

# h
mean(t.kml)
mean(t.kg)
