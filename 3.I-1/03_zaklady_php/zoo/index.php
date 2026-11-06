<?php
require "classes/animal.php";
require "classes/pen.php";
require "classes/zoo.php";

$a = new Animal("slon", "Pepa", 10);
$a2 = new Animal("žirafa", "Anička", 15);
$a3 = new Animal("had", "Karel", 2);
$a4 = new Animal("panda", "Kateřina", 5);

$p1 = new Pen(3);
$p2 = new Pen(5);

$p1->addAnimal($a);
$p1->addAnimal($a2);
$p1->addAnimal($a3);
$p2->addAnimal($a4);

$z = new Zoo("zoo Praha");

$z->addPen($p1);
$z->addPen($p2);


echo($z->countAnimals());
