import Sortable from './node_modules/sortablejs/modular/sortable.core.esm.js';


var array1 = []



let bar = document.getElementById('bar');

if (bar != null) {
  Sortable.create(bar, {
    group: {
      name: 'bar',
      filter: '.f', // 'f' class is not draggable
      pull: true
    },
    animation: 100
  });
}


let btn_del = document.getElementsByClassName('btn_del');
for (let index = 0; index < btn_del.length; index++) {
  (function (index) {
    array1[index] = (btn_del[index]);
    btn_del[index].addEventListener("click", function () {
      let x = (array1[index].parentElement).parentElement;
      // console.log(x);
      x.outerHTML = '';
    })
  })(index);
}

let btn_add = document.getElementById('add_city');
btn_add.addEventListener('click', function () {
  var name = document.getElementById("inci").value;
  var ul = document.getElementById("bar");

  var li = document.createElement("li");
  li.setAttribute("class", "list-group-item");

  var di = document.createElement("div");
  di.setAttribute("class", "row");

  var btn1 = document.createElement("button");
  btn1.setAttribute("class", "btn col-1 btn-sm btn-primary btn-circle");
  var i1 = document.createElement("i");
  i1.setAttribute("class", "fa fa-chain");
  btn1.appendChild(i1);
  di.appendChild(btn1);

  var te = document.createElement("div");
  te.appendChild(document.createTextNode(name));
  te.setAttribute("class", "col-10");
  di.appendChild(te);

  var btn2 = document.createElement("button");
  btn2.setAttribute("class", "btn btn-sm btn-circle-3d btn-danger col-1 btn-circle btn_del");
  var i2 = document.createElement("i");
  i2.setAttribute("class", "fa fa-trash");
  btn2.appendChild(i2);
  di.appendChild(btn2);

  li.appendChild(di);
  ul.appendChild(li);

  document.getElementById("inci").value = '';


  btn2.addEventListener("click", function () {
    var ia = array1.length;
    array1.push(btn2);
    let x = (array1[ia].parentElement).parentElement;
    // console.log(x);
    x.outerHTML = '';
  });

})

var scrly = document.getElementById('table-scroll');
var scrolly = 0.63 * window.screen.height;
scrly.setAttribute("style", "height:" + scrolly + "px");
// console.log(scrly);

var scrly = document.getElementById('table-scroll_1');
var scrolly = 0.63 * window.screen.height;
scrly.setAttribute("style", "height:" + scrolly + "px");
// console.log(scrly);

// **********************************

document.addEventListener('DOMContentLoaded', () => {

  document.querySelector('#test').onsubmit = () => {

    // Initialize new request
    const request = new XMLHttpRequest();
    // const currency = document.querySelector('#currency').value;

    let booo = [];
    let baa = document.getElementsByClassName('lasm');
    // console.log(baa);
    for (let index = 0; index < btn_del.length; index++) {
      (function (index) {
        booo[index] = ((baa[index].innerHTML).replace("\n", "")).trim();
        // console.log((booo[index].replace("\n", "")).trim());

      })(index);
    }
    let myJSON = JSON.stringify(booo);
    console.log(myJSON);
    request.open('POST', '/results/');

    // Callback function for when request completes
    request.onload = () => {
12
      // Extract JSON data from request
      const data = JSON.parse(request.responseText);
      console.log(data);

      // Update the result div
      if (true) {
        console.log("sadkvod,l");
        
        // console.log(data);
        // ~~code here 
        let resultf = document.getElementById('result_data');
        let results12 = data.results;
        resultf.innerHTML = '';
        let asdfghjkl = "";
        for(let i=0 ; i < results12.length ; i++){
          console.log(i);
          asdfghjkl += "<tr>";
          for (var key in results12[i]) {
            // check if the property/key is defined in the object itself, not in parent
              asdfghjkl += "<td>";
            if (results12[i].hasOwnProperty(key)) {           
                console.log(key, results12[i][key]);
                asdfghjkl += results12[i][key];
            }
            asdfghjkl += "</td>";
          }
          asdfghjkl += "</tr>";
          // resultf.innerHTML += "<tr>";
          //   resultf.innerHTML += "<td>";
          //   // console.log(result12[i][j]);
          //   resultf.innerHTML += (results12[i].no);
          //   resultf.innerHTML += "</td>";

          //   resultf.innerHTML += "<td>";
          //   resultf.innerHTML +=(results12[i].From);
          //   resultf.innerHTML += "</td>";

          //   resultf.innerHTML += "<td>";
          //   resultf.innerHTML +=(results12[i].To);
          //   resultf.innerHTML += "</td>";
            
          //   resultf.innerHTML += "<td>";
          //   resultf.innerHTML +=(results12[i].Flight_No);
          //   resultf.innerHTML += "</td>";
            
          //   resultf.innerHTML += "<td>";
          //   resultf.innerHTML +=(results12[i].Date);
          //   resultf.innerHTML += "</td>";
            
          //   resultf.innerHTML += "<td>";
          //   resultf.innerHTML +=(results12[i].Price);
          //   resultf.innerHTML += "</td>";

          // // }
          // resultf.innerHTML += "</tr>";
        }
        console.log(asdfghjkl);
        
        resultf.innerHTML += asdfghjkl;
        
        
        
        // const contents = `1 USD is equal to ${data.rate} ${currency}.`
        // document.querySelector('#result').innerHTML = contents;
      } else {
        console.log("error");
        
        // document.querySelector('#result').innerHTML = 'There was an error.';
      }
    }

    // Add data to send with request

    const data = new FormData();
    data.append('Cities_Results', myJSON);

    // Send request


    request.send(data);
    return false;
  };

});


// $(document).ready(function () {
//   $("#test").submit(function (event) {
//     let booo = [];
// let baa = document.getElementsByClassName('lasm');
// console.log(baa);

//     for (let index = 0; index < btn_del.length; index++) {
//       (function (index) {
//         booo[index] = ((baa[index].innerHTML).replace("\n","")).trim();
//         console.log((booo[index].replace("\n","")).trim());

//       })(index);
//     }
//     var myJSON = JSON.stringify(booo);
//     event.preventDefault();
//     $.ajax({
//       type: "POST",
//       url: "/results/",
//       data: {
//         'Cities_Results': myJSON // from form
//       },
//       success: function () {
//         // console.log(data);

//         $('#message').html("<h2>Contact Form Submitted!</h2>")
//       }
//     });
//     return false;
//   });
// });