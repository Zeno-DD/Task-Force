<?php
$xml = simplexml_load_file("products.xml");
?>
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Danh sách sản phẩm gaming</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>

<h2>🕹️ Danh sách dụng cụ gaming</h2>
<table>
    <tr>
        <th>Tên sản phẩm</th>
        <th>Giá</th>
        <th>Loại</th>
    </tr>
    <?php foreach($xml->product as $product): ?>
    <tr>
        <td><?= htmlspecialchars($product->name) ?></td>
        <td><?= number_format((float)$product->price, 0, ',', '.') ?> đ</td>
        <td><?= htmlspecialchars($product->category) ?></td>
    </tr>
    <?php endforeach; ?>
</table>

<a href="add.php" class="button">➕ Thêm sản phẩm mới</a>

</body>
</html>