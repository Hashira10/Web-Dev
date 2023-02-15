// Task 1.
// Hello object
let user = {};
user.name = "John";
user.surname = "Smith";
user.name = "Pete";
delete user.name;

// Task 2.
// Check for emptiness
function isEmpty(obj){
    for(let i in obj){
        return false;
    }
    return true;
}

// Task 3.
// Sum object properties.

let salaries = {
    John: 100,
    Ann: 160,
    Pete: 130
}
let sum = 0;
for(let i in salaries){
    sum += salaries[i];
}
alert(sum);

// Task 4.
// Multiply numeric property values by 2.

let menu = {
    width: 200,
    height: 300,
    title: "My menu"
  };
  
  multiplyNumeric(menu);
  
  // after the call
  menu = {
    width: 400,
    height: 600,
    title: "My menu"
  };


  function multiplyNumeric(obj){
    for(let i in obj){
        if(typeof(obj[i]) == "number"){
            obj[i] *= 2;
        }
    }
  }