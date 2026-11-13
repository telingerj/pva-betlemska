<?php
require "classes/animal.php";
require "classes/pen.php";
require "classes/zoo.php";
require "classes/employee.php";

$a = new Elefant("slon", "Pepa", 10, 10);
$a2 = new Animal("žirafa", "Anička", 15);
$a3 = new Animal("had", "Karel", 2);
$a4 = new Animal("panda", "Kateřina", 5);

$p1 = new Pen(3);
$p2 = new Pen(5);

$p1->addAnimal($a);
$p1->addAnimal($a2);
$p1->addAnimal($a3);
$p2->addAnimal($a4);

$z1 = new Zoo("zoo Praha");
$z2 = new Zoo("zoo Olomouc");

$z1->addPen($p1);
$z2->addPen($p2);

$em1 = new Employee("Karel", 51);
$em2 = new Employee("Milan", 31);

$em1->assign($z1, $p1);

echo($a->hello() . "<br>");
echo($a2->hello());
