require! 'prelude-ls': {map}
require! './graphs.js': {Node}

jsonize = JSON.stringify _, ->
    | &0 is 'origin' => '...'
    else &1

[A, B, C] = [new Node!, new Node!, new Node!]

A.connect-to B, 10
B.connect-to C, 5
A.connect-to C, 12

console.log jsonize [A, B, C]

A.shortest-path-to C

console.log jsonize [A, B, C]
