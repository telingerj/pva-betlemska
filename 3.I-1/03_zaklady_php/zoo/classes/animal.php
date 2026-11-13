<?php

class Animal
{
    protected string $species;
    protected string $name;
    protected int $age;

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

class Elefant extends Animal
{
    protected int $trunkLength;

    public function __construct(string $species, string $name, int $age, int $trunkLength)
    {
        $this->species = $species;
        $this->name = $name;
        $this->age = $age;
        $this->trunkLength = $trunkLength;
    }

    public function hello()
    {
        return "Ahoj, já jsem " . $this->species . " "
        . $this->name . ", je mi " . $this->age . " let a mám délku chobotu " . $this->trunkLength;
    }
}

//TODO: udělejte potomka třídy Animal pro každé zvíře, které máme v progamu
// a každému z nich přidejte nějaký atribut navíc

//TODO: odstaňte atribut $species (je zbytečný, pro druhy již máme třídy)
