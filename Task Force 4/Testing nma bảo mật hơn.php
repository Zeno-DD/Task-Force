<?php
if (isset($_GET['ip'])) {
    $ip = $_GET['ip'];

    if (preg_match('/^[0-9\.]+$/', $ip)) {
        $output = shell_exec("ping -n 2 " . escapeshellarg($ip));
        echo "<pre>$output</pre>";
    } else {
        echo "IP không hợp lệ!";
    }
} else {
    echo '<form method="GET">
            Nhập IP: <input type="text" name="ip">
            <input type="submit" value="Ping">
          </form>';
}
?>