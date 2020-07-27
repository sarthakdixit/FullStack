let v = 0;
let actual_answer = [" ", " ", " ", " ", " "];
let your_answer = [" ", " ", " ", " ", " "];
var apt = 0;
var res = 0;
var cprogram = 0;

function goToTest(){
  if(error){
    document.getElementById("askVideoAudio").style.display = "none";
    document.getElementById("notAllowed").style.display = "block";
  }else{
    isTestStarted = true;
    document.getElementById("alertBox").style.display = "none";
    document.getElementById("Test").style.display = "block";
    showQuestions();
  }
}

function drawTable(){
  let head = ["Section", "Correct Answer", "Wrong Answer", "Percentage"];
  let aptArray = ["Quants", apt, 5-apt, (apt/5)*100];
  let resArray = ["Resoning", res, 5-res, (res/5)*100];
  let cArray = ["C Programming", cprogram, 5-cprogram, (cprogram/5)*100];
  let table_container = document.getElementById("resultBox");
  let table = document.createElement("table");
  table.className = "table";
  let row = document.createElement("tr");
  for(let i=0;i<4;i++){
    let col = document.createElement("th");
    col.scope = "col";
    cell = document.createTextNode(head[i]);
    col.appendChild(cell);
    row.appendChild(col);
  }
  table.appendChild(row);
  row = document.createElement("tr");
  for(let i=0;i<4;i++){
    let col = document.createElement("td");
    col.scope = "col";
    cell = document.createTextNode(aptArray[i]);
    col.appendChild(cell);
    row.appendChild(col);
  }
  table.appendChild(row);
  row = document.createElement("tr");
  for(let i=0;i<4;i++){
    let col = document.createElement("td");
    col.scope = "col";
    cell = document.createTextNode(resArray[i]);
    col.appendChild(cell);
    row.appendChild(col);
  }
  table.appendChild(row);
  row = document.createElement("tr");
  for(let i=0;i<4;i++){
    let col = document.createElement("td");
    col.scope = "col";
    cell = document.createTextNode(cArray[i]);
    col.appendChild(cell);
    row.appendChild(col);
  }
  table.appendChild(row);
  table_container.appendChild(table);
}

function finishTest(){
  getYourAnswer();
  let c = 0;
  for(let i=0;i<5;i++){
    if(your_answer[i] === actual_answer[i]){
      c++;
    }
    your_answer[i] = "";
    actual_answer[i] = "";
  }
  cprogram = c;
  document.getElementById("Test").style.display = "none";
  document.getElementById("resultBox").style.display = "block";
  drawTable();
}

function nextSection(){
  getYourAnswer();
  let c = 0;
  for(let i=0;i<5;i++){
    if(your_answer[i] === actual_answer[i]){
      c++;
    }
    your_answer[i] = " ";
    actual_answer[i] = " ";
  }
  if(database == "aptitude"){
    apt = c ;
    database = "resoning";
    document.getElementById("aptitude").disabled = true;
    document.getElementById("resoning").disabled = false;
  }else if(database == "resoning"){
    res = c;
    database = "cprogramming";
    document.getElementById("resoning").disabled = true;
    document.getElementById("cprogramming").disabled = false;
  }
  v = 0;
  document.getElementById("next").style.display = "block";
  document.getElementById("nextSection").style.display = "none";
  showQuestions();
}

function getYourAnswer(){
  if(document.getElementById("radioA").checked){
    your_answer[v] = document.getElementById("radioA").value;
    document.getElementById("radioA").checked = false;
  }else if(document.getElementById("radioB").checked){
    your_answer[v] = document.getElementById("radioB").value;
    document.getElementById("radioB").checked = false;
  }else if(document.getElementById("radioC").checked){
    your_answer[v] = document.getElementById("radioC").value;
    document.getElementById("radioC").checked = false;
  }else if(document.getElementById("radioD").checked){
    your_answer[v] = document.getElementById("radioD").value;
    document.getElementById("radioD").checked = false;
  }
}

function nextQuestions(){
  getYourAnswer();
  if(v == 3){
    if(database === "cprogramming"){
      document.getElementById("next").style.display = "none";
      document.getElementById("finish").style.display = "block";
    }else{
      document.getElementById("next").style.display = "none";
      document.getElementById("nextSection").style.display = "block";
    }
  }
  v++;
  showQuestions();
}

function showQuestions(){
  $.ajax({
    url: "data.php",
    type: "get",
    data: { 
      database: database, 
      queID: que_id[v]
    },
    success: function(response) {
      var obj = JSON.parse(response);
      document.getElementById("que").innerHTML = "Q) "+obj["question"];
      document.getElementById("A").innerHTML = "A) "+obj["A"];
      document.getElementById("B").innerHTML = "B) "+obj["B"];
      document.getElementById("C").innerHTML = "C) "+obj["C"];
      document.getElementById("D").innerHTML = "D) "+obj["D"];
      actual_answer[v] = obj["answer"];
      console.log(actual_answer);
    },
    error: function(xhr) {
      alert(xhr);
    }
  });
}

function backToAlert(){
  document.getElementById("askVideoAudio").style.display = "block";
  document.getElementById("notAllowed").style.display = "none";
}

$('input[type=radio][name=radio]').change(function() {
  if(this.value == "A"){
      document.getElementById("radioB").checked = false;
      document.getElementById("radioC").checked = false;
      document.getElementById("radioD").checked = false;
  }else if(this.value == "B"){
    document.getElementById("radioA").checked = false;
    document.getElementById("radioC").checked = false;
    document.getElementById("radioD").checked = false;
  }else if(this.value == "C"){
    document.getElementById("radioA").checked = false;
    document.getElementById("radioB").checked = false;
    document.getElementById("radioD").checked = false;
  }else{
    document.getElementById("radioA").checked = false;
    document.getElementById("radioB").checked = false;
    document.getElementById("radioC").checked = false;
  }
});