<?php

class Zoo
{
    private array $pens;
    private string $name;

    public function __construct(string $name)
    {
        $this->name = $name;
        $this->pens = [];
    }

    public function addPen(Pen $pen)
    {
        array_push($this->pens, $pen);
    }

    public function listPens()
    {
        return "zoo " . $this->name . " obsahuje " . sizeof($this->pens) . " výběhů";
    }

    public function countAnimals()
    {
        $counter = 0;
        foreach ($this->pens as $pen)
        {
            $counter += sizeof($pen->getAnimals());
        }
        return $counter;
    }

    public function containsPen(Pen $pen)
    {
        foreach ($this->pens as $currentPen)
        {
            if ($pen == $currentPen)
            {
                return true;
            }
        }
        return false;
    }
}
