<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Thêm sản phẩm</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>

<h2>➕ Thêm dụng cụ gaming</h2>
<form action="save.php" method="post">
    <p>Tên sản phẩm: <br><input type="text" name="name" required></p>
    <p>Giá (VNĐ): <br><input type="number" name="price" required></p>
    <p>Loại sản phẩm: <br><input type="text" name="category" required></p>
    <p><input type="submit" value="Lưu sản phẩm"></p>
</form>

<a href="index.php" class="button">⬅ Quay lại danh sách</a>

</body>
</html>
