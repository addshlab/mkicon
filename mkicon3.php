<?php

$make = new MakeProfileIcon();

for ($i=0; $i<100; $i++) {
    $make->generate();
}

class MakeProfileIcon {

    public function color( $image, $times = 1, $hex_colors ){
        $x1 = 50; // 共通 +50
        $y1 = 50 * $times;
        $x2 = 0; // 共通 +50
        $y2 = 50 * $times - 50;
        foreach ($hex_colors as $hex_color) {
            $hex = str_split($hex_color,2);
            $r = hexdec($hex[0]);
            $g = hexdec($hex[1]);
            $b = hexdec($hex[2]);
            $color = imagecolorallocate($image, $r, $g, $b);
            ImageFilledRectangle($image, $x1, $y1, $x2, $y2, $color);
            $x1 = $x1 + 50;
            $x2 = $x2 + 50;
        }
    }

    public function is_odd($int){
        if( in_array( $int, [1,3,5,7,9,'b','d','f'])) {
            return true;
        }
        return false;
    }

    public function generate() { 
        $datetime = new DateTime();
        $date = $datetime->format('YmdHisv');
        $md5 = md5($date);
        $md5_18 = substr( $md5, 0, 18);
        $md5_18_color = substr( $md5, 0, 6);
        $md5_18_bg = substr( $md5, 7, 13);
        $bg = substr( $md5, 7, 13);
        $md5_18_array = str_split($md5_18, 1);
        $array = [];
        foreach( $md5_18_array as $str) {
            if( $this->is_odd($str)){
                $array[] = $md5_18_bg;
            } else {
                $array[] = $md5_18_color;
            }
        }

        list($a1,$a2,$a3,$a4,$a5,$a6,$b1,$b2,$b3,$b4,$b5,$b6,$c1,$c2,$c3,$c4,$c5,$c6) = $array;

        $im = imagecreatetruecolor(400,400);
        $this->color( $im, 1, [$bg, $bg, $bg, $bg, $bg, $bg, $bg, $bg,] );
        $this->color( $im, 2, [$bg, $a1, $b1, $c1, $c1, $b1, $a1, $bg,] );
        $this->color( $im, 3, [$bg, $a2, $b2, $c2, $c2, $b2, $a2, $bg,] );
        $this->color( $im, 4, [$bg, $a3, $b3, $c3, $c3, $b3, $a3, $bg,] );
        $this->color( $im, 5, [$bg, $a4, $b4, $c4, $c4, $b4, $a4, $bg,] );
        $this->color( $im, 6, [$bg, $a5, $b5, $c5, $c5, $b5, $a5, $bg,] );
        $this->color( $im, 7, [$bg, $a6, $b6, $c6, $c6, $b6, $a6, $bg,] );
        $this->color( $im, 8, [$bg, $bg, $bg, $bg, $bg, $bg, $bg, $bg,] );

        ImagePNG($im, "icon3/$date.png");
    }
} // class end
