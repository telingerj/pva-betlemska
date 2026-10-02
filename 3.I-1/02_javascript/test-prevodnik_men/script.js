window.onload = function()
{
    
    let czk = document.getElementById("czk");
    let eur = document.getElementById("eur");
    czk.onclick = function()
    {
        let vstup = document.getElementById("vstup");
        alert(vstup.value * 24);
    }
    eur.onclick = function()
    {
        let vstup = document.getElementById("vstup");
        alert(vstup.value / 24);
    }
}