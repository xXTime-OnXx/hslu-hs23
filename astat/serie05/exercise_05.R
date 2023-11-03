# Aufgabe 5.4
x <- c(-5, -4, 1, 3, 6)
p <- c(0.3, 0.1, 0.1, 0.2, 0.3)

sum(x*p)

# Aufgabe 5.5
# b
x <- 2:12
p <- c(1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1) / 36

E <- sum(x*p)
E

var.X <- sum((x-E)**2*p)
var.X

sigma <- sqrt(var.X)
sigma
