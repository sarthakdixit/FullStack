function informationShowContent(){
  document.getElementById('information_show_content').style.display = "none";
  document.getElementById('information_add_content').style.display = "block";
}

function informationAddContent(){
  document.getElementById('information_show_content').style.display = "block";
  document.getElementById('information_add_content').style.display = "none";
}

function creatingYourProfile(){
  document.getElementById('beAnAgent_create_button').style.display = "none";
  document.getElementById('beAnAgent_form').style.display = "block";
}

function cancelingYourProfile(){
  document.getElementById('beAnAgent_create_button').style.display = "block";
  document.getElementById('beAnAgent_form').style.display = "none";
}

function creatingYourDesigner(){
  document.getElementById('beADesigner_create_button').style.display = "none";
  document.getElementById('beADesigner_form').style.display = "block";
}

function cancelingYourDesigner(){
  document.getElementById('beADesigner_create_button').style.display = "block";
  document.getElementById('beADesigner_form').style.display = "none";
}