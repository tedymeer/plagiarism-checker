<?php 
if(isset($_POST['submit'])){
 // Count total files
 $countfiles = count($_FILES['file']['name']);
 
 // Looping all files
 for($i=0;$i<$countfiles;$i++){
   $filename = $_FILES['file']['name'][$i];
   
   // Upload file
   move_uploaded_file($_FILES['file']['tmp_name'][$i],'files/'.$filename);
    
 }
} 
?>
<!DOCTYPE html>
<html>
<head>
  <title>PHP File Upload</title>
  <link rel="stylesheet" href="dropzone.css">
  <link rel="preconnect" href="https://fonts.gstatic.com">
<link href="https://fonts.googleapis.com/css2?family=Squada+One&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
</head>
<style>
.desc{
  color:grey;
  margin-top:20px;
}
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
<center>
  <div class="desc">
  <h3>PLAGIARISM DETECTOR</h3>
  <p>Helping students reach their full potential</p>
</div>
  <form style="font-size:180%;margin:0%;border:5px dotted grey;width:50%;padding:0%;margin-top:3%;margin-bottom:0%" action="uploadHandler.php" class="dropzone image-uploader">
<img  height="150" width="150" src="https://cdn1.iconfinder.com/data/icons/hawcons/32/698394-icon-130-cloud-upload-512.png">
</form>
 </center>
  <form method='post' action='' enctype='multipart/form-data' style="display:flex;flex-wrap:wrap;justify-content:center;margin:2%">
 
 <!-- <input class="choosebtn" type="file" name="file[]" id="file"  multiple >
 <br/>
 <input class="uploadbtn" type='submit' name='submit' value='Upload'> -->

</form>

  <?php
        if(array_key_exists('button1', $_POST)) {
            button1();
        }
        function button1() {
            $output = shell_exec("python gst.py");
            
            // file_put_contents('output.txt', $output);
            session_start();
            $_SESSION['result'] = $output;   
            // echo $output;
        }

    
       ?>
      
  <center>
    <form method="post">
        <input type="submit" name="button1" class="btn btn-success" 
                class="button" style=" margin-top:0px; font-size:20px;padding:1%;width:20%;background-color:green;font-weight: bold;border:none" value="Check plag" />
    <a  style=" margin-top:0px; font-size:20px;padding:1%;width:20%;background-color:#007ef5;font-weight: bold;border:none " class="btn btn-success" class="button" href="results.php" title="" pointer-events: none>Show results</a>
    </form>   

</center>
       

    <script src="dropzone.js"></script>
	 <script type="text/javascript">
	    $(document).ready(function () {
	 
	    Dropzone.options.myAwesomeDropzone = {
	        paramName: "file", // The name that will be used to transfer the file
	        maxFilesize: 20, // MB
	        dictDefaultMessage: "Drop files here or click to upload",
			parallelUploads: 1,
	        accept: function (file, done) {
	            if (file.name == "justinbieber.jpg") {
	                done("Naha, you don't.");
	            }
	            else {
	                done();
	            }
	        }
	    };
	</script>
  <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
<div class="footer">
  <p style="margin-top:15px;font-weight: bold;">CREATED BY TEM</p>
</div>
</body>
</html>