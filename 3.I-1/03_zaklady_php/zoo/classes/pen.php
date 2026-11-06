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
        if (sizeof($this->animals) < $this->size)
        {
            array_push($this->animals, $animal);
        }
    }

    public function removeAnimal(Animal $animal)
    {
        $pozice = 0;
        for ($i = 0; $i < sizeof($this->animals); $i++)
        {
            if ($this->animals[$i] == $animal)
            {
                $pozice = $i;
            }
        }
        array_splice($this->animals, $pozice, 1);
    }

    public function listAnimals()
    {
        $r = "Výběh o rozloze " . $this->size . " ha obsahuje tato zvířata: ";
        foreach ($this->animals as $animal)
        {
            $r .= $animal->getSpecies() . " " . $animal->getName() . ", ";
        }
        return $r;
    }

    public function getAnimals()
    {
        return $this->animals;
    }
}
