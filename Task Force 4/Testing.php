<?php
if (isset($_GET['ip'])) {
    $ip = $_GET['ip'];
    echo "<pre>";
    system("ping -n 2 " . $ip);
    echo "</pre>";
} else {
?>
    <form method="GET">
        Nhập IP để ping:<br>
        <input type="text" name="ip">
        <input type="submit" value="Ping">
    </form>
<?php
}
?>