<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
  <title>Document</title>
  <script type="text/javascript" src="res.js"></script>
</head>
<style>
  .footer {
  position: fixed;
  left: 0;
  bottom: 0;
  height: 50px;
  width: 100%;
  background-color: #007ef5;
  color: white ;
  margin-top: 25px;
  text-align: center;

</style>
<body>
<nav class="navbar navbar-dark bg-primary justify-content-between"
>
  <a class="navbar-brand" style="font-size:30px;color:white;font-family: 'Squada One', cursive;">PLAGIARISM DETECTOR</a>
  
</nav>
<?php

session_start(); // this NEEDS TO BE AT THE TOP of the page before any output etc
  //echo $_SESSION['result'];
  echo "<br>
  RESULTS ARE SHOWN BELOW
  <br>";
  // echo "<pre>";
  print_r($_SESSION['result']);


  

// session_unset();

?>


<div class="footer">
  <p style="margin-top:15px;font-weight: bold;">CREATED BY TEM</p>
</div>
<script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<center>
<a href="index.php" style=" margin-top:0px; font-size:20px;padding:1%;width:20%;background-color:green;font-weight: bold;border:none " class="btn btn-success" class="button" href="results.php" title="" >GO TO BACK</a>
</center>

</body>
</html>


