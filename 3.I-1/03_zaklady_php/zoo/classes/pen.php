<?php

class Pen
{
    private int $size;
    private array $animals;

    public function __construct(int $size)
    {
        $this->size = $size;
        $this->animals = [];
    }

    public function addAnimal(Animal $animal)
    {
        array_push($this->animals, $animal);
    }

    //TODO: removeAnimal

    public function listAnimals()
    {
        $r = "Výběh o rozloze " . $this->size . " ha obsahuje tato zvířata: ";
        foreach ($this->animals as $animal)
        {
            $r .= $animal->getSpecies() . " " . $animal->getName() . ", ";
        }
        return $r;
    }
}
