<?php
require "classes/animal.php";
require "classes/pen.php";

$a = new Animal("slon", "Franta", 10);
$a2 = new Animal("žirafa", "Anička", 15);
$a3 = new Animal("had", "Karel", 2);

$p = new Pen(20);

$p->addAnimal($a);
$p->addAnimal($a2);
$p->addAnimal($a3);

//echo($a->name . "<br>");
//echo($a->age . "<br>");
//echo($a->species . "<br>");

echo($a->hello());
echo("<br>");
echo($p->listAnimals());
