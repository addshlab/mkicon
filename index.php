<html>
<head>
<style>
img {
    max-width: 50px;
    width: 100%;
}
.box {
    width: 70px;
    height: 70px;
    padding: 10px;
    margin: 3px;
    float: left;
    text-align: center;
    background: #000;
}
.name {
    margin-top: 3px;
    font-size: 8px;
    font-family: monospace;
    word-break: break-all;
    text-align: left;
    color: #FFF;
}
</style>
</head>
<body>
<?php
$lists = glob('./icon3/*');

foreach($lists as $list) :
    echo '<div class="box">';
    echo '<div><img src="' . $list . '" /></div>';
    echo '<div class="name">' . basename($list, '.png') . '</div>';
    echo '</div>';
endforeach;
?>
</body>
</html>
