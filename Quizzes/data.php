<?php
  include 'connection.php';

  $id = $_GET['queID'];
  $database = $_GET['database'];
  $myObj = null;

  $query = "SELECT * FROM $database WHERE QID=$id";
  $data = mysqli_query($conn, $query);
  $row = mysqli_num_rows($data);
  if($row){
    while($result = mysqli_fetch_assoc($data)){
      $myObj->question = $result['Question'];
      $myObj->image = $result['Image'];
      $myObj->A = $result['A'];
      $myObj->B = $result['B'];
      $myObj->C = $result['C'];
      $myObj->D = $result['D'];
      $myObj->answer = $result['Answer'];
    }
    echo json_encode($myObj);
  }

?>