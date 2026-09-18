window.onload = function()
{
    let image = document.getElementById("img1");
    let x = 0;
    let y = 0;
    let dx = 1;
    let dy = 1;
    setInterval(function()
    {
        move(image, x, y);
        x += dx;
        y += dy;
        if (bounceCheckX(x, y))
            dx *= -1;
        if (bounceCheckY(x, y))
            dy *= -1;
    }, 1);
    
}

function move(element, posX, posY)
{
    element.style.left = posX + "px";
    element.style.top = posY + "px";
}

function bounceCheckX(posX, posY)
{
    // vrací true / false - podle toho, jestli se obrázek má odrazit
    // window.innerHeight
    if (posX == 0)  // levá hranice
    {
        return true;
    }
    if (posX == window.innerWidth - 200)  // pravá hranice
    {
        return true;
    }
    return false;
}

function bounceCheckY(posX, posY)
{
    // vrací true / false - podle toho, jestli se obrázek má odrazit
    if (posY == 0)  // horní hranice
    {
        return true;
    }
    if (posY == window.innerHeight - 200)  // dolní hranice
    {
        return true;
    }
    return false;
}


/*

setTimeout(function()  // počká jen jednou
{
    alert("počkal jsem");
}, 1000);

setInterval(function()  // počká opakovaně pořád dokola
{
    alert("počkal jsem");
}, 2000);

*/

