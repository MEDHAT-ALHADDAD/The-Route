var c = 1;
function showDropdown()
{
    var t = document.getElementById("drop");
    var a = document.getElementsByName("time_slot");
    a.required = true;
    t.classList.remove("shown");
}
function hideDropdown()
{
    var t = document.getElementById("drop");
    t.classList.add("shown");
    var a = document.getElementsByName("time_slot");
    a.required = false;
}

function checkFields(){
    if(document.forms["Submission"]["team_name"].value === "")
        return false;
    if(document.forms["Submission"]["leader_name"].value === "")
        return false;
    return true;
}
function show(){
    if(checkFields())
    {
        var ok = true;
        for (var i = 1; i <= 5; i++)
        {
            var a = document.getElementsByName("Label" + i)[0];
            if(a.classList.contains("d-none")){
                ok = false;
                break;
            }
        }
        if(!ok)
        {
            var t = document.getElementsByClassName("d-none")[1];
            t.classList.toggle("d-none");
            c++;
            if(c == 6)
            {
                var b = document.getElementById("add");
                b.disabled = true;
            }
        }
    }
    else
    {
        alert("Fill in required fields and last member first");
    }
}
function hide(objButton){
        
        var n = (objButton.name).charAt(4);
        var l = document.getElementsByName("Label"+n)[0]
        l.classList.toggle("d-none");
        if(c == 6)
            {
                var b = document.getElementById("add");
                b.disabled = false;
            }
        c--;

            
}
function check()
{
    for (var i = 1; i <= c; i++)
    {
        var temp = document.getElementsByName(i + "_member_phone")[0];
        if(document.getElementsByName(i + "_member_name")[0].value != "")
        {
            temp.required = true;
        }
        else
        {
            temp.required = false;
        }
    }
    var ch = document.getElementsByName(c + "_member_name")[0].value;
    var t;
    for (var i = (c-1); i >= 1; i--)
    {
        var t = document.getElementsByName(i + "_member_name")[0];
        if(ch != "" && document.getElementsByName(i + "_member_name")[0].value === "")
        {
            t.required = true;
        }
        else
        {
            t.required = false;
        }
        ch = t.value;
    }
}

var slideIndex = 1;
showSlides(slideIndex);

// Next/previous controls
function plusSlides(n) {
  showSlides(slideIndex += n);
}

// Thumbnail image controls
function currentSlide(n) {
  showSlides(slideIndex = n);
}

function showSlides(n) {
  var i;
  var slides = document.getElementsByClassName("mySlides");
  var dots = document.getElementsByClassName("dot");
  if (n > slides.length) {slideIndex = 1}
  if (n < 1) {slideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
      slides[i].style.display = "none";
  }
  for (i = 0; i < dots.length; i++) {
      dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex-1].style.display = "block";
  dots[slideIndex-1].className += " active";
} 

