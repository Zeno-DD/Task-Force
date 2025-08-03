<?php
if ($_SERVER["REQUEST_METHOD"] === "POST") {
    $name = $_POST["name"];
    $price = $_POST["price"];
    $category = $_POST["category"];

    $xml = simplexml_load_file("products.xml");

    $newProduct = $xml->addChild("product");
    $newProduct->addChild("name", $name);
    $newProduct->addChild("price", $price);
    $newProduct->addChild("category", $category);

    $xml->asXML("products.xml");

    header("Location: index.php");
    exit();
}
?>