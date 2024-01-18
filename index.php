<html>
<head>
<style>
img {
    max-width: 50px;
    width: 100%;
}
.box {
    width: 100%;
    height: auto;
    padding: 10px;
    margin: 3px;
    float: left;
    text-align: left;
    background: #000;
    color: #FFF;
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
$lists = glob('./dist/images/*');

foreach($lists as $list) :
    $json_file = file_get_contents(str_replace(array('images','.png'), array('json','.json'), $list));
    echo '<div class="box">';
    echo '<div><img src="' . $list . '" /></div>';
    echo '<div class="name">' . basename($list, '.png') . '</div>';
    echo '<pre>' . $json_file . '</pre>';
    echo '</div>';
endforeach;
?>
</body>
</html>
