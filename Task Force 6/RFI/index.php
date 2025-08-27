<?php
// RFI demo - VULNERABLE (demo only)
// WARNING: allow_url_include must be On để include từ URL hoạt động
$remote = isset($_GET['url']) ? $_GET['url'] : 'pages/home.php';

// If url starts with http:// or https://, include will try remote include
include($remote);
?>