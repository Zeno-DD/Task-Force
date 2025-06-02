<!DOCTYPE html>
<html>
<head><title>Login & Register</title>
</head>
<body>
<h2>Đăng nhập</h2>
<form action="Log in.php" method="POST">
    Name: <input type="text" name="name" required><br><br>
    Password: <input type="text" name="password"><br><br>
    <button type="submit">Đăng nhập</button><br><br>
</form>
<div class="tenor-gif-embed" data-postid="1591458100909827176" data-share-method="host" data-aspect-ratio="1.20874" data-width="20%"><a href="https://tenor.com/view/stich-gif-1591458100909827176">Stich GIF</a>from <a href="https://tenor.com/search/stich-gifs">Stich GIFs</a></div> <script type="text/javascript" async src="https://tenor.com/embed.js"></script>

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
    Password: <input type="text" name="password" ><br><br>
    <button type="submit">Đăng ký</button>
</form>
</body>
</html>
