#Define the (High-order) function to compare two functions for single value to return a string

MaxFunction(fn1::Function, fn2::Function, val) = 
    fn1(val) > fn2(val) ? 
        "Exponential Function is larger " : 
        "Polynomial Function is larger"

#Define two functions describing mathematical equations

ExponentialFunc(x) = 2^x

PolynomialFunc(x) = x^100


#Call the compare function

MaxFunction( ExponentialFunc, PolynomialFunc, 12)

MaxFunction( ExponentialFunc, PolynomialFunc, 100)


#Define a function to convert string in upper case

ToUpper(val::String) = return val.uppercase()

#Call the Function
ToUpper("Programming is Fun!")