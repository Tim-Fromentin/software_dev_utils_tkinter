<?php 
$servername = "DbExample"; 
$username = "root"; 
$password = "admin"; 
$conn = new mysqli($servername, $username, $password);
if ($conn->connect_error) { 
die("Connection failed: " . $conn->connect_error); 
} 
echo "Connected successfully"; 
?>