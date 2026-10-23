<?php

class Animal
{
    private string $species;
    private string $name;
    private int $age;

    public function __construct(string $species,
     string $name, int $age)
    {
        $this->species = $species;
        $this->name = $name;
        $this->age = $age;
    }

    public function hello()
    {
        return "Ahoj, já jsem " . $this->species . " "
        . $this->name . " a je mi " . $this->age . " let";
    }

    public function getName()
    {
        return $this->name;
    }

    public function getSpecies()
    {
        return $this->species;
    }
}
