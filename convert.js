// to run the file type -  -   node 01_convert.js
// let a = 0;
// let b = 1;

// for(let i = 0 ; i<=18 ; i++){
//     let newfibo = a+ b;
//     console.log(newfibo);
//     a=b;
//     b=newfibo;
// }

// for(let i in range(18)){ //range(18) not a function so it gives error in used oly to check the value from for loop in an array index
//     let newfibo = a+ b;
//     console.log(newfibo);
//     a=b;
//     b=newfibo;
//     i++;
// }

// console.log(0);
// console.log(1);
// var count = 2;

// function febonacci(a ,b){
//     if(count <10){
//         let newFebo = a+b;
//         console.log(newFebo);
//         a =b ;
//         b = newFebo;
//         count += 1;
//         febonacci(a,b);
//     }
// }
// febonacci(0,1);

//find min value in a array

// let array = [2,4,1,10];
// let minValue = array[0];

// for( let i of array){
//     if(i < minValue){
//         minValue=i;
//     }
   
// }
//  console.log(minValue);
// array.map((e)=>{
//     if(e < minValue){
//         minValue = e
//     }                 //this is map method
// })
// console.log(minValue);

// array.forEach((e)=>{
//     if(e<minValue){
//         minValue = e;  //This is the for each method
//     }
// })
// console.log(minValue);
// let arr = [34,5,67,6,21,3];
// let n = arr.length

// for(let i = 0 ; i < n ; i++){
//     for(let j=0 ; j< n-i-1 ; j++){
//         if(arr[j]<arr[j+1]){
//             //correct way of swapping
//             [arr[j] , arr[j+1]] = [arr[j+1],arr[j]];  //array Destructuring
//         }
//     }
// }
// console.log(arr);
//  // [67, 34, 21, 6, 5, 3] (Descending order)
// let asSort = arr.sort((a,b)=>a-b);
// console.log(asSort);
// let dsSort = arr.sort((a,b)=>b-a);
// console.log(dsSort);
// let sorting = arr.sort();
// console.log(sorting);
//using sort with spread operator then the original array not changed

// let sortedArr = [...arr].sort((a,b) => a-b);
// console.log(sortedArr);
// console.log(arr)
// //Allthe above methods to sort the array only for number for sting
// let stArr = [ "Apple" , 'Orange' ,'Lemon'];
// let SorArr = stArr.sort();
// console.log(SorArr);


//insertion sorting
 let arr =[64, 34, 25, 5, 22, 11, 90, 12];
//  let n = arr.length

//  for(let i = 0 ; i < n-1 ; i++){
//     let minIndex = i;
//     for(let j = i+1 ; j < n ; j++){
//         if(arr[j] < arr[minIndex]){
//             minIndex = j;
//         }
//     }
//     // let minValue  = arr.splice(minIndex , 1)[0]; //remove min element
//     // arr.splice( i ,0, minValue) // insert that value inplace of i
//     // we can do that things with swaping the elements
//     [arr[i] , arr[minIndex] ] = [arr[minIndex] ,arr[i]];
//  }
//  console.log(arr);
let n = arr.length;

// for(let i =1 ; i < n ; i++){  // it takes the 1st index not oth index value
//     let insertIndex = i
//     let currentValue = arr.splice( i , 1)[0]; //poped up tthis value
//     for( let j = i-1 ; j>= 0 ; j --){  //it takes the values before the index value chosed by i and goes to back to check the i index values which are sorted are less or gratern using if statement
//        if(arr[j] > currentValue){
//         insertIndex = j;
//        }
//     }
//     arr.splice(insertIndex , 0 , currentValue); // it insert the value of which index select by j and o indicates the no elemenmt will be remove from the array and the current value which index value will be takes by j

// }
// console.log(arr);


     

     