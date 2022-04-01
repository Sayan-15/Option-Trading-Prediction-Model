objects = [
  {
    "Name": "frighten",
    "Bid Price": "suit",
    "Ask Price": "sort",
    "LTP": "electricity",
    "Spread": "not",
    "Volume": "she"
  },
  {
    "Name": "frighten",
    "Bid Price": "hello",
    "Ask Price": "nani",
    "LTP": "papa",
    "Spread": "momo",
    "Volume": "golu"
  },
  {
    "Name": "frighten",
    "Bid Price": "suit",
    "Ask Price": "sort",
    "LTP": "electricity",
    "Spread": "not",
    "Volume": "she"
  },
  {
    "Name": "frighten",
    "Bid Price": "suit",
    "Ask Price": "sort",
    "LTP": "electricity",
    "Spread": "not",
    "Volume": "she"
  },
]


//   objects.forEach(object => {
//     for (let key in object) {
//       document.getElementsByClassName("row1")[i].innerText = object[key];
//     }
// });
// for(let j=0;j<6;j++){
//   for(let i=0;i<5;i++){
//     document.getElementsByClassName("row1")[i].innerText = objects[j][document.getElementsByClassName("row0")[i].innerText];
//   }
// }

// console.log(document.getAnimations("column1"))


function getdata(objects, tablename) {


  //gets table
  var oTable = document.getElementById(`${tablename}`);

  //gets rows of table
  var rowLength = oTable.rows.length;
  console.log(rowLength)

  //loops through rows    
  for (i = 1; i < rowLength; i++) {

    //gets cells of current row
    var oCells = oTable.rows.item(i).cells;

    //gets amount of cells of current row
    var cellLength = oCells.length;

    //loops through each cell in current row
    for (var j = 1; j < cellLength; j++) {
      /* get your cell info here */
      var cellVal = oCells.item(j).innerText = objects[i][oTable.rows.item(0).cells.item(j).innerText];

    }
  }
}

getdata(objects,"myTable2")

// row_length = document.getElementsByClassName("row1").length;

// for(let i=0;i<row_length;i++)

