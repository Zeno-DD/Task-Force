<!DOCTYPE html>
<html>
<head><title>Login & Register</title></head>
<body>
<h2>Đăng nhập</h2>
<form action="Log in.php" method="POST">
    Name: <input type="text" name="name" required><br><br>
    Password: <input type="text" name="password" required><br><br>
    <button type="submit">Đăng nhập</button><br><br>
</form>

<h2>Đăng ký</h2>
<form action="Register.php" method="POST">
    Name: <input type="text" name="name" required><br><br>
    Genda: 
    <select name="gender">
        <option value="Male">Male</option>
        <option value="Female">Female</option>
    </select><br><br>
    Email: <input type="email" name="email" required><br><br>
    Address: <input type="text" name="address"><br><br>
    Phone number: <input type="text" name="number"><br><br>
    Password: <input type="text" name="password" required><br><br>
    <button type="submit">Đăng ký</button>
</form>
</body>
</html>
