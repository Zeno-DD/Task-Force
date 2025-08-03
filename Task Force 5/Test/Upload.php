<?php
error_reporting(E_ALL);
ini_set('display_errors', 1);

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $xml = file_get_contents($_FILES['xmlfile']['tmp_name']);

    $dom = new DOMDocument();
    $dom->resolveExternals = true;
    $dom->substituteEntities = true;
  
    $dom->loadXML($xml);

    $data = simplexml_import_dom($dom);

    echo "<h3>Kết quả:</h3>";
    echo "Sản phẩm: <b>" . htmlspecialchars($data->name) . "</b>";
}
?>

<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>XXE Upload</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <h2>– Upload XML</h2>
    <form method="POST" enctype="multipart/form-data">
        <input type="file" name="xmlfile" required>
        <button type="submit">Tải lên</button>
    </form>
    <p><a href="index.php">⬅ Quay về danh sách sản phẩm</a></p>
</body>
</html>