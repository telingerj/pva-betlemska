<?php

class Employee
{
    private string $name;
    private int $age;
    private ?Zoo $zoo;
    private ?Pen $pen;

    public function __construct(string $name, int $age)
    {
        $this->name = $name;
        $this->age = $age;
        $this->pen = null;
        $this->zoo = null;
    }

    public function assign(Zoo $z, Pen $p)
    {
        if (!$z->containsPen($p))
        {
            throw new InvalidArgumentException("Zoo does not contain pen");
        }
        $this->zoo = $z;
        $this->pen = $p;
        
    }
}