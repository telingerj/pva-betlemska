<?php
    function is_triangle($a, $b, $c)
    {
        if ($a + $b > $c && $a + $c > $b && $b + $c > $a)
        {
            return "může to být trojúhelník";
        }
        // && = a zároveň (pravý Alt + C)
        // || = nebo (pravý alt + W)
        return "nemůže to být trojúhelník";
    }

    // a: (10;15>
    // b: (0;10)
    // c: <6;7>
    // d: (2, +inf)
    // e: (-5;0) u (5;10>

    function interval_a($n) // vrátit písmeno intervalu, pokud číslo leží v intervalu, jinak vrátit prázdný řetězec
    {
        if ($n > 10 && $n <= 15)
            return "a";
        return "";
    }

    function interval_b($n)
    {
        if ($n > 0 && $n < 10)
            return "b";
        return "";
    }

    function interval_c($n)
    {
        if ($n >= 6 && $n <= 7)
            return "c";
        return "";
    }

    function interval_d($n)
    {
        if ($n > 2)
            return "d";
        return "";
    }

    function interval_e($n)
    {
        if (($n > -5 && $n < 0) || ($n > 5 && $n <= 10))
            return "e";
        return "";
    }
?>


<!DOCTYPE html>

<html>
    <body>
        <h1>Já jsem php soubor</h1>
        <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Provident facere corporis dolore tenetur ipsam officiis architecto sint soluta impedit rem. Aliquid inventore facilis quod ut error, molestias voluptatum distinctio esse.</p>
        <p>Hodnoty 1, 1, 1: <?php echo(is_triangle(1, 1, 1)); ?></p>
        <p>Hodnoty 5, 2, 1: <?php echo(is_triangle(5, 2, 1)); ?></p>
        <p>Hodnoty 8, 9, 7: <?php echo(is_triangle(8, 9, 7)); ?></p>
        <p>Hodnoty 5, 6, 7: <?php echo(is_triangle(5, 6, 7)); ?></p>
        <p>číslo 5 patří do: <?php echo(interval_a(5)); echo(interval_b(5)); echo(interval_c(5)); echo(interval_d(5)); echo(interval_e(5)); ?></p>
    </body>
</html>