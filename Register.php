<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    
<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    include "MySQLinitial.php";
    $name = $_POST['name'];
    $password = $_POST['password'];
    $email = $_POST['email'];
    $phone = $_POST['phone'];
    $gender = $_POST['gender'] ?? '';
    $address = $_POST['address'];
    $sql = "SELECT * FROM users WHERE name = '$name' OR email = '$email'";
    $result = $conn->query($sql);

    if ($result->num_rows > 0) {
        echo "<p>Cút ra ngoài.</p>";
    } else {
        $sql = "INSERT INTO users (name, password, gender, email, address, phone)
                      VALUES ('$name', '$password', '$gender', '$email', '$address', '$number')";
        
        if ($conn->query($sql) === TRUE) {
            echo "<p style='color:green;'>Đăng ký thành công! <a href='login.php'>Đăng nhập</a></p>";
        } else {
            echo "<p style='color:red;'>Nhập nhanh cmm lên " . "</p>";
        }
    }
}
?>
</body>
</html>