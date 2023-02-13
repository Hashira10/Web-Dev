// Task 1.
// What is the last value alerted by this code? Why?
// let i = 3;

while (i) {
  alert( i-- );
}

// 1 because when i = 1 its show 1 and decrease it to 0


//Task 2.
// For every loop iteration, write down which value it outputs and then compare it with the solution.

// Both loops alert the same values, or not?

// The prefix form ++i:

let i2 = 0;
while (++i2 < 5) alert( i2 ); // 1-4

// The postfix form i2++

let i3 = 0;
while (i3++ < 5) alert( i3 ); // 1-5


//Task 3.
// For each loop write down which values it is going to show. Then compare with the answer.
// Both loops alert same values or not?

// The postfix form:

for (let i4 = 0; i4 < 5; i4++) alert( i4 ); // 0 - 4

// The prefix form:

for (let i4 = 0; i4 < 5; ++i4) alert( i4 ); // 0 - 4


// Task 4.
// Use the for loop to output even numbers from 2 to 10.

for(let i5 = 2; i5 <= 10; i5+=2){
    alert(i5);
}

//Task 5.

// Rewrite the code changing the for loop to while without altering its behavior (the output should stay same).
let i6 = 0;
while (i6 < 3) {
  alert( `number ${i6}!` );
  i6++;
}


//Task 6.
// Write a loop which prompts for a number greater than 100. If the visitor enters another number – ask them to input again.

// The loop must ask for a number until either the visitor enters a number greater than 100 or cancels the input/enters an empty line.

// Here we can assume that the visitor only inputs numbers. There’s no need to implement a special handling for a non-numeric input in this task.

let num;

do {
  num = prompt("Enter a number greater than 100?", 0);
} while (num <= 100 && num);


//Task 7.
// An integer number greater than 1 is called a prime if it cannot be divided without a remainder by anything except 1 and itself.

// In other words, n > 1 is a prime if it can’t be evenly divided by anything except 1 and n.

// For example, 5 is a prime, because it cannot be divided without a remainder by 2, 3 and 4.

// Write the code which outputs prime numbers in the interval from 2 to n.

// For n = 10 the result will be 2,3,5,7.

// P.S. The code should work for any n, not be hard-tuned for any fixed value.

let n = 10;

nextPrime:
for (let i7 = 2; i7 <= n; i7++) { 

  for (let j = 2; j < i7; j++) { 
    if (i7 % j == 0) continue nextPrime;
  }

  alert( i7 ); // a prime
}