import Sortable from './node_modules/sortablejs/modular/sortable.core.esm.js';


var array1 = []


  Sortable.create(bar, {
    group: {
      name: 'bar',
      filter: '.f', // 'f' class is not draggable
      pull: true
    },
    animation: 100
  });


  let btn_del = document.getElementsByClassName('btn_del');
  for (let index = 0; index < btn_del.length; index++) {
    (function(index) {
      array1[index] = (btn_del[index]);
      console.log(index + ": " + array1[index]);
      btn_del[index].addEventListener("click", function() {
         let x =(array1[index].parentElement).parentElement;
         console.log(x);
         x.outerHTML = '';
       })
    })(index);
  }