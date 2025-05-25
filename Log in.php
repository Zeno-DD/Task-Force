<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
<?php
session_start();
include "MySQLinitial.php";

$name = $_POST["name"];
$password = $_POST["password"];

$sql = "SELECT * FROM users WHERE name='$name'"; 
$result = $conn->query($sql);

if ($result->num_rows == 1) {
    $row = $result->fetch_assoc(); //associative 
    if ($password === $row["password"]) {
        $_SESSION["user"] = $row;
        header("Location: accounts.php");
    } else {
        echo "Sai mật khẩu";
    }
} else {
    echo "Không tìm thấy tài khoản";
}
//t đã thật sự ngồi đến 2h sáng đọc tài liệu nc ngoài thay vì hỏi chat gpt dù
//p/s: đọc chat gpt rồi vẫn đéo hiểu
//nô lệ của học banr chaats
?>

   

</body>
</html>