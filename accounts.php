<?php
session_start();

if (!isset($_SESSION['user'])) {
    header("Location: Log, register.php");
    exit();
}

$user = $_SESSION['user'];
?>

<h2>Thông tin tài khoản</h2>    
Name: <?= htmlspecialchars($user['name']) ?> <br><br>
Gender: <?= htmlspecialchars($user['gender']) ?> <br><br>
Email: <?= htmlspecialchars($user['email']) ?><br><br>
Address: <?= htmlspecialchars($user['address']) ?><br><br>
Phone number: <?= htmlspecialchars($user['phone']) ?><br><br>
ditme chat gpt giải thích như cc, t cx éo hiểu t đang làm j nữa