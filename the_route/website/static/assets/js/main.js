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

let baa = [];


$(document).ready(function () {
  $("#test").submit(function (event) {
    let booo = ['london','cairo','paris','moscow'];
    var myJSON = JSON.stringify(booo);
    event.preventDefault();
    $.ajax({
      type: "POST",
      url: "/results/",
      data: {
        'Cities_Results':  myJSON// from form
      },
      success: function () {
        $('#message').html("<h2>Contact Form Submitted!</h2>")
      }
    });
    return false;
  });
});


