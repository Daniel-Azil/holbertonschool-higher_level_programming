#!/usr/bin/node

// A script that returns the factorial number
// of given input from the command line argument

const cmdArg = process.argv[2]

function recursive_factorial (arg) {
    if (isNaN(arg) || arg === 0) {
        return 1;
    } else {
        return (arg * recursive_factorial(arg - 1));
    }
}

console.log(recursive_factorial(cmdArg));