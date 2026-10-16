<?php
function cisla()
{
    $r = "";
    for ($i = 0; $i < 10; $i++)
    {
        $r .= (strval($i) . " ");
    }
    return $r;
}

function cislaPozpatku()
{
    $r = "";
    for ($i = 10; $i >= 0; $i--)
    {
        $r .= (strval($i) . " ");
    }
    return $r;
}

function barevnaCisla()
{
    // liché číslo červené
    // sudé číslo modré
    $r = "";
    for ($i = 0; $i <= 10; $i++)
    {
        
        if ($i % 2 == 0)
        {
            $r .= "<span style=\"color: blue;\">" . strval($i) . " </span>";
        }
        else
        {
            $r .= "<span style=\"color: red;\">" . strval($i) . " </span>";
        }

        /*
        if ($i == 6 || $i == 7)
        {
            $r .= "<span style=\"color: red;\">" . strval($i) . " </span>";
        }
        else
        {
            $r .= strval($i) . " ";
        }
            */
    }
    return $r;
}

function nasobilka()
{
    $r = "";
    for ($j = 1; $j <= 10; $j++)
    {
        $r .= "<tr>";
        for ($i = 1; $i <= 10; $i++)
        {
            $r .= "<td>" . strval($i * $j) . "</td>";
        }
        $r .= "</tr>";
    }


    return $r;
}

?>

<!DOCTYPE html>

<html>
    <body>
        <p>Čísla od 0 do 10: <?php echo(cisla()); ?></p>
        <p>Čísla od 10 do 0: <?php echo(cislaPozpatku()); ?></p>
        <p>Barevná čísla: <?php echo (barevnaCisla());?></p>
        <table border="1">
            <tr>
                <td>první buňka</td>
                <td>druhá buňka</td>
                <td>třetí buňka</td>
            </tr>
            <tr>
                <td>čtvrtá buňka</td>
                <td>pátá buňka</td>
                <td>šestá buňka</td>
            </tr>
        </table>
        <table border="1">
            <?php echo(nasobilka()); ?>
        </table>
    </body>
</html>