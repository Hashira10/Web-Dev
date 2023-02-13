// What’s wrong with the code style below?

function pow(x,n)  //  no space between arguments
{  // figure bracket on a separate line
  let result=1;   // no spaces before or after =
  for(let i=0;i<n;i++) {result*=x;}   // no spaces
  // the contents of { ... } should be on a new line
  return result;
}

let x=prompt("x?",''), n=prompt("n?",'') 
// make it 2 lines, no spaces and missing ;
if (n<=0)  //  no spaces inside, and should be extra line above it
{   // figure bracket on a separate line
  // below - long lines can be split into multiple lines for improved readability
  alert(`Power ${n} is not supported, please enter an integer number greater than zero`);
}
else // could write it on a single line like "} else {"
{
  alert(pow(x,n))  // no spaces and missing ;
}


//fixed
function pow(x, n) {
    let result = 1;
  
    for (let i = 0; i < n; i++) {
      result *= x;
    }
  
    return result;
  }
  
  let x1 = prompt("x1?", "");
  let n1 = prompt("n1?", "");
  
  if (n1 <= 0) {
    alert(`Power ${n1} is not supported,
      please enter an integer number greater than zero`);
  } else {
    alert( pow(x1, n1) );
  }



//   Task 2.
//   What’s wrong in the test of pow below?

it("Raises x to the power n", function() {
  let x = 5;

  let result = x;
  assert.equal(pow(x, 1), result);

  result *= x;
  assert.equal(pow(x, 2), result);

  result *= x;
  assert.equal(pow(x, 3), result);
});
// P.S. Syntactically the test is correct and passes.


// There are three tests written as one function with three checks, 
// and if an error occurs, it is much more difficult to understand what went wrong.
// It is much better to split the test into several it blocks.

describe("Возводит x в степень n", function() {
    it("5 в степени 1 будет 5", function() {
      assert.equal(pow(5, 1), 5);
    });
  
    it("5 в степени 2 будет 25", function() {
      assert.equal(pow(5, 2), 25);
    });
  
    it("5 в степени 3 будет 125", function() {
      assert.equal(pow(5, 3), 125);
    });
  });